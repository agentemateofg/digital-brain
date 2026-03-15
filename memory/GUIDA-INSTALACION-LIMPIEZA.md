# 🧹 LIMPIEZA SEMANAL - Guía de Instalación del Cron Job

## ✅ IMPLEMENTACIÓN COMPLETADA

### **Componentes Creados:**

1. **Script Principal:**
   ```
   📁 /Users/piter/.copaw/scripts/cleanup-weekly.sh
   └─ 7281 bytes (ejecutable)
   ```

2. **Documentación:**
   ```
   📁 /Users/piter/.copaw/memory/LIMPIEZA_SEMANAL.md
   └─ 6708 bytes (guía completa)
   ```

3. **Backup en GitHub:**
   ```
   ✅ Commit: "Limpieza semanal: Script y documentación"
   📦 Repositorio: https://github.com/agentemateofg/digital-brain.git
   ```

---

## ⏰ CONFIGURACIÓN CRON JOB (Dashboard CoPaw)

### **Opción A: Dashboard CoPaw (Recomendado)**

**URL del Dashboard:** http://localhost:50971

**Pasos para crear el cron job:**

1. **Abrir Dashboard CoPaw:**
   ```bash
   # En tu navegador, accede a:
   http://localhost:50971
   ```

2. **Navegar a sección de Cron Jobs:**
   - Buscar menú "Cron Jobs" o "Scheduled Tasks"
   - Click en "Create New Job" o "+"

3. **Configurar nuevo cron job:**
   ```json
   {
     "type": "text",
     "message": "🧹 Iniciar LIMPIEZA SEMANAL - Optimización workspace automática",
     "schedule": "0 4:30 * * 0",
     "description": "Limpieza semanal automática del workspace"
   }
   ```

4. **Guardar y activar:**
   - Click en "Save" o "Create"
   - Confirmar que el cron job aparece en la lista activa

5. **Verificar estado:**
   - El cron job debería aparecer con estado "Active"
   - Próxima ejecución: Domingo siguiente a las 4:30 AM

---

### **Opción B: Crontab Tradicional (Alternativa)**

Si prefieres usar crontab del sistema operativo:

```bash
# Añadir al crontab del usuario:
crontab -e

# Pegar esta línea:
30 4 * * 0 /Users/piter/.copaw/scripts/cleanup-weekly.sh >> /Users/piter/.copaw/logs/cleanup-weekly.log 2>&1

# Guardar y salir (Ctrl+X, luego Y para confirmar)
```

**Explicación de la línea:**
- `30 4` → 4:30 AM
- `* * 0` → Cada domingo (último día del mes = 0)
- `/Users/piter/.copaw/scripts/cleanup-weekly.sh` → Script a ejecutar
- `>> /Users/piter/.copaw/logs/cleanup-weekly.log 2>&1` → Redirigir logs

---

### **Opción C: Manual con Recordatorio (Mínima intervención)**

Crear un cron job de recordatorio solo:

```json
{
  "type": "text",
  "message": "🧹 Recordatorio: Ejecutar LIMPIEZA SEMANAL hoy (domingo 4:30 AM)",
  "schedule": "0 4:30 * * 0"
}
```

El agente te preguntará si quieres ejecutar la limpieza.

---

## 📋 VERIFICACIÓN POST-INSTALACIÓN

### **1. Verificar que el cron job está activo:**

**Dashboard CoPaw:**
```
Cron Jobs → Listado de tareas activas
→ Deberías ver: "LIMPIEZA SEMANAL" con estado "Active"
```

**Crontab tradicional:**
```bash
crontab -l
# Debería mostrar la línea del cleanup-weekly.sh
```

### **2. Verificar logs de ejecución:**

```bash
tail -50 /Users/piter/.copaw/logs/cleanup-weekly.log
```

