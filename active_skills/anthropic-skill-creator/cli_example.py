#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejemplo de uso de anthropic-skill-creator desde CLI."""

import sys
from anthropic_skills import create_skill, enhance_skill, add_tests, review_skill


def main():
    """Función principal para ejecutar ejemplos desde CLI."""
    
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - EJEMPLO DE USO")
    print("=" * 70)
    
    # Ejemplo 1: Crear una skill básica
    print("\n" + "-" * 70)
    print("EJEMPLO 1: Crear una skill básica")
    print("-" * 70)
    
    result = create_skill(
        name="skill-resumen-diario",
        description="Genera un resumen diario de actividades y logros",
        context="Se activa cada mañana a las 8:00 AM o cuando el usuario solicita manual",
    )
    
    print(f"\n✓ Skill creada con éxito!")
    print(f"  Nombre: {result['skill_name']}")
    print(f"  Ruta: {result['path']}")
    print(f"\nContenido inicial:")
    print(result['content_preview'])
    
    # Ejemplo 2: Añadir casos de prueba
    print("\n" + "-" * 70)
    print("EJEMPLO 2: Añadir casos de prueba")
    print("-" * 70)
    
    test_cases = [
        {
            "name": "resumen_completo",
            "description": "Resumen con datos de todo el día anterior",
            "input": {"date": "2024-01-15"},
            "expected_output": {
                "summary": str,
                "insights": list,
                "tasks_completed": int,
            },
        },
        {
            "name": "resumen_vacio",
            "description": "Día sin actividades registradas",
            "input": {"date": "2024-01-16"},
            "expected_output": {
                "summary": "No hay actividades registradas para este día",
                "insights": [],
                "tasks_completed": 0,
            },
        },
    ]
    
    result = add_tests(
        skill_name="skill-resumen-diario",
        test_cases=test_cases,
    )
    
    print(f"\n✓ Tests añadidos con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Tests creados: {result['test_cases_count']}")
    print(f"  Ruta: {result['path']}")
    
    # Ejemplo 3: Añadir recursos y referencias
    print("\n" + "-" * 70)
    print("EJEMPLO 3: Añadir recursos y referencias")
    print("-" * 70)
    
    result = enhance_skill(
        skill_name="skill-resumen-diario",
        enhancements=["add_references", "add_assets"],
    )
    
    print(f"\n✓ Recursos añadidos con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Mejoras aplicadas: {result['enhancements_applied']}")
    print(f"  Ruta: {result['path']}")
    
    # Ejemplo 4: Revisar estado final
    print("\n" + "-" * 70)
    print("EJEMPLO 4: Revisión de skill")
    print("-" * 70)
    
    result = review_skill(skill_name="skill-resumen-diario")
    
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
    print("¡Ejemplos completados con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    main()
