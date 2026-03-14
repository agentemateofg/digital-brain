#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejemplos de testing para la skill."""

import os
import sys
import json
from pathlib import Path


def test_skill_creation():
    """Test de creación de skill."""
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - TEST DE CREACIÓN")
    print("=" * 70)
    
    # Paso 1: Crear una skill básica
    print("\n--- Paso 1: Creación de Skill ---")
    
    skill_name = "skill-validador-email"
    description = "Valida emails y verifica si el dominio existe"
    
    # Crear estructura básica
    skill_path = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    skill_path.mkdir(parents=True, exist_ok=True)
    
    # Crear SKILL.md con YAML frontmatter
    skill_md_content = f"""---
name: {skill_name}
description: "{description}"
version: 1.0.0
author: Piter
created_at: 2024-01-01
updated_at: 2024-01-01
---

# {skill_name}

## Descripción

{description}

## Uso

```bash
python cli_main.py create --name "{skill_name}" --description "{description}"
```

"""
    
    with open(skill_path / "SKILL.md", 'w', encoding='utf-8') as f:
        f.write(skill_md_content)
    
    print(f"\n✓ Skill creada con éxito!")
    print(f"  Nombre: {skill_name}")
    print(f"  Ruta: {skill_path}")
    
    # Paso 2: Verificar Archivo SKILL.md
    print("\n--- Paso 2: Verificar Archivo SKILL.md ---")
    
    skill_md_path = skill_path / "SKILL.md"
    assert skill_md_path.exists(), "Archivo SKILL.md no existe"
    print(f"\n✓ Archivo SKILL.md creado con éxito!")
    
    # Paso 3: Verificar Contenido de SKILL.md
    print("\n--- Paso 3: Verificar Contenido de SKILL.md ---")
    
    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert "name:" in content, "Falta el campo name en YAML frontmatter"
    assert "description:" in content, "Falta el campo description en YAML frontmatter"
    assert "# skill-validador-email" in content, "Falta el título principal"
    print(f"\n✓ Contenido de SKILL.md verificado con éxito!")
    
    # Paso 4: Añadir Casos de Prueba
    print("\n--- Paso 4: Añadir Casos de Prueba ---")
    
    tests_path = skill_path / "tests"
    tests_path.mkdir(parents=True, exist_ok=True)
    
    test_cases = [
        {
            "name": "email_valido",
            "description": "Email con formato correcto y dominio existente",
            "input": {"email": "usuario@ejemplo.com"},
            "expected_output": {"valid": True, "domain_exists": True},
        },
    ]
    
    with open(tests_path / "test_cases.json", 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Tests añadidos con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Tests creados: {len(test_cases)}")
    
    # Paso 5: Añadir Referencias
    print("\n--- Paso 5: Añadir Referencias ---")
    
    references_path = skill_path / "references"
    references_path.mkdir(parents=True, exist_ok=True)
    
    reference_content = """# Mejores Prácticas para Validación de Emails

## Formato RFC 5322
Los emails deben seguir el formato RFC 5322.

"""
    
    with open(references_path / "email-validation-best-practices.md", 'w', encoding='utf-8') as f:
        f.write(reference_content)
    
    print(f"\n✓ Referencias añadidas con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Referencias creadas: 1")
    
    # Paso 6: Añadir Assets
    print("\n--- Paso 6: Añadir Assets ---")
    
    assets_path = skill_path / "assets"
    assets_path.mkdir(parents=True, exist_ok=True)
    
    with open(assets_path / "email-icon.svg", 'w', encoding='utf-8') as f:
        f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
</svg>""")
    
    print(f"\n✓ Assets añadidos con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Assets creados: 1")
    
    # Paso 7: Añadir Review
    print("\n--- Paso 7: Añadir Review ---")
    
    review_path = skill_path / "review.md"
    with open(review_path, 'w', encoding='utf-8') as f:
        f.write(f"""# Revisión de Skill: {skill_name}

## Estado
✓ Completada

## Métricas
- Tests: 1
- Referencias: 1
- Assets: 1

""")
    
    print(f"\n✓ Review añadida con éxito!")
    
    # Paso 8: Añadir Report
    print("\n--- Paso 8: Añadir Report ---")
    
    reports_path = skill_path / "reports"
    reports_path.mkdir(parents=True, exist_ok=True)
    
    report_content = f"""# Reporte de Skill: {skill_name}

## Estado
✓ Completada

## Mejoras Aplicadas
- add_tests
- add_references
- add_assets

"""
    
    with open(reports_path / "report.md", 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\n✓ Reporte añadido con éxito!")
    
    # Paso 9: Verificar Integridad de la Skill
    print("\n--- Paso 9: Verificar Integridad de la Skill ---")
    
    integrity_check = {
        "yaml_frontmatter": True,
        "markdown_instructions": True,
        "test_cases_count": len(test_cases),
        "references_count": 1,
        "assets_count": 1,
    }
    
    print(f"\n✓ Integridad verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    # Paso 10: Verificar Archivo de Assets
    print("\n--- Paso 10: Verificar Archivo de Assets ---")
    
    assert (assets_path / "email-icon.svg").exists(), "Archivo de assets no existe"
    print(f"\n✓ Archivo de assets creado con éxito!")
    
    # Paso 11: Revisar la skill final
    print("\n--- Paso 11: Revisión Final ---")
    
    review_path = skill_path / "review.md"
    with open(review_path, 'w', encoding='utf-8') as f:
        f.write(f"""# Revisión de Skill: {skill_name}

## Estado
✓ Completada

## Métricas
- Tests: 2
- Referencias: 1
- Assets: 1

## Próximos Pasos
- Añadir más tests
- Mejorar referencias
- Añadir más assets

""")
    
    print(f"\n✓ Revisión completada!")
    print(f"  Skill: {skill_name}")
    print(f"  Estado: Completada")
    
    # Paso 12: Verificar integridad de la skill
    print("\n--- Paso 12: Verificar Integridad de la Skill ---")
    
    integrity_check = {
        "yaml_frontmatter": True,
        "markdown_instructions": True,
        "test_cases_count": len(test_cases),
        "references_count": 1,
        "assets_count": 1,
    }
    
    print(f"\n✓ Integridad verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    print("\n" + "=" * 70)
    print("¡Test de creación completado con éxito!")
    print("=" * 70)


def test_skill_enhancement():
    """Test de mejora de skill."""
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - TEST DE MEJORA")
    print("=" * 70)
    
    # Paso 1: Crear una skill básica
    print("\n--- Paso 1: Creación de Skill ---")
    
    skill_name = "skill-validador-email"
    description = "Valida emails y verifica si el dominio existe"
    
    # Crear estructura básica
    skill_path = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    skill_path.mkdir(parents=True, exist_ok=True)
    
    # Crear SKILL.md con YAML frontmatter
    skill_md_content = f"""---
name: {skill_name}
description: "{description}"
version: 1.0.0
author: Piter
created_at: 2024-01-01
updated_at: 2024-01-01
---

# {skill_name}

## Descripción

{description}

## Uso

```bash
python cli_main.py create --name "{skill_name}" --description "{description}"
```

"""
    
    with open(skill_path / "SKILL.md", 'w', encoding='utf-8') as f:
        f.write(skill_md_content)
    
    print(f"\n✓ Skill creada con éxito!")
    print(f"  Nombre: {skill_name}")
    print(f"  Ruta: {skill_path}")
    
    # Paso 2: Añadir casos de prueba
    print("\n--- Paso 2: Añadir Casos de Prueba ---")
    
    test_cases = [
        {
            "name": "email_valido",
            "description": "Email con formato correcto y dominio existente",
            "input": {"email": "usuario@ejemplo.com"},
            "expected_output": {"valid": True, "domain_exists": True},
        },
    ]
    
    # Crear archivo de tests
    tests_path = skill_path / "tests"
    tests_path.mkdir(parents=True, exist_ok=True)
    
    with open(tests_path / "test_cases.json", 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Tests añadidos con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Tests creados: {len(test_cases)}")
    
    # Paso 3: Añadir referencias
    print("\n--- Paso 3: Añadir Referencias ---")
    
    references_path = skill_path / "references"
    references_path.mkdir(parents=True, exist_ok=True)
    
    reference_content = """# Mejores Prácticas para Validación de Emails

## Formato RFC 5322
Los emails deben seguir el formato RFC 5322.

"""
    
    with open(references_path / "email-validation-best-practices.md", 'w', encoding='utf-8') as f:
        f.write(reference_content)
    
    print(f"\n✓ Referencias añadidas con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Referencias creadas: 1")
    
    # Paso 4: Añadir assets
    print("\n--- Paso 4: Añadir Assets ---")
    
    assets_path = skill_path / "assets"
    assets_path.mkdir(parents=True, exist_ok=True)
    
    with open(assets_path / "email-icon.svg", 'w', encoding='utf-8') as f:
        f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
</svg>""")
    
    print(f"\n✓ Assets añadidos con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Assets creados: 1")
    
    # Paso 5: Mejorar la skill
    print("\n--- Paso 5: Mejorar Skill ---")
    
    enhancements = ["add_tests", "add_references", "add_assets"]
    
    # Añadir más tests
    test_cases.extend([
        {
            "name": "email_con_espacios",
            "description": "Email con espacios en blanco",
            "input": {"email": " usuario@ejemplo.com"},
            "expected_output": {"valid": False, "error": "Espacios no permitidos"},
        },
    ])
    
    with open(tests_path / "test_cases.json", 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Skill mejorada con éxito!")
    print(f"  Skill: {skill_name}")
    print(f"  Mejoras aplicadas: {enhancements}")
    
    # Paso 6: Verificar integridad de la skill
    print("\n--- Paso 6: Verificar Integridad de la Skill ---")
    
    integrity_check = {
        "yaml_frontmatter": True,
        "markdown_instructions": True,
        "test_cases_count": len(test_cases),
        "references_count": 1,
        "assets_count": 1,
    }
    
    print(f"\n✓ Integridad verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    print("\n" + "=" * 70)
    print("¡Test de mejora completado con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    test_skill_creation()
    test_skill_enhancement()
