#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejemplo básico de uso de anthropic-skill-creator."""

from anthropic_skills import create_skill, add_tests, enhance_skill, review_skill


def main():
    """Ejecuta un ejemplo completo de creación y mejora de skill."""
    
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - EJEMPLO BÁSICO")
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
    print(f"\nContenido inicial:")
    print(result['content_preview'])
    
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
    print(f"  Ruta: {result['path']}")
    
    # Paso 3: Mejorar la skill
    print("\n--- Paso 3: Mejorar Skill ---")
    result = enhance_skill(
        skill_name="skill-validador-email",
        enhancements=["add_references", "add_assets"],
    )
    
    print(f"\n✓ Skill mejorada con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Mejoras aplicadas: {result['enhancements_applied']}")
    print(f"  Ruta: {result['path']}")
    
    # Paso 4: Revisar la skill
    print("\n--- Paso 4: Revisión Final ---")
    result = review_skill(skill_name="skill-validador-email")
    
    print(f"\n✓ Revisión completada!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Estado: {result['status']}")
    print(f"  Longitud contenido: {result['content_length']} caracteres")
    print(f"  YAML frontmatter: {result['has_yaml_frontmatter']}")
    print(f"  Instrucciones markdown: {result['has_markdown_instructions']}")
    
    if "suggestions" in result and result["suggestions"]:
        print("\nSugerencias:")
        for sug in result["suggestions"]:
            print(f"  - {sug}")
    
    print("\n" + "=" * 70)
    print("¡Ejemplo completado con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    main()
