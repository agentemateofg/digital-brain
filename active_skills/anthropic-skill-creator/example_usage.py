#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejemplos de uso detallados de anthropic-skill-creator."""

from anthropic_skills import create_skill, enhance_skill, add_tests, review_skill


def ejemplo_1_creacion_basica():
    """
    EJEMPLO 1: Creación básica de una skill
    
    Crea una nueva skill con nombre y descripción.
    """
    
    print("=" * 70)
    print("EJEMPLO 1: Creación Básica")
    print("=" * 70)
    
    # Crear skill básica
    result = create_skill(
        name="skill-validador-email",
        description="Valida emails y verifica si el dominio existe",
    )
    
    print(f"\n✓ Skill creada con éxito!")
    print(f"  Nombre: {result['skill_name']}")
    print(f"  Ruta: {result['path']}")
    print(f"\nContenido inicial:")
    print(result['content_preview'])
    
    return result


def ejemplo_2_creacion_con_contexto():
    """
    EJEMPLO 2: Creación con contexto de activación
    
    Crea una skill especificando cuándo se activa.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 2: Creación con Contexto")
    print("=" * 70)
    
    # Crear skill con contexto
    result = create_skill(
        name="skill-resumen-diario",
        description="Genera un resumen diario de actividades y logros",
        context="Se activa cada mañana a las 8:00 AM o cuando el usuario solicita manual",
    )
    
    print(f"\n✓ Skill creada con contexto!")
    print(f"  Nombre: {result['skill_name']}")
    print(f"  Ruta: {result['path']}")
    print(f"\nContenido:")
    print(result['content_preview'])
    
    return result


def ejemplo_3_creacion_yaml():
    """
    EJEMPLO 3: Creación con YAML frontmatter
    
    Crea una skill con formato YAML para integración con otros sistemas.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 3: Creación con YAML Frontmatter")
    print("=" * 70)
    
    # Crear skill con YAML
    result = create_skill(
        name="skill-backup-datos",
        description="Realiza copias de seguridad automáticas de archivos importantes",
    )
    
    print(f"\n✓ Skill creada con YAML frontmatter!")
    print(f"  Nombre: {result['skill_name']}")
    print(f"  Ruta: {result['path']}")
    print(f"\nContenido:")
    print(result['content_preview'])
    
    return result


