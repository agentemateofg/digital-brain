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

- **TOKEN-OPTIMIZATION.md** → Sistema completo de optimización tokens
- **CHECKLIST-CONTEXTO.md** → Checklist por nivel de contexto
- **GUIDA-LECTURA-ARCHIVOS.md** → Guía práctica lectura archivos
- **CACHE-USAGE-GUIDE.md** → Uso del sistema de caché

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
| Ahorro lectura archivos | ~70% | ✅ Activo |

## 📁 Proyectos Principales (Referencia Rápida)

- **DOM** → Club Voleibol San Martiño (Dompodomo, Ourense)
- **FAM** → Familia M (Mónica, Moni)
- **FED** → Federación Galega de Voleibol (Director competiciones)
- **TEO** → Personal (intereses, aprendizaje, proyectos individuales)

---

**Última actualización**: 14 de marzo de 2026  
**Tamaño optimizado**: ~2KB (reducido de ~8KB) ✅
**Backup GitHub**: https://github.com/agentemateofg/digital-brain (commit diario a las 5:30 AM)
**Cron Job**: `30 5 * * *` - Backup automático diario a las 5:30 AM
