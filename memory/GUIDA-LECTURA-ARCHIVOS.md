# 📂 Guía Práctica - Estrategia de Lectura de Archivos
## 🎯 Principio Fundamental
### ❌ NO LEER ARCHIVOS "POR SI CASO"
**Regla de oro:** Solo leer bajo demanda, según el tipo de tarea.
---
## 📋 Tipos de Lectura y Ejemplos Prácticos
---
### 1️⃣ `"fix_error"` - Arreglar Error
#### ¿Cuándo usar?
Cuando hay un error que necesitas diagnosticar y solucionar.
#### Qué leer:
- ✅ Contexto del error (últimas 50 líneas donde falló)
- ✅ Stack trace si existe
- ✅ Archivos relacionados con imports
#### ❌ Qué NO leer:
- ❌ Archivo completo
- ❌ Funciones no relacionadas al error
- ❌ Configuraciones estáticas
---
#### 📝 Ejemplo Práctico
**Tarea:** "Arregla el error en config.json"
```markdown
LECTURA REQUERIDA:
✅ Últimas 50 líneas de config.json (donde está el error)
✅ Stack trace del error (si existe)
✅ Archivos que importan config.json
NO LEER:
❌ Archivo completo de config.json (1300+ líneas)
❌ Otros archivos de configuración no relacionados
```
**Resultado:** Solo 50 tokens en lugar de 1300+ ✅
---
### 2️⃣ `"understand_function"` - Entender Función
#### ¿Cuándo usar?
Cuando necesitas entender cómo funciona una función específica.
#### Qué leer:
- ✅ Firma de función + docstring
- ✅ Implementación completa de la función
- ✅ Llamadas a esta función (imports/dependencias)
#### ❌ Qué NO leer:
- ❌ Funciones no relacionadas
- ❌ Código de archivos no importados
---
#### 📝 Ejemplo Práctico
**Tarea:** "Explica qué hace la función `process_data()`"
```markdown
LECTURA REQUERIDA:
✅ Definición de process_data() + docstring (10 líneas)
✅ Implementación completa de la función (50 líneas)
✅ Archivos que importan esta función (3 archivos, 20 líneas cada uno)
NO LEER:
❌ Archivo completo del módulo (2000+ líneas)
❌ Funciones no relacionadas en el mismo archivo
```
**Resultado:** ~100 tokens en lugar de 2000+ ✅
---
### 3️⃣ `"add_feature"` - Añadir Feature
#### ¿Cuándo usar?
Cuando vas a añadir una nueva funcionalidad.
#### Qué leer:
- ✅ Sección donde se añadirá la feature
- ✅ Tests existentes si aplica
- ✅ Configuración relevante
#### ❌ Qué NO leer:
- ❌ Todo el archivo
- ❌ Código no relacionado con la feature
---
#### 📝 Ejemplo Práctico
**Tarea:** "Añade validación de email en el formulario"
```markdown
LECTURA REQUERIDA:
✅ Sección del formulario (30 líneas)
✅ Tests existentes para el formulario (15 líneas)
✅ Configuración de validación (10 líneas)
NO LEER:
❌ Archivo completo del formulario (800+ líneas)
❌ Lógica de backend no relacionada
```
**Resultado:** ~60 tokens en lugar de 800+ ✅
---
### 4️⃣ `"read_with_limit"` - Lectura General
#### ¿Cuándo usar?
Cuando necesitas entender un archivo pero no hay tipo específico.
#### Qué leer:
- ✅ Máximo 200 líneas desde el inicio
- ✅ O desde la última modificación (git blame)
#### ❌ Qué NO leer:
- ❌ Archivo completo si es muy grande (>1000 líneas)
---
#### 📝 Ejemplo Práctico
**Tarea:** "Revisa este archivo"
```markdown
LECTURA REQUERIDA:
✅ Primeras 200 líneas del archivo
✅ O últimas 200 líneas si el error está al final
NO LEER:
❌ Archivo completo (3000+ líneas)
```
**Resultado:** ~500 tokens en lugar de 3000+ ✅
---
## 🎯 Priorización de Archivos
### ✅ PREFERIR LEER:
| Prioridad | Criterio | Ejemplo |
|-----------|----------|---------|
| 🔴 **1º** | Modificado en las últimas 2h | `config.json` (modificado hace 30 min) |
| 🟠 **2º** | Mencionado en error/stack trace | `error.log: line 45` |
| 🟡 **3º** | Última modificación reciente (git) | `utils.py` (modificado ayer) |
| 🟢 **4º** | Relacionado por imports | `main.py` importa `utils.py` |
### ❌ EVITAR LEER:
| Evitar | Razón | Ejemplo |
|--------|-------|---------|
| No modificado >7 días | Probablemente no relevante | `legacy_module.py` (no tocado desde 2025) |
| Configuración estática | No cambia frecuentemente | `package.json` (solo lectura) |
| Documentación | A menos que se solicite explícitamente | `README.md`, `docs/` |
---
## 💾 Cache Inteligente
### Reglas de Caché:
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
## 📊 Comparativa de Ahorro de Tokens
| Escenario | Lectura Tradicional | Lectura Estratégica | Ahorro |
|-----------|---------------------|---------------------|--------|
| **Arreglar error** | 1300 tokens (archivo completo) | 50 tokens (contexto error) | **96% ✅** |
| **Entender función** | 2000 tokens (módulo completo) | 100 tokens (función + imports) | **95% ✅** |
| **Añadir feature** | 800 tokens (archivo completo) | 60 tokens (sección relevante) | **93% ✅** |
| **Lectura general** | 3000 tokens (archivo completo) | 500 tokens (200 líneas) | **83% ✅** |
**Ahorro promedio: ~90% de tokens** 🚀
---
## 🎯 Checklist Rápido Antes de Leer
```markdown
[ ] ¿Cuál es el tipo de tarea? (fix_error, understand_function, add_feature, general)
[ ] ¿Hay archivos modificados en las últimas 2h? → Priorizar estos
[ ] ¿El archivo ya fue leído recientemente? → Usar caché
[ ] ¿Es un archivo pequeño (<500 líneas)? → Leer completo
[ ] ¿Es un archivo grande (>2000 líneas)? → Usar estrategia específica
```
---
## 💡 Consejos Prácticos
### ✅ Buenas Prácticas:
1. **Siempre especificar el tipo de lectura** cuando sea posible
2. **Priorizar archivos modificados recientemente**
3. **Usar caché para archivos no modificados**
4. **Leer solo lo necesario para la tarea**
### ❌ Malas Prácticas:
1. Leer "por si acaso" archivos grandes
2. Ignorar el contexto de la tarea al elegir qué leer
3. No usar caché cuando hay archivos recientes en memoria
4. Leer documentación completa sin necesidad
---
## 📝 Referencias
- **Documentación principal**: `memory/TOKEN-OPTIMIZATION.md`
- **Checklist de contexto**: `memory/CHECKLIST-CONTEXTO.md`
- **Configuración activa**: `/Users/piter/.copaw/config.json`
---
**Última actualización**: 13 de marzo de 2026  
**Estado**: ✅ Activo y en uso
