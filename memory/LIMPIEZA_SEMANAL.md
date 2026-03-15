# 🧹 LIMPIEZA SEMANAL - Documentación del Proceso

## 📋 RESUMEN

**Nombre:** LIMPIEZA SEMANAL  
**Frecuencia:** Cada domingo a las 4:30 AM  
**Tipo:** Optimización automática del workspace  
**Autor:** Piter (Asistente personal de Mateo)

---

## 🎯 OBJETIVO

Optimizar el workspace de forma automática manteniendo equilibrio entre:
- ✅ Ahorro de tokens (~5-10% semanal acumulado)
- ✅ Contexto preservado 100% (proyectos + docs técnicas)
- ✅ Sin saturar archivos importantes

---

## 📦 COMPONENTES

### **Script Principal**
```
📁 /Users/piter/.copaw/scripts/cleanup-weekly.sh
   ├─ Subproceso 1: AUDITO RÁPIDO
   ├─ Subproceso 2: COMPRESIÓN CONSERVADORA
   ├─ Subproceso 3: ARCHIVO HISTÓRICO
   ├─ Subproceso 4: ACTUALIZACIÓN HEARTBEAT
   ├─ Subproceso 5: VERIFICACIÓN INTEGRIDAD
   └─ Subproceso 6: REPORTE FINAL
```

### **Logs**
```
📁 /Users/piter/.copaw/logs/cleanup-weekly.log
```

---

## ⏰ CRONOGRAMA

| Hora | Día | Acción |
|------|-----|--------|
| 4:30 AM | Domingo | Ejecutar LIMPIEZA SEMANAL |

**Formato cron:** `0 4:30 * * 0` (cada domingo a las 4:30 AM)

---

## 🔄 SUBPROCESOS DETALLADOS

### **1. AUDITO RÁPIDO**
- Leer archivos principales (AGENTS.md, MEMORY.md, SOUL.md, PROFILE.md)
- Identificar nuevas redundancias
- Detectar contenido obsoleto

### **2. COMPRESIÓN CONSERVADORA**
- Eliminar duplicados claros (skills, reglas repetidas)
- Compresión de texto sin perder instrucciones clave
- Referenciar documentación técnica externa

### **3. ARCHIVO HISTÓRICO**
- Mover consolidaciones a registro diario (memory/YYYY-MM-DD.md)
- Eliminar archivos de sesión antiguos (>30 días)
- Mantener documentación técnica intacta

### **4. ACTUALIZACIÓN HEARTBEAT**
- Revisar proyectos DOM/FAM/FED/TEO por cambios recientes
- Añadir contexto nuevo a checklist
- Eliminar items obsoletos

