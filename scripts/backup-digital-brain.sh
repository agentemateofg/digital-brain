#!/bin/bash
# Script de backup automático para el cerebro digital
# Ejecutado diariamente a las 5:30 AM

set -e

REPO_PATH="/Users/piter/.copaw"
COMMIT_MSG="Backup automático del cerebro digital - $(date '+%Y-%m-%d %H:%M')"

echo "🔄 Iniciando backup del cerebro digital..."
cd "$REPO_PATH"

# Añadir cambios no rastreados
git add . 2>/dev/null || true

# Hacer commit si hay cambios
if git diff --cached --quiet; then
    echo "ℹ️  No hay cambios nuevos para commit."
else
    git commit -m "$COMMIT_MSG" -q
    echo "✅ Commit realizado: $COMMIT_MSG"
fi

# Push al repositorio remoto
git push origin main -q
echo "✅ Backup completado y sincronizado con GitHub"