**Salida esperada:**
```
=== 🧹 LIMPIEZA SEMANAL - 2026-03-XX 04:30 ===
[SUBPROCESO 1/6] 📊 AUDITO RÁPIDO...
  AGENTS.md: 8743 bytes
  MEMORY.md: 3804 bytes
  ✅ Sin duplicados de skills
[SUBPROCESO 2/6] ✂️ COMPRESIÓN CONSERVADORA...
  ✅ Sin archivos de consolidación antiguos para eliminar
[SUBPROCESO 3/6] 📁 ARCHIVO HISTÓRICO...
  ✅ memory/projects/: 4 archivos presentes
[SUBPROCESO 4/6] 🫀 ACTUALIZACIÓN HEARTBEAT...
[SUBPROCESO 5/6] 🔍 VERIFICACIÓN INTEGRIDAD...
  ✅ TOKEN-OPTIMIZATION.md presente
[SUBPROCESO 6/6] 📊 REPORTE FINAL...
=== ✅ LIMPIEZA SEMANAL COMPLETADA ===
```

### **3. Verificar archivos intactos:**

```bash
# Confirmar que no se tocaron archivos importantes:
ls -lh /Users/piter/.copaw/memory/TOKEN-OPTIMIZATION.md
ls -1 /Users/piter/.copaw/memory/projects/
ls -1 /Users/piter/.copaw/memory/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md
```

**Salida esperada:**
```
-rw-r--r--@  1 piter  staff   20K Mar 14 14:48 TOKEN-OPTIMIZATION.md
DOM.md  FAM.md  FED.md  TEO.md
2025-01-06.md  2026-03-13.md  2026-03-15.md
```

---

## 📊 MÉTRICAS DE ÉXITO

| Métrica | Objetivo | Frecuencia |
|---------|----------|------------|
| Ahorro tokens semanal | ~5-10% acumulado | Cada semana |
| Archivos optimizados | 1-2 archivos principales | Cada semana |
| Contexto preservado | 100% (proyectos + docs técnicas) | Siempre |
| Errores de contexto overflow | 0 | Siempre |

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

## 📞 SOPORTE Y AJUSTES

### **Si el cron job no se ejecuta:**

1. **Verificar logs del sistema:**
   ```bash
   tail -100 /Users/piter/.copaw/copaw.log
   ```

2. **Reiniciar CoPaw app:**
   ```bash
   # Detener:
   killall copaw
   
   # Iniciar:
   /Users/piter/.copaw/venv/bin/copaw app
   ```

3. **Verificar crontab:**
   ```bash
   crontab -l
   crontab -r  # Eliminar si hay errores
   crontab -e  # Reconfigurar
   ```

### **Si quieres ajustar la frecuencia:**

**Cambiar a cada lunes (en lugar de domingo):**
```json
"schedule": "0 4:30 * * 1"  # Lunes = 1
```

**Cambiar a cada viernes:**
```json
"schedule": "0 4:30 * * 5"  # Viernes = 5
```

**Ejecutar todos los días (no recomendado):**
```json
"schedule": "0 4:30 * * *"  # Todos los días
```

---

## 📦 ARCHIVOS CREADOS

```
📁 /Users/piter/.copaw/scripts/cleanup-weekly.sh      ✅ Script principal
📁 /Users/piter/.copaw/memory/LIMPIEZA_SEMANAL.md     ✅ Documentación completa
📁 /Users/piter/.copaw/logs/cleanup-weekly.log        ✅ Logs de ejecución
```

---

## 🎯 PRÓXIMOS PASOS

1. **Configurar cron job en Dashboard CoPaw** (Opción A - Recomendada)
2. **Verificar que el cron job está activo** en la lista de tareas
3. **Esperar próximo domingo a las 4:30 AM** para primera ejecución automática
4. **Revisar logs** después de la primera ejecución para confirmar funcionamiento

---

## 📞 CONTACTO

Para reportar problemas o solicitar ajustes:
- Revisar logs en `/Users/piter/.copaw/logs/cleanup-weekly.log`
- Consultar documentación en `memory/LIMPIEZA_SEMANAL.md`
- Contactar con Piter (asistente personal)

---

**Instalación completada:** 15 de marzo de 2026  
**Estado:** ✅ Listo para configurar cron job  
**Próxima ejecución automática:** Domingo siguiente a las 4:30 AM
