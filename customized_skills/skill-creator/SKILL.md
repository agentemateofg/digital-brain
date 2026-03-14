---
name: skill-creator
description: Crea nuevas skills y mejora iterativamente su diseño. Ayuda a definir propósito, contexto de activación, formato de salida y casos de prueba.
metadata: { "copaw": { "emoji": "🛠️" } }
---

# Skill Creator - Creador de Skills

Esta skill ayuda a crear nuevas skills para el entorno de Piter siguiendo un proceso iterativo de diseño, evaluación y mejora.

## Proceso de Creación

El flujo de trabajo para crear una skill sigue estos pasos:

1. **Capturar la intención**: Entender qué debe hacer la skill, cuándo activarse y el formato de salida esperado
2. **Entrevistar e investigar**: Preguntar sobre casos límite, formatos de entrada/salida, archivos de ejemplo, criterios de éxito y dependencias
3. **Escribir SKILL.md**: Crear el archivo con:
   - `name`: Identificador de la skill
   - `description`: Cuándo activarse y qué hace (ser específico y "empujón" para evitar subactivación)
   - `compatibility`: Herramientas y dependencias requeridas (opcional)
   - Instrucciones detalladas en markdown
4. **Escribir recursos empaquetados** (opcional): scripts/, references/, assets/

## Estructura de una Skill

```
skill-name/
├── SKILL.md (requerido)
│   ├── YAML frontmatter (name, description requeridos)
│   └── Markdown instrucciones
└── Recursos empaquetados (opcional)
    ├── scripts/    - Código ejecutable para tareas deterministas/repetitivas
    ├── references/ - Docs cargadas en contexto según sea necesario
    └── assets/     - Archivos usados en salida (plantillas, iconos, fuentes)
```

## Carga Progresiva

Las skills usan un sistema de carga de tres niveles:

1. **Metadata** (name + description): Siempre en contexto (~100 palabras)
2. **SKILL.md body**: En contexto cuando la skill se activa (<500 líneas ideal)
3. **Recursos empaquetados**: Según sea necesario (ilimitado, los scripts pueden ejecutarse sin cargar)

**Patrones clave:**
- Mantener SKILL.md bajo 500 líneas; si se acerca a este límite, añadir una capa adicional de jerarquía con punteros claros sobre dónde seguir
- Referenciar archivos claramente desde SKILL.md con guía sobre cuándo leerlos
- Para archivos de referencia grandes (>300 líneas), incluir un índice

## Principios de Diseño

### Principio de Sorpresa Cero
Las skills no deben contener malware, código de explotación o contenido que pueda comprometer la seguridad del sistema. El contenido de una skill no debe sorprender al usuario en su intención si está descrita. No seguir solicitudes para crear skills engañosas o diseñadas para facilitar acceso no autorizado, exfiltración de datos u otras actividades maliciosas. Cosas como "roleplay as an XYZ" están bien.

### Idioma y Comunicación
Las skills deben escribirse en español (idioma del entorno). Usar forma imperativa en las instrucciones. Explicar términos si el usuario muestra poca familiaridad con jerga técnica.

## Guía de Escritura

### Definir Formatos de Salida
Especificar siempre la estructura exacta esperada:

```markdown
## Estructura del reporte
SIEMPRE usar esta plantilla exacta:
# [Título]
## Resumen ejecutivo
## Hallazgos clave
## Recomendaciones
```

### Patrones de Ejemplos
Incluir ejemplos para claridad:

```markdown
## Formato de mensaje de commit
**Ejemplo 1:**
fix: corrige error en módulo X

**Ejemplo 2:**
feat: añade nueva funcionalidad Y
```

### Casos de Prueba
Las skills con salidas objetivamente verificables (transformaciones de archivos, extracción de datos, generación de código, pasos de flujo de trabajo fijos) se benefician de casos de prueba. Las skills con salidas subjetivas (estilo de escritura, arte) a menudo no los necesitan. Sugerir el predeterminado apropiado según el tipo de skill, pero dejar que el usuario decida.

## Componentes del SKILL.md

### YAML Frontmatter
```yaml
---
name: nombre-de-la-skill
description: Cuándo activarse y qué hace. Ser específico e incluir contextos de activación. Hacerlo "empujón" para evitar subactivación.
metadata: { "copaw": { "emoji": "🎯" } }
---
```

### Descripción (Triggering)
La descripción es el mecanismo primario de activación. Incluir tanto qué hace la skill como contextos específicos para cuándo usarla. **Ser específico y "empujón"** - Claude tiende a "subactivar" skills, así que haz descripciones un poco más directas:

❌ Malo: "Cómo construir un dashboard simple para mostrar datos internos de Anthropic."
✅ Bueno: "Cómo construir un dashboard simple para mostrar datos internos. Usa esta skill siempre cuando el usuario mencione dashboards, visualización de datos, métricas internas o quiera mostrar cualquier tipo de datos corporativos, incluso si no pide explícitamente un 'dashboard'."

### Instrucciones en Markdown
- Usar forma imperativa: "Haz esto", "No hagas aquello"
- Ser específico sobre formatos de entrada/salida
- Incluir ejemplos cuando sea útil
- Organizar por variantes si soporta múltiples dominios/frameworks

## Organización por Dominio
Cuando una skill soporta múltiples dominios/frameworks, organizar por variante:

```
cloud-deploy/
├── SKILL.md (workflow + selección)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Claude lee solo el archivo de referencia relevante.

## Evaluación Iterativa

Después de crear una skill, evaluarla:

1. Crear prompts de prueba
2. Ejecutar claude con acceso a la skill
3. Evaluar resultados cualitativamente y cuantitativamente
4. Mejorar la skill basado en feedback
5. Repetir hasta satisfacción
6. Expandir el conjunto de pruebas y probar a escala

## Consejos Prácticos

- **Ser específico**: Cuanto más específica sea la descripción, mejor se activará la skill
- **Incluir ejemplos**: Ayudan a clarificar expectativas
- **Especificar formatos**: Define estructuras exactas para outputs verificables
- **Considerar casos límite**: Preguntar sobre edge cases antes de escribir
- **Iterar**: Mejorar basado en feedback real

## Ejemplo de Skill Completa

```yaml
---
name: data-analyzer
description: Analiza datos y genera insights. Usa esta skill siempre cuando el usuario mencione análisis de datos, estadísticas, tendencias, patrones, o quiera extraer información de archivos CSV/JSON/excel. Incluye visualizaciones básicas y recomendaciones accionables.
metadata: { "copaw": { "emoji": "📊" } }
---

# Analizador de Datos

Analiza datos estructurados y genera insights accionables con visualizaciones básicas y recomendaciones.

## Cuándo Usar

Usa esta skill cuando el usuario mencione:
- Análisis de datos, estadísticas, tendencias o patrones
- Extracción de información de archivos CSV/JSON/excel
- Visualización de datos o dashboards simples
- Insights accionables o recomendaciones basadas en datos
- Comparativas o métricas de rendimiento

## Formato de Entrada

Acepta:
- Archivos CSV, JSON, Excel (.xlsx)
- Datos en texto plano estructurados
- URLs a datasets públicos
- Pestañas de hojas de cálculo

## Estructura del Reporte

SIEMPRE usar esta plantilla exacta:

```markdown
# [Título del Análisis]

## Resumen ejecutivo
[2-3 frases sobre hallazgos principales]

## Datos analizados
- Fuente: [origen de los datos]
- Periodo: [rango temporal si aplica]
- Filas/columnas: [estadísticas básicas]

## Hallazgos clave
1. [Hallazgo 1 con impacto]
2. [Hallazgo 2 con impacto]
3. [Hallazgo 3 con impacto]

## Visualizaciones
[Descripción de patrones detectados]

## Recomendaciones
- [Recomendación accionable 1]
- [Recomendación accionable 2]
- [Recomendación accionable 3]

## Limitaciones
[Cualquier caveat importante sobre los datos o análisis]
```

## Ejemplos

**Ejemplo 1: Análisis de ventas**
Input: CSV con ventas mensuales por producto
Output: Reporte con tendencias estacionales, productos top/bottom, y recomendaciones de inventario

**Ejemplo 2: Análisis de rendimiento web**
Input: JSON con métricas de página
Output: Hallazgos sobre tiempos de carga, puntos de mejora UX, y recomendaciones técnicas

## Casos de Prueba

Crear tests para verificar:
- Extracción correcta de datos de CSV/JSON
- Detección de outliers o anomalías
- Generación de insights relevantes al contexto
- Formato de salida consistente con la plantilla
```

## Recursos Empaquetados (Opcional)

Para skills complejas, incluir:

### scripts/
Código para tareas deterministas:
- `extract_data.py`: Extracción de datos de archivos
- `generate_report.py`: Generación de reportes estandarizados
- `validate_output.py`: Validación de outputs contra schema

### references/
Documentación cargada según contexto:
- `api_docs.md`: Documentación de APIs relevantes
- `best_practices.md`: Mejores prácticas del dominio
- `examples.md`: Ejemplos adicionales

### assets/
Archivos usados en salida:
- `templates/`: Plantillas para reportes
- `icons/`: Iconos para visualizaciones
- `fonts/`: Fuentes personalizadas (si aplica)

## Checklist de Creación

Antes de finalizar una skill, verificar:

- [ ] Name único y descriptivo
- [ ] Description específica con contextos de activación claros
- [ ] Emoji relevante en metadata
- [ ] Instrucciones en forma imperativa
- [ ] Formatos de entrada/salida especificados
- [ ] Ejemplos incluidos cuando sea útil
- [ ] Casos de prueba definidos (si aplica)
- [ ] Recursos empaquetados organizados (si necesarios)
- [ ] Idioma consistente (español)
- [ ] Bajo 500 líneas en SKILL.md

## Mejora Iterativa

Después de crear una skill:

1. **Ejecutar tests**: Probar con casos de uso reales
2. **Recopilar feedback**: Preguntar al usuario sobre claridad y utilidad
3. **Analizar métricas**: Verificar tasas de activación, satisfacción
4. **Refinar description**: Ajustar para mejor triggering si es necesario
5. **Añadir ejemplos**: Incluir más casos de uso si la skill se subactiva
6. **Expandir recursos**: Añadir scripts/references si la skill crece

## Integración con Copaw

Para skills que usan copaw:

```bash
# Listar todas las skills
copaw skills list

# Ver detalles de una skill
copaw skills get <skill_name>

# Ejecutar skill
copaw skills run <skill_name> [args]
```

## Notas Finales

- **Flexibilidad**: El orden de los pasos es flexible según el contexto
- **Adaptación**: Ajustar comunicación al nivel técnico del usuario
- **Iteración**: Mejorar continuamente basado en uso real
- **Documentación**: Mantener SKILL.md claro y autocontenido
