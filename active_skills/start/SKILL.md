---
name: start
description: 🚀 Maneja el comando /start en Telegram para mostrar ayuda e iniciar sesión
emoji: 🚀
trigger: "/start"
context: "Telegram bot commands, session initialization, help display"
---

## 🎯 Propósito

Manejar el comando `/start` en Telegram para:
- Mostrar información de ayuda al usuario
- Inicializar una nueva sesión del bot
- Presentar capacidades disponibles
- Reiniciar contexto si es necesario

## 📋 Formato de Salida

### Respuesta por defecto (primera vez)
```markdown
¡Hola! 👋 Soy Piter, tu asistente personal.

**Capacidades:**
- 🖥️ Navegación web (Marca, noticias, etc.)
- 📄 PDF: Lectura/edición de archivos
- 📊 Excel: Hojas de cálculo y fórmulas
- 📝 Word: Documentos con formato profesional
- ☔ Clima: Predicciones meteorológicas
- ⏰ Tareas programadas (cron)

**Comandos útiles:**
- `/browser <url>` - Abrir página web
- `/news` - Noticias de España hoy
- `/weather <ciudad>` - Previsión del tiempo
- `/start` - Mostrar esta ayuda

¿En qué puedo ayudarte? 🤔
```

### Respuesta en sesiones posteriores
```markdown
¡Hola de nuevo! 👋

**Sesión iniciada.** ¿Qué necesitas hacer hoy?

Puedo ayudarte con:
- Navegación web y noticias
- Gestión de archivos (PDF, Excel, Word)
- Clima y tareas programadas

¿En qué trabajamos? 🚀
```

## ⚙️ Configuración Recomendada

En `/Users/piter/.copaw/config.json`:
```json
{
  "telegram": {
    "enabled": true,
    "bot_prefix": "/",
    "filter_thinking": true,
    "allow_from": ["1350110165"]
  }
}
```

## 🧪 Casos de Prueba

### Test 1: Primer /start
**Input:** `/start`  
**Expected:** Mensaje completo con capacidades y comandos  
**Status:** ✅ Verificar que muestra toda la información

### Test 2: Segundo /start (misma sesión)
**Input:** `/start`  
**Expected:** Mensaje breve de reconfirmación  
**Status:** ✅ Verificar respuesta concisa

### Test 3: Con contexto previo
**Input:** Después de una tarea, `/start`  
**Expected:** Reconocer que hay contexto activo  
**Status:** ⚠️ Evaluar si guardar/resumir contexto primero

## 📝 Notas Importantes

- El comando `/start` puede usarse para **reiniciar sesión** (opcional)
- Si el usuario quiere mantener contexto, no borrar automáticamente
- Considerar guardar resumen de conversación antes de reiniciar
