# Recursos y conocimientos necesarios

## Resumen ejecutivo

El desarrollo de un robot humanoide constituye una empresa multidisciplinaria de considerable complejidad técnica. Este documento establece los fundamentos teóricos y prácticos necesarios para abordar con éxito un proyecto de esta naturaleza, organizados en doce dominios de conocimiento interrelacionados. Cada dominio se vincula con las secciones correspondientes del repositorio donde se aplican estos conocimientos, facilitando la navegación entre teoría y práctica.

El presente documento está orientado a servir como referencia técnica comprehensiva para investigadores y desarrolladores que trabajan en el campo de la robótica humanoide, con particular énfasis en los aspectos relevantes para investigación de nivel doctoral.

## Introducción: la complejidad de la robótica humanoide

La robótica humanoide representa uno de los desafíos más ambiciosos en el campo de la ingeniería y la ciencia de la computación. A diferencia de robots especializados en tareas únicas, un robot humanoide debe integrar múltiples capacidades —locomoción bípeda, manipulación diestra, percepción multimodal, y cognición artificial— en un sistema coherente y coordinado.

El proceso de desarrollo comienza con el diseño estructural: un esqueleto mecánico que debe equilibrar resistencia y peso, permitiendo rangos de movimiento comparables a los del cuerpo humano. Esta estructura debe soportar no solo su propio peso, sino también las fuerzas dinámicas generadas durante la locomoción y la manipulación de objetos.

Sobre esta base mecánica se integran los sistemas sensoriales y actuadores. Los sensores proporcionan al robot percepción de su entorno (sensores exteroceptivos) y conciencia de su propia configuración y estado (sensores propioceptivos). Los actuadores traducen decisiones computacionales en movimientos físicos bajo el control de sistemas que deben operar en tiempo real.

La capa computacional coordina estos elementos físicos mediante arquitecturas de software jerárquicas. Los controladores de bajo nivel gestionan actuadores individuales, mientras que sistemas de más alto nivel implementan planificación de movimientos, fusión sensorial, y toma de decisiones autónomas. En el nivel superior, algoritmos de inteligencia artificial permiten que el robot aprenda de la experiencia, se adapte a situaciones no previstas, y ejecute tareas que requieren reconocimiento de patrones complejos.

Finalmente, el propósito y contexto de aplicación determinan qué capacidades específicas debe desarrollar el robot. Algunos robots humanoides se orientan a la asistencia médica, otros a tareas industriales, y otros más a la investigación fundamental sobre inteligencia artificial embodied (encarnada en un cuerpo físico).

## Marco teórico: inteligencias múltiples aplicadas a la robótica

La teoría de las inteligencias múltiples propuesta por Howard Gardner (1983) ofrece un marco conceptual valioso para estructurar el desarrollo de capacidades en robots humanoides. Aunque originalmente formulada para describir la cognición humana, la teoría puede adaptarse productivamente al diseño de sistemas robóticos, ayudando a identificar qué competencias desarrollar en cada subsistema.

### Adaptación del marco teórico

La siguiente tabla sintetiza cómo cada tipo de inteligencia identificado por Gardner puede manifestarse en sistemas robóticos, junto con las competencias técnicas requeridas y las áreas que aún presentan desafíos importantes:

| Inteligencia | Manifestación en robótica | Competencias técnicas clave | Desafíos actuales |
|--------------|---------------------------|----------------------------|-------------------|
| Lingüística-verbal | Procesamiento y generación de lenguaje natural | Reconocimiento de voz, comprensión semántica, síntesis de lenguaje | Comprensión de contexto, ironía y emociones en el lenguaje |
| Lógico-matemática | Razonamiento, cálculo y resolución de problemas | Planificación algorítmica, optimización, aprendizaje automático | Razonamiento abductivo y creatividad algorítmica |
| Espacial-visual | Percepción y modelado del entorno | Reconocimiento de objetos, SLAM, simulación 3D | Comprensión contextual y anticipación de movimientos |
| Musical | Análisis y generación de patrones sonoros | Reconocimiento de ritmos, clasificación de audio, síntesis sonora | Detección de emociones y generación expresiva |
| Corporal-kinestésica | Coordinación y ejecución de movimientos físicos | Control de actuadores, coordinación multiarticulada, control háptico | Movimientos naturales, fluidos y adaptativos |
| Interpersonal | Interacción social con humanos | Detección de emociones, comunicación no verbal, colaboración | Empatía artificial y adaptación cultural |
| Intrapersonal | Autogestión y autorregulación | Evaluación de estado interno, planificación autónoma, gestión de prioridades | Metacognición artificial (conocimiento del propio conocimiento) |
| Naturalista | Reconocimiento y clasificación de entornos | Sensores ambientales, identificación de patrones naturales, análisis ecológico | Interpretación contextual y relaciones ecosistémicas |

### Aplicación al desarrollo del prototipo

Este marco teórico estructura el desarrollo de capacidades del robot a lo largo del proyecto. Cada tipo de inteligencia se mapea a subsistemas específicos del repositorio:

**Inteligencia lingüística-verbal:** Implementada en los módulos de percepción auditiva (02_Percepcion_Vision/sensores/audio/) y procesamiento de lenguaje natural (05_Aprendizaje_IA/nlp/).

**Inteligencia lógico-matemática:** Fundamental en los sistemas de planificación (04_Planificacion_Control/planificacion/) y herramientas computacionales (10_Herramientas/).

**Inteligencia espacial-visual:** Desarrollada en visión computacional (02_Percepcion_Vision/vision/) y localización y mapeo simultáneos (03_Localizacion_Mapeo/).

**Inteligencia musical:** Aplicable en procesamiento de audio (02_Percepcion_Vision/sensores/audio/) y aplicaciones creativas especializadas.

**Inteligencia corporal-kinestésica:** Pilar fundamental del control de movimiento (04_Planificacion_Control/control/) y la integración con hardware (06_Integracion_Hardware/).

**Inteligencia interpersonal:** Implementada en módulos de interacción social (05_Aprendizaje_IA/nlp/).

**Inteligencia intrapersonal:** Manifestada en sistemas de toma de decisiones autónomas y gestión de recursos internos.

**Inteligencia naturalista:** Aplicable en sensores químicos y ambientales (02_Percepcion_Vision/sensores/chemical/) para aplicaciones especializadas.

### Desarrollo progresivo por fases

El desarrollo de estas inteligencias se estructura en tres fases temporales:

**Fase 1 (fundamentos):** Prioriza las capacidades espacial-visual, corporal-kinestésica y lógico-matemática. Estas inteligencias constituyen los requisitos mínimos para que el robot pueda navegar, manipular objetos, y planificar acciones básicas.

**Fase 2 (interacción):** Incorpora las inteligencias lingüística-verbal e interpersonal, permitiendo que el robot interactúe de manera más natural con humanos mediante reconocimiento de voz y detección de emociones.

**Fase 3 (autonomía):** Desarrolla la inteligencia intrapersonal para toma de decisiones verdaderamente autónoma, complementada opcionalmente con capacidades musicales y naturalistas según las aplicaciones específicas previstas.

### Prioridades de investigación

Tres áreas presentan desafíos particularmente significativos que requieren investigación adicional:

**Metacognición (inteligencia intrapersonal):** El desarrollo de sistemas que "sepan lo que saben" requiere avances en cuantificación de incertidumbre y aprendizaje auto-supervisado.

**Empatía artificial (inteligencia interpersonal):** El reconocimiento de emociones multimodal, la adaptación cultural, y la implementación de teoría de la mente (theory of mind) permanecen como problemas abiertos.

**Comprensión pragmática del lenguaje (inteligencia lingüística):** La interpretación de ironía, sarcasmo, y el mantenimiento de contexto conversacional de largo plazo requieren modelos más sofisticados que los actuales.

### Referencias teóricas fundamentales

**Fundamentos teóricos:**
- Gardner, H. (1983). "Frames of Mind: The Theory of Multiple Intelligences"
- Dautenhahn, K. (2007). "Socially intelligent robots: dimensions of human–robot interaction"
- Breazeal, C. (2003). "Toward sociable robots"

**Aplicaciones en inteligencia artificial:**
- Multi-task learning para desarrollar múltiples inteligencias con arquitecturas compartidas
- Ensemble methods donde diferentes modelos especializados representan distintas inteligencias
- Curriculum learning para desarrollar inteligencias de manera secuencial y acumulativa


## 1. Mecánica y diseño mecánico

**Carpeta principal:** [06_Integracion_Hardware/](../06_Integracion_Hardware/)

El diseño mecánico constituye la base física sobre la cual se construyen todas las demás capacidades del robot. Esta disciplina abarca desde los principios fundamentales de la mecánica clásica hasta técnicas avanzadas de optimización estructural.

### Fundamentos teóricos de mecánica

**Mecánica clásica.** Los principios newtonianos de fuerza, movimiento y conservación de energía son fundamentales para predecir el comportamiento del robot. El análisis de estática determina cómo las estructuras soportan cargas sin movimiento, mientras que la dinámica describe cómo las fuerzas producen aceleraciones y movimientos.

**Mecánica de materiales.** La comprensión de cómo los materiales se deforman bajo carga permite diseñar estructuras que sean simultáneamente resistentes y ligeras. Conceptos como esfuerzo, deformación, módulo de Young y límites elásticos son esenciales para la selección apropiada de materiales.

### Diseño de articulaciones humanoides

Las articulaciones determinan la capacidad de movimiento del robot. El diseño debe emular los rangos y tipos de movimiento de las articulaciones humanas:

**Articulaciones de giro simple** (como codos y rodillas) permiten rotación en un solo eje. **Articulaciones esféricas** (como hombros y caderas) permiten rotación en múltiples ejes, ofreciendo mayor versatilidad pero presentando desafíos significativos en diseño y control.

