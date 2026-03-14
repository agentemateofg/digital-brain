# -*- coding: utf-8 -*-
"""Skill para crear nuevas skills en el entorno de Piter.

Esta skill ayuda a definir propósito, contexto de activación, formato de salida
y casos de prueba para nuevas skills. Sigue los principios de la skill original
pero adaptada al estilo y estructura de CoPaw.
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any

from agentscope import Message, Role


def create_skill(
    name: str,
    description: str,
    context: str | None = None,
    output_format: str = "markdown",
) -> dict[str, Any]:
    """Crea una nueva skill con estructura básica.

    Args:
        name: Nombre de la skill (sin prefijo 'skill-')
        description: Descripción breve de la funcionalidad
        context: Contexto adicional sobre cuándo activar esta skill
        output_format: Formato de salida ('markdown' o 'yaml')

    Returns:
        Ruta del archivo SKILL.md creado
    """
    # Normalizar nombre (añadir prefijo si no existe)
    if not name.startswith("skill-"):
        name = f"skill-{name}"

    skill_dir = Path(f"/Users/piter/.copaw/active_skills/{name}")
    
    # Crear directorio de la skill
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # Escribir SKILL.md
    skillembedding_path = skill_dir / "SKILL.md"
    
    if output_format == "yaml":
        content = _generate_yaml_skill(name, description, context)
    else:
        content = _generate_markdown_skill(name, description, context)
    
    with open(skillembedding_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return {
        "status": "created",
        "skill_name": name,
        "path": str(skillembedding_path),
        "content_preview": content[:500] + "..." if len(content) > 500 else content,
    }


def enhance_skill(
    skill_name: str,
    enhancements: list[str],
    context: str | None = None,
) -> dict[str, Any]:
    """Mejora una skill existente con nuevas funcionalidades.

    Args:
        skill_name: Nombre de la skill (con prefijo 'skill-')
        enhancements: Lista de mejoras a añadir
            - "add_tests": Añadir casos de prueba
            - "add_references": Añadir documentación de referencia
            - "add_assets": Añadir plantillas/iconos/fuentes
            - "update_instructions": Actualizar instrucciones principales
        context: Contexto adicional sobre las mejoras

    Returns:
        Resumen de las mejoras aplicadas
    """
    skill_dir = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    
    if not skill_dir.exists():
        return {
            "status": "error",
            "message": f"Skill '{skill_name}' no existe. Usa create_skill primero.",
        }
    
    skillembedding_path = skill_dir / "SKILL.md"
    
    # Leer contenido actual
    with open(skillembedding_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Aplicar mejoras
    updated_content = content
    
    if "add_tests" in enhancements:
        updated_content += "\n\n## Casos de prueba\n\nAñade casos de prueba para validar la skill:\n\n```python\ndef test_skill():\n    # Implementa tests aquí\n    pass\n```\n\nEjecuta los tests con:\n```bash\npytest /Users/piter/.copaw/active_skills/{skill_name}/test_*.py\n```"
    
    if "add_references" in enhancements:
        refs_dir = skill_dir / "references"
        refs_dir.mkdir(exist_ok=True)
        
        # Crear archivo de referencia genérico
        ref_path = refs_dir / "README.md"
        with open(ref_path, "w", encoding="utf-8") as f:
            f.write(f"# Referencias para {skill_name}\n\nAñade aquí documentación de contexto relevante.\n\n## Recursos recomendados\n\n- [Documentación oficial](https://example.com/docs)\n- [Ejemplos de uso](https://example.com/examples)\n")
        
        updated_content += f"\n\n### Referencias\nVer `/Users/piter/.copaw/active_skills/{skill_name}/references/README.md`"
    
    if "add_assets" in enhancements:
        assets_dir = skill_dir / "assets"
        assets_dir.mkdir(exist_ok=True)
        
        # Crear directorios para diferentes tipos de assets
        (assets_dir / "scripts").mkdir(exist_ok=True)
        (assets_dir / "templates").mkdir(exist_ok=True)
        (assets_dir / "icons").mkdir(exist_ok=True)
        
        updated_content += f"\n\n### Assets\nVer `/Users/piter/.copaw/active_skills/{skill_name}/assets/`"
    
    if "update_instructions" in enhancements:
        # Actualizar sección de instrucciones principales
        if "## Instrucciones" not in updated_content:
            updated_content = updated_content.replace(
                "# -*- coding: utf-8 -*-\n\"\"\"",
                "# -*- coding: utf-8 -*-\n\"\"\"\n## Instrucciones\n\n",
                1,
            )
    
    # Escribir contenido actualizado
    with open(skillembedding_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    return {
        "status": "enhanced",
        "skill_name": skill_name,
        "path": str(skillembedding_path),
        "enhancements_applied": enhancements,
    }


def add_tests(
    skill_name: str,
    test_cases: list[dict[str, Any]],
) -> dict[str, Any]:
    """Añade casos de prueba a una skill existente.

    Args:
        skill_name: Nombre de la skill (con prefijo 'skill-')
        test_cases: Lista de casos de prueba con estructura:
            {
                "name": "nombre del test",
                "description": "Descripción breve",
                "input": {"param1": "valor"},
                "expected_output": "resultado esperado",
                "steps": ["paso 1", "paso 2"]
            }

    Returns:
        Resumen de los tests añadidos
    """
    skill_dir = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    
    if not skill_dir.exists():
        return {
            "status": "error",
            "message": f"Skill '{skill_name}' no existe.",
        }
    
    tests_file = skill_dir / "test_skill.py"
    
    # Generar contenido de tests
    test_content = "# -*- coding: utf-8 -*-\n\"\"\"\nCasos de prueba para la skill {name}.\n\nGenerado automáticamente por anthropic-skill-creator.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport pytest\n\n\n@pytest.mark.integration\ndef test_{name}_basic():\n    \"\"\"Test básico de la skill.\"\"\"\n    # Implementa el test aquí\n    pass\n\n\n@pytest.mark.integration\ndef test_{name}_edge_case():\n    \"\"\"Test de caso límite.\"\"\"\n    # Implementa el test aquí\n    pass\n"
    
    for i, test_case in enumerate(test_cases):
        test_name = test_case.get("name", f"test_{i}")
        description = test_case.get("description", "")
        
        test_content += f"\n\n@pytest.mark.integration\ndef test_{test_name}():\n    \"\"\"{description}\"\"\"\n    # Implementa el test aquí\n    pass\n"
    
    with open(tests_file, "w", encoding="utf-8") as f:
        f.write(test_content)
    
    return {
        "status": "tests_added",
        "skill_name": skill_name,
        "path": str(tests_file),
        "test_cases_count": len(test_cases),
    }


def review_skill(skill_name: str) -> dict[str, Any]:
    """Revisa y actualiza la documentación de una skill.

    Args:
        skill_name: Nombre de la skill (con prefijo 'skill-')

    Returns:
        Resumen del estado actual de la skill
    """
    skill_dir = Path(f"/Users/piter/.copaw/active_skills/{skill_name}")
    
    if not skill_dir.exists():
        return {
            "status": "error",
            "message": f"Skill '{skill_name}' no existe.",
        }
    
    skillembedding_path = skill_dir / "SKILL.md"
    
    # Leer contenido actual
    with open(skillembedding_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Analizar estructura
    has_yaml_frontmatter = "# -*- coding:" in content
    has_markdown_instructions = "## Instrucciones" in content or "## Activación" in content
    
    # Generar resumen
    summary = {
        "status": "reviewed",
        "skill_name": skill_name,
        "path": str(skillembedding_path),
        "has_yaml_frontmatter": has_yaml_frontmatter,
        "has_markdown_instructions": has_markdown_instructions,
        "content_length": len(content),
    }
    
    # Sugerencias de mejora
    suggestions = []
    if not has_yaml_frontmatter:
        suggestions.append("Consider añadir YAML frontmatter con metadata")
    if not has_markdown_instructions:
        suggestions.append("Asegúrate de incluir sección '## Instrucciones' clara")
    
    if suggestions:
        summary["suggestions"] = suggestions
    
    return summary


def _generate_yaml_skill(
    name: str,
    description: str,
    context: str | None = None,
) -> str:
    """Genera contenido YAML para SKILL.md."""
    
    yaml_content = f"""# -*- coding: utf-8 -*-
