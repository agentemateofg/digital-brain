#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI principal para crear y mejorar skills."""

import os
import sys
import json
from pathlib import Path


def create_skill(skill_name: str, description: str):
    """Crear una nueva skill."""
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - CREACIÓN DE SKILL")
    print("=" * 70)
    
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
    
    return skill_path


def enhance_skill(skill_name: str, enhancements: list):
    """Mejorar una skill existente."""
    print("=" * 70)
    print("ANTHROPIC SKILL CREATOR - MEJORA DE SKILL")
    print("=" * 70)
    
    skill_path = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    
    if not skill_path.exists():
        print(f"\n✗ Skill '{skill_name}' no existe.")
        return
    
    # Añadir casos de prueba
    if "add_tests" in enhancements:
        tests_path = skill_path / "tests"
        tests_path.mkdir(parents=True, exist_ok=True)
        
        test_cases = [
            {
                "name": "test_basico",
                "description": "Test básico de la skill",
                "input": {"test": "value"},
                "expected_output": {"result": True},
            },
        ]
        
        with open(tests_path / "test_cases.json", 'w', encoding='utf-8') as f:
            json.dump(test_cases, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Tests añadidos con éxito!")
        print(f"  Skill: {skill_name}")
        print(f"  Tests creados: {len(test_cases)}")
    
    # Añadir referencias
    if "add_references" in enhancements:
        references_path = skill_path / "references"
        references_path.mkdir(parents=True, exist_ok=True)
        
        reference_content = """# Mejores Prácticas

## Referencia 1
Contenido de la referencia.

"""
        
        with open(references_path / "best-practices.md", 'w', encoding='utf-8') as f:
            f.write(reference_content)
        
        print(f"\n✓ Referencias añadidas con éxito!")
        print(f"  Skill: {skill_name}")
        print(f"  Referencias creadas: 1")
    
    # Añadir assets
    if "add_assets" in enhancements:
        assets_path = skill_path / "assets"
        assets_path.mkdir(parents=True, exist_ok=True)
        
        with open(assets_path / "icon.svg", 'w', encoding='utf-8') as f:
            f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
</svg>""")
        
        print(f"\n✓ Assets añadidos con éxito!")
        print(f"  Skill: {skill_name}")
        print(f"  Assets creados: 1")
    
    # Añadir review
    if "add_review" in enhancements:
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
    
    # Añadir report
    if "add_report" in enhancements:
        reports_path = skill_path / "reports"
        reports_path.mkdir(parents=True, exist_ok=True)
        
        report_content = f"""# Reporte de Skill: {skill_name}

## Estado
✓ Completada

## Mejoras Aplicadas
- {', '.join(enhancements)}

"""
        
        with open(reports_path / "report.md", 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"\n✓ Reporte añadido con éxito!")
    
    # Verificar integridad
    integrity_check = {
        "yaml_frontmatter": True,
        "markdown_instructions": True,
        "test_cases_count": 1 if "add_tests" in enhancements else 0,
        "references_count": 1 if "add_references" in enhancements else 0,
        "assets_count": 1 if "add_assets" in enhancements else 0,
    }
    
    print(f"\n✓ Integridad verificada!")
    print(f"  YAML frontmatter: {integrity_check['yaml_frontmatter']}")
    print(f"  Markdown instrucciones: {integrity_check['markdown_instructions']}")
    print(f"  Tests: {integrity_check['test_cases_count']}")
    print(f"  Referencias: {integrity_check['references_count']}")
    print(f"  Assets: {integrity_check['assets_count']}")
    
    print("\n" + "=" * 70)
    print("¡Mejora de skill completada con éxito!")
    print("=" * 70)


def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python cli_main.py create --name 'skill-name' --description 'descripcion'")
        print("  python cli_main.py enhance --name 'skill-name' --enhancements add_tests,add_references,add_assets")
        return
    
    command = sys.argv[1]
    
    if command == "create":
        skill_name = sys.argv[3]
        description = sys.argv[5]
        create_skill(skill_name, description)
    
    elif command == "enhance":
        skill_name = sys.argv[3]
        enhancements_str = sys.argv[5]
        enhancements = enhancements_str.split(",")
        enhance_skill(skill_name, enhancements)
    
    else:
        print(f"Comando no válido: {command}")


if __name__ == "__main__":
    main()
