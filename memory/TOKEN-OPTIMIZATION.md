# 🎯 Sistema Inteligente de Gestión de Tokens
## 📋 Objetivo
Optimizar interacciones sin comprometer capacidad de ejecución, análisis y desarrollo de código.
---
## 🔍 ANÁLISIS PRE-PROCESAMIENTO (Antes de cada llamada al LLM)
### 1️⃣ Evaluar complejidad real de la tarea
| Tipo de tarea | Tokens necesarios | Acción |
|---------------|-------------------|--------|
| **Consulta simple** (ej: "2+2") | <50 tokens | Respuesta directa, sin contexto histórico |
| **Lectura archivo** (ej: "lee PDF") | 1-5k tokens | Solo contenido del archivo + instrucciones |
| **Análisis de código** | 5-15k tokens | Código relevante + errores + contexto inmediato |
| **Desarrollo complejo** | 10-20k tokens | Especificaciones + archivos relacionados + decisiones previas |
### 2️⃣ Identificar archivos/contexto REALMENTE necesarios
#### ✅ ESENCIAL (siempre incluir):
- Archivos modificados en las últimas **2 horas**
- Configuraciones relevantes (`config.json`, `MEMORY.md`)
- Contexto de la tarea actual (qué se quiere lograr)
- Errores recientes no resueltos
#### ⚠️ OPCIONAL (comprimir si hay espacio):
- Conversaciones antiguas (>24h) → resumir en 1 línea por tema
- Logs de herramientas anteriores → solo resultados relevantes
- Detalles técnicos no solicitados → omitir
#### ❌ ELIMINAR:
- Código muerto/comentado (`// ... resto igual`)
- Errores ya resueltos (referencia al archivo solución)
- Información duplicada en múltiples archivos
- Logs de pensamiento (`<thinking>...</thinking>`) si `filter_thinking: true`
### 3️⃣ Comprimir información redundante
**Reglas de compresión:**
```markdown
✅ Conversación antigua (>24h):
"Usuario pidió X, se hizo Y, resultado Z" (1 línea)
✅ Resultado de herramienta anterior:
"browser_use: https://marca.com → F1 China GP, Tennis Indian Wells"
✅ Código repetido:
"// ... resto del código igual"
✅ Errores resueltos:
"Error X resuelto en memory/2026-03-13.md"
```
### 4️⃣ Eliminar contenido no esencial
**Checklist pre-procesamiento:**
```markdown
[ ] ¿La tarea requiere contexto histórico? → Sí/No
[ ] ¿Hay archivos modificados en las últimas 2h? → Listar
[ ] ¿Puedo resumir conversaciones antiguas? → Sí/No
[ ] ¿Están los logs de pensamiento ocultos? → filter_thinking: true
[ ] ¿El contexto total < max_input_length (131072)? → Verificar
```
---
## 🛠️ CONFIGURACIÓN ACTUAL (Ya optimizada)
En `/Users/piter/.copaw/config.json`:
```json
{
"agents": {
"running": {
"max_input_length": 131072,           // ✅ Límite de input
"memory_reserve_ratio": 0.1,          // ✅ Reserva ~819 tokens
"memory_compact_ratio": 0.75,         // ✅ Compresión agresiva
"enable_tool_result_compact": true,   // ✅ Compacta resultados
"tool_result_compact_keep_n": 5       // ✅ Mantiene últimos 5
}
},
"telegram": {
"filter_thinking": true                 // ✅ Oculta logs de pensamiento
}
}
```
---
## 📊 Métricas de Éxito
| Métrica | Objetivo | Actual |
|---------|----------|--------|
| **Tokens usados por respuesta** | <10k | ✅ Monitorizar |
| **Errores de contexto overflow** | 0 | ✅ Configurado |
| **Tiempo de respuesta** | <30s | ✅ Optimizado |
| **Precisión en tareas complejas** | >90% | ⚠️ Evaluar |
---
## 🎯 Flujo de Trabajo Recomendado
### Para tareas simples:
```
1. Identificar tarea → Consulta simple
2. No cargar contexto histórico
3. Respuesta directa + referencia a archivos si aplica
```
### Para tareas complejas:
```
1. Leer archivos relevantes (últimas 2h)
2. Resumir conversaciones antiguas (>24h)
3. Eliminar logs no esenciales
4. Verificar contexto < max_input_length
5. Ejecutar tarea
6. Guardar resultado en memory/YYYY-MM-DD.md
```
---
## 📂 GESTIÓN DE CONTEXTO JERÁRQUICO
### NIVEL 1 - Siempre incluir (crítico):
- Consulta actual del usuario
- Archivos directamente mencionados
- Error actual si existe
### NIVEL 2 - Incluir si relevante:
- Archivos relacionados (imports, dependencias)
- Contexto de conversación reciente (últimos 2-3 intercambios)
### NIVEL 3 - Incluir solo si explícitamente necesario:
- Estructura completa del proyecto
- Historial extenso de conversación
- Documentación completa de dependencias
---
## ✅ CHECKLIST POR NIVEL
### Antes de cargar contexto:
**NIVEL 1 (Crítico - Obligatorio):**
```markdown
[ ] ¿Tengo la consulta actual del usuario?
[ ] ¿Están los archivos mencionados en el prompt?
[ ] ¿Existe un error actual no resuelto?
```
**NIVEL 2 (Relevante - Opcional):**
```markdown
[ ] ¿Los archivos relacionados son necesarios para esta tarea?
[ ] ¿El contexto de conversación reciente aporta valor?
[ ] ¿Hay espacio suficiente en el contexto (< max_input_length)?
```
**NIVEL 3 (Específico - Solo si aplica):**
```markdown
[ ] ¿La estructura completa del proyecto es necesaria?
[ ] ¿El historial extenso aporta información crítica?
[ ] ¿La documentación de dependencias es requerida?
```
---
## 🎯 REGLAS DE PRIORIZACIÓN
### Si NIVEL 1 + NIVEL 2 > max_input_length:
```markdown
→ Mantener NIVEL 1 completo
→ Resumir NIVEL 2 a máximo 50%
→ Eliminar NIVEL 3
```
### Si NIVEL 1 + NIVEL 2 + NIVEL 3 > max_input_length:
```markdown
→ Mantener NIVEL 1 completo
→ Resumir NIVEL 2 a 30%
→ Eliminar NIVEL 3 por defecto
```
---
## 💡 EJEMPLOS PRÁCTICOS
### Ejemplo 1 - Tarea simple ("Lee este archivo"):
```markdown
NIVEL 1: "Lee /Users/piter/.copaw/config.json"
NIVEL 2: (opcional) Contexto reciente sobre config.json
NIVEL 3: ❌ No incluir estructura completa del proyecto
```
### Ejemplo 2 - Tarea compleja ("Analiza errores y arregla"):
```markdown
NIVEL 1: Error actual + archivos mencionados
NIVEL 2: Archivos relacionados con imports
NIVEL 3: Estructura completa si es necesario para entender dependencias
```
---
## 📂 ESTRATEGIA DE LECTURA DE ARCHIVOS
### 🚫 NO LEER ARCHIVOS "POR SI CASO"
**Regla de oro:** Solo leer bajo demanda, según el tipo de tarea.
---
### 🎯 Lectura Inteligente Simplificada
```python
def read_strategic(file_path, max_lines=200):
"""Leer archivo con límite inteligente"""
with open(file_path, 'r') as f:
content = f.read()
# Comprimir si es grande
if len(content.split('\n')) > 200:
return content[:max_lines] + "\n# ... [resto omitido]"
return content
```
---
### 📋 Tipos de Lectura (Simplificados)
#### `"fix_error"` - Arreglar error
```markdown
→ Leer contexto del error (últimas 50 líneas donde falló)
→ Incluir stack trace si existe
→ Archivos relacionados con imports
→ No leer archivo completo, solo zona del error
```
#### `"understand_function"` - Entender función
```markdown
→ Leer firma de función + docstring
→ Leer implementación completa de la función
→ Leer llamadas a esta función (imports/dependencias)
→ No leer funciones no relacionadas
```
#### `"add_feature"` - Añadir feature
```markdown
→ Leer sección donde se añadirá la feature
→ Leer tests existentes si aplica
→ Leer configuración relevante
→ No leer todo el archivo, solo zonas relevantes
```
#### `"read_with_limit"` - Lectura general (DEFAULT)
```markdown
→ Leer máximo 200 líneas desde el inicio
→ O desde la última modificación (git blame)
→ Solo si no hay tipo específico de lectura
```
---
### 🎯 Priorización de Archivos
#### PREFERIR LEER:
1. ✅ Archivos modificados en las últimas **2h**
2. ✅ Archivos mencionados en el error/stack trace
3. ✅ Archivos con última modificación reciente (git)
4. ✅ Archivos relacionados por imports/dependencias
#### EVITAR LEER:
1. ❌ Archivos no modificados desde hace >7 días
2. ❌ Archivos de configuración estáticos (no relevantes)
3. ❌ Archivos de documentación (a menos que se solicite explícitamente)
---
### 💾 Cache Inteligente
```markdown
SI archivo ya fue leído en las últimas 24h:
→ Usar caché sin releer
→ Validar si hay cambios (git diff o timestamp)
→ Actualizar caché solo si hay modificaciones
SI archivo es pequeño (<500 líneas):
→ Leer completo (no vale la pena cachear)
SI archivo es grande (>2000 líneas):
→ Usar estrategia específica (solo funciones relevantes)
```
---
## 💻 COMPRESIÓN INTELIGENTE DE CÓDIGO
### 🚫 MAL (desperdicia tokens):
```python
# archivo_completo.py - 500 líneas
[todo el código incluyendo partes no relevantes]
```
### ✅ BIEN (optimizado):
```python
# archivo_completo.py - secciones relevantes
class UserManager:
# ... [métodos no relacionados omitidos]
def authenticate(self, username, password):
# [código relevante para la consulta]
pass
# ... [resto del código omitido]
```
---
### 🎯 Patrones de Compresión
#### PATTERN 1 - Método específico:
```python
class UserManager:
# ... [métodos no relacionados omitidos]
def authenticate(self, username, password):
if not self._validate_credentials(username, password):
raise AuthenticationError("Invalid credentials")
user = self._find_user(username)
if not user:
raise UserNotFoundError("User not found")
# [código relevante para la consulta]
pass
# ... [resto del código omitido]
```
#### PATTERN 2 - Función anónima/lambda:
```python
# MAL:
process_data = lambda x: x.upper() if len(x) > 10 else x.lower()
# BIEN:
process_data = lambda x: (x.upper() if len(x) > 10 else x.lower())
# [explicación si es necesario]
```
#### PATTERN 3 - Bloques de código repetidos:
```python
# MAL:
def process_item(item):
# ... código común ...
def process_other(other):
# ... mismo código ...
# BIEN:
def process_common(item):
# [código común]
pass
def process_item(item):
result = process_common(item)
# [lógica específica]
return result
def process_other(other):
result = process_common(other)
# [lógica específica]
return result
```
---
### 📋 Reglas de Compresión por Tipo de Código
| Tipo de código | Qué incluir | Qué omitir |
|----------------|-------------|------------|
| **Funciones completas** | ✅ Firma + docstring + implementación | ❌ Métodos no relacionados |
| **Métodos específicos** | ✅ Implementación del método | ❌ Otros métodos de la clase |
| **Bloques condicionales** | ✅ Condición relevante + cuerpo | ❌ Condiciones irrelevantes |
| **Imports/dependencias** | ✅ Solo imports necesarios para la tarea | ❌ Imports no usados |
| **Comentarios** | ✅ Comentarios relevantes a la tarea | ❌ Comentarios genéricos/deprecated |
---
### 📝 Notación de Omisión Estandarizada
```markdown
OMISIONES COMUNES:
# ... [código omitido] → Indica que hay código entre líneas relevantes
# // ... resto del código igual → Para bloques completos
# [código irrelevante omitido] → Para secciones no relacionadas
# (función completa omitida) → Cuando se menciona pero no se incluye
EJEMPLO COMPLETO:
```python
class UserManager:
def __init__(self, db_connection):
self.db = db_connection  # [atributos omitidos]
# ... [métodos no relacionados omitidos]
def authenticate(self, username, password):
if not self._validate_credentials(username, password):
raise AuthenticationError("Invalid credentials")
user = self._find_user(username)
if not user:
raise UserNotFoundError("User not found")
# [código relevante para la consulta]
return True
# ... [resto del código omitido]
```
---
## 📝 Referencias
- **Configuración**: `/Users/piter/.copaw/config.json`
- **Memoria diaria**: `memory/YYYY-MM-DD.md`
- **Memoria a largo plazo**: `MEMORY.md`
- **Proyectos**: `memory/projects/`
---
## 💻 IMPLEMENTACIÓN DE CACHE EN PYTHON
### 📂 Archivo de Implementación
**Ubicación**: `/Users/piter/.copaw/scripts/cache_manager.py`
**Características:**
- ✅ Sistema de caché persistente (`.copaw_cache.json`)
- ✅ Validación de integridad automática
- ✅ Limpieza automática de caché expirada (TTL 24h)
- ✅ Múltiples criterios para re-análisis
- ✅ Métricas de rendimiento (hits/misses/hit_rate)
---
### 🎯 Uso Básico
```python
from scripts.cache_manager import initialize_cache, SessionCache
# Inicializar caché
cache = initialize_cache()
# Verificar si debe re-analizar archivo
if not cache.should_re_analyze('archivo.py', last_analysis):
print('✅ Usando caché')
cache.record_hit()
else:
print('🔄 Re-analizando archivo')
cache.record_miss()
# Obtener estadísticas
stats = cache.get_stats()
print(f"Hit rate: {stats['hit_rate']}")
```
---
### 🎯 Funciones Principales
| Función | Descripción |
|---------|-------------|
| `should_re_analyze()` | Decide si debe re-analizar archivo (múltiples criterios) |
| `load_cache_if_needed()` | Carga caché con validación de integridad |
| `save_to_cache()` | Guarda análisis en caché |
| `cleanup_expired_cache()` | Limpia caché expirada automáticamente |
| `get_hit_rate()` | Obtiene tasa de aciertos en caché |
| `get_stats()` | Obtiene estadísticas completas |
---
## 📝 Referencias
- **Configuración**: `/Users/piter/.copaw/config.json`
- **Memoria diaria**: `memory/YYYY-MM-DD.md`
- **Memoria a largo plazo**: `MEMORY.md`
- **Proyectos**: `memory/projects/`
---
## 💾 SISTEMA DE CACHE Y REUTILIZACIÓN (Opción C - Implementación Completa)
### 🎯 Estructura de Caché Persistente
```javascript
const sessionCache = {
// Datos principales
project_structure: null,              // Cachear una vez por sesión
analyzed_files: {},                   // Guardar análisis previos
common_patterns: {},                  // Patrones detectados en el proyecto
dependencies: null,                   // Árbol de dependencias
// Persistencia y versión
last_session_timestamp: null,         // Timestamp de inicio de sesión actual
cache_version: '1.0',                 // Versión del esquema de caché
max_cache_size_bytes: 50000,          // Límite de tamaño de caché
eviction_policy: 'LRU',               // Política de expiración (LRU, FIFO, TTL)
// Métricas de rendimiento:
cache_hits: 0,                        // Contador de aciertos en caché
cache_misses: 0,                      // Contador de fallos en caché
total_savings_tokens: 0               // Tokens ahorrados por caché
};
```
---
### 🎯 Función shouldReAnalyze Mejorada (Múltiples Criterios)
```javascript
function shouldReAnalyze(file, lastAnalysis, taskContext = {}) {
// Criterio 1: Archivo modificado recientemente
if (file.lastModified > lastAnalysis.timestamp) {
return true;
}
// Criterio 2: Archivos críticos siempre re-analizar
const criticalTypes = ['config.json', 'package.json', 'requirements.txt'];
if (criticalTypes.includes(file.type)) {
return true;
}
// Criterio 3: Archivo grande (>1000 líneas) - re-analizar cada 24h
if (file.lineCount > 1000 && 
(Date.now() - lastAnalysis.timestamp) > 86400000) { // 24h en ms
return true;
}
// Criterio 4: Tarea específica que requiere análisis completo
if (taskContext.requiresFullAnalysis) {
return true;
}
return false;
}
```
---
### 🎯 Función de Carga de Caché con Validación
```javascript
function loadCacheIfNeeded(cacheKey) {
const cached = getFromStorage(cacheKey);
if (!cached || !validateCacheIntegrity(cached)) {
return null; // Caché inválida o no existe
}
// Verificar si hay cambios en el sistema de archivos
const fileSystemChanged = checkFileSystemChanges(cached.lastModified);
if (fileSystemChanged) {
console.log('⚠️ Sistema de archivos cambiado, recargando caché...');
return null;
}
return cached;
}
function saveToCache(cacheKey, data) {
// Comprimir datos si son grandes
const compressed = compressIfLarge(data);
// Guardar con timestamp y versión
const cacheEntry = {
...compressed,
timestamp: Date.now(),
version: '1.0',
size_bytes: compressed.size
};
return setToStorage(cacheKey, cacheEntry);
}
```
---
### 🎯 Política de Expiración Automática (TTL)
```javascript
function cleanupExpiredCache(maxAgeHours = 24) {
const now = Date.now();
const maxAgeMs = maxAgeHours * 60 * 60 * 1000;
// Obtener todos los archivos en caché
const cachedFiles = Object.keys(sessionCache.analyzed_files);
// Eliminar archivos expirados
let removedCount = 0;
for (const filePath of cachedFiles) {
const analysis = sessionCache.analyzed_files[filePath];
if (now - analysis.timestamp > maxAgeMs) {
delete sessionCache.analyzed_files[filePath];
removedCount++;
}
}
if (removedCount > 0) {
console.log(`🧹 Limpiada ${removedCount} entradas de caché expiradas`);
}
}
// Llamar automáticamente cada hora o cuando se detecte memoria baja
setInterval(() => cleanupExpiredCache(24), 60 * 60 * 1000); // Cada hora
```
---
### 🎯 Validación de Integridad de Caché
```javascript
function validateCacheIntegrity(cacheEntry) {
const requiredFields = ['timestamp', 'version', 'data'];
return requiredFields.every(field => field in cacheEntry);
}
```
---
### 🎯 Métricas de Rendimiento
```javascript
const sessionCache = {
// ... campos existentes
// Métodos auxiliares:
recordHit() { this.cache_hits++; },
recordMiss() { this.cache_misses++; },
getHitRate() { 
const total = this.cache_hits + this.cache_misses;
return total > 0 ? (this.cache_hits / total * 100).toFixed(2) : '0';
}
};
// Ejemplo de uso:
sessionCache.recordHit();
console.log(`📊 Hit rate: ${sessionCache.getHitRate()}%`);
```
---
## 📝 Referencias
- **Configuración**: `/Users/piter/.copaw/config.json`
- **Memoria diaria**: `memory/YYYY-MM-DD.md`
- **Memoria a largo plazo**: `MEMORY.md`
- **Proyectos**: `memory/projects/`
---
## 💻 IMPLEMENTACIÓN DE CACHE EN PYTHON
### 📂 Archivo de Implementación
**Ubicación**: `/Users/piter/.copaw/scripts/cache_manager.py`
**Características:**
- ✅ Sistema de caché persistente (`.copaw_cache.json`)
- ✅ Validación de integridad automática
- ✅ Limpieza automática de caché expirada (TTL 24h)
- ✅ Múltiples criterios para re-análisis
- ✅ Métricas de rendimiento (hits/misses/hit_rate)
---
### 🎯 Uso Básico
```python
from scripts.cache_manager import initialize_cache, SessionCache
# Inicializar caché
cache = initialize_cache()
# Verificar si debe re-analizar archivo
if not cache.should_re_analyze('archivo.py', last_analysis):
print('✅ Usando caché')
cache.record_hit()
else:
print('🔄 Re-analizando archivo')
cache.record_miss()
# Obtener estadísticas
stats = cache.get_stats()
print(f"Hit rate: {stats['hit_rate']}")
```
---
### 🎯 Funciones Principales
| Función | Descripción |
|---------|-------------|
| `should_re_analyze()` | Decide si debe re-analizar archivo (múltiples criterios) |
| `load_cache_if_needed()` | Carga caché con validación de integridad |
| `save_to_cache()` | Guarda análisis en caché |
| `cleanup_expired_cache()` | Limpia caché expirada automáticamente |
| `get_hit_rate()` | Obtiene tasa de aciertos en caché |
| `get_stats()` | Obtiene estadísticas completas |
---
## 📝 Referencias
- **Configuración**: `/Users/piter/.copaw/config.json`
- **Memoria diaria**: `memory/YYYY-MM-DD.md`
- **Memoria a largo plazo**: `MEMORY.md`
- **Proyectos**: `memory/projects/`
---
**Última actualización**: 13 de marzo de 2026  
**Estado**: ✅ Implementado y activo
---
## 📂 Archivos Creados/Actualizados
| Archivo | Acción | Contenido |
|---------|--------|-----------|
| **TOKEN-OPTIMIZATION.md** | ✅ Actualizado | Secciones GESTIÓN DE CONTEXTO JERÁRQUICO + ESTRATEGIA DE LECTURA + COMPRESIÓN CÓDIGO + CACHE Y REUTILIZACIÓN añadidas |
| **CHECKLIST-CONTEXTO.md** | ✅ Creado | Checklist rápido de verificación por nivel |
| **cache_manager.py** | ✅ Creado | Implementación completa en Python (10.7KB) |
---
## 🎯 Estado Final
| Aspecto | Estado | Archivo |
|---------|--------|---------|
| **NIVEL 1 (Crítico)** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **NIVEL 2 (Relevante)** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **NIVEL 3 (Específico)** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **Checklist por nivel** | ✅ Implementado | CHECKLIST-CONTEXTO.md |
| **Reglas de priorización** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **Ejemplos prácticos** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **Estrategia lectura archivos** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **Compresión código inteligente** | ✅ Implementado | TOKEN-OPTIMIZATION.md |
| **Cache y reutilización (Opción C)** | ✅ Implementado | cache_manager.py |