name: {name}
description: "{description}"

context: {context or "Skill general-purpose"}

instructions: |
  ## Activación
  
  Se activa cuando el usuario quiere:
  - Crear una nueva skill desde cero
  - Mejorar una skill existente con más funcionalidades
  - Añadir casos de prueba a una skill
  - Revisar o actualizar la documentación de una skill
  
  ## Flujo de trabajo
  
  1. Capturar la intención del usuario (qué skill quiere crear/mejorar)
  2. Entrevistar sobre:
     - Casos límite y escenarios especiales
     - Formatos de salida esperados
     - Recursos necesarios (scripts, references, assets)
  3. Escribir SKILL.md inicial con YAML frontmatter + markdown instructions
  4. Crear casos de prueba y ejecutar iterativamente
  5. Evaluar feedback del usuario
  6. Iterar hasta satisfacción
  
  ## Principios clave
  
  - **Descripción específica**: Ser "empujón" para evitar subactivación
  - **Carga progresiva**: Metadata → SKILL.md body → recursos empaquetados
  - **Principio de sorpresa cero**: No malware, no contenido malicioso
  - **Idioma español**: Todo el contenido en español
  - **Formatos definidos**: Especificar estructuras exactas para outputs verificables
  
  ## Estructura recomendada
  
  ```
  skill-name/
  ├── SKILL.md (requerido)
  │   ├── YAML frontmatter (name, description requeridos)
  │   └── Markdown instrucciones
  └── Recursos empaquetados (opcional)
      ├── scripts/    - Código ejecutable
      ├── references/ - Docs de contexto
      └── assets/     - Plantillas/iconos/fuentes
  ```