El compromiso entre rango de movimiento, resistencia mecánica, y complejidad de fabricación guía las decisiones de diseño. Frecuentemente se opta por aproximaciones que sacrifican algo de versatilidad a cambio de mayor fiabilidad y facilidad de construcción.

### Modelado asistido por computadora

El diseño moderno de componentes mecánicos se realiza mediante software de CAD (diseño asistido por computadora). Estas herramientas permiten:

- Modelado paramétrico donde las dimensiones pueden ajustarse y el diseño completo se actualiza automáticamente
- Simulación de ensamblajes para verificar que los componentes encajan correctamente
- Detección de interferencias para identificar colisiones entre piezas móviles
- Generación automática de planos técnicos para fabricación

Las herramientas más utilizadas incluyen SolidWorks (entorno profesional, ampliamente usado en industria), Fusion 360 (solución multiplataforma con características avanzadas), y FreeCAD (alternativa de código abierto).

### Selección de materiales

La selección de materiales implica equilibrar múltiples propiedades: resistencia mecánica, peso, costo, facilidad de fabricación, y disponibilidad.

**Plásticos de ingeniería** (ABS, PLA, PETG, nylon) son livianos, económicos y compatibles con impresión 3D. Se emplean para carcasas, soportes y componentes no estructurales.

**Metales** (aluminio, acero, titanio) ofrecen resistencia superior y se utilizan en la estructura principal, ejes de rotación y elementos que soportan cargas elevadas. El aluminio es particularmente popular por su favorable relación resistencia-peso.

**Materiales compuestos** (fibra de carbono, fibra de vidrio) proporcionan la mejor relación resistencia-peso, pero son más costosos y requieren técnicas de fabricación especializadas. Se reservan para componentes estructurales críticos donde la minimización de peso es prioritaria.

### Cinemática y dinámica

**Cinemática directa** resuelve el problema de determinar la posición del efector final (por ejemplo, la mano) dados los ángulos de todas las articulaciones. Este problema tiene solución única y directa mediante transformaciones geométricas.

**Cinemática inversa** aborda el problema inverso: dados una posición y orientación deseadas, determinar qué ángulos articulares son necesarios. Este problema es más complejo y puede tener múltiples soluciones o ninguna. Las convenciones de Denavit-Hartenberg proporcionan un marco sistemático para resolver estos problemas.

**Dinámica** extiende el análisis cinemático incorporando fuerzas y torques. Permite calcular cuánta fuerza debe generar cada actuador para producir movimientos deseados, considerando la masa de cada segmento, la fricción en las articulaciones, y los efectos de la gravedad.

### Simulación y validación virtual

Antes de fabricar componentes físicos, la simulación permite identificar problemas potenciales:

**Análisis de elementos finitos (FEA)** divide una pieza en miles de elementos pequeños y calcula cómo se distribuyen los esfuerzos bajo diferentes cargas. Esto permite identificar puntos de concentración de esfuerzo donde podrían producirse fallas.

**Simulación física** (Gazebo, PyBullet, V-REP) permite probar el comportamiento del robot completo en entornos virtuales. Es posible experimentar con controladores y algoritmos sin riesgo de dañar hardware.

### Referencias bibliográficas

- Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2006). "Robot Modeling and Control"
- Craig, J. J. (2005). "Introduction to Robotics: Mechanics and Control"
- Murray, R. M., Li, Z., & Sastry, S. S. (1994). "A Mathematical Introduction to Robotic Manipulation"

---

## 2. Electrónica y sistemas eléctricos

**Carpeta principal:** [06_Integracion_Hardware/](../06_Integracion_Hardware/)

Los sistemas electrónicos proporcionan la infraestructura para sensar, procesar y actuar. Esta sección abarca desde fundamentos de circuitos hasta arquitecturas de control distribuido.

### Fundamentos de circuitos eléctricos

Los circuitos eléctricos se rigen por leyes fundamentales que permiten analizar y diseñar sistemas de cualquier complejidad:

**Ley de Ohm** (V = I × R) relaciona voltaje, corriente y resistencia. **Leyes de Kirchhoff** establecen que la suma de corrientes en un nodo es cero, y que la suma de voltajes en un lazo cerrado es cero. Estos principios fundamentales permiten analizar circuitos arbitrariamente complejos.

La **potencia eléctrica** (P = V × I) determina cuánta energía se consume o disipa. Este cálculo es crítico para dimensionar fuentes de alimentación y sistemas de refrigeración.

### Componentes electrónicos fundamentales

**Componentes pasivos** (resistencias, capacitores, inductores) no requieren alimentación y se utilizan para condicionar señales, filtrar ruido, y almacenar energía. **Diodos** permiten flujo de corriente en una dirección, siendo fundamentales para rectificación y protección de circuitos.

**Componentes activos** como transistores actúan como interruptores controlados electrónicamente o amplificadores de señal. Los **transistores MOSFET** son particularmente útiles para controlar cargas de potencia (motores) con señales de bajo voltaje procedentes de microcontroladores.

**Reguladores de voltaje** convierten voltajes de entrada variables o inadecuados en voltajes estables apropiados para componentes sensibles. Los reguladores lineales son simples pero ineficientes, mientras que los reguladores conmutados (buck/boost) son más eficientes para diferencias grandes de voltaje.

### Plataformas de procesamiento

Diferentes tareas requieren diferentes plataformas de procesamiento:

**Arduino** y microcontroladores similares son apropiados para control de bajo nivel: leer sensores simples, generar señales PWM para servomotores, y ejecutar bucles de control en tiempo real. Su simplicidad y gran comunidad los hacen accesibles para prototipado rápido.

**Raspberry Pi** es una computadora completa en formato compacto, capaz de ejecutar Linux y software complejo. Es apropiada para procesamiento de nivel medio: visión computacional básica, interfaz de usuario, y coordinación de sistemas.

**Nvidia Jetson** proporciona capacidades de procesamiento paralelo (GPU) optimizadas para aprendizaje profundo y visión computacional. Representa la opción de alto rendimiento para tareas que requieren procesamiento intensivo de imágenes o inferencia de redes neuronales.

### Protocolos de comunicación

La coordinación entre múltiples procesadores y dispositivos requiere protocolos de comunicación robustos:

**UART/Serial** es el protocolo más simple, apropiado para comunicación punto a punto a corta distancia.

**I2C** permite conectar múltiples dispositivos con solo dos cables, aunque a velocidades moderadas. Es común en sensores.

**SPI** ofrece velocidades superiores a costa de más conexiones, siendo preferido para dispositivos que transfieren grandes volúmenes de datos.

**CAN bus** proporciona comunicación robusta en entornos con ruido eléctrico, siendo estándar en aplicaciones automotrices.

### Actuadores y su control

**Servomotores** integran motor, reductora y controlador de posición en una unidad compacta. Se controlan mediante señales PWM (modulación por ancho de pulso) que especifican la posición angular deseada.

**Motores DC** con reductora proporcionan torques elevados y se controlan típicamente mediante puentes H que permiten invertir la dirección de rotación.

**Motores paso a paso** permiten posicionamiento preciso sin sensores de retroalimentación, avanzando en incrementos angulares discretos.

### Gestión energética

El diseño del sistema de alimentación debe considerar:

- Consumo máximo de todos los subsistemas simultáneamente activos
- Selección de baterías con capacidad y tasa de descarga apropiadas
- Regulación y distribución de voltajes a diferentes subsistemas
- Protección contra sobrecorriente, cortocircuitos y sobrecarga
- Monitoreo del estado de carga para gestión autónoma de la batería

### Referencias bibliográficas

- Horowitz, P., & Hill, W. (2015). "The Art of Electronics" (3rd ed.)
- Scherz, P., & Monk, S. (2013). "Practical Electronics for Inventors"
- Hughes, J. F. (2016). "Electric Motors and Drives: Fundamentals, Types and Applications"

---

## 3. Programación y control

**Carpetas principales:** 
- [04_Planificacion_Control/control/](../04_Planificacion_Control/control/)
- [04_Planificacion_Control/planificacion/](../04_Planificacion_Control/planificacion/)

## 3. Programación y control

**Carpetas principales:** 
- [04_Planificacion_Control/control/](../04_Planificacion_Control/control/)
- [04_Planificacion_Control/planificacion/](../04_Planificacion_Control/planificacion/)

El software de control coordina todos los elementos del robot, desde controladores de bajo nivel hasta planificación de alto nivel y toma de decisiones autónomas.

### Lenguajes de programación

Diferentes lenguajes sirven propósitos específicos en el desarrollo del robot:

**Python** se utiliza para prototipado rápido, procesamiento de alto nivel, y desarrollo de algoritmos de inteligencia artificial. Bibliotecas como NumPy y SciPy proporcionan capacidades de cálculo numérico, mientras que frameworks especializados (ROS bindings, PyBullet) facilitan la integración con otras herramientas de robótica.

**C++** es el lenguaje preferido para control en tiempo real y código que debe ejecutarse con máxima eficiencia. La implementación nativa de ROS es en C++, y muchas bibliotecas de robótica están optimizadas para este lenguaje.

**C** se emplea principalmente para programación de microcontroladores, donde el acceso directo a hardware y el control fino de recursos son críticos.

**MATLAB/Octave** son valiosos para simulación y prototipado de algoritmos de control, aunque típicamente se migra a otros lenguajes para implementación final.

### Arquitectura de software

El software de un robot se organiza típicamente en capas jerárquicas:

- **Capa de drivers de hardware:** Interfaz directa con sensores y actuadores
- **Capa de control de bajo nivel:** Algoritmos PID y control de torque
- **Capa de control de movimiento:** Cinemática y generación de trayectorias
- **Capa de planificación:** Toma de decisiones de alto nivel
- **Capa de interfaz:** Comunicación con usuarios u otros sistemas

Esta organización modular permite que diferentes componentes evolucionen independientemente y facilita la depuración de problemas específicos.

### Teoría de control

