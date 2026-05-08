# Gestión del proyecto: robot humanoide

## Propósito

Esta sección contiene la documentación relacionada  los marcos metodológicos, la distribución de tareas, los recursos necesarios y las estrategias de organización que guían el desarrollo del prototipo.

## Estructura de la documentación

```
01_Proyecto/
├── README.md (este archivo)
├── recursos_conocimientos.md
└── metodologia.md
```

## Descripción general del proyecto

La construcción de un robot humanoide constituye un desafío multidisciplinario que integra conocimientos de mecánica, electrónica, computación e inteligencia artificial. El presente proyecto representa un esfuerzo de investigación aplicada orientado al desarrollo de competencias en robótica humanoide, con potencial aplicación en trabajos de doctorado en el campo.

### Dominios integrados

El proyecto abarca cuatro dominios técnicos principales, cada uno con sus propios desafíos y requisitos específicos:

**Diseño mecánico.** El desarrollo de la estructura física del robot requiere el diseño de un esqueleto que sea simultáneamente resistente, liviano y articulado. Las estructuras deben soportar las cargas estáticas y dinámicas del sistema, permitiendo rangos de movimiento comparables a los de la anatomía humana.

**Sistemas electrónicos.** La integración de sensores, actuadores y sistemas de control demanda una arquitectura electrónica robusta. Los sensores proporcionan percepción del entorno y retroalimentación propioceptiva, mientras que los actuadores ejecutan las acciones planificadas bajo la supervisión de sistemas de control en tiempo real.

**Arquitectura de software.** El software de control coordina todos los subsistemas del robot. Incluye desde controladores de bajo nivel que gestionan actuadores individuales, hasta sistemas de alto nivel que implementan comportamientos complejos, planificación de tareas y toma de decisiones autónomas.

**Inteligencia artificial.** La incorporación de capacidades de aprendizaje automático y procesamiento inteligente permite que el robot se adapte a nuevas situaciones, mejore su desempeño con la experiencia, y ejecute tareas que requieren reconocimiento de patrones o toma de decisiones no determinística.

## Objetivos del proyecto

Los objetivos del proyecto se han estructurado para guiar el desarrollo progresivo del prototipo:

1. **Construir un prototipo funcional.** Desarrollar un robot humanoide operativo desde los fundamentos, integrando diseño, fabricación y programación.

2. **Integrar sistemas heterogéneos.** Lograr la coordinación efectiva entre subsistemas mecánicos, electrónicos y computacionales, cada uno con sus propios requisitos y restricciones.

3. **Implementar capacidades autónomas.** Desarrollar e integrar algoritmos de inteligencia artificial que permitan al robot operar de manera autónoma en tareas específicas.

4. **Generar conocimiento aplicable.** Documentar el proceso y los resultados de manera que el trabajo pueda contribuir a investigación de nivel doctoral en robótica humanoide.

## Navegación de la documentación

### Recursos y fundamentos teóricos

El documento [recursos_conocimientos.md](recursos_conocimientos.md) proporciona una revisión exhaustiva de los fundamentos teóricos y prácticos necesarios para cada área del proyecto. Incluye referencias bibliográficas, herramientas recomendadas, y conexiones con las diferentes secciones del repositorio.

### Marco metodológico

El documento [metodologia.md](metodologia.md) establece el proceso de desarrollo que se seguirá, incluyendo el modelo espiral iterativo adoptado, las fases de desarrollo, estrategias de gestión de riesgos, y criterios de evaluación.

### Implementaciones técnicas

Las carpetas numeradas del proyecto (01 a 12) contienen las implementaciones específicas de cada subsistema, con su propia documentación técnica detallada.

## Herramientas y tecnologías principales

El desarrollo del proyecto requiere un conjunto diverso de herramientas de software y componentes de hardware:

### Entorno de software

**Diseño asistido por computadora (CAD):**
- SolidWorks (entorno profesional)
- Fusion 360 (alternativa multiplataforma)
- FreeCAD (solución de código abierto)

**Desarrollo de software:**
- Python (procesamiento de alto nivel, inteligencia artificial)
- C++ (control en tiempo real)
- ROS (Robot Operating System, middleware de robótica)

**Simulación y validación:**
- Gazebo (simulación de robots en entornos 3D)
- PyBullet (motor de física)
- V-REP/CoppeliaSim (simulación multipropósito)

**Control de versiones:**
- Git (gestión de código fuente y documentación)

### Componentes de hardware

**Plataformas de procesamiento:**
- Arduino (control de bajo nivel)
- Raspberry Pi (procesamiento de nivel medio)
- Jetson Nano (procesamiento de visión e inteligencia artificial)

**Sensores:**
- Cámaras (visión computacional)
- LIDAR (mapeo y navegación)
- IMU (orientación y aceleración)
- Sensores de fuerza (retroalimentación táctil)

**Actuadores:**
- Servomotores (articulaciones con control de posición)
- Motores paso a paso (posicionamiento preciso)

**Fabricación:**
- Impresora 3D (fabricación de componentes)
- Herramientas de mecanizado CNC (componentes de precisión)

---

## Licencia

<div align="center">
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" alt="CC BY-NC-SA 4.0" width="120" height="40">
  </a>
  <br>
  <p>Este proyecto está licenciado bajo <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons BY-NC-SA 4.0</a></p>
</div>

---

<div align="center">
  <p><strong>Construyendo el futuro de la robótica, un paso a la vez</strong></p>
  <p><em>"La construcción de un robot humanoide es un proceso complejo que requiere una combinación de habilidades mecánicas, electrónicas y de programación. El resultado final puede ser un robot capaz de realizar tareas impresionantes y mejorar la vida de las personas."</em></p>
</div>


