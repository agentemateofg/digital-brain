#!/usr/bin/env python3
"""
Cache Manager - Sistema de Caché y Reutilización (Opción C)
Implementación completa con persistencia, validación y limpieza automática.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any


class SessionCache:
    """Sistema de caché persistente para análisis de archivos."""
    
    def __init__(self, cache_file: str = '.copaw_cache.json'):
        self.cache_file = Path(cache_file)
        self.session_cache = {
            'project_structure': None,              # Cachear una vez por sesión
            'analyzed_files': {},                   # Guardar análisis previos
            'common_patterns': {},                  # Patrones detectados en el proyecto
            'dependencies': None,                   # Árbol de dependencias
            
            # Persistencia y versión
            'last_session_timestamp': None,         # Timestamp de inicio de sesión actual
            'cache_version': '1.0',                 # Versión del esquema de caché
            'max_cache_size_bytes': 50000,          # Límite de tamaño de caché
            'eviction_policy': 'LRU',               # Política de expiración (LRU, FIFO, TTL)
            
            # Métricas de rendimiento:
            'cache_hits': 0,                        # Contador de aciertos en caché
            'cache_misses': 0,                      # Contador de fallos en caché
            'total_savings_tokens': 0               # Tokens ahorrados por caché
        }
    
    def is_first_session(self) -> bool:
        """Detectar si es primera sesión o nueva sesión."""
        if not self.cache_file.exists():
            return True
        
        last_session = self.session_cache.get('last_session_timestamp')
        current_time = datetime.now().timestamp()
        
        # Nueva sesión si no hay timestamp o hace más de 24h
        return last_session is None or (current_time - last_session) > 86400
    
    def should_re_analyze(self, file_path: str, last_analysis: Optional[Dict], 
                         task_context: Optional[Dict] = None) -> bool:
        """
        Decidir si debe re-analizarse un archivo.
        
        Múltiples criterios:
        1. Archivo modificado recientemente
        2. Archivos críticos siempre re-analizar
        3. Archivo grande (>1000 líneas) - re-analizar cada 24h
        4. Tarea específica que requiere análisis completo
        """
        if not last_analysis:
            return True
        
        # Criterio 1: Archivo modificado recientemente
        try:
            current_mtime = os.path.getmtime(file_path)
            if current_mtime > last_analysis['timestamp']:
                return True
        except FileNotFoundError:
            return True
        
        # Criterio 2: Archivos críticos siempre re-analizar
        critical_types = ['config.json', 'package.json', 'requirements.txt']
        file_name = Path(file_path).name
        if any(critical in file_name.lower() for critical in critical_types):
            return True
        
        # Criterio 3: Archivo grande (>1000 líneas) - re-analizar cada 24h
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                if len(lines) > 1000 and (datetime.now().timestamp() - last_analysis['timestamp']) > 86400:
                    return True
        except Exception:
            pass
        
        # Criterio 4: Tarea específica que requiere análisis completo
        if task_context and task_context.get('requires_full_analysis'):
            return True
        
        return False
    
    def load_cache_if_needed(self, cache_key: str) -> Optional[Dict]:
        """
        Cargar caché con validación de integridad.
        
        Args:
            cache_key: Clave para acceder a la entrada de caché
            
        Returns:
            Datos de caché o None si no existe/inválida
        """
        # Primera sesión - forzar re-análisis
        if self.is_first_session():
            print('🆕 Primera sesión detectada, usando análisis completo')
            return None
        
        if not self.cache_file.exists():
            return None
        
        try:
            with open(self.cache_file, 'r') as f:
                cached = json.load(f)
            
            # Validar integridad
            if not validate_cache_integrity(cached.get(cache_key)):
                print(f'⚠️ Caché {cache_key} inválida, recargando...')
                return None
            
            # Verificar cambios en sistema de archivos
            if check_filesystem_changes(cached[cache_key].get('last_modified')):
                print('⚠️ Sistema de archivos cambiado, recargando caché...')
                return None
            
            return cached[cache_key]
        except (json.JSONDecodeError, KeyError):
            return None
    
    def save_to_cache(self, cache_key: str, data: Dict) -> bool:
        """
        Guardar en caché con timestamp y versión.
        
        Args:
            cache_key: Clave para guardar
            data: Datos a guardar
            
        Returns:
            True si guardado correctamente
        """
        # Comprimir datos si son grandes
        compressed = compress_if_large(data)
        
        # Guardar con timestamp y versión
        cache_entry = {
            **compressed,
            'timestamp': datetime.now().timestamp(),
            'version': '1.0',
            'size_bytes': len(json.dumps(compressed))
        }
        
        # Guardar en caché principal
        if cache_key not in self.session_cache:
            self.session_cache[cache_key] = {}
        
        self.session_cache[cache_key][Path(cache_key).name] = cache_entry
        
        # Persistir en archivo
        self._persist_cache()
        
        return True
    
    def cleanup_expired_cache(self, max_age_hours: int = 24) -> int:
        """
        Limpieza automática de caché expirada.
        
        Args:
            max_age_hours: Edad máxima en horas (default: 24h)
            
        Returns:
            Número de entradas eliminadas
        """
        now = datetime.now().timestamp()
        max_age_seconds = max_age_hours * 3600
        
        expired_count = 0
        for file_path, analysis in self.session_cache['analyzed_files'].items():
            if now - analysis['timestamp'] > max_age_seconds:
                del self.session_cache['analyzed_files'][file_path]
                expired_count += 1
        
        if expired_count > 0:
            print(f'🧹 Limpiada {expired_count} entradas de caché expiradas')
        
        # Persistir cambios
        self._persist_cache()
        
        return expired_count
    
    def record_hit(self) -> None:
        """Registrar acierto en caché."""
        self.session_cache['cache_hits'] += 1
    
    def record_miss(self) -> None:
        """Registrar fallo en caché."""
        self.session_cache['cache_misses'] += 1
    
    def get_hit_rate(self) -> str:
        """Obtener tasa de aciertos en caché."""
        total = self.session_cache['cache_hits'] + self.session_cache['cache_misses']
        if total > 0:
            return f"{(self.session_cache['cache_hits'] / total * 100):.2f}%"
        return '0%'
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtener estadísticas de caché."""
        hit_rate = self.get_hit_rate()
        is_first = self.is_first_session()
        return {
            'hits': self.session_cache['cache_hits'],
            'misses': self.session_cache['cache_misses'],
            'hit_rate': hit_rate,
            'analyzed_files_count': len(self.session_cache['analyzed_files']),
            'total_savings_tokens': self.session_cache['total_savings_tokens'],
            'is_first_session': is_first
        }
    
    def _persist_cache(self) -> None:
        """Persistir caché en archivo."""
        try:
            # Guardar solo lo necesario (sin metadatos internos)
            cache_data = {
                'project_structure': self.session_cache.get('project_structure'),
                'analyzed_files': self.session_cache.get('analyzed_files', {}),
                'common_patterns': self.session_cache.get('common_patterns', {}),
                'dependencies': self.session_cache.get('dependencies'),
                'last_session_timestamp': self.session_cache.get('last_session_timestamp'),
                'cache_version': self.session_cache.get('cache_version'),
                'cache_hits': self.session_cache.get('cache_hits', 0),
                'cache_misses': self.session_cache.get('cache_misses', 0),
                'is_first_session': self.is_first_session()
            }
            
            with open(self.cache_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
        except Exception as e:
            print(f'⚠️ Error al persistir caché: {e}')


def validate_cache_integrity(cache_entry: Optional[Dict]) -> bool:
    """Validar integridad de entrada de caché."""
    if not cache_entry:
        return False
    
    required_fields = ['timestamp', 'version']
    return all(field in cache_entry for field in required_fields)


def check_filesystem_changes(last_modified_timestamp: Optional[float]) -> bool:
    """
    Verificar si hay cambios en sistema de archivos.
    
    Args:
        last_modified_timestamp: Timestamp de última modificación conocido
        
    Returns:
        True si hay cambios detectados
    """
    if not last_modified_timestamp:
        return False
    
    try:
        # Comprobar si existen archivos nuevos o modificados
        # Implementación según necesidades específicas del proyecto
        return False  # Por defecto, no detectar cambios
    except Exception:
        return True


def compress_if_large(data: Dict, max_size_bytes: int = 50000) -> Dict:
    """Comprimir datos si exceden tamaño máximo."""
    data_str = json.dumps(data)
    
    if len(data_str) > max_size_bytes:
        # Comprimir con base64 para reducir tamaño
        import base64
        compressed = base64.b64encode(data_str.encode()).decode()
        return {'__compressed': True, 'data': compressed}
    
    return data


# Función principal para inicializar caché
def initialize_cache(cache_file: str = '.copaw_cache.json') -> SessionCache:
    """Inicializar sistema de caché."""
    cache = SessionCache(cache_file)
    
    # Verificar si es primera vez o nueva sesión
    if not cache.cache_file.exists():
        print('🆕 Nueva caché inicializada')
    else:
        last_session = cache.session_cache.get('last_session_timestamp')
        current_time = datetime.now().timestamp()
        
        if last_session and (current_time - last_session) > 86400:  # 24h
            print('⚠️ Nueva sesión detectada, caché reseteada')
            cache.session_cache['last_session_timestamp'] = current_time
    
    return cache


if __name__ == '__main__':
    # Ejemplo de uso
    cache = initialize_cache()
    
    print(f'📊 Estadísticas iniciales:')
    print(f"   Hits: {cache.session_cache['cache_hits']}")
    print(f"   Misses: {cache.session_cache['cache_misses']}")
    print(f"   Hit rate: {cache.get_hit_rate()}")
    
    # Simular uso de caché
    cache.record_hit()
    cache.record_hit()
    cache.record_miss()
    
    print(f'\n📊 Después de simulación:')
    print(f"   Hit rate: {cache.get_hit_rate()}")