**Controladores PID** (proporcional-integral-derivativo) son fundamentales en robótica. El término proporcional reacciona a la magnitud del error actual, el integral compensa errores acumulados a lo largo del tiempo, y el derivativo anticipa la tendencia del error. La sintonización apropiada de estas tres ganancias es crucial para lograr un control estable y responsivo.

**Controladores avanzados** como LQR (regulador lineal cuadrático), MPC (control predictivo basado en modelo), y control adaptativo permiten comportamientos más sofisticados a costa de mayor complejidad computacional. Estos enfoques son especialmente valiosos cuando el sistema tiene múltiples objetivos que deben equilibrarse simultáneamente o cuando los parámetros del sistema no son conocidos con exactitud.

### ROS (Robot Operating System)

ROS proporciona infraestructura de middleware para sistemas robóticos complejos. Aunque su nombre sugiere lo contrario, no es un sistema operativo sino un framework que facilita la comunicación entre procesos, gestión de paquetes, y abstracción de hardware.

Los conceptos fundamentales de ROS incluyen:

- **Nodos:** Procesos individuales que realizan funciones específicas
- **Topics:** Canales de comunicación asíncrona entre nodos mediante paso de mensajes
- **Servicios:** Llamadas síncronas de solicitud-respuesta para interacciones que requieren confirmación
- **Acciones:** Mecanismo para tareas de larga duración con retroalimentación de progreso
- **Mensajes y parámetros:** Estructuras de datos tipadas y configuración del sistema

ROS incluye herramientas valiosas para visualización (RViz), simulación (Gazebo), grabación y reproducción de datos (rosbag), y depuración de sistemas distribuidos.

### Integración de sensores

El procesamiento de datos sensoriales típicamente sigue un pipeline estructurado:

1. **Adquisición:** Lectura de datos mediante drivers de hardware
2. **Filtrado:** Eliminación de ruido y valores atípicos
3. **Calibración:** Corrección de sesgos y no-linealidades
4. **Fusión sensorial:** Combinación de información de múltiples sensores
5. **Estimación de estado:** Determinación del estado del robot basándose en datos procesados

La fusión de sensores es particularmente importante cuando múltiples dispositivos proporcionan información complementaria o redundante. Técnicas como filtros de Kalman permiten combinar datos con diferentes niveles de incertidumbre de manera óptima.

### Referencias bibliográficas

- Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). "Introduction to Autonomous Mobile Robots"
- Thrun, S., Burgard, W., & Fox, D. (2005). "Probabilistic Robotics"
- Corke, P. (2017). "Robotics, Vision and Control: Fundamental Algorithms in MATLAB"
- Lynch, K. M., & Park, F. C. (2017). "Modern Robotics: Mechanics, Planning, and Control"

---

## Dominios adicionales de conocimiento

Debido a la extensión del material, las siguientes áreas se encuentran documentadas de forma detallada en sus carpetas correspondientes del proyecto:

**4. Percepción** ([01_Percepcion/](../01_Percepcion/)): Procesamiento de sensores visuales, auditivos, táctiles y propioceptivos. Incluye visión computacional, procesamiento de audio, y fusión sensorial.

**5. Localización y mapeo** ([02_Localizacion_Mapeo/](../02_Localizacion_Mapeo/)): Algoritmos SLAM (Simultaneous Localization and Mapping), filtros de Kalman, particle filters, y construcción de mapas del entorno.

**6. Planificación de movimientos** ([03_Planificacion/](../03_Planificacion/)): Planificación de trayectorias, evasión de obstáculos, planificación de tareas de alto nivel, y coordinación de movimientos complejos.

**7. Aprendizaje automático** ([05_Aprendizaje_Maquina/](../05_Aprendizaje_Maquina/)): Técnicas de aprendizaje supervisado y no supervisado, aprendizaje por refuerzo, redes neuronales profundas, y su aplicación a problemas de robótica.

**8. Visión computacional** ([06_Vision/](../06_Vision/)): Procesamiento de imágenes, detección y reconocimiento de objetos, seguimiento visual, reconstrucción 3D, y técnicas de aprendizaje profundo para visión.

**9. Simulación y pruebas** ([07_Simulacion_Pruebas/](../07_Simulacion_Pruebas/)): Entornos de simulación, validación de algoritmos, pruebas de integración, y metodologías de testing para sistemas robóticos.

**10. Comunicaciones** ([09_Comunicaciones_Interfaces/](../09_Comunicaciones_Interfaces/)): Protocolos de red, interfaces web, APIs, comunicación humano-robot, y sistemas distribuidos.

**11. Gestión de datos** ([10_Datasets_Experimentos/](../10_Datasets_Experimentos/)): Recolección, almacenamiento, y análisis de datos experimentales. Metodologías para experimentos reproducibles.

**12. Ética y seguridad** ([12_Etica_Seguridad/](../12_Etica_Seguridad/)): Consideraciones éticas en robótica autónoma, seguridad física y ciberseguridad, transparencia algorítmica, y aspectos regulatorios.

---

## Conclusiones

El desarrollo de un robot humanoide requiere la integración de conocimientos de múltiples disciplinas. Si bien cada área tiene profundidad técnica considerable, el verdadero desafío radica en la integración coherente de todos estos elementos en un sistema funcional.

Este documento proporciona un mapa conceptual de los dominios de conocimiento involucrados. La exploración en profundidad de cada área se encuentra en las carpetas correspondientes del proyecto, donde se incluyen implementaciones, experimentos, y documentación técnica detallada.

El aprendizaje en robótica es necesariamente iterativo: la teoría se estudia, se implementa en prototipos, se valida experimentalmente, y se refina basándose en los resultados obtenidos. Este ciclo de investigación aplicada constituye la esencia del desarrollo en este campo.

---

**Última actualización:** Marzo de 2026

#### 3.8 Planificación de movimiento

**Algoritmos**:
- **RRT (Rapidly-exploring Random Trees)**: Exploración espacial
- **A***: Búsqueda en grafos
- **Dijkstra**: Camino más corto
- **Potential Fields**: Navegación reactiva

#### 3.9 Lógica de comportamiento

**Máquinas de estado**:
```python
from enum import Enum

class RobotState(Enum):
    IDLE = 1
    WALKING = 2
    GRASPING = 3
    TALKING = 4

class BehaviorController:
    def __init__(self):
        self.state = RobotState.IDLE
    
    def update(self, inputs):
        if self.state == RobotState.IDLE:
            if inputs['start_button']:
                self.state = RobotState.WALKING
        # ... más transiciones
```

#### 3.10 Depuración y optimización

**Herramientas**:
- GDB: Depurador C/C++
- pdb: Depurador Python
- Valgrind: Detección de memory leaks
- Profilers: cProfile, gprof

**Mejores prácticas**:
- Logging estructurado
- Unit testing
- Continuous Integration
- Code review

### Referencias y recursos
- "Programming Robots with ROS" - Quigley, Gerkey, Smart
- "Modern Robotics" - Lynch & Park
- ROS Tutorials: wiki.ros.org
- GitHub: Awesome Robotics

---

## 4. Mecatrónica

**Carpeta principal**: [`08_Integracion_Hardware/`](../08_Integracion_Hardware/)

### Conocimientos fundamentales

#### 4.1 Integración mecánica-electrónica

**Diseño para integración**:
- Espacios para cableado
- Accesibilidad para mantenimiento
- Protección de componentes electrónicos
- Gestión térmica
- EMI/EMC (interferencia electromagnética)

#### 4.2 Sistemas de transmisión

**Opciones de transmisión**:
- **Engranajes**: 
  - Rectos, helicoidales, cónicos
  - Reductores planetarios
  - Relaciones de transmisión
  
- **Correas y Poleas**:
  - Correas dentadas (GT2)
  - Cálculo de tensión
  
- **Cables y Tendones**:
  - Actuación remota
  - Routing de cables
  
- **Tornillos de potencia**:
  - Movimiento lineal
  - Ball screws

#### 4.3 Actuadores vs sensores

**Integración**:
- Coubicación de encoder con motor
- Sensores de límite (end-stops)
- Sensores de fuerza en articulaciones
- Retroalimentación táctil

#### 4.4 Diseño de PCB integrado

**Consideraciones**:
- Montaje en estructura mecánica
- Conectores robustos
- Protección contra vibración
- Disipación de calor

#### 4.5 Cableado y routing

**Mejores prácticas**:
- Cable management
- Strain relief
- Cables flexibles para articulaciones
- Etiquetado claro
- Esquemas de cableado

#### 4.6 Sistemas de refrigeración

**Métodos**:
- Ventilación pasiva
- Ventiladores activos
- Disipadores de calor
- Heat pipes
- Espaciado adecuado de componentes

#### 4.7 Interfaz mecánica-electrónica

**Montajes comunes**:
- Encoder en eje de motor
- Servo bracket
- Sensor mount
- PCB standoffs

#### 4.8 Pruebas de integración

**Verificaciones**:
- Rango de movimiento sin colisiones
- Acceso a todos los conectores
- Funcionamiento de sistemas de enfriamiento
- Routing de cables sin tensión excesiva

### Referencias y recursos
- "Mechatronics: Electronic Control Systems in Mechanical Engineering" - Bolton
- "Introduction to Mechatronic Design" - Carryer, Ohline, Kenny

---

## 5. Diseño de software

**Carpeta principal**: [`09_Comunicaciones_Interfaces/`](../09_Comunicaciones_Interfaces/)

### Conocimientos fundamentales

#### 5.1 Arquitectura de software

**Patrones de diseño**:
- **MVC** (Model-View-Controller)
- **Observer**: Notificaciones de eventos
- **Strategy**: Algoritmos intercambiables
- **Factory**: Creación de objetos
- **Singleton**: Instancia única

**Arquitectura modular**:
```
robot_software/
├── core/           # Funcionalidad central
├── drivers/        # Drivers de hardware
├── perception/     # Procesamiento sensorial
├── control/        # Controladores
├── planning/       # Planificación
├── interfaces/     # GUI, API
└── utils/          # Utilidades
```

