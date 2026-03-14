# Anthropic Skill Creator

Skill para crear y mejorar skills siguiendo las mejores prácticas de Anthropic.

## Descripción

Esta skill ayuda a:
- Crear nuevas skills con estructura completa (SKILL.md, tests, referencias, assets)
- Mejorar skills existentes añadiendo casos de prueba, referencias y recursos
- Verificar la integridad de las skills creadas
- Generar documentación y reportes automáticos

## Uso

### Crear una nueva skill

```bash
python cli_main.py create --name "skill-nombre" --description "descripcion"
```

Ejemplo:
```bash
python cli_main.py create --name "skill-validador-email" --description "Valida emails y verifica si el dominio existe"
```

### Mejorar una skill existente

```bash
python cli_main.py enhance --name "skill-nombre" --enhancements add_tests,add_references,add_assets
```

Ejemplo:
```bash
python cli_main.py enhance --name "skill-validador-email" --enhancements add_tests,add_references,add_assets
```

### Ejecutar tests de ejemplo

```bash
python testing_example.py
```

## Estructura de una Skill

```
skill-nombre/
├── SKILL.md (requerido)
│   ├── YAML frontmatter (name, description requeridos)
│   └── Markdown instrucciones
├── tests/ (opcional)
│   └── test_cases.json
├── references/ (opcional)
│   └── documentación.md
├── assets/ (opcional)
│   ├── icon.svg
│   └── otros recursos
├── review.md (opcional)
└── reports/ (opcional)
    └── report.md
```

## Mejores Prácticas

### 1. YAML Frontmatter

Cada skill debe tener un archivo SKILL.md con YAML frontmatter:

```yaml
name: skill-nombre
description: "descripcion clara y concisa"
version: 1.0.0
author: Piter
created_at: 2024-01-01
updated_at: 2024-01-01
```

### 2. Markdown Instrucciones

Después del YAML frontmatter, incluir instrucciones claras en markdown:

```markdown
# skill-nombre

## Descripción

Descripción clara de la funcionalidad.

## Uso

Ejemplos de uso con código.

## Mejores Prácticas

Consejos y recomendaciones.
```

### 3. Casos de Prueba

Añadir casos de prueba en formato JSON:

```json
[
  {
    "name": "test_nombre",
    "description": "Descripción del test",
    "input": {"parametro": "valor"},
    "expected_output": {"resultado_esperado": true}
  }
]
```

### 4. Referencias

Incluir documentación y mejores prácticas:

```markdown
# Mejores Prácticas para [funcionalidad]

## Formato estándar
Descripción del formato.

## Ejemplos
Ejemplos de uso correcto.
```

### 5. Assets

Añadir recursos visuales o utilitarios:

- Iconos SVG
- Plantillas
- Scripts de utilidad

## Flujo de Trabajo

1. **Capturar intención**: Entender qué skill se necesita crear
2. **Entrevistar**: Preguntar sobre casos límite y formatos
3. **Escribir SKILL.md**: Crear archivo con YAML frontmatter e instrucciones
4. **Crear tests**: Añadir casos de prueba en JSON
5. **Añadir referencias**: Incluir documentación y mejores prácticas
6. **Añadir assets**: Incluir recursos visuales o utilitarios
7. **Verificar integridad**: Asegurar que todos los componentes están presentes
8. **Generar reportes**: Crear documentación del proceso

## Ejemplos de Uso

### Skill de Validación de Emails

```bash
python cli_main.py create --name "skill-validador-email" --description "Valida emails y verifica si el dominio existe"
```

Estructura resultante:
```
skill-validador-email/
├── SKILL.md
├── tests/
│   └── test_cases.json
├── references/
│   └── email-validation-best-practices.md
├── assets/
│   └── email-icon.svg
├── review.md
└── reports/
    └── report.md
```

### Skill de Formateo de Markdown

```bash
python cli_main.py create --name "skill-formateador-markdown" --description "Formatea y mejora documentos markdown"
```

## Mejoras Iterativas

Puedes mejorar una skill existente añadiendo:

- **add_tests**: Añadir más casos de prueba
- **add_references**: Añadir más documentación
- **add_assets**: Añadir más recursos

Ejemplo:
```bash
python cli_main.py enhance --name "skill-validador-email" --enhancements add_tests,add_references,add_assets
```

## Verificación de Integridad

Cada skill debe verificar que tiene:

- ✓ YAML frontmatter con name y description
- ✓ Markdown instrucciones claras
- ✓ Al menos un caso de prueba (opcional)
- ✓ Al menos una referencia (opcional)
- ✓ Al menos un asset (opcional)

## Ejecución de Tests

```bash
python testing_example.py
```

Esto ejecuta todos los tests de ejemplo y verifica que la skill funciona correctamente.

## Contribución

Para contribuir con esta skill:

1. Crea una nueva skill siguiendo el flujo de trabajo
2. Añade casos de prueba para tu skill
3. Mejora la documentación si es necesario
4. Reporta bugs o mejoras en issues

## Licencia

Esta skill está disponible bajo la licencia MIT.
