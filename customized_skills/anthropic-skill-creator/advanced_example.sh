#!/bin/bash
# Ejemplo avanzado de uso de anthropic-skill-creator

echo "=========================================="
echo "ANTHROPIC SKILL CREATOR - EJEMPLO AVANZADO"
echo "=========================================="

# Paso 1: Crear una skill básica con YAML frontmatter
echo ""
echo "--- Paso 1: Creación de Skill Básica ---"
python cli_main.py create \
    --name "skill-validador-email" \
    --description "Valida emails y verifica si el dominio existe"

# Paso 2: Añadir casos de prueba detallados
echo ""
echo "--- Paso 2: Añadir Casos de Prueba Detallados ---"
python cli_main.py tests add \
    --skill-name "skill-validador-email" \
    --test-cases '[
        {
            "name": "email_valido",
            "description": "Email con formato correcto y dominio existente",
            "input": {"email": "usuario@ejemplo.com"},
            "expected_output": {"valid": true, "domain_exists": true},
            "priority": "high"
        },
        {
            "name": "email_invalido_formato",
            "description": "Email con formato incorrecto",
            "input": {"email": "usuario@"},
            "expected_output": {"valid": false, "error": "Formato inválido"},
            "priority": "high"
        },
        {
            "name": "email_invalido_dominio",
            "description": "Email con dominio que no existe",
            "input": {"email": "usuario@noexiste.com"},
            "expected_output": {"valid": true, "domain_exists": false},
            "priority": "medium"
        },
        {
            "name": "email_con_espacios",
            "description": "Email con espacios en blanco",
            "input": {"email": " usuario@ejemplo.com"},
            "expected_output": {"valid": false, "error": "Espacios no permitidos"},
            "priority": "medium"
        },
        {
            "name": "email_con_caracteres_especiales",
            "description": "Email con caracteres especiales inválidos",
            "input": {"email": "usuario@ejemplo.com!"},
            "expected_output": {"valid": false, "error": "Caracteres especiales no permitidos"},
            "priority": "low"
        }
    ]'

# Paso 3: Mejorar la skill con múltiples recursos
echo ""
echo "--- Paso 3: Mejorar Skill con Recursos ---"
python cli_main.py enhance \
    --skill-name "skill-validador-email" \
    --enhancements "add_tests,add_references,add_assets"

# Paso 4: Añadir scripts de ejemplo
echo ""
echo "--- Paso 4: Añadir Scripts de Ejemplo ---"
python cli_main.py scripts add \
    --skill-name "skill-validador-email" \
    --scripts '[
        {
            "name": "validate_email.py",
            "description": "Script Python para validar emails",
            "content": "def validate_email(email):\n    import re\n    pattern = r\"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,6}\"\"\n    return bool(re.match(pattern, email))"
        },
        {
            "name": "check_domain.py",
            "description": "Script Python para verificar dominio",
            "content": "def check_domain(domain):\n    import socket\n    try:\n        socket.gethostbyname(domain)\n        return True\n    except socket.gaierror:\n        return False"
        }
    ]'

# Paso 5: Añadir referencias adicionales
echo ""
echo "--- Paso 5: Añadir Referencias Adicionales ---"
python cli_main.py references add \
    --skill-name "skill-validador-email" \
    --references '[
        {
            "name": "email-validation-best-practices.md",
            "description": "Mejores prácticas para validación de emails",
            "content": "# Mejores Prácticas para Validación de Emails\n\n## Formato RFC 5322\nLos emails deben seguir el formato RFC 5322...\n\n## Dominios DNS\nVerificar que el dominio tenga registros MX válidos..."
        },
        {
            "name": "email-security-considerations.md",
            "description": "Consideraciones de seguridad para validación de emails",
            "content": "# Consideraciones de Seguridad\n\n## Protección contra SPAM\nEvitar filtrar información sensible...\n\n## Privacidad\nNo almacenar emails en logs..."
        }
    ]'

# Paso 6: Añadir assets adicionales
echo ""
echo "--- Paso 6: Añadir Assets Adicionales ---"
python cli_main.py assets add \
    --skill-name "skill-validador-email" \
    --assets '[
        {
            "name": "email-icon.svg",
            "description": "Icono SVG para representar emails",
            "content": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\"><path d=\"M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z\"/></svg>"
        },
        {
            "name": "email-icon.png",
            "description": "Icono PNG para representar emails",
            "content": "[Base64 encoded PNG image]"
        }
    ]'

# Paso 7: Revisar la skill final
echo ""
echo "--- Paso 7: Revisión Final ---"
python cli_main.py review --skill-name "skill-validador-email"

echo ""
echo "=========================================="
echo "¡Ejemplo avanzado completado con éxito!"
echo "=========================================="
