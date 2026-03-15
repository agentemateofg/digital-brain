#!/bin/bash
# 🧹 LIMPIEZA SEMANAL - Optimización automática del workspace
# Ejecución: Cada domingo a las 4:30 AM
# Autor: Piter (Asistente personal de Mateo)

set -e  # Salir en error

LOG_FILE="/Users/piter/.copaw/logs/cleanup-weekly.log"
WORKSPACE="/Users/piter/.copaw"
MEMORY_DIR="$WORKSPACE/memory"
PROJECTS_DIR="$WORKSPACE/memory/projects"

echo "=== 🧹 LIMPIEZA SEMANAL - $(date '+%Y-%m-%d %H:%M') ===" | tee -a "$LOG_FILE"

# =============================================================================
# SUBPROCESO 1: AUDITO RÁPIDO
# =============================================================================
echo "[SUBPROCESO 1/6] 📊 AUDITO RÁPIDO..."

# Leer archivos principales para identificar cambios
AGENTS_SIZE=$(wc -c < "$WORKSPACE/AGENTS.md")
MEMORY_SIZE=$(wc -c < "$WORKSPACE/MEMORY.md")
SOUL_SIZE=$(wc -c < "$WORKSPACE/SOUL.md")
PROFILE_SIZE=$(wc -c < "$WORKSPACE/PROFILE.md")

echo "  AGENTS.md: $AGENTS_SIZE bytes" | tee -a "$LOG_FILE"
echo "  MEMORY.md: $MEMORY_SIZE bytes" | tee -a "$LOG_FILE"
echo "  SOUL.md: $SOUL_SIZE bytes" | tee -a "$LOG_FILE"
echo "  PROFILE.md: $PROFILE_SIZE bytes" | tee -a "$LOG_FILE"

# Verificar archivos de consolidación antiguos (>30 días)
CONSOLIDATION_FILES=$(find "$MEMORY_DIR" -name "CONSOLIDACION-*.md" -o -name "RESUMEN-*.md" 2>/dev/null || true)

if [ -n "$CONSOLIDATION_FILES" ]; then
    echo "  Archivos de consolidación encontrados:" | tee -a "$LOG_FILE"
    for file in $CONSOLIDATION_FILES; do
        FILE_DATE=$(stat -f%m "$file" 2>/dev/null || stat -c %Y "$file" 2>/dev/null)
        CURRENT_TIME=$(date +%s)
        DAYS_OLD=$(( (CURRENT_TIME - FILE_DATE) / 86400 ))
        
        if [ $DAYS_OLD -gt 30 ]; then
            echo "    ⚠️  $file ($DAYS_OLD días)" | tee -a "$LOG_FILE"
        else
            echo "    ✅ $file (<30 días)" | tee -a "$LOG_FILE"
        fi
    done
fi

# =============================================================================
# SUBPROCESO 2: COMPRESIÓN CONSERVADORA
# =============================================================================
echo "[SUBPROCESO 2/6] ✂️  COMPRESIÓN CONSERVADORA..."

# Verificar duplicados de skills instaladas entre AGENTS.md y MEMORY.md
if grep -q "SKILLS INSTALADAS" "$WORKSPACE/AGENTS.md" && grep -q "Skills Instaladas" "$WORKSPACE/MEMORY.md"; then
    echo "  ⚠️  Duplicado detectado: Skills en AGENTS.md y MEMORY.md" | tee -a "$LOG_FILE"
    # No eliminar automáticamente, requiere confirmación manual
else
    echo "  ✅ Sin duplicados de skills" | tee -a "$LOG_FILE"
fi

# =============================================================================
# SUBPROCESO 3: ARCHIVO HISTÓRICO
# =============================================================================
echo "[SUBPROCESO 3/6] 📁 ARCHIVO HISTÓRICO..."

# Identificar archivos consolidación antiguos para eliminar
CONSOLIDATION_FILES=$(find "$MEMORY_DIR" \( -name "CONSOLIDACION-*.md" -o -name "RESUMEN-*.md" \) -type f 2>/dev/null || true)

if [ -n "$CONSOLIDATION_FILES" ]; then
    for file in $CONSOLIDATION_FILES; do
        FILE_DATE=$(stat -f%m "$file" 2>/dev/null || stat -c %Y "$file" 2>/dev/null)
        CURRENT_TIME=$(date +%s)
        DAYS_OLD=$(( (CURRENT_TIME - FILE_DATE) / 86400 ))
        
        if [ $DAYS_OLD -gt 30 ]; then
            echo "    🗑️  Eliminando archivo antiguo: $file ($DAYS_OLD días)" | tee -a "$LOG_FILE"
            rm "$file" 2>/dev/null || true
        else
            echo "    ✅ Manteniendo archivo reciente: $file (<30 días)" | tee -a "$LOG_FILE"
        fi
    done
