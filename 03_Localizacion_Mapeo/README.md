# Localización y mapeo

## Propósito:
- Implementar y experimentar con métodos de localización y SLAM (2D/3D) para robots móviles.

## PARTE I — Plan de Investigación (PI)

### 1. Antecedentes y contexto

Una de las capacidades más características de los seres humanos es nuestra **capacidad de orientación**. Esta no es innata: la vamos construyendo a partir del conocimiento acumulado del entorno. Sabemos dónde estamos porque reconocemos lugares, recordamos caminos y actualizamos mentalmente nuestra posición a medida que nos movemos.

Trasladar esta capacidad a un robot de servicio es el siguiente gran reto tras resolver la visión. No basta con que el robot vea el entorno: necesita saber **dónde está dentro de ese entorno**, construir una representación del mismo y ser capaz de decidir **cómo moverse** de manera óptima para llegar a su objetivo.

Este módulo aborda el problema de la localización y el mapeo como extensión directa del sistema de visión, añadiendo una capa de comprensión espacial que habilita la autonomía real del robot.


### 2. Planteamiento del problema

Un robot de servicio que solo detecta objetos pero no sabe dónde está ni cómo moverse de forma óptima no puede operar de manera autónoma en entornos reales. Para ello necesita resolver tres problemas encadenados:

1. **¿Dónde estoy?** → Localización: determinar la posición del robot en el entorno.
2. **¿Cómo es el entorno?** → Mapeo: construir una representación del espacio.
3. **¿Cuál es el mejor camino?** → Planificación de trayectorias: calcular la ruta óptima hacia el objetivo.

La pregunta de investigación central de este módulo es:

> ¿Cómo implementar un sistema integrado de localización, mapeo y planificación de trayectorias que permita a un robot de servicio orientarse y moverse de forma autónoma y eficiente en entornos reales, tanto en representaciones 2D como 3D?


### 3. Objetivos de investigación

**Objetivo general:**  
Diseñar e implementar un sistema de localización y mapeo simultáneo (SLAM) integrado con un módulo de planificación de trayectorias que permita al robot de servicio orientarse, representar su entorno y optimizar su desplazamiento de forma autónoma.

**Objetivos específicos:**

1. Estudiar y comparar los métodos de localización disponibles, tanto para representaciones de entorno plano (2D) como tridimensional (3D).

2. Analizar las técnicas de mapeo robótico y los formatos de representación del entorno más adecuados para robots de servicio en interiores.

3. Investigar los algoritmos de planificación de trayectorias aplicados a robótica móvil, con especial atención a los métodos de optimización iterativa inspirados en el descenso de gradiente.

4. Explorar cómo el robot puede tomar decisiones entre múltiples acciones posibles a partir del mapa generado, integrando el sistema de localización con el módulo de toma de decisiones.

5. Implementar y validar un sistema SLAM completo que genere un mapa del entorno y lo actualice de forma continua durante el desplazamiento del robot.


### 4. Hipótesis de trabajo

Un sistema SLAM que combine sensores de profundidad (LiDAR o cámara RGB-D) con algoritmos de optimización de trayectorias basados en descenso de gradiente permite al robot de servicio construir una representación fiel del entorno y seleccionar en cada momento la acción de desplazamiento óptima, logrando una navegación autónoma eficiente incluso en entornos dinámicos.


### 5. Marco conceptual

#### 5.1 La orientación como capacidad aprendida: analogía humana

Los seres humanos no nacemos sabiendo dónde estamos: **aprendemos a orientarnos** a través de la experiencia. Cada vez que recorremos un espacio, almacenamos información sobre él —distancias, referencias visuales, puntos de referencia— y la usamos para actualizarnos continuamente sobre nuestra posición.

El robot necesita replicar este proceso. La diferencia es que no puede apoyarse en experiencias previas acumuladas: debe construir su representación del entorno **al mismo tiempo que se mueve** por él. Esto es exactamente lo que resuelve el paradigma **SLAM** (*Simultaneous Localization and Mapping*): localizar y mapear de forma simultánea.

#### 5.2 Localización: saber dónde está el robot

La localización consiste en estimar la posición y orientación del robot en un sistema de coordenadas. Se puede abordar en dos dimensiones o en tres:

