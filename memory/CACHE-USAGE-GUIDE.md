# Guía de Uso del Sistema de Caché
## 🎯 Cuándo usar caché:
### ✅ RECOMENDADO (Activar caché):
1. **Archivos modificados en las últimas 2h**
```python
if not cache.should_re_analyze('archivo.py', last_analysis):
# Usar caché
```
2. **Archivos grandes (>500 líneas)**
```python
# Archivos grandes se benefician de caché
if len(content.split('\n')) > 500:
cache.save_to_cache('archivo.py', analysis)
```
3. **Tareas repetitivas (mismo archivo, misma función)**
```python
# Múltiples llamadas al mismo análisis
for i in range(10):
if not cache.should_re_analyze('utils.py', last_analysis):
data = cache.load_cache_if_needed('utils.py')
```
4. **Proyectos grandes (>10 archivos)**
```python
# Proyectos con muchos archivos se benefician de caché
if len(files) > 10:
enable_cache = True
```
---
## ❌ Cuándo NO usar caché:
### ⚠️ NO RECOMENDADO (Forzar re-análisis):
1. **Primera sesión del día**
```python
# El sistema detecta automáticamente y muestra mensaje
if cache.is_first_session():
print('🆕 Primera sesión, usando análisis completo')
```
2. **Consultas simples ("2+2", "suma 5+3")**
```python
# No vale la pena cachear consultas triviales
if task_type == "simple_calculation":
enable_cache = False
```
3. **Archivos pequeños (<100 líneas)**
```python
# El overhead de caché no compensa el ahorro
if len(content.split('\n')) < 100:
enable_cache = False
```
4. **Errores críticos que requieren análisis completo**
```python
# Errores en producción necesitan análisis completo
if task_context.get('is_critical_error'):
enable_cache = False
```
5. **Archivos con cambios recientes (git diff)**
```python
# Si hay cambios no detectados, forzar re-análisis
if git_has_uncommitted_changes(file_path):
enable_cache = False
```
---
## 📊 Métricas a Monitorizar:
### Hit Rate (Tasa de aciertos)
| Hit Rate | Estado | Acción |
|----------|--------|--------|
| **> 70%** | ✅ Excelente | Sistema funcionando bien |
| **50-70%** | 🟡 Bueno | Funcionando correctamente |
| **30-50%** | 🟠 Marginal | Revisar políticas de expiración |
| **< 30%** | 🔴 Malo | Revisar configuración de caché |
### Ejemplo de consulta de métricas:
```python
stats = cache.get_stats()
print(f"📊 Estadísticas de caché:")
print(f"   Hits: {stats['hits']}")
print(f"   Misses: {stats['misses']}")
print(f"   Hit rate: {stats['hit_rate']}")
print(f"   Archivos analizados: {stats['analyzed_files_count']}")
print(f"   Primera sesión: {stats['is_first_session']}")
```
---
## 🧹 Limpieza Automática de Caché
### Política de Expiración (TTL)
- **Por defecto**: 24 horas
- **Archivos grandes (>1000 líneas)**: Re-analizar cada 24h
- **Archivos críticos (config.json, package.json)**: Siempre re-analizar
### Ejemplo de limpieza manual:
```python
# Limpiar caché expirada (cada hora automáticamente)
cache.cleanup_expired_cache(max_age_hours=24)
# Verificar cuántos archivos eliminados
removed = cache.cleanup_expired_cache(24)
print(f'🧹 Eliminados {removed} archivos de caché')
```
---
## 🎯 Configuración Recomendada
### Para proyectos pequeños (<10 archivos):
```python
cache = initialize_cache()
# Desactivar caché para consultas simples
if task_type in ["simple_calculation", "quick_question"]:
enable_cache = False
```
### Para proyectos medianos (10-50 archivos):
```python
cache = initialize_cache()
# Activar caché por defecto
enable_cache = True
# Expiración 24h
cleanup_interval_hours = 24
```
### Para proyectos grandes (>50 archivos):
```python
cache = initialize_cache()
# Activar caché agresivamente
enable_cache = True
# Expiración más corta (12h) para mantener frescura
cleanup_interval_hours = 12
```
---
## 📈 Mejores Prácticas
### ✅ DO's (Lo que debes hacer):
1. **Monitorizar hit rate regularmente**
```python
stats = cache.get_stats()
if float(stats['hit_rate']) < 50:
print('⚠️ Hit rate bajo, revisar configuración')
```
2. **Limpiar caché manualmente cada día**
```python
# Ejecutar al inicio del día
cache.cleanup_expired_cache(24)
```
3. **Forzar re-análisis en errores críticos**
```python
if task_context.get('is_critical'):
force_re_analyze = True
```
### ❌ DON'Ts (Lo que no debes hacer):
1. **No confiar ciegamente en caché**
```python
# MAL:
data = cache.load_cache_if_needed('archivo.py')  # Sin validación
# BIEN:
if not cache.should_re_analyze('archivo.py', last_analysis):
data = cache.load_cache_if_needed('archivo.py')
else:
# Re-analizar
pass
```
2. **No ignorar mensajes de primera sesión**
```python
# MAL:
if cache.is_first_session():
pass  # Ignorar mensaje
# BIEN:
if cache.is_first_session():
print('🆕 Primera sesión, usando análisis completo')
```
3. **No dejar caché sin limpieza**
```python
# MAL:
# Nunca limpiar caché
# BIEN:
# Limpiar cada hora o cuando se detecta memoria baja
cache.cleanup_expired_cache(24)
```
---
## 🚨 Solución de Problemas Comunes
### Problema 1: Hit rate muy bajo (<30%)
**Causas posibles:**
- Archivos expirados sin re-analizar
- Política de expiración demasiado agresiva
- Errores en validación de caché
**Solución:**
```python
# Aumentar tiempo de expiración
cache.cleanup_expired_cache(max_age_hours=48)
# Verificar integridad de caché
if not validate_cache_integrity(cached_data):
print('⚠️ Caché inválida, recargando...')
```
### Problema 2: Memoria excesiva en caché
**Causas posibles:**
- Archivos grandes guardados sin compresión
- No se limpian archivos expirados
**Solución:**
```python
# Limpiar caché agresivamente
cache.cleanup_expired_cache(max_age_hours=12)
# Comprimir datos grandes antes de guardar
compressed = compress_if_large(data, max_size_bytes=50000)
```
### Problema 3: Errores al cargar caché
**Causas posibles:**
- Caché corrupta o inválida
- Cambios en sistema de archivos no detectados
**Solución:**
```python
# Forzar re-análisis si hay errores
if not cache.load_cache_if_needed(cache_key):
print('⚠️ Error al cargar caché, re-analizando...')
# Re-analizar archivo
```
---
## 📝 Referencias
- **Documentación principal**: `memory/TOKEN-OPTIMIZATION.md`
- **Implementación caché**: `scripts/cache_manager.py`
- **Configuración activa**: `/Users/piter/.copaw/config.json`
---
**Última actualización**: 13 de marzo de 2026  
**Estado**: ✅ Activo y en uso
