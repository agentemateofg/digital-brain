# ✅ Checklist Rápido - Gestión Jerárquica de Contexto

## 🎯 Antes de cada llamada al LLM

---

## NIVEL 1 - CRÍTICO (Obligatorio)

```markdown
[ ] Consulta actual del usuario
[ ] Archivos directamente mencionados
[ ] Error actual si existe
```

**Regla:** Si falta alguno → ❌ No ejecutar tarea

---

## NIVEL 2 - RELEVANTE (Opcional)

```markdown
[ ] Archivos relacionados (imports, dependencias)
[ ] Contexto de conversación reciente (últimos 2-3 intercambios)
```

**Regla:** Incluir si aporta valor + hay espacio en contexto

---

## NIVEL 3 - ESPECÍFICO (Solo si aplica)

```markdown
[ ] Estructura completa del proyecto
[ ] Historial extenso de conversación
[ ] Documentación completa de dependencias
```

**Regla:** Solo incluir si es explícitamente necesario

---

## 🚨 REGLAS DE PRIORIZACIÓN

### Caso A: NIVEL 1 + NIVEL 2 > max_input_length
```
✅ Mantener NIVEL 1 completo
⚠️ Resumir NIVEL 2 a máximo 50%
❌ Eliminar NIVEL 3
```

### Caso B: NIVEL 1 + NIVEL 2 + NIVEL 3 > max_input_length
```
✅ Mantener NIVEL 1 completo
⚠️ Resumir NIVEL 2 a 30%
❌ Eliminar NIVEL 3 por defecto
```

---

## 📊 Resumen de Prioridades

| Nivel | Prioridad | Siempre? | Espacio requerido |
|-------|-----------|----------|-------------------|
| **NIVEL 1** | 🔴 Crítico | ✅ Sí | Mínimo |
| **NIVEL 2** | 🟡 Relevante | ⚠️ Opcional | Medio |
| **NIVEL 3** | 🟢 Específico | ❌ Solo si aplica | Máximo |

---

## 💡 Ejemplos Rápidos

### "Lee config.json"
```
N1: ✅ "Lee /Users/piter/.copaw/config.json"
N2: ⚠️ (opcional) Contexto reciente sobre config.json
N3: ❌ No incluir estructura completa
```

### "Analiza errores y arregla"
```
N1: ✅ Error actual + archivos mencionados
N2: ✅ Archivos relacionados con imports
N3: ⚠️ Estructura completa si es necesario
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

## 💾 CACHE Y REUTILIZACIÓN (Python Implementation)

### 📂 Archivo de Implementación

**Ubicación**: `scripts/cache_manager.py`

**Características:**
- ✅ Sistema de caché persistente (`.copaw_cache.json`)
- ✅ Validación de integridad automática
- ✅ Limpieza automática de caché expirada (TTL 24h)
- ✅ Múltiples criterios para re-análisis
- ✅ Métricas de rendimiento (hits/misses/hit_rate)

---

### 🎯 Uso Básico

```python
from scripts.cache_manager import initialize_cache

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

## 🚨 REGLAS DE PRIORIZACIÓN

### Caso A: NIVEL 1 + NIVEL 2 > max_input_length
```
✅ Mantener NIVEL 1 completo
⚠️ Resumir NIVEL 2 a máximo 50%
❌ Eliminar NIVEL 3
```

### Caso B: NIVEL 1 + NIVEL 2 + NIVEL 3 > max_input_length
```
✅ Mantener NIVEL 1 completo
⚠️ Resumir NIVEL 2 a 30%
❌ Eliminar NIVEL 3 por defecto
```

---

## 📊 Resumen de Prioridades

| Nivel | Prioridad | Siempre? | Espacio requerido |
|-------|-----------|----------|-------------------|
| **NIVEL 1** | 🔴 Crítico | ✅ Sí | Mínimo |
| **NIVEL 2** | 🟡 Relevante | ⚠️ Opcional | Medio |
| **NIVEL 3** | 🟢 Específico | ❌ Solo si aplica | Máximo |

---

## 📝 Referencias

- **Documentación principal**: `memory/TOKEN-OPTIMIZATION.md`
- **Guía de lectura estratégica**: `memory/GUIDA-LECTURA-ARCHIVOS.md`
- **Implementación caché**: `scripts/cache_manager.py`
- **Guía uso caché**: `memory/CACHE-USAGE-GUIDE.md`
- **Configuración activa**: `/Users/piter/.copaw/config.json`

---

**Última actualización**: 13 de marzo de 2026  
**Estado**: ✅ Activo y en uso con mejoras implementadas