| Tipo | Descripción | Cuándo usarlo |
|---|---|---|
| **Localización 2D** | Posición en un plano (x, y, ángulo) | Entornos planos, navegación en planta única |
| **Localización 3D** | Posición en el espacio (x, y, z, orientación) | Entornos con desniveles, rampas o múltiples plantas |

Los métodos más habituales para estimar la posición son:

- **Odometría:** estimación de la posición a partir del movimiento de las ruedas. Es simple pero acumula error con el tiempo.
- **Filtro de partículas (MCL / AMCL):** localización probabilística que mantiene múltiples hipótesis sobre la posición del robot y las actualiza con cada nueva observación del entorno.
- **Filtro de Kalman extendido (EKF):** estima la posición combinando el modelo de movimiento del robot con las mediciones de los sensores, minimizando el error de forma continua.

> La localización nunca es perfecta: siempre existe incertidumbre. Por eso los algoritmos modernos no dan una única posición, sino una **distribución de probabilidad** sobre las posiciones posibles, que se va refinando con cada nueva lectura del sensor.

#### 5.3 Mapeo: construir una representación del entorno

El mapa es la representación interna que el robot construye del espacio en el que opera. Existen distintos formatos según la información que se quiera representar:

| Tipo de mapa | Descripción | Uso habitual |
|---|---|---|
| **Mapa de ocupación (grid map)** | Cuadrícula donde cada celda indica si hay obstáculo o espacio libre | Navegación 2D en interiores |
| **Mapa de puntos (point cloud)** | Nube de puntos 3D que representa superficies del entorno | Navegación 3D, manipulación |
| **Mapa topológico** | Grafo de nodos (lugares) y aristas (conexiones entre ellos) | Planificación de rutas a alto nivel |
| **Mapa semántico** | Mapa que incluye el significado de los elementos detectados | Interacción con el entorno |

#### 5.4 SLAM: localizar y mapear al mismo tiempo

El problema SLAM es el corazón de la navegación autónoma. El reto consiste en que **la localización necesita un mapa y el mapeo necesita saber dónde está el robot**, creando una dependencia circular que los algoritmos SLAM resuelven de forma iterativa.

Los enfoques más importantes son:

- **SLAM basado en filtro (EKF-SLAM, Particle Filter SLAM):** mantiene una estimación probabilística conjunta de la posición del robot y los elementos del mapa.
- **SLAM basado en grafos (Graph-SLAM, g2o, GTSAM):** representa el problema como un grafo de poses y observaciones, y lo optimiza minimizando el error global.
- **SLAM visual (ORB-SLAM, LSD-SLAM):** utiliza cámaras en lugar de LiDAR para construir el mapa a partir de características visuales.
- **SLAM con LiDAR (Cartographer, LOAM):** utiliza sensores láser para obtener mediciones de distancia precisas y construir mapas de alta fidelidad.

#### 5.5 Planificación de trayectorias: encontrar el mejor camino

Una vez que el robot tiene un mapa y sabe dónde está, necesita decidir **cómo llegar a su destino**. Este es el problema de la planificación de trayectorias.

La analogía con el **descenso de gradiente** es muy útil para entender el proceso: igual que en optimización matemática se busca el mínimo de una función siguiendo el gradiente descendente paso a paso, en navegación el robot evalúa iterativamente sus opciones de movimiento y selecciona en cada instante la acción que más le acerca al objetivo, teniendo en cuenta los obstáculos del entorno.

Los algoritmos principales son:

| Algoritmo | Tipo | Características |
|---|---|---|
| **A\*** | Búsqueda heurística | Óptimo y completo; muy usado en mapas de cuadrícula |
| **Dijkstra** | Búsqueda por costo | Garantiza el camino más corto; sin heurística |
| **RRT / RRT\*** | Muestreo aleatorio | Eficiente en espacios de alta dimensión; adecuado para 3D |
| **DWA** (*Dynamic Window Approach*) | Local, reactivo | Evita obstáculos en tiempo real combinando velocidad y dirección |
| **Basado en gradiente potencial** | Campo de fuerzas | Modela el objetivo como atractor y los obstáculos como repulsores |

> El planificador global encuentra la ruta óptima en el mapa; el planificador local la ejecuta en tiempo real, adaptándose a obstáculos no previstos. Ambos deben trabajar juntos para una navegación fluida.

#### 5.6 Toma de decisiones sobre acciones de movimiento

