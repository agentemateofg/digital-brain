# 🧠 MEMORY.md - Memoria Curada del Sistema

## 🛡️ Reglas de Seguridad (OBLIGATORIO) ⭐⭐⭐

| Regla | Acción | Ejemplo |
|-------|--------|---------|
| **ARGUMENTOS REQUERIDOS** | write_file() siempre con file_path + content | `write_file(file_path="/path.md", content="...")` |
| **VERIFICAR ANTES ESCRIBIR** | if not file_exists() → create, else edit | Verificar antes de modificar archivos |
| **EDIT_FILE PARA CAMBIOS PEQUEÑOS** | old_text + new_text | `edit_file(file_path="/path.md", old="x", new="y")` |

## 🛠️ Skills Instaladas (10)

| Skill | Propósito | Ubicación |
|-------|-----------|-----------|
| xlsx | Hojas de cálculo | `/active_skills/xlsx/SKILL.md` |
| pdf | Manipulación PDFs | `/active_skills/pdf/SKILL.md` |
| browser_visible | Navegador visible | `/active_skills/browser_visible/SKILL.md` |
| news | Noticias | `/active_skills/news/SKILL.md` |
| pptx | Presentaciones | `/active_skills/pptx/SKILL.md` |
| file_reader | Leer texto | `/active_skills/file_reader/SKILL.md` |
| docx | Documentos Word | `/active_skills/docx/SKILL.md` |
| cron | Tareas programadas | `/active_skills/cron/SKILL.md` |
| skill-creator | Crear skills | `/active_skills/skill-creator/SKILL.md` |

## 📚 Documentación del Sistema (Leer cuando necesites)

- **TOKEN-OPTIMIZATION.md** → Sistema completo de optimización tokens (documentación técnica detallada)
- **CHECKLIST-CONTEXTO.md** → Checklist por nivel de contexto
- **GUIDA-LECTURA-ARCHIVOS.md** → Guía práctica lectura archivos
- **CACHE-USAGE-GUIDE.md** → Uso del sistema de caché

📌 Nota: Esta sección resume lo esencial. Para detalles técnicos completos, ver TOKEN-OPTIMIZATION.md.

## 🎯 Configuración Activa

```json
{
  "max_input_length": 32768,
  "memory_reserve_ratio": 0.05,
  "memory_compact_ratio": 0.6,
  "enable_tool_result_compact": true,
  "telegram_filter_thinking": true
}
```

## 📊 Métricas Clave

| Métrica | Objetivo | Estado |
|---------|----------|--------|
| Tokens/respuesta | <10k | ⚠️ Monitorizar |
| Errores overflow | 0 | ✅ Configurado |
| Tiempo respuesta | <30s | ⚠️ Mejorar |

## 🎯 REGLAS DE COMPORTAMIENTO (Configuración Actual)

### **1. USAR SKILLS CUANDO SEA POSIBLE** ⭐
- ✅ Priorizar skills para tareas especializadas
- ✅ Verificar skill antes de procesar manualmente
- ✅ Ejemplos: pdf, xlsx, docx, weather, browser_visible, etc.

### **2. DETENER Y PREGUNTAR AL SEGUNDO INTENTO FALLIDO** ⚠️
- ✅ Detener proceso después de 2 fallos consecutivos
- ✅ Preguntar al usuario qué hacer
- ✅ Ofrecer alternativas cuando sea posible
- ⚠️ Excepciones: errores triviales, conocidos, o transitorios

### **3. COMPRESIÓN CONSERVADORA**
- ✅ Eliminar redundancias sin perder contexto
- ✅ Mantener documentación técnica intacta
- ✅ Referenciar archivos externos en lugar de duplicar

### **4. CONTEXTUALIZACIÓN PROYECTOS**
- ✅ Verificar DOM/FAM/FED/TEO antes de actuar
- ✅ No asumir información sin consultar memoria

### **5. SINCERIDAD EN ERRORES**
- ✅ Reportar errores claramente con causa raíz
- ✅ Ofrecer alternativas cuando sea posible

---

**Fecha configuración:** 15 de marzo de 2026  
**Estado:** ✅ Activo y funcionando| Ahorro lectura archivos | ~70% | ✅ Activo |

## 📁 Proyectos Principales (Referencia Rápida)

- **DOM** → Club Voleibol San Martiño (Dompodomo, Ourense)
- **FAM** → Familia M (Mónica, Moni)
- **FED** → Federación Galega de Voleibol (Director competiciones)
- **TEO** → Personal (intereses, aprendizaje, proyectos individuales)

---

**Última actualización**: 15 de marzo de 2026  
**Tamaño optimizado**: ~2KB (reducido de ~8KB) ✅
**Backup GitHub**: https://github.com/agentemateofg/digital-brain (commit diario a las 5:30 AM)
**Cron Job**: `30 5 * * *` - Backup automático diario a las 5:30 AM

## 📅 Comparativa Cron Jobs

| Característica | Crontab Tradicional | Dashboard CoPaw |
|----------------|---------------------|------------------|
| **Ubicación** | Archivos sistema (`~/.crontab`) | Base datos CoPaw |
| **Formato** | Expresión cron + comando shell | JSON spec (tipo: text/agent) |
| **Gestión** | CLI (`crontab -e`) | Web UI + `copaw cron` |
| **Logs** | Manual (redirección stdout) | Integrado CoPaw |
| **Integración** | Sistema operativo | Agent + canales (Telegram/Discord) |
| **Tipos de tareas** | Cualquier comando shell | Text/Agent (mensajes/preguntas) |

### Configuración Actual
```bash
# Crontab tradicional (CONFIGURADO para backups Git)
30 5 * * * /Users/piter/.copaw/scripts/backup-digital-brain.sh >> /Users/piter/.copaw/logs/backup.log 2>&1

# Dashboard CoPaw (para tareas de agente: notificaciones, preguntas al agente)
```

### Recomendación
- **Para backups Git**: Crontab tradicional ✅ (más flexible para comandos arbitrarios)
- **Para notificaciones/agentes**: Dashboard CoPaw ✅ (integrado con canales)