#### 5.2 Programación orientada a objetos

**Conceptos clave**:
```python
class Joint:
    """Clase base para articulaciones"""
    def __init__(self, name, min_angle, max_angle):
        self.name = name
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = 0
    
    def move_to(self, target_angle):
        if self.min_angle <= target_angle <= self.max_angle:
            self.current_angle = target_angle
            return True
        return False

class RevoluteJoint(Joint):
    """Articulación rotacional"""
    def __init__(self, name, min_angle, max_angle, motor_id):
        super().__init__(name, min_angle, max_angle)
        self.motor_id = motor_id
```

#### 5.3 Desarrollo de GUI

**Qt/PyQt ejemplo**:
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer

class RobotControlGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Robot Control')
        
        start_btn = QPushButton('Start', self)
        start_btn.clicked.connect(self.start_robot)
        
        # Timer para actualizar UI
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(100)  # 10 Hz
    
    def start_robot(self):
        # Código de inicio
        pass
    
    def update_display(self):
        # Actualizar visualización
        pass
```

#### 5.4 APIs y comunicación

**REST API ejemplo (Flask)**:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/robot/move', methods=['POST'])
def move_robot():
    data = request.json
    x = data['x']
    y = data['y']
    z = data['z']
    
    # Mover robot
    result = robot.move_to(x, y, z)
    
    return jsonify({'success': result})

@app.route('/robot/status', methods=['GET'])
def get_status():
    status = robot.get_status()
    return jsonify(status)
```

#### 5.5 Manejo de errores

**Estrategias**:
```python
class RobotException(Exception):
    """Excepción base para errores del robot"""
    pass

class MotorException(RobotException):
    """Error en motor"""
    pass

def safe_move(joint, angle):
    try:
        joint.move_to(angle)
    except MotorException as e:
        logger.error(f"Motor error: {e}")
        robot.emergency_stop()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise
```

#### 5.6 Logging y debugging

**Configuración de logging**:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('robot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("Robot initialized")
logger.warning("Battery low")
logger.error("Motor failure")
```

#### 5.7 Testing

**Unit testing**:
```python
import unittest

class TestJoint(unittest.TestCase):
    def setUp(self):
        self.joint = Joint("test_joint", -90, 90)
    
    def test_move_within_range(self):
        result = self.joint.move_to(45)
        self.assertTrue(result)
        self.assertEqual(self.joint.current_angle, 45)
    
    def test_move_out_of_range(self):
        result = self.joint.move_to(100)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
```

#### 5.8 Documentación de código

**Docstrings**:
```python
def calculate_inverse_kinematics(target_pos, target_orient, robot_model):
    """
    Calcula la cinemática inversa para alcanzar una posición objetivo.
    
    Args:
        target_pos (tuple): Posición objetivo (x, y, z) en metros
        target_orient (tuple): Orientación objetivo (roll, pitch, yaw) en radianes
        robot_model (RobotModel): Modelo del robot
    
    Returns:
        list: Ángulos articulares en radianes
        
    Raises:
        IKException: Si no se encuentra solución
        
    Example:
        >>> angles = calculate_inverse_kinematics((0.3, 0.2, 0.5), (0, 0, 0), robot)
        >>> print(angles)
        [0.52, -0.78, 1.23, 0.45, -0.32, 0.67]
    """
    # Implementación
    pass
```

### Referencias y recursos
- "Clean Code" - Robert C. Martin
- "Design Patterns" - Gang of Four
- Real Python, PyQt documentation

---

## 6. Inteligencia artificial y aprendizaje automático

**Carpetas principales**: 
- [`05_Aprendizaje_Maquina/`](../05_Aprendizaje_Maquina/)
- [`06_Vision/`](../06_Vision/)

### Conocimientos fundamentales

#### 6.1 Conceptos de IA

**Tipos de IA**:
- **IA reactiva**: Responde a estímulos
- **Memoria limitada**: Usa experiencia reciente
- **Teoría de la mente**: Comprende emociones (objetivo)
- **Autoconciencia**: Conciencia propia (futuro lejano)

#### 6.2 Aprendizaje automático

**Paradigmas**:

**Supervisado**:
- Clasificación (SVM, Random Forest, Neural Networks)
- Regresión (Linear, Polynomial, Neural Networks)
- Aplicaciones: Reconocimiento de objetos, predicción

**No supervisado**:
- Clustering (K-means, DBSCAN, Hierarchical)
- Reducción dimensionalidad (PCA, t-SNE)
- Aplicaciones: Segmentación, detección de anomalías

**Por refuerzo**:
- Q-Learning
- Deep Q-Networks (DQN)
- Policy Gradient
- Actor-Critic
- Aplicaciones: Control de locomoción, navegación

#### 6.3 Redes neuronales

**Arquitecturas**:

**Feedforward** (MLP):
```python
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

**Convolucionales** (CNN):
- Aplicación: Visión computacional
- Capas: Conv2D, MaxPool, Flatten, Dense

**Recurrentes** (RNN, LSTM, GRU):
- Aplicación: Secuencias, predicción
- Memoria de estados anteriores

**Transformers**:
- Atención: Enfoque en partes relevantes
- Aplicación: NLP, visión

#### 6.4 Deep learning frameworks

**PyTorch**:
```python
import torch
import torch.optim as optim

model = SimpleNN(input_size=784, hidden_size=128, num_classes=10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenamiento
for epoch in range(num_epochs):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

**TensorFlow/Keras**:
```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, validation_split=0.2)
```

#### 6.5 Visión por computadora

**OpenCV básico**:
```python
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('image.jpg')

# Convertir a espacio de color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Detección de bordes
edges = cv2.Canny(img, 100, 200)

# Detección de contornos
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos
cv2.drawContours(img, contours, -1, (0,255,0), 2)
```

**Detección de objetos**:
- **YOLO (You Only Look Once)**: Rápido, tiempo real
- **SSD (Single Shot Detector)**: Balance velocidad-precisión
- **Faster R-CNN**: Alta precisión
- **EfficientDet**: Eficiente

**Ejemplo YOLO con OpenCV**:
```python
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Procesar detecciones
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Objeto detectado
            pass
```

#### 6.6 Procesamiento de lenguaje natural

**Bibliotecas**:
- NLTK: Procesamiento básico
- spaCy: Producción, rápido
- Transformers (Hugging Face): Modelos pre-entrenados

**Reconocimiento de voz**:
```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Habla ahora...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language='es-ES')
    print(f"Dijiste: {text}")
except:
    print("No pude entender")
```

**Síntesis de voz (TTS)**:
```python
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

engine.say("Hola, soy un robot humanoide")
engine.runAndWait()
```

#### 6.7 Aprendizaje por refuerzo

**Conceptos**:
- **Estado** (s): Situación actual
- **Acción** (a): Lo que el agente puede hacer
- **Recompensa** (r): Feedback del entorno
- **Política** (π): Estrategia de decisión
- **Valor** (V): Calidad de un estado

**Implementación simple Q-Learning**:
```python
import numpy as np

class QLearningAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.q_table = np.zeros((n_states, n_actions))
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
    
    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(len(self.q_table[state]))
        return np.argmax(self.q_table[state])
    
    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.gamma * np.max(self.q_table[next_state])
        self.q_table[state, action] += self.alpha * (target - predict)
```

#### 6.8 Transfer learning

**Uso de modelos pre-entrenados**:
```python
from torchvision import models

# Cargar ResNet pre-entrenado
resnet = models.resnet50(pretrained=True)

# Congelar capas
for param in resnet.parameters():
    param.requires_grad = False

# Reemplazar última capa
resnet.fc = nn.Linear(resnet.fc.in_features, num_classes)