El sistema de planificación genera un conjunto de **acciones posibles** (avanzar, girar, detenerse, rodear un obstáculo). El robot necesita un mecanismo para **elegir entre ellas** en cada instante. Este módulo se conecta directamente con el sistema de aprendizaje por refuerzo descrito en el módulo de visión: el mapa y la localización son el **estado** que el agente observa, y las acciones de movimiento son el **espacio de decisión** sobre el que actúa.

La arquitectura resultante combina:

- **Capa de percepción:** sensores + visión → estado del entorno.
- **Capa de localización y mapeo:** SLAM → posición del robot + mapa actualizado.
- **Capa de planificación:** algoritmo de trayectorias → secuencia de acciones óptimas.
- **Capa de decisión:** modelo de RL → selección de la acción concreta a ejecutar.


### 6. Metodología de investigación

| Fase | Descripción |
|---|---|
| **Fase 1 — Revisión del estado del arte** | Análisis de algoritmos SLAM, métodos de localización 2D/3D y planificadores de trayectorias. Fuentes: IEEE Robotics, arxiv.org (cs.RO), ROS wiki. |
| **Fase 2 — Selección de sensores y algoritmos** | Comparativa entre LiDAR, cámaras RGB-D y odometría como fuentes de datos para SLAM. Selección del algoritmo SLAM más adecuado para el entorno de prueba. |
| **Fase 3 — Implementación en simulador** | Despliegue del sistema SLAM seleccionado en Gazebo o Isaac Sim. Generación de mapas 2D y 3D en entornos controlados. |
| **Fase 4 — Integración con planificador** | Conexión del mapa generado con el planificador de trayectorias (Nav2 en ROS2). Validación de rutas óptimas en distintos escenarios. |
| **Fase 5 — Validación en hardware real** | Pruebas del sistema completo en el robot físico. Evaluación de la precisión del mapa, error de localización y eficiencia de las trayectorias. |


### 7. Variables de estudio

- **Variable independiente:** algoritmo SLAM y tipo de sensor utilizado (LiDAR vs. cámara RGB-D).
- **Variable dependiente:** precisión del mapa generado, error de localización acumulado y calidad de las trayectorias planificadas.
- **Variable de control:** entorno físico fijo, velocidad de desplazamiento constante y condiciones de iluminación estables.


## PARTE II 

### 1. Justificación

La localización y el mapeo constituyen una disciplina técnica con fundamentos matemáticos sólidos (probabilidad, álgebra lineal, optimización) y herramientas de software específicas. La formación en este módulo requiere partir de los conceptos teóricos de los algoritmos SLAM y avanzar hasta su implementación práctica en ROS2, conectando con las competencias ya desarrolladas en el módulo de visión artificial.


### 2. Competencias a desarrollar

#### Bloque A — Fundamentos matemáticos de localización
- Probabilidad bayesiana aplicada a la estimación de posición.
- Filtros de Kalman: fundamentos y variantes (EKF, UKF).
- Filtros de partículas y Monte Carlo Localization (MCL/AMCL).
- Representación de la incertidumbre en sistemas robóticos.

#### Bloque B — Algoritmos SLAM
- Conceptos fundamentales de SLAM: problema de la dependencia circular posición-mapa.
- SLAM basado en grafos: construcción y optimización del grafo de poses.
- SLAM visual: ORB-SLAM3, funcionamiento con cámaras monoculares y RGB-D.
- SLAM con LiDAR: Cartographer (Google), LOAM, configuración y ajuste.

#### Bloque C — Representación del entorno y mapas
- Mapas de ocupación (OccupancyGrid): generación, actualización y lectura.
- Nubes de puntos 3D: procesamiento con PCL (*Point Cloud Library*).
- Mapas semánticos: integración de información de detección de objetos en el mapa.
- Formatos de intercambio: PGM, YAML, PCD, ROS map format.

#### Bloque D — Planificación de trayectorias
- Algoritmos de búsqueda: A\*, Dijkstra, implementación sobre mapas de cuadrícula.
- Planificadores por muestreo: RRT, RRT\* para espacios 3D.
- Planificación local en tiempo real: DWA, TEB (*Timed Elastic Band*).
- Nav2: stack de navegación en ROS2, configuración de planificadores global y local.

