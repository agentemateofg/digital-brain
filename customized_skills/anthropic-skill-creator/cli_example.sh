#!/bin/bash
# Ejemplo de uso de anthropic-skill-creator desde CLI

echo "=========================================="
echo "ANTHROPIC SKILL CREATOR - EJEMPLO CLI"
echo "=========================================="

# Paso 1: Crear una skill básica
echo ""
echo "--- Paso 1: Creación de Skill ---"
python cli_main.py create --name "skill-validador-email" --description "Valida emails y verifica si el dominio existe"

# Paso 2: Añadir casos de prueba
echo ""
echo "--- Paso 2: Añadir Casos de Prueba ---"
python cli_main.py tests add \
    --skill-name "skill-validador-email" \
    --test-cases '[{"name": "email_valido", "description": "Email con formato correcto y dominio existente", "input": {"email": "usuario@ejemplo.com"}, "expected_output": {"valid": true, "domain_exists": true}}, {"name": "email_invalido", "description": "Email con formato incorrecto", "input": {"email": "usuario@"}, "expected_output": {"valid": false, "error": "Formato inválido"}}]'

# Paso 3: Mejorar la skill
echo ""
echo "--- Paso 3: Mejorar Skill ---"
python cli_main.py enhance \
    --skill-name "skill-validador-email" \
    --enhancements "add_tests,add_references,add_assets"

# Paso 4: Revisar la skill
echo ""
echo "--- Paso 4: Revisión Final ---"
python cli_main.py review --skill-name "skill-validador-email"

echo ""
echo "=========================================="
echo "¡Ejemplo CLI completado con éxito!"
echo "=========================================="
