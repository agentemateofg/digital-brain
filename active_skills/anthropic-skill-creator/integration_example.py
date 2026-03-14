#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejemplo de integración de anthropic-skill-creator con otros sistemas."""

import os
import json
from anthropic_skills import create_skill, add_tests, enhance_skill, review_skill


def main():
    """Ejecuta un ejemplo completo de integración de skill."""
    
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - EJEMPLO DE INTEGRACIÓN")
    print("=" * 70)
    
    # Paso 1: Crear una skill básica
    print("\n--- Paso 1: Creación de Skill ---")
    result = create_skill(
        name="skill-validador-email",
        description="Valida emails y verifica si el dominio existe",
    )
    
    print(f"\n✓ Skill creada con éxito!")
    print(f"  Nombre: {result['skill_name']}")
    print(f"  Ruta: {result['path']}")
    
    # Paso 2: Añadir casos de prueba
    print("\n--- Paso 2: Añadir Casos de Prueba ---")
    test_cases = [
        {
            "name": "email_valido",
            "description": "Email con formato correcto y dominio existente",
            "input": {"email": "usuario@ejemplo.com"},
            "expected_output": {"valid": True, "domain_exists": True},
        },
        {
            "name": "email_invalido",
            "description": "Email con formato incorrecto",
            "input": {"email": "usuario@"},
            "expected_output": {"valid": False, "error": "Formato inválido"},
        },
    ]
    
    result = add_tests(
        skill_name="skill-validador-email",
        test_cases=test_cases,
    )
    
    print(f"\n✓ Tests añadidos con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Tests creados: {result['test_cases_count']}")
    
    # Paso 3: Mejorar la skill
    print("\n--- Paso 3: Mejorar Skill ---")
    result = enhance_skill(
        skill_name="skill-validador-email",
        enhancements=["add_references", "add_assets"],
    )
    
    print(f"\n✓ Skill mejorada con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Mejoras aplicadas: {result['enhancements_applied']}")
    
    # Paso 4: Revisar la skill
    print("\n--- Paso 4: Revisión Final ---")
    result = review_skill(skill_name="skill-validador-email")
    
    print(f"\n✓ Revisión completada!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Estado: {result['status']}")
    
    # Paso 5: Exportar skill a formato JSON
    print("\n--- Paso 5: Exportar Skill a Formato JSON ---")
    export_path = "/Users/piter/.copaw/active_skills/anthropic-skill-creator/export/skill-validador-email.json"
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    
    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Skill exportada a formato JSON!")
    print(f"  Ruta: {export_path}")
    
    # Paso 6: Importar skill desde archivo JSON
    print("\n--- Paso 6: Importar Skill desde Archivo JSON ---")
    import_path = "/Users/piter/.copaw/active_skills/anthropic-skill-creator/import/skill-validador-email.json"
    os.makedirs(os.path.dirname(import_path), exist_ok=True)
    
    with open(import_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Skill importada desde archivo JSON!")
    print(f"  Ruta: {import_path}")
    
    # Paso 7: Verificar integridad de la skill
    print("\n--- Paso 7: Verificar Integridad de la Skill ---")
    integrity_check = {
        "yaml_frontmatter": result.get("has_yaml_frontmatter", False),
        "markdown_instructions": result.get("has_markdown_instructions", False),
        "test_cases_count": result.get("test_cases_count", 0),
        "references_count": result.get("references_count", 0),
        "assets_count": result.get("assets_count", 0),
    }
    
    print(f"\n✓ Integridad verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    # Paso 8: Generar documentación de la skill
    print("\n--- Paso 8: Generar Documentación de la Skill ---")
    doc_path = "/Users/piter/.copaw/active_skills/anthropic-skill-creator/docs/skill-validador-email.md"
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)
    
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(f"# {result['skill_name']}\n\n")
        f.write(f"## Descripción\n\n{result.get('description', '')}\n\n")
        f.write(f"## Tests\n\n")
        for test in result.get("test_cases", []):
            f.write(f"### {test['name']}\n\n")
            f.write(f"{test['description']}\n\n")
    
    print(f"\n✓ Documentación generada!")
    print(f"  Ruta: {doc_path}")
    
    # Paso 9: Generar report de la skill
    print("\n--- Paso 9: Generar Report de la Skill ---")
    report_path = "/Users/piter/.copaw/active_skills/anthropic-skill-creator/reports/skill-validador-email-report.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Reporte de Skill: {result['skill_name']}\n\n")
        f.write(f"## Estado\n\n")
        f.write(f"- **Nombre**: {result['skill_name']}\n")
        f.write(f"- **Descripción**: {result.get('description', '')}\n")
        f.write(f"- **Estado**: {result['status']}\n\n")
        f.write(f"## Métricas\n\n")
        f.write(f"- **Tests**: {result.get('test_cases_count', 0)}\n")
        f.write(f"- **Referencias**: {result.get('references_count', 0)}\n")
        f.write(f"- **Assets**: {result.get('assets_count', 0)}\n\n")
    
    print(f"\n✓ Reporte generado!")
    print(f"  Ruta: {report_path}")
    
    # Paso 10: Verificar integridad final
    print("\n--- Paso 10: Verificar Integridad Final ---")
    integrity_check = {
        "yaml_frontmatter": result.get("has_yaml_frontmatter", False),
        "markdown_instructions": result.get("has_markdown_instructions", False),
        "test_cases_count": result.get("test_cases_count", 0),
        "references_count": result.get("references_count", 0),
        "assets_count": result.get("assets_count", 0),
    }
    
    print(f"\n✓ Integridad final verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    print("\n" + "=" * 70)
    print("¡Ejemplo de integración completado con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    main()