"""
    return yaml_content


def _generate_markdown_skill(
    name: str,
    description: str,
    context: str | None = None,
) -> str:
    """Genera contenido Markdown para SKILL.md."""
    
    markdown_content = f"""# -*- coding: utf-8 -*-
\"\"\"Skill para crear nuevas skills en el entorno de Piter.

Esta skill ayuda a definir propósito, contexto de activación, formato de salida
y casos de prueba para nuevas skills. Sigue los principios de la skill original
pero adaptada al estilo y estructura de CoPaw.

## Activación

Se activa cuando el usuario quiere:
- Crear una nueva skill desde cero
- Mejorar una skill existente con más funcionalidades
- Añadir casos de prueba a una skill
- Revisar o actualizar la documentación de una skill

## Flujo de trabajo

1. Capturar la intención del usuario (qué skill quiere crear/mejorar)
2. Entrevistar sobre:
   - Casos límite y escenarios especiales
   - Formatos de salida esperados
   - Recursos necesarios (scripts, references, assets)
3. Escribir SKILL.md inicial con YAML frontmatter + markdown instructions
4. Crear casos de prueba y ejecutar iterativamente
5. Evaluar feedback del usuario
6. Iterar hasta satisfacción

## Principios clave

- **Descripción específica**: Ser "empujón" para evitar subactivación
- **Carga progresiva**: Metadata → SKILL.md body → recursos empaquetados
- **Principio de sorpresa cero**: No malware, no contenido malicioso
- **Idioma español**: Todo el contenido en español
- **Formatos definidos**: Especificar estructuras exactas para outputs verificables

## Estructura recomendada

```
skill-name/
├── SKILL.md (requerido)
│   ├── YAML frontmatter (name, description requeridos)
│   └── Markdown instrucciones
└── Recursos empaquetados (opcional)
    ├── scripts/    - Código ejecutable
    ├── references/ - Docs de contexto
    └── assets/     - Plantillas/iconos/fuentes
```

## Métodos disponibles

- `create_skill(name: str, description: str)` → Crea una nueva skill con estructura básica
- `enhance_skill(skill_name: str, enhancements: list[str])` → Mejora una skill existente
- `add_tests(skill_name: str, test_cases: list[dict])` → Añade casos de prueba
- `review_skill(skill_name: str)` → Revisa y actualiza la documentación

## Ejemplo de uso

```python
from anthropic_skills import create_skill

create_skill(
    name="skill-nombre",
    description="Descripción breve de la funcionalidad"
)
```

\"\"\"

"""
    return markdown_content


# Función principal para invocación desde CLI o API
def main(action: str, **kwargs) -> dict[str, Any]:
    """Función principal para invocación directa.

    Args:
        action: Acción a realizar ('create', 'enhance', 'add_tests', 'review')
        **kwargs: Parámetros según la acción

    Returns:
        Resultado de la operación
    """
    actions = {
        "create": create_skill,
        "enhance": enhance_skill,
        "add_tests": add_tests,
        "review": review_skill,
    }
    
    if action not in actions:
        return {
            "status": "error",
            "message": f"Acción no válida: {action}. Opciones: {list(actions.keys())}",
        }
    
    return actions[action](**kwargs)