# Solo entrenar nueva capa
optimizer = optim.Adam(resnet.fc.parameters(), lr=0.001)
```

### Referencias y recursos
- "Deep Learning" - Goodfellow, Bengio, Courville
- "Hands-On Machine Learning" - Aurélien Géron
- "Reinforcement Learning: An Introduction" - Sutton & Barto
- Coursera: Deep Learning Specialization (Andrew Ng)
- Fast.ai courses
- Papers With Code

---

## 7. Materiales y fabricación

**Carpeta principal**: [`08_Integracion_Hardware/`](../08_Integracion_Hardware/)

### Conocimientos fundamentales

#### 7.1 Propiedades de materiales

**Propiedades mecánicas**:
- **Resistencia tensil**: Fuerza antes de ruptura
- **Módulo de Young**: Rigidez
- **Elongación**: Deformación antes de ruptura
- **Dureza**: Resistencia a penetración
- **Tenacidad**: Resistencia a fractura
- **Fatiga**: Resistencia a ciclos de carga

**Propiedades físicas**:
- Densidad (kg/m³)
- Conductividad térmica
- Coeficiente de expansión térmica
- Conductividad eléctrica

#### 7.2 Plásticos

**Termoplásticos** (re-moldeables):

**PLA** (Poliácido Láctico):
- Pros: Fácil impresión, biodegradable
- Contras: Frágil, baja temperatura
- Uso: Prototipos, carcasas no estructurales

**ABS** (Acrilonitrilo Butadieno Estireno):
- Pros: Resistente, flexible, mecanizable
- Contras: Requiere cama caliente, vapores
- Uso: Carcasas, partes funcionales

**PETG** (Tereftalato de Polietileno Glicol):
- Pros: Fuerte, flexible, resistente químicamente
- Contras: Puede ser pegajoso
- Uso: Partes funcionales, protección

**Nylon** (Poliamida):
- Pros: Muy resistente, duradero, flexible
- Contras: Absorbe humedad, difícil impresión
- Uso: Engranajes, partes móviles

**TPU** (Poliuretano Termoplástico):
- Pros: Flexible, elástico, resistente abrasión
- Contras: Lenta impresión
- Uso: Juntas, amortiguadores

**Termofijos** (no re-moldeables):
- Resina epoxi
- Poliuretano
- Fibra de vidrio

#### 7.3 Metales

**Aluminio**:
- **Aleación 6061-T6**: Uso general
- Pros: Ligero (2.7 g/cm³), resistente corrosión
- Contras: Menor resistencia que acero
- Uso: Estructura, chasis, soportes

**Acero**:
- **Acero al carbono**: Económico, fuerte
- **Acero inoxidable 304**: Resistente corrosión
- Pros: Muy resistente
- Contras: Pesado (7.85 g/cm³)
- Uso: Ejes, pernos, partes críticas

**Titanio**:
- Pros: Alta resistencia-peso, resistente corrosión
- Contras: Costoso, difícil mecanizar
- Uso: Aplicaciones avanzadas

**Latón/Bronce**:
- Pros: Buena maquinabilidad, baja fricción
- Uso: Bujes, conectores

#### 7.4 Materiales compuestos

**Fibra de Carbono**:
- Pros: Excelente relación resistencia-peso
- Contras: Costoso, frágil a impactos
- Uso: Estructura ligera y rígida

**Fibra de Vidrio**:
- Pros: Resistente, económico
- Contras: Más pesado que fibra carbono
- Uso: Carcasas, paneles

#### 7.5 Técnicas de fabricación

#### Impresión 3D

**FDM** (Fused Deposition Modeling):
- Proceso: Extrusión de filamento termoplástico
- Materiales: PLA, ABS, PETG, Nylon, TPU
- Ventajas: Económico, accesible
- Desventajas: Líneas de capa visibles, anisotropía
- Configuraciones clave:
  - Temperatura nozzle/cama
  - Velocidad impresión
  - Altura de capa (0.1-0.3mm típico)
  - Infill (10-100%)

**SLA** (Stereolithography):
- Proceso: Curado de resina con láser/UV
- Ventajas: Alta resolución, superficies lisas
- Desventajas: Materiales limitados, post-procesado
- Uso: Detalles finos, prototipos

**SLS** (Selective Laser Sintering):
- Proceso: Sinterización de polvo con láser
- Materiales: Nylon, metales
- Ventajas: No requiere soportes, resistente
- Desventajas: Costoso, textura granular

#### Mecanizado CNC

**Fresado CNC**:
- Elimina material con herramientas rotatorias
- Ejes: 3, 4, o 5 ejes
- Tolerancias: ±0.01mm típico
- Materiales: Metales, plásticos, madera

**Torneado CNC**:
- Piezas cilíndricas
- Alta precisión en diámetros

**G-code básico**:
```gcode
G21         ; Unidades mm
G90         ; Posicionamiento absoluto
G00 X10 Y10 ; Movimiento rápido a (10,10)
G01 Z-2 F100; Movimiento lineal a Z=-2, velocidad 100mm/min
G02 X20 Y20 I5 J5 F200  ; Arco horario
M30         ; Fin programa
```

#### Corte láser

- Materiales: Madera, acrílico, cartón, algunos metales
- Precisión alta
- Bordes limpios
- 2D principalmente

#### Otros procesos

**Moldeo por Inyección**:
- Producción en masa de plásticos
- Requiere molde (costoso)
- Bajo costo unitario en volumen

**Fundición**:
- Metales fundidos en molde
- Sand casting, investment casting

**Conformado de Chapa**:
- Doblado, estampado
- Partes de metal delgado

#### 7.6 Post-procesamiento

**Lijado**: Suavizar superficies
**Pintado**: Estética, protección
**Vapores de acetona** (ABS): Superficie lisa
**Anodizado** (aluminio): Protección, color
**Soldadura**: Unir metales

### Referencias y recursos
- "Manufacturing Processes for Engineering Materials" - Kalpakjian
- Simplify3D Print Quality Troubleshooting Guide
- MatWeb: Base de datos de materiales

---

## 8. Baterías y energía

**Carpeta principal**: [`08_Integracion_Hardware/`](../08_Integracion_Hardware/)

### Conocimientos fundamentales

#### 8.1 Tipos de baterías

**Litio-Polímero (LiPo)**:
- Voltaje nominal: 3.7V por celda
- Pros: Alta densidad energética, ligera, descarga alta
- Contras: Requiere cuidado, riesgo incendio
- Configuración: 2S, 3S, 4S (S = series)
- Capacidad: 1000-10000+ mAh
- C-rating: Tasa de descarga (20C = 20× capacidad)
- Uso: Drones, robots móviles

**Litio-Ion (Li-Ion)**:
- Celdas comunes: 18650, 21700
- Voltaje nominal: 3.6-3.7V
- Pros: Más seguro que LiPo, alta capacidad
- Contras: Menor tasa de descarga
- Uso: Portátiles, vehículos eléctricos

**Níquel-Metal Hidruro (NiMH)**:
- Voltaje nominal: 1.2V por celda
- Pros: Seguro, económico
- Contras: Menor densidad energética, auto-descarga
- Uso: Juguetes, dispositivos legacy

#### 8.2 Especificaciones clave

**Capacidad** (mAh, Ah):
- Cantidad de energía almacenada
- Ejemplo: 5000mAh = 5A durante 1h

**Voltaje** (V):
- LiPo: 3.7V nominal, 4.2V cargada, 3.0V descargada
- Configuración series: n×3.7V
- Configuración paralelo: misma V, suma capacidad

**C-Rating**:
- Tasa máxima de descarga
- Ejemplo: 5000mAh 20C = 100A máximo

**Energía** (Wh):
- Wh = V × Ah
- Ejemplo: 11.1V (3S) × 5Ah = 55.5Wh

#### 8.3 Cálculo de autonomía

```python
def calcular_autonomia(capacidad_mah, voltaje_v, potencia_watts):
    """
    Calcula autonomía aproximada de batería
    
    Args:
        capacidad_mah: Capacidad batería en mAh
        voltaje_v: Voltaje nominal en V
        potencia_watts: Consumo promedio en W
    
    Returns:
        float: Tiempo en horas
    """
    capacidad_ah = capacidad_mah / 1000
    energia_wh = voltaje_v * capacidad_ah
    autonomia_h = energia_wh / potencia_watts
    return autonomia_h * 0.8  # Factor eficiencia 80%

# Ejemplo
autonomia = calcular_autonomia(5000, 11.1, 50)
print(f"Autonomía: {autonomia:.2f} horas")
# Resultado: ~0.89 horas ≈ 53 minutos
```

#### 8.4 Sistema de gestión de baterías (BMS)

**Funciones**:
- **Protección sobrecarga**: Detiene carga a 4.2V/celda
- **Protección sobredescarga**: Corta a 3.0V/celda
- **Balanceo de celdas**: Ecualiza voltajes
- **Protección sobrecorriente**: Límite de A
- **Protección sobrecalentamiento**: Monitoreo temperatura

**Ejemplo de monitoreo**:
```python
import board
import busio
from adafruit_ina219 import INA219

# Sensor corriente/voltaje
i2c = busio.I2C(board.SCL, board.SDA)
ina219 = INA219(i2c)

while True:
    voltage = ina219.bus_voltage + ina219.shunt_voltage
    current = ina219.current
    power = ina219.power
    
    print(f"Voltaje: {voltage:.2f}V")
    print(f"Corriente: {current:.2f}mA")
    print(f"Potencia: {power:.2f}mW")
    
    if voltage < 10.5:  # 3.5V/celda para 3S
        print("¡BATERÍA BAJA!")
    
    time.sleep(1)
```

#### 8.5 Regulación de voltaje

**Reguladores Lineales**:
- LM7805 (5V), LM7812 (12V), LM317 (ajustable)
- Pros: Simple, ruido bajo
- Contras: Ineficiente (disipa calor)
- Uso: Bajo consumo, voltajes fijos

**Reguladores Switching**:

**Buck** (Step-Down):
- Reduce voltaje
- Eficiencia ~90%
- Ejemplo: LM2596 (12V→5V)

**Boost** (Step-Up):
- Aumenta voltaje
- Ejemplo: MT3608 (5V→12V)

**Buck-Boost**:
- Aumenta o reduce
- Mayor flexibilidad

#### 8.6 Distribución de energía

**Esquema típico**:
```
Batería (11.1V LiPo 3S)
    │
    ├─→ BMS ─→ [Protección]
    │
    ├─→ Buck 5V ─→ Raspberry Pi, Arduino
    │
    ├─→ Buck 6V ─→ Servomotores
    │
    └─→ Directo ─→ Motores DC (con ESC)