### **5. VERIFICACIÓN INTEGRIDAD**
- Confirmar que TOKEN-OPTIMIZATION.md intacto
- Verificar memory/projects/* intactos
- Reporte de cambios realizados

### **6. REPORTE FINAL**
- Métricas de optimización
- Archivos diarios preservados
- Documentación técnica intacta

---

## 🛡️ REGLAS DE SEGURIDAD

### ✅ PERMITIDO:
- Eliminar duplicados claros entre archivos principales
- Mover contenido histórico a registro diario
- Compresión conservadora de texto
- Referencias a documentación técnica externa

### ⚠️ REQUERIR CONFIRMACIÓN:
- Eliminar archivo >30 días (si no está resumido en diario)
- Modificar TOKEN-OPTIMIZATION.md (documentación técnica)
- Eliminar memoria/projects/* (contexto proyectos)

### ❌ PROHIBIDO:
- Reducir configuración tokens (debe mantenerse original)
- Eliminar documentación técnica útil
- Tocar registros históricos diarios (memory/YYYY-MM-DD.md)

---

## 📊 ARCHIVOS INTACTOS (Nunca se tocan)

```
✅ memory/YYYY-MM-DD.md     → Registros históricos diarios
✅ memory/TOKEN-OPTIMIZATION.md  → Documentación técnica
✅ memory/CACHE-USAGE-GUIDE.md   → Documentación caché
✅ memory/CHECKLIST-CONTEXTO.md   → Checklist contexto
✅ memory/GUIDA-LECTURA-ARCHIVOS.md → Guía práctica
✅ memory/projects/*        → Contexto proyectos (DOM/FAM/FED/TEO)
```

---

## 📈 MÉTRICAS DE ÉXITO

| Métrica | Objetivo | Frecuencia |
|---------|----------|------------|
| Ahorro tokens semanal | ~5-10% acumulado | Cada semana |
| Archivos optimizados | 1-2 archivos principales | Cada semana |
| Contexto preservado | 100% (proyectos + docs técnicas) | Siempre |
| Errores de contexto overflow | 0 | Siempre |

---

## 📝 LOGS Y AUDITORÍA

### **Archivo de logs:**
```
📁 /Users/piter/.copaw/logs/cleanup-weekly.log
```

**Contenido típico:**
```
=== 🧹 LIMPIEZA SEMANAL - 2026-03-15 04:30 ===
[SUBPROCESO 1/6] 📊 AUDITO RÁPIDO...
  AGENTS.md: 8743 bytes
  MEMORY.md: 3804 bytes
  ✅ Sin duplicados de skills
[SUBPROCESO 2/6] ✂️ COMPRESIÓN CONSERVADORA...
  ✅ Sin archivos de consolidación antiguos para eliminar
[SUBPROCESO 3/6] 📁 ARCHIVO HISTÓRICO...
  ✅ memory/projects/: 4 archivos presentes
[SUBPROCESO 4/6] 🫀 ACTUALIZACIÓN HEARTBEAT...
  DOM: Actualizado 15 de marzo de 2026
  FAM: Actualizado 15 de marzo de 2026
  FED: Actualizado 15 de marzo de 2026
  TEO: Actualizado 15 de marzo de 2026
[SUBPROCESO 5/6] 🔍 VERIFICACIÓN INTEGRIDAD...
  ✅ TOKEN-OPTIMIZATION.md presente
  ✅ memory/projects/: 4 archivos presentes
  ✅ MEMORY.md referencia TOKEN-OPTIMIZATION.md
[SUBPROCESO 6/6] 📊 REPORTE FINAL...
  Tamaño total workspace: 61234 bytes
  Diarios YYYY-MM-DD.md preservados: 4
  Documentación técnica intacta: 4/4 archivos

=== ✅ LIMPIEZA SEMANAL COMPLETADA ===
Fecha: 2026-03-15 04:30:00
Estado: ÓPTIMO
```

---

## 🚀 CONFIGURACIÓN CRON JOB

### **Opción A: Dashboard CoPaw (Recomendado)**

Crear cron job en el dashboard CoPaw con:
- **Tipo:** `text`
- **Mensaje:** `🧹 Iniciar LIMPIEZA SEMANAL - Optimización workspace automática`
- **Programación:** `0 4:30 * * 0` (cada domingo a las 4:30 AM)

### **Opción B: Crontab Tradicional**

Añadir al crontab del usuario:
```bash
30 4 * * 0 /Users/piter/.copaw/scripts/cleanup-weekly.sh >> /Users/piter/.copaw/logs/cleanup-weekly.log 2>&1
```

### **Opción C: Script Shell Directo**

Ejecutar manualmente:
```bash
/Users/piter/.copaw/scripts/cleanup-weekly.sh
```

---

## 📞 NOTIFICACIONES (OPCIONAL)

Si está configurado Telegram, el script enviará notificación al completar:

```json
{
  "bot_token": "TU_TELEGRAM_BOT_TOKEN",
  "chat_id": "TU_CHAT_ID"
}
```

**Mensaje de notificación:**
```
🧹 Limpieza semanal completada

✅ Optimización automática realizada
📊 Workspace optimizado
🛡️ Contexto preservado 100%
```

---

## 🔍 VERIFICACIÓN POST-EJECUCIÓN

Después de cada ejecución, verificar:

```bash
# Verificar logs
tail -50 /Users/piter/.copaw/logs/cleanup-weekly.log

# Verificar archivos intactos
ls -lh /Users/piter/.copaw/memory/TOKEN-OPTIMIZATION.md
ls -1 /Users/piter/.copaw/memory/projects/

# Verificar tamaño workspace
du -sh /Users/piter/.copaw
```

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### **Problema: Script no se ejecuta automáticamente**
**Solución:** Verificar crontab o dashboard CoPaw
```bash
crontab -l  # Verificar crontab actual
copaw cron list  # Verificar cron jobs en dashboard
```

### **Problema: Error de permisos**
**Solución:** Hacer script ejecutable
```bash
chmod +x /Users/piter/.copaw/scripts/cleanup-weekly.sh
```

### **Problema: TOKEN-OPTIMIZATION.md eliminado por error**
**Solución:** Restaurar desde backup GitHub
```bash
git checkout HEAD~1 memory/TOKEN-OPTIMIZATION.md  # Restaurar versión anterior
```

---

## 📞 SOPORTE

Para reportar problemas o solicitar mejoras:
- Revisar logs en `/Users/piter/.copaw/logs/cleanup-weekly.log`
- Consultar documentación en `memory/`
- Contactar con Piter (asistente personal)

---

**Última actualización:** 15 de marzo de 2026  
**Versión:** 1.0  
**Estado:** ✅ Activo y optimizado
