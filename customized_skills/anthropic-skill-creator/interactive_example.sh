#!/bin/bash
# Ejemplo interactivo de uso de anthropic-skill-creator

echo "=========================================="
echo "ANTHROPIC SKILL CREATOR - EJEMPLO INTERACTIVO"
echo "=========================================="

# Paso 1: Crear una skill básica
echo ""
echo "--- Paso 1: Creación de Skill ---"
read -p "Nombre de la skill (ej: skill-validador-email): " skill_name
read -p "Descripción de la skill (ej: Valida emails y verifica si el dominio existe): " description

python cli_main.py create --name "$skill_name" --description "$description"

# Paso 2: Añadir casos de prueba
echo ""
echo "--- Paso 2: Añadir Casos de Prueba ---"
read -p "¿Deseas añadir casos de prueba? (s/n): " add_tests_response

if [ "$add_tests_response" = "s" ]; then
    read -p "Número de casos de prueba (ej: 3): " num_tests
    
    for i in $(seq 1 $num_tests); do
        read -p "Nombre del test (ej: email_valido): " test_name
        read -p "Descripción del test (ej: Email con formato correcto y dominio existente): " test_desc
        read -p "Input JSON (ej: {\"email\": \"usuario@ejemplo.com\"}): " test_input
        read -p "Output esperado JSON (ej: {\"valid\": true, \"domain_exists\": true}): " test_output
        
        echo "{\"name\": \"$test_name\", \"description\": \"$test_desc\", \"input\": $test_input, \"expected_output\": $test_output},"
    done
    
    # Eliminar la última coma
    sed -i '' '$ { /^$/d; s/,$// }' /dev/stdin
    
    python cli_main.py tests add \
        --skill-name "$skill_name" \
        --test-cases "$(cat)"
fi

# Paso 3: Mejorar la skill
echo ""
echo "--- Paso 3: Mejorar Skill ---"
read -p "¿Deseas mejorar la skill? (s/n): " enhance_response

if [ "$enhance_response" = "s" ]; then
    read -p "Mejoras a aplicar (add_tests,add_references,add_assets) (ej: add_tests,add_references): " enhancements
    
    python cli_main.py enhance \
        --skill-name "$skill_name" \
        --enhancements "$enhancements"
fi

# Paso 4: Revisar la skill
echo ""
echo "--- Paso 4: Revisión Final ---"
python cli_main.py review --skill-name "$skill_name"

echo ""
echo "=========================================="
echo "¡Ejemplo interactivo completado con éxito!"
echo "=========================================="