def ejemplo_4_agregar_tests():
    """
    EJEMPLO 4: Añadir casos de prueba
    
    Añade casos de prueba a una skill existente.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 4: Añadir Casos de Prueba")
    print("=" * 70)
    
    # Definir casos de prueba
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
    
    # Añadir tests
    result = add_tests(
        skill_name="skill-validador-email",
        test_cases=test_cases,
    )
    
    print(f"\n✓ Tests añadidos con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Tests creados: {result['test_cases_count']}")
    print(f"  Ruta: {result['path']}")
    
    return result


def ejemplo_5_mejorar_skill():
    """
    EJEMPLO 5: Mejorar una skill existente
    
    Añade recursos y referencias a una skill.
    """
    
    print("\n" + "=" * 70)
    print("EJEMPLO 5: Mejorar Skill Existente")
    print("=" * 70)
    
    # Mejorar skill
    result = enhance_skill(
        skill_name="skill-resumen-diario",
        enhancements=["add_tests", "add_references", "add_assets"],
    )
    
    print(f"\n✓ Skill mejorada con éxito!")
    print(f"  Skill: {result['skill_name']}")
    print(f"  Mejoras aplicadas: {result['enhancements_applied']}")
    print(f"  Ruta: {result['path']}")
    
    return result


def ejemplo_6_revisar_skill():
    """
    EJEMPLO 6: Revisar una skill
    
    Revisa y actualiza la documentación de una skill.
    """
    
    # Primero creamos la skill
    create_skill(
        name="skill-backup-datos",
        description="Realiza copias de seguridad automáticas de archivos importantes",
    )
    
    # Revisar skill
    result = review_skill(skill_name="skill-backup-datos")
    
    print("\n" + "=" * 70)
    print("EJEMPLO 6: Revisar Skill")
    print("=" * 70)
    
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
    
    return result


def ejemplo_7_flujo_completo():
    """
    EJEMPLO 7: Flujo completo de creación y mejora
    
    Demuestra el proceso completo desde la creación hasta la revisión.
    """
    
    print("=" * 70)
    print("FLUJO COMPLETO: Creación y Mejora de Skill")
    print("=" * 70)
    
    # Paso 1: Crear skill básica
    print("\n--- Paso 1: Crear skill básica ---")
    create_skill(
        name="skill-resumen-semanal",
        description="Genera un resumen semanal de actividades y logros",
    )
    
    # Paso 2: Añadir casos de prueba
    print("\n--- Paso 2: Añadir casos de prueba ---")
    add_tests(
        skill_name="skill-resumen-semanal",
        test_cases=[
            {
                "name": "semana_completa",
                "description": "Resumen con datos de toda la semana",
                "input": {"week_start": "2024-01-01", "week_end": "2024-01-07"},
                "expected_output": {"summary": str, "insights": list},
            },
        ],
    )
    
    # Paso 3: Añadir recursos
    print("\n--- Paso 3: Añadir recursos ---")
    enhance_skill(
        skill_name="skill-resumen-semanal",
        enhancements=["add_references", "add_assets"],
    )
    
    # Paso 4: Revisar estado final
    print("\n--- Paso 4: Revisión final ---")
    review_skill(skill_name="skill-resumen-semanal")
    
    print("\n" + "=" * 70)
    print("¡Flujo completado con éxito!")
    print("=" * 70)


def ejemplo_8_crear_skill_avanzada():
    """
    EJEMPLO 8: Crear una skill avanzada
    
    Crea una skill completa con todos los componentes.
    """
    
    print("=" * 70)
    print("EJEMPLO 8: Skill Avanzada Completa")
    print("=" * 70)
    
    # Paso 1: Crear skill básica
    print("\n--- Paso 1: Creación ---")
    create_skill(
        name="skill-analisis-sentimiento",
        description="Analiza el sentimiento de textos y comentarios",
        context="Se activa cuando el usuario proporciona un texto para analizar",
    )
    
    # Paso 2: Añadir casos de prueba
    print("\n--- Paso 2: Casos de Prueba ---")
    add_tests(
        skill_name="skill-analisis-sentimiento",
        test_cases=[
            {
                "name": "texto_positivo",
                "description": "Texto con sentimiento positivo",
                "input": {"text": "¡Me encanta este producto!"},
                "expected_output": {"sentiment": "positive", "confidence": 0.95},
            },
            {
                "name": "texto_negativo",
                "description": "Texto con sentimiento negativo",
                "input": {"text": "Estoy muy decepcionado"},
                "expected_output": {"sentiment": "negative", "confidence": 0.92},
            },
            {
                "name": "texto_neutro",
                "description": "Texto con sentimiento neutro",
                "input": {"text": "El producto es correcto"},
                "expected_output": {"sentiment": "neutral", "confidence": 0.88},
            },
        ],
    )
    
    # Paso 3: Añadir recursos
    print("\n--- Paso 3: Recursos ---")
    enhance_skill(
        skill_name="skill-analisis-sentimiento",
        enhancements=["add_references", "add_assets"],
    )
    
    # Paso 4: Revisar estado final
    print("\n--- Paso 4: Revisión Final ---")
    review_skill(skill_name="skill-analisis-sentimiento")
    
    print("\n" + "=" * 70)
    print("¡Skill avanzada creada con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    
    ejemplo_1_creacion_basica()
    ejemplo_2_creacion_con_contexto()
    ejemplo_3_creacion_yaml()
    ejemplo_4_agregar_tests()
    ejemplo_5_mejorar_skill()
    ejemplo_6_revisar_skill()
    ejemplo_7_flujo_completo()
    ejemplo_8_crear_skill_avanzada()