```

**Consideraciones**:
- Cable adecuado (AWG): Mayor corriente = cable más grueso
- Fusibles/breakers en cada línea
- Capacitores de desacople cerca de cada componente
- Ground común

#### 8.7 Carga de baterías

**Cargadores LiPo**:
- Balance charging: Carga cada celda individualmente
- Tasa de carga: Típicamente 1C (capacidad en A)
- Ejemplo: Batería 5000mAh → cargar a 5A
- Nunca dejar sin supervisión

**Protocolo de carga**:
1. CC (Corriente Constante): Hasta 4.2V/celda
2. CV (Voltaje Constante): Corriente decae

#### 8.8 Almacenamiento y seguridad

**Almacenamiento LiPo**:
- Voltaje: 3.8V/celda (modo storage)
- Lugar: Bolsa LiPo resistente al fuego
- Temperatura: Ambiente, seco
- Inspección: No hinchar, dañar

**Seguridad**:
- ADVERTENCIA: Nunca sobre-descargar (<3.0V)
- ADVERTENCIA: Nunca sobre-cargar (>4.2V)
- ADVERTENCIA: Nunca perforar
- ADVERTENCIA: Desechar si está hinchada o dañada

#### 8.9 Alternativas de energía

**Supercapacitores**:
- Carga/descarga muy rápida
- Vida útil muy larga
- Baja densidad energética
- Uso: Picos de potencia, backup

**Celdas de Combustible**:
- Hidrógeno + O2 → electricidad + agua
- Larga duración
- Costoso, complejo
- Uso: Aplicaciones especializadas

### Referencias y recursos
- "Battery Management Systems" - Gregory Plett
- Battery University
- Oscar Liang: LiPo Battery Guide

---

## 9. Diseño ergonómico y biomecánica

**Carpeta principal**: [`04_Control/`](../04_Control/)

### Conocimientos fundamentales

#### 9.1 Anatomía humana

**Articulaciones principales**:

**Pierna**:
- Cadera: 3 DOF (flexión/extensión, abducción/aducción, rotación)
- Rodilla: 1 DOF (flexión/extensión) ~130°
- Tobillo: 2 DOF (dorsiflexión/plantarflexión, inversión/eversión)

**Brazo**:
- Hombro: 3 DOF (esférica) ~360°
- Codo: 1 DOF (flexión) ~145°
- Muñeca: 2 DOF (flexión/extensión, desviación radial/ulnar)
- Mano: 20+ DOF (dedos)

**Torso**:
- Columna: Flexión, extensión, rotación
- Cuello: 3 DOF

**DOF típico robot humanoide**:
- Cabeza: 2-3
- Cada brazo: 6-7
- Torso: 1-3
- Cada pierna: 6
- **Total**: 25-30 DOF

#### 9.2 Biomecánica del movimiento

**Centro de Masa (COM)**:
- Humano: Aprox. a nivel de S2 (segunda vértebra sacra)
- Crítico para equilibrio
- Debe estar dentro del polígono de soporte

**Zero Moment Point (ZMP)**:
- Punto donde no hay momento de vuelco
- Usado para locomoción estable
- Debe estar dentro de pies de soporte

**Gait (Marcha)**:
```
Ciclo de marcha humano:
1. Heel strike (impacto talón)
2. Foot flat (pie plano)
3. Mid stance (apoyo medio)
4. Heel off (despegue talón)
5. Toe off (despegue dedos)
6. Swing phase (fase de balanceo)
```

#### 9.3 Cinemática humanoide

**Denavit-Hartenberg (DH)**:
Parametrización estándar de cadenas cinemáticas

```python
import numpy as np

def dh_matrix(theta, d, a, alpha):
    """
    Matriz de transformación DH
    
    theta: ángulo articulación (rad)
    d: desplazamiento en z
    a: longitud enlace
    alpha: ángulo de torsión
    """
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    
    return np.array([
        [ct, -st*ca, st*sa, a*ct],
        [st, ct*ca, -ct*sa, a*st],
        [0, sa, ca, d],
        [0, 0, 0, 1]
    ])

# Ejemplo: Brazo 3-DOF simple
# DH parameters: [theta, d, a, alpha]
dh_params = [
    [theta1, 0, 0, np.pi/2],
    [theta2, 0, L1, 0],
    [theta3, 0, L2, 0]
]

T = np.eye(4)
for params in dh_params:
    T = T @ dh_matrix(*params)

# T contiene la transformación de base a end-effector
```

#### 9.4 Dinámica de movimiento

**Ecuación de Euler-Lagrange**:
```
τ = M(q)q̈ + C(q,q̇)q̇ + G(q)

Donde:
τ: Torques articulares
M(q): Matriz de inercia
C(q,q̇): Fuerzas centrífugas y Coriolis
G(q): Gravedad
q: Posiciones articulares
```

#### 9.5 Control de equilibrio

**Estrategias**:

**Ankle Strategy**:
- Ajustes pequeños usando tobillo
- Perturbaciones leves

**Hip Strategy**:
- Movimiento de cadera
- Perturbaciones moderadas

**Step Strategy**:
- Dar un paso
- Perturbaciones grandes

**Implementación PID para balanceo**:
```python
class BalanceController:
    def __init__(self):
        self.pid_pitch = PIDController(Kp=10, Ki=0.1, Kd=5)
        self.pid_roll = PIDController(Kp=10, Ki=0.1, Kd=5)
    
    def update(self, imu_data, dt):
        # Leer orientación
        pitch = imu_data['pitch']
        roll = imu_data['roll']
        
        # Calcular correcciones
        ankle_pitch = self.pid_pitch.update(0, pitch, dt)
        ankle_roll = self.pid_roll.update(0, roll, dt)
        
        return ankle_pitch, ankle_roll
```

#### 9.6 Locomoción bípeda

**Generación de Trayectorias**:

**Método de Captura de Movimiento (MoCap)**:
- Grabar movimiento humano real
- Adaptar a robot

**Optimización**:
- Minimizar energía
- Maximizar estabilidad
- Suavidad de movimiento

**Preview Control**:
- Anticipar movimientos futuros
- Planificar ZMP con antelación

**Ejemplo simplificado de paso**:
```python
def generate_step_trajectory(start_pos, end_pos, step_height, duration, freq=100):
    """
    Genera trayectoria de un paso
    
    start_pos: (x, y, z) inicio
    end_pos: (x, y, z) fin
    step_height: altura del paso
    duration: duración en segundos
    freq: frecuencia Hz
    """
    num_points = int(duration * freq)
    t = np.linspace(0, 1, num_points)
    
    # Interpolación lineal en x, y
    x = start_pos[0] + (end_pos[0] - start_pos[0]) * t
    y = start_pos[1] + (end_pos[1] - start_pos[1]) * t
    
    # Trayectoria parabólica en z
    z = start_pos[2] + 4 * step_height * t * (1 - t)
    
    trajectory = np.column_stack([x, y, z])
    return trajectory
```

#### 9.7 Interacción física

**Compliance (Flexibilidad)**:
- Articulaciones no rígidas
- Absorbe impactos
- Más seguro

**Impedance Control**:
- Control de fuerza y posición
- Permite interacción suave

```python
class ImpedanceController:
    def __init__(self, K, D):
        self.K = K  # Rigidez (stiffness)
        self.D = D  # Amortiguamiento (damping)
    
    def calculate_torque(self, pos_desired, pos_actual, vel_actual):
        error_pos = pos_desired - pos_actual
        torque = self.K * error_pos - self.D * vel_actual
        return torque
```

#### 9.8 Ergonomía del robot

**Diseño centrado en humanos**:
- Altura adecuada (típicamente 150-180cm)
- Alcance de brazos funcional
- Interfaz natural (gestos, voz)
- Apariencia amigable

**Uncanny Valley**:
- Muy similar a humano puede ser perturbador
- Balance entre realismo y abstracción

### Referencias y recursos
- "Humanoid Robots: Modeling and Control" - Vukobratović, Borovac
- "Biped Locomotion" - Kajita et al.
- Papers: ZMP-based walking, Preview control
- Open Humanoid Project

---

## 10. Comunicación y Redes

**Carpeta principal**: [`09_Comunicaciones_Interfaces/`](../09_Comunicaciones_Interfaces/)

### Conocimientos fundamentales

#### 10.1 Protocolos de comunicación inalámbrica

**WiFi (802.11)**:
- Alcance: 50-100m interior
- Velocidad: 54Mbps (802.11g) - 1.3Gbps (802.11ac)
- Uso: Telemetría, video streaming, control
- Frecuencias: 2.4GHz (largo alcance) y 5GHz (más rápido)

**Configuración WiFi en Raspberry Pi**:
```bash
# /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="RobotNetwork"
    psk="password123"
}

# Verificar conexión
ifconfig wlan0
ping 8.8.8.8
```

**Bluetooth/BLE**:
- Bluetooth Classic: Audio, datos (1-3Mbps)
- BLE (Low Energy): Sensores, bajo consumo
- Alcance: 10-100m
- Uso: Periféricos, gamepad, sensores

**Zigbee**:
- Bajo consumo, mesh network
- Uso: Red de sensores distribuidos

**LoRa**:
- Largo alcance (km), bajo bitrate
- Uso: Telemetría remota

#### 10.2 Arquitecturas de red

**Client-Server**:
```
Robot (Client) ←→ Servidor Central
```
- Servidor hace procesamiento pesado
- Robot envía datos, recibe comandos

**P2P (Peer-to-Peer)**:
```
Robot ←→ Controlador
```
- Comunicación directa
- Sin intermediarios

**Publish-Subscribe (ROS)**:
```
Nodo A (Publisher) → Topic → Nodo B (Subscriber)
```
- Desacoplamiento
- Múltiples suscriptores

#### 10.3 Protocolos de aplicación

**MQTT** (Message Queue Telemetry Transport):
- Ligero, pub-sub
- Ideal para IoT

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado con código:", rc)
    client.subscribe("robot/commands")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.topic} - {msg.payload}")
    # Procesar comando

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
```

**HTTP/REST API**:
- Estándar web
- Request-Response

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/robot/move', methods=['POST'])
def move():
    data = request.json
    x, y, z = data['x'], data['y'], data['z']
    # Mover robot
    return jsonify({'status': 'moving', 'position': [x, y, z]})

@app.route('/robot/status', methods=['GET'])
def status():
    return jsonify({
        'battery': get_battery_level(),
        'position': get_current_position(),
        'status': 'operational'
    })

app.run(host='0.0.0.0', port=5000)
```

**WebSocket**:
- Bidireccional, tiempo real
- Ideal para control en vivo

```python
import asyncio
import websockets

async def robot_handler(websocket, path):
    async for message in websocket:
        # Procesar comando
        response = process_command(message)
        await websocket.send(response)