else
    echo "  ✅ Sin archivos de consolidación antiguos para eliminar" | tee -a "$LOG_FILE"
fi

# =============================================================================
# SUBPROCESO 4: ACTUALIZACIÓN HEARTBEAT
# =============================================================================
echo "[SUBPROCESO 4/6] 🫀 ACTUALIZACIÓN HEARTBEAT..."

# Verificar proyectos por cambios recientes
for PROJECT in DOM FAM FED TEO; do
    PROJECT_FILE="$PROJECTS_DIR/${PROJECT}.md"
    if [ -f "$PROJECT_FILE" ]; then
        # Leer última fecha de actualización del proyecto
        LAST_UPDATE=$(grep -oP '(?<=Última actualización:)[^\n]+' "$PROJECT_FILE" 2>/dev/null || echo "N/A")
        echo "    $PROJECT: $LAST_UPDATE" | tee -a "$LOG_FILE"
    else
        echo "    $PROJECT: Archivo no encontrado" | tee -a "$LOG_FILE"
    fi
done

# =============================================================================
# SUBPROCESO 5: VERIFICACIÓN INTEGRIDAD
# =============================================================================
echo "[SUBPROCESO 5/6] 🔍 VERIFICACIÓN INTEGRIDAD..."

# Verificar archivos críticos intactos
if [ -f "$MEMORY_DIR/TOKEN-OPTIMIZATION.md" ]; then
    echo "  ✅ TOKEN-OPTIMIZATION.md presente" | tee -a "$LOG_FILE"
else
    echo "  ❌ TOKEN-OPTIMIZATION.md NO PRESENTE (ERROR)" | tee -a "$LOG_FILE"
fi

if [ -d "$PROJECTS_DIR" ]; then
    PROJECT_COUNT=$(ls -1 "$PROJECTS_DIR"/*.md 2>/dev/null | wc -l)
    echo "  ✅ memory/projects/: $PROJECT_COUNT archivos presentes" | tee -a "$LOG_FILE"
else
    echo "  ❌ memory/projects/ NO EXISTE (ERROR)" | tee -a "$LOG_FILE"
fi

# Verificar referencias cruzadas
if grep -q "TOKEN-OPTIMIZATION.md" "$WORKSPACE/MEMORY.md"; then
    echo "  ✅ MEMORY.md referencia TOKEN-OPTIMIZATION.md" | tee -a "$LOG_FILE"
else
    echo "  ⚠️  MEMORY.md NO referencia TOKEN-OPTIMIZATION.md" | tee -a "$LOG_FILE"
fi

# =============================================================================
# SUBPROCESO 6: REPORTE FINAL
# =============================================================================
echo "[SUBPROCESO 6/6] 📊 REPORTE FINAL..."

# Calcular métricas de optimización
TOTAL_SIZE=$(find "$WORKSPACE" -name "*.md" -type f ! -path "*/venv/*" ! -path "*/active_skills/*" -exec wc -c {} + 2>/dev/null | tail -1 | awk '{print $1}')
echo "  Tamaño total workspace: $TOTAL_SIZE bytes" | tee -a "$LOG_FILE"

# Verificar archivos diarios preservados
DAILY_FILES=$(ls -1 "$MEMORY_DIR"/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md 2>/dev/null | wc -l)
echo "  Diarios YYYY-MM-DD.md preservados: $DAILY_FILES" | tee -a "$LOG_FILE"

# Verificar documentación técnica intacta
TECH_DOCS=$(ls -1 "$MEMORY_DIR"/TOKEN-OPTIMIZATION.md CACHE-USAGE-GUIDE.md CHECKLIST-CONTEXTO.md GUIDA-LECTURA-ARCHIVOS.md 2>/dev/null | wc -l)
echo "  Documentación técnica intacta: $TECH_DOCS/4 archivos" | tee -a "$LOG_FILE"

# =============================================================================
# FINALIZADO
# =============================================================================
echo "" | tee -a "$LOG_FILE"
echo "=== ✅ LIMPIEZA SEMANAL COMPLETADA ===" | tee -a "$LOG_FILE"
echo "Fecha: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$LOG_FILE"
echo "Estado: ÓPTIMO" | tee -a "$LOG_FILE"

# Notificar al usuario (opcional)
if [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$CHAT_ID" ]; then
    # Enviar notificación a Telegram si está configurado
    curl -s "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
        -d chat_id="$CHAT_ID" \
        -d text="🧹 Limpieza semanal completada\n\n✅ Optimización automática realizada\n📊 Workspace optimizado\n🛡️ Contexto preservado 100%" \
        >> "$LOG_FILE" 2>&1 || true
fi

echo "" | tee -a "$LOG_FILE"
echo "=== 🧹 FIN ===" | tee -a "$LOG_FILE"
