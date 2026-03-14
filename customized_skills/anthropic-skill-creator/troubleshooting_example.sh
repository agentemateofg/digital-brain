#!/bin/bash
# Ejemplo de troubleshooting de uso de anthropic-skill-creator

echo "=========================================="
echo "ANTHROPIC SKILL CREATOR - EJEMPLO TROUBLESHOOTING"
echo "=========================================="

# Paso 1: Verificar estructura del workspace
echo ""
echo "--- Paso 1: Verificar Estructura del Workspace ---"
ls -la /Users/piter/.copaw/active_skills/anthropic-skill-creator/

# Paso 2: Verificar contenido de SKILL.md
echo ""
echo "--- Paso 2: Verificar Contenido de SKILL.md ---"
cat /Users/piter/.copaw/active_skills/anthropic-skill-creator/SKILL.md

# Paso 3: Verificar configuración YAML
echo ""
echo "--- Paso 3: Verificar Configuración YAML ---"
cat /Users/piter/.copaw/active_skills/anthropic-skill-creator/config.yaml

# Paso 4: Ejecutar ejemplo básico y verificar salida
echo ""
echo "--- Paso 4: Ejecutar Ejemplo Básico ---"
python python_example.py

# Paso 5: Verificar que se crearon los archivos esperados
echo ""
echo "--- Paso 5: Verificar Archivos Creados ---"
find /Users/piter/.copaw/active_skills/anthropic-skill-creator -type f -name "*.md" | head -20

# Paso 6: Verificar que se crearon los scripts
echo ""
echo "--- Paso 6: Verificar Scripts Creados ---"
find /Users/piter/.copaw/active_skills/anthropic-skill-creator/scripts -type f 2>/dev/null || echo "Directorio scripts vacío o no existe"

# Paso 7: Verificar que se crearon las referencias
echo ""
echo "--- Paso 7: Verificar Referencias Creadas ---"
find /Users/piter/.copaw/active_skills/anthropic-skill-creator/references -type f 2>/dev/null || echo "Directorio references vacío o no existe"

# Paso 8: Verificar que se crearon los assets
echo ""
echo "--- Paso 8: Verificar Assets Creados ---"
find /Users/piter/.copaw/active_skills/anthropic-skill-creator/assets -type f 2>/dev/null || echo "Directorio assets vacío o no existe"

# Paso 9: Ejecutar ejemplo CLI y verificar salida
echo ""
echo "--- Paso 9: Ejecutar Ejemplo CLI ---"
bash cli_example.sh

# Paso 10: Verificar que se crearon los archivos adicionales
echo ""
echo "--- Paso 10: Verificar Archivos Adicionales Creados ---"
find /Users/piter/.copaw/active_skills/anthropic-skill-creator -type f -name "*.md" | head -20

# Paso 11: Revisar la skill final
echo ""
echo "--- Paso 11: Revisión Final de Skill ---"
python cli_main.py review --skill-name "skill-validador-email"

echo ""
echo "=========================================="
echo "¡Ejemplo troubleshooting completado con éxito!"
echo "=========================================="