start_server = websockets.serve(robot_handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

#### 10.4 ROS communication

**Topics** (Pub-Sub):
```python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

# Publisher
pub = rospy.Publisher('/joint_commands', JointState, queue_size=10)

# Subscriber
def callback(data):
    rospy.loginfo(f"Received: {data.data}")

sub = rospy.Subscriber('/sensor_data', String, callback)

rospy.init_node('robot_com', anonymous=True)
rospy.spin()
```

**Services** (Request-Response):
```python
from std_srvs.srv import SetBool, SetBoolResponse

def handle_enable_motor(req):
    # Habilitar/deshabilitar motor
    success = enable_motor(req.data)
    return SetBoolResponse(success=success)

service = rospy.Service('enable_motor', SetBool, handle_enable_motor)
```

**Actions** (Long-running tasks):
```python
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.pose.position.x = 1.0
goal.target_pose.pose.position.y = 2.0

client.send_goal(goal)
client.wait_for_result()
```

#### 10.5 Streaming de video

**GStreamer**:
```bash
# En robot (Raspberry Pi)
rpicam-vid -t 0 --inline -o - | gst-launch-1.0 fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.1.100 port=5000

# En estación base
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,payload=96 ! rtph264depay ! avdec_h264 ! autovideosink
```

**OpenCV + Socket**:
```python
import cv2
import socket
import pickle
import struct

# Servidor (robot)
cap = cv2.VideoCapture(0)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8485))
server_socket.listen(5)

conn, addr = server_socket.accept()

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message = struct.pack("Q", len(data)) + data
    conn.sendall(message)
```

#### 10.6 Control remoto

**Gamepad/Joystick**:
```python
import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    pygame.event.pump()
    
    # Leer ejes
    left_x = joystick.get_axis(0)
    left_y = joystick.get_axis(1)
    
    # Leer botones
    button_a = joystick.get_button(0)
    
    # Enviar comandos al robot
    send_velocity_command(left_x, left_y)
```

**App móvil**:
- MIT App Inventor (simple)
- Flutter/React Native (profesional)
- Comunicación vía HTTP o WebSocket

#### 10.7 Seguridad de comunicación

**Encriptación**:
- TLS/SSL para HTTP (HTTPS)
- Certificados SSL

**Autenticación**:
```python
from flask import Flask, request
from functools import wraps

app = Flask(__name__)

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('API-Key')
        if api_key != 'SECRET_KEY_123':
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/robot/command', methods=['POST'])
@require_api_key
def command():
    # Comando seguro
    pass
```

**Firewall**:
```bash
# UFW en Raspberry Pi
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 5000/tcp  # API
sudo ufw allow from 192.168.1.0/24  # Red local
sudo ufw enable
```

#### 10.8 Latencia y quality of service

**Medición de latencia**:
```python
import time
import requests

def measure_latency(url, iterations=10):
    latencies = []
    for _ in range(iterations):
        start = time.time()
        requests.get(url)
        latency = (time.time() - start) * 1000  # ms
        latencies.append(latency)
    
    avg_latency = sum(latencies) / len(latencies)
    print(f"Latencia promedio: {avg_latency:.2f}ms")
    return avg_latency
```

**Optimización**:
- Reducir tamaño de mensajes
- Compresión (gzip, etc.)
- Priorización de mensajes críticos
- Buffering inteligente

### Referencias y recursos
- "Computer Networks" - Tanenbaum
- ROS Communication Patterns
- MQTT official documentation

---

## 11. Seguridad y ética

**Carpeta principal**: [`12_Etica_Seguridad/`](../12_Etica_Seguridad/)

### Conocimientos fundamentales

#### 11.1 Seguridad física

**Diseño Seguro**:
- **Bordes redondeados**: Evitar cortes
- **Limitación de fuerza**: Torque máximo en articulaciones
- **Sensores de colisión**: Detener ante contacto
- **E-stop (parada de emergencia)**: Botón físico accesible

**Ejemplo de limitación de fuerza**:
```python
class SafeJoint:
    def __init__(self, max_torque=5.0):  # Newton-metros
        self.max_torque = max_torque
        self.current_sensor = get_current_sensor()
    
    def move_with_safety(self, target_angle):
        torque = calculate_required_torque(target_angle)
        
        if torque > self.max_torque:
            logger.warning("Torque excedido - limitando")
            torque = self.max_torque
        
        # Monitorear corriente (proporcional a torque)
        current = self.current_sensor.read()
        if current > SAFE_CURRENT_LIMIT:
            self.emergency_stop()
            raise SafetyException("Corriente excedida - posible colisión")
        
        apply_torque(torque)
```

**Sensores de seguridad**:
- Bumpers (parachoques)
- Sensores capacitivos (proximidad humanos)
- Sensores de fuerza en piel artificial
- Cámaras para detección de personas

#### 11.2 Zonas de seguridad

**Clasificación de espacios**:
1. **Zona colaborativa**: Robot + humano trabajando juntos
   - Velocidad limitada (<250 mm/s según ISO/TS 15066)
   - Detección constante de colisión
   
2. **Zona supervisada**: Humano puede entrar ocasionalmente
   - Robot reduce velocidad cuando detecta persona
   
3. **Zona restringida**: Solo robot
   - Máxima velocidad
   - Barreras físicas

#### 11.3 Ciberseguridad

**Amenazas**:
- Acceso no autorizado
- Inyección de comandos maliciosos
- Intercepción de comunicaciones
- DoS (Denial of Service)

**Medidas de protección**:

**Autenticación**:
```python
import hashlib
import hmac

SECRET_KEY = "super_secret_key"

def verify_command(command, signature):
    """
    Verifica que el comando viene de fuente autorizada
    """
    expected_sig = hmac.new(
        SECRET_KEY.encode(),
        command.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_sig)

# Uso
if verify_command(received_command, received_signature):
    execute_command(received_command)
else:
    logger.warning("Comando no autorizado rechazado")
```

**Encriptación de datos sensibles**:
```python
from cryptography.fernet import Fernet

# Generar clave
key = Fernet.generate_key()
cipher = Fernet(key)

# Encriptar
sensitive_data = "posición_secreta: x=10, y=20"
encrypted = cipher.encrypt(sensitive_data.encode())

# Desencriptar
decrypted = cipher.decrypt(encrypted).decode()
```

**Actualizaciones seguras**:
- Firma digital de actualizaciones
- Verificación de integridad (checksums)
- Rollback automático si falla

#### 11.4 Privacidad de datos

**GDPR/Normativas**:
- Consentimiento explícito para recopilar datos
- Derecho al olvido
- Transparencia en uso de datos
- Minimización de datos

**Anonimización**:
```python
import hashlib

def anonymize_user_id(user_id):
    """
    Anonimiza ID de usuario
    """
    return hashlib.sha256(user_id.encode()).hexdigest()

def collect_telemetry(user_id, data):
    """
    Recolecta datos anonimizados
    """
    anon_id = anonymize_user_id(user_id)
    telemetry = {
        'user': anon_id,
        'timestamp': time.time(),
        'data': data  # Sin información personal
    }
    save_telemetry(telemetry)
```

**Datos sensibles a proteger**:
- Imágenes/video de caras
- Grabaciones de audio
- Ubicación del hogar
- Patrones de comportamiento

#### 11.5 Ética de la IA

**Principios**:
1. **Transparencia**: Sistema explicable
2. **Equidad**: Sin discriminación
3. **Responsabilidad**: Accountability
4. **Privacidad**: Respeto a datos personales
5. **Seguridad**: No causar daño

**Detección de sesgo**:
```python
def evaluate_fairness(model, test_data, sensitive_attribute):
    """
    Evalúa si modelo es justo respecto a atributo sensible
    (ej: género, edad, etnia - donde sea relevante y legal)
    """
    groups = test_data.groupby(sensitive_attribute)
    
    accuracies = {}
    for group_name, group_data in groups:
        predictions = model.predict(group_data.features)
        accuracy = (predictions == group_data.labels).mean()
        accuracies[group_name] = accuracy
    
    # Disparidad
    max_acc = max(accuracies.values())
    min_acc = min(accuracies.values())
    disparity = max_acc - min_acc
    
    if disparity > 0.1:  # 10% diferencia
        logger.warning(f"Posible sesgo detectado: {accuracies}")
    
    return accuracies
```

**Explicabilidad** (XAI):
```python
import shap

# SHAP values para explicar predicciones
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Visualizar qué características influyeron
shap.plots.waterfall(shap_values[0])
```

#### 11.6 Leyes de la Robótica (Asimov - filosóficas)

1. Un robot no puede dañar a un humano
2. Un robot debe obedecer órdenes (excepto si viola #1)
3. Un robot debe proteger su existencia (excepto si viola #1 o #2)

**Implementación conceptual**:
```python
class EthicalDecisionMaker:
    def evaluate_action(self, action):
        # Ley 1: ¿Daña a humano?
        if self.will_harm_human(action):
            return False, "Viola Ley 1: Posible daño a humano"
        
        # Ley 2: ¿Es orden de humano?
        if action.is_human_order:
            return True, "Cumple Ley 2: Orden humana"
        
        # Ley 3: ¿Es auto-preservación?
        if action.is_self_preservation:
            return True, "Cumple Ley 3: Auto-preservación"
        
        return True, "Acción neutral"
    
    def will_harm_human(self, action):
        # Simular acción y predecir resultado
        simulation = self.physics_engine.simulate(action)
        
        # Detectar humanos en área
        humans_detected = self.perception.detect_humans()
        
        for human in humans_detected:
            if simulation.collision_with(human):
                return True
            if simulation.force_on(human) > SAFE_FORCE_THRESHOLD:
                return True
        
        return False
```

#### 11.7 Normativas y estándares

**ISO/TS 15066**: Robots colaborativos
- Límites de fuerza y presión
- Requisitos de seguridad

**ISO 13482**: Robots de cuidado personal
- Seguridad en interacción humano-robot

**ISO 10218**: Robots industriales
- Requisitos generales de seguridad

**IEC 60950/62368**: Seguridad eléctrica
- Protección contra choques eléctricos
- Aislamiento

#### 11.8 Gestión de riesgos

**Análisis FMEA** (Failure Mode and Effects Analysis):
```
| Modo de Fallo | Efecto | Severidad | Probabilidad | Detección | RPN | Mitigación |
|---------------|--------|-----------|--------------|-----------|-----|------------|
| Motor falla | Caída | 8 | 3 | 7 | 168 | Redundancia, e-stop |
| Software crash | Movimiento errático | 9 | 4 | 5 | 180 | Watchdog, failsafe |
| Batería agotada | Parada súbita | 6 | 5 | 2 | 60 | Alerta temprana |
```

RPN = Severidad × Probabilidad × Detección (priorizar si >100)

**Plan de contingencia**:
```python
class EmergencyHandler:
    def __init__(self):
        self.watchdog = Watchdog(timeout=2.0)
        self.safe_state = SafeState()
    
    def monitor(self):
        try:
            # Bucle principal
            while True:
                self.watchdog.kick()
                robot.update()
                
                # Verificar condiciones
                if battery.voltage < CRITICAL_VOLTAGE:
                    self.handle_low_battery()
                
                if not self.watchdog.is_alive():
                    self.emergency_stop()
                    
        except Exception as e:
            logger.critical(f"Exception crítica: {e}")
            self.emergency_stop()
    
    def emergency_stop(self):
        logger.critical("EMERGENCY STOP")
        # Detener todos los motores
        for motor in robot.motors:
            motor.stop()
        # Posición segura (ej: agacharse lentamente)
        robot.move_to_safe_position()
        # Notificar
        send_alert("Robot en modo seguro")
```

### Referencias y recursos
- "Robot Ethics" - Lin, Abney, Bekey
- "AI Ethics" - Coeckelbergh
- ISO standards (ISO.org)
- EU AI Act
- IEEE Ethically Aligned Design

---

## 12. Gestión de Proyectos

**Carpeta principal**: [`00_Gestion_Proyecto/`](../00_Gestion_Proyecto/)

### Conocimientos fundamentales

#### 12.1 Metodologías

**Cascada (Waterfall)**:
```
Requisitos → Diseño → Implementación → Pruebas → Despliegue
```
- Secuencial
- Bueno para requisitos bien definidos

**Ágil (Agile)**:
- Iterativo e incremental
- Sprints de 1-4 semanas
- Adaptable a cambios

**Scrum**:
- Roles: Product Owner, Scrum Master, Equipo
- Eventos: Sprint Planning, Daily Standup, Review, Retrospective
- Artefactos: Product Backlog, Sprint Backlog, Increment

**Adaptación para proyecto personal**:
- Sprints semanales
- Revisión semanal (retrospectiva)
- Backlog priorizado

#### 12.2 Planificación

**WBS** (Work Breakdown Structure):
```
Robot Humanoide
├── 1. Diseño
│   ├── 1.1 Mecánico
│   ├── 1.2 Electrónico
│   └── 1.3 Software
├── 2. Fabricación
│   ├── 2.1 Impresión 3D
│   ├── 2.2 Ensamblaje
│   └── 2.3 Soldadura
├── 3. Programación
│   ├── 3.1 Control bajo nivel
│   ├── 3.2 Percepción
│   └── 3.3 IA
└── 4. Pruebas
    ├── 4.1 Unitarias
    ├── 4.2 Integración
    └── 4.3 Sistema
```

**Diagrama de Gantt**:
```
Tarea                | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
---------------------|-------|-------|-------|-------|
Diseño Mecánico      |████████|       |       |       |
Diseño Electrónico   |  ████████|     |       |       |
Fabricación          |       |████████|       |       |
Programación         |       |   ██████████████|       |
Integración          |       |       |   ████████|     |
Pruebas              |       |       |       |████████|
```

**Ruta crítica**:
- Secuencia de tareas que determina duración mínima
- Identificar para priorizar recursos

#### 12.3 Gestión de recursos

**Presupuesto ejemplo**:
```
Categoría          | Cantidad | Costo Unit | Total
-------------------|----------|------------|-------
Mecánica           |          |            |
- Aluminio         | 5 kg     | $10/kg     | $50
- Filamento PLA    | 5 kg     | $20/kg     | $100
- Tornillería      | Lote     | $50        | $50
                   |          |            |
Electrónica        |          |            |
- Raspberry Pi 4   | 1        | $75        | $75
- Arduino Mega     | 2        | $40        | $80
- Servomotores     | 20       | $15        | $300
- Sensores (IMU, cam) | Varios | $150    | $150
- Baterías LiPo    | 2        | $60        | $120
                   |          |            |
Software           |          |            |
- Licencias (si aplica) | -   | $0         | $0
                   |          |            |
Herramientas       |          |            |
- Multímetro       | 1        | $30        | $30
- Soldador         | 1        | $40        | $40
                   |          |            |
Contingencia (20%) |          |            | $199
                   |          |            |
**TOTAL**          |          |            | **$1,194**
```

#### 12.4 Gestión de riesgos

**Registro de riesgos**:
```
| ID | Riesgo | Probabilidad | Impacto | Mitigación | Contingencia |
|----|--------|--------------|---------|------------|--------------|
| R1 | Pieza no encaja | Media | Alto | Tolerancias en diseño | Rediseñar |
| R2 | Sensor defectuoso | Baja | Medio | Comprar repuestos | Reemplazar |
| R3 | Retraso entregas | Alta | Medio | Pedir con anticipación | Proveedores alternativos |
| R4 | Bug crítico | Media | Alto | Testing exhaustivo | Rollback |
```

#### 12.5 Seguimiento y control

**KPIs** (Key Performance Indicators):
- **Cumplimiento cronograma**: % tareas a tiempo
- **Presupuesto**: Gasto vs. planificado
- **Calidad**: # bugs, # pruebas pasadas
- **Velocidad**: Tareas completadas por sprint

**Herramientas**:
- Trello/Asana: Gestión de tareas
- GitHub Projects: Integrado con código
- Notion: Documentación y planificación
- Excel/Sheets: Tracking manual

#### 12.6 Documentación continua

**Estructura**:
```
docs/
├── architecture/
│   ├── hardware_design.md
│   └── software_architecture.md
├── user_manual/
│   ├── setup.md
│   ├── operation.md
│   └── troubleshooting.md
├── developer/
│   ├── api_reference.md
│   ├── contributing.md
│   └── testing.md
├── decisions/
│   └── ADR-001-choice-of-microcontroller.md
└── meetings/
    └── 2026-02-27-weekly-review.md
```

**ADR** (Architecture Decision Records):
```markdown
# ADR-001: Elección de ROS como Framework

## Contexto
Necesitamos un framework para integrar sensores, actuadores y algoritmos.

## Decisión
Usar ROS (Robot Operating System) versión Noetic.

## Consecuencias
**Positivo**:
- Ecosistema amplio
- Herramientas de visualización (RViz)
- Comunidad activa

**Negativo**:
- Curva de aprendizaje
- Overhead en sistemas simples

## Alternativas consideradas
- Framework propio (demasiado esfuerzo)
- Middleware ligero (menos funcionalidad)
```

### Referencias y recursos
- "The Lean Startup" - Eric Ries
- "Scrum: The Art of Doing Twice the Work in Half the Time" - Jeff Sutherland
- PM BoK (Project Management Body of Knowledge)

---

## Resumen por carpeta del proyecto

| Carpeta | Conocimientos Principales |
|---------|---------------------------|
| [`00_Gestion_Proyecto/`](../00_Gestion_Proyecto/) | **12** Gestión de Proyectos |
| [`01_Percepcion/`](../01_Percepcion/) | Sensores, fusión sensorial, filtrado |
| [`02_Localizacion_Mapeo/`](../02_Localizacion_Mapeo/) | SLAM, odometría, mapeo |
| [`03_Planificacion/`](../03_Planificacion/) | **3** Programación, planificación de trayectorias |
| [`04_Control/`](../04_Control/) | **3** Programación y Control, **9** Biomecánica |
| [`05_Aprendizaje_Maquina/`](../05_Aprendizaje_Maquina/) | **6** IA y Aprendizaje Automático |
| [`06_Vision/`](../06_Vision/) | **6** Visión por Computadora, detección objetos |
| [`07_Simulacion_Pruebas/`](../07_Simulacion_Pruebas/) | Gazebo, PyBullet, testing |
| [`08_Integracion_Hardware/`](../08_Integracion_Hardware/) | **1** Mecánica, **2** Electrónica, **4** Mecatrónica, **7** Materiales, **8** Energía |
| [`09_Comunicaciones_Interfaces/`](../09_Comunicaciones_Interfaces/) | **5** Diseño de Software, **10** Comunicación |
| [`10_Datasets_Experimentos/`](../10_Datasets_Experimentos/) | Datos de entrenamiento, experimentos |
| [`11_Herramientas_Utilidades/`](../11_Herramientas_Utilidades/) | Scripts, utilidades |
| [`12_Etica_Seguridad/`](../12_Etica_Seguridad/) | **11** Seguridad y Ética |

---

## Recomendaciones de aprendizaje

### Ruta de aprendizaje

**Fase 1: Fundamentos (Meses 1-3)**
1. Python (básico → avanzado)
2. Electrónica básica
3. Mecánica básica
4. Linux/Bash

**Fase 2: Robótica (Meses 4-6)**
1. ROS
2. Cinemática y control
3. Visión por computadora
4. Diseño CAD

**Fase 3: IA y Avanzado (Meses 7-12)**
1. Machine Learning
2. Deep Learning
3. Aprendizaje por refuerzo
4. Integración completa

### Recursos online gratuitos

**Cursos**:
- Coursera: "Robotics Specialization" (UPenn)
- edX: "Autonomous Mobile Robots" (ETH Zurich)
- YouTube: "MIT OpenCourseWare - Robotics"
- YouTube: "Sentdex - ROS tutorials"

**Documentación**:
- ROS Wiki: wiki.ros.org
- PyTorch Tutorials: pytorch.org/tutorials
- OpenCV Docs: docs.opencv.org

**Comunidades**:
- r/robotics (Reddit)
- ROS Discourse
- Robotics Stack Exchange
- DIY Drones Forum

---

**Última actualización**: Febrero 2026

**Nota**: Este es un documento vivo - actualizar conforme se adquieren nuevos conocimientos y se descubren mejores prácticas.