#### Bloque E — Integración y toma de decisiones
- Arquitectura de navegación autónoma en ROS2: perception → SLAM → planning → control.
- Conexión del sistema SLAM con el módulo de aprendizaje por refuerzo (Módulo 1).
- Ajuste de parámetros y puesta a punto del sistema completo en hardware real.



### 3. Itinerario formativo

| Módulo | Contenido | Recursos sugeridos |
|---|---|---|
| **Módulo 1** — Matemáticas de localización | Probabilidad bayesiana, filtros de Kalman y partículas | "Probabilistic Robotics" (Thrun, Burgard, Fox) — referencia fundamental |
| **Módulo 2** — SLAM visual y LiDAR | ORB-SLAM3, Cartographer, configuración práctica | Repositorios oficiales ORB-SLAM3 y Cartographer en GitHub |
| **Módulo 3** — Mapas y nubes de puntos | OccupancyGrid, PCL, mapas semánticos | Documentación PCL, tutoriales ROS2 map_server |
| **Módulo 4** — Planificación de trayectorias | A\*, RRT\*, DWA, Nav2 | Documentación Nav2 (navigation.ros.org), curso ROS2 Navigation (The Construct) |
| **Módulo 5** — Integración completa | Pipeline SLAM + Nav2 + RL en hardware real | Proyectos de referencia en ROS2 con Nav2 y robots reales |


### 4. Indicadores de logro

Al finalizar el plan de formación, se habrán alcanzado los siguientes hitos:

1. Generación de un mapa 2D preciso de un entorno interior mediante SLAM, con error de cierre < 5 cm.
2. Localización del robot en el mapa generado con error de posición < 10 cm en condiciones normales.
3. Planificación y ejecución autónoma de trayectorias entre puntos del mapa evitando obstáculos estáticos y dinámicos.
4. Integración funcional del sistema SLAM con Nav2 en ROS2, operativo en hardware embebido.
5. Documentación del sistema: diagrama de arquitectura, parámetros de configuración y análisis de resultados.


### 5. Relación entre formación e investigación

| Objetivo de investigación | Competencia formativa asociada |
|---|---|
| Estudiar métodos de localización 2D/3D | Bloque A — Fundamentos matemáticos de localización |
| Analizar técnicas de mapeo robótico | Bloque B — Algoritmos SLAM + Bloque C — Representación del entorno |
| Investigar algoritmos de planificación | Bloque D — Planificación de trayectorias |
| Integrar localización con toma de decisiones | Bloque E — Integración y toma de decisiones |
| Implementar y validar sistema SLAM completo | Bloque B + D + E con itinerario Módulos 2, 4 y 5 |


### 6. Conexión con el módulo anterior (Visión Artificial)

Este módulo amplía el sistema de visión desarrollado en el Módulo 1 de la siguiente manera:

- Las **cámaras RGB-D** y los sensores de profundidad son la fuente de datos tanto para la detección de objetos (Módulo 1) como para el SLAM visual (este módulo).
- El **mapa semántico** integra la información de detección de objetos (qué hay en el entorno) con la información espacial (dónde está cada cosa).
- El sistema de **aprendizaje por refuerzo** del Módulo 1 recibe ahora, además de la imagen de la cámara, el estado de localización del robot en el mapa, lo que enriquece enormemente su capacidad de toma de decisiones.

La arquitectura completa del robot quedaría:

```
Sensores (cámara + LiDAR)
        ↓
Visión (detección de objetos)   +   SLAM (localización + mapa)
        ↓                                    ↓
              Planificador de trayectorias (Nav2)
                            ↓
              Agente de decisión (Reinforcement Learning)
                            ↓
                    Actuadores (movimiento)
```

---

*Documento generado en formato PIyPFP · Módulo 2 — Localización, Mapeo y Planificación de Trayectorias*



Contenido sugerido:
- `slam/` : implementaciones y wrappers (GMapping, Hector, Cartographer, ORB-SLAM)
- `odom/` : odometría, corrección y modelos de movimiento
- `gmapping_examples/` : datasets de prueba y scripts de reproducibilidad
- `evaluacion/` : métricas y herramientas para comparar mapas y trayectorias

Cómo usar:
- Pruebas con datos simulados y reales; soporte para ROS bags y formatos comunes.

Notas:
- Añadir instrucciones para reproducir experimentos con `rosbag` y simuladores.