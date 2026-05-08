# Planificación y control - cerebro motor del robot

## Propósito

Este módulo implementa el **sistema de planificación y control** del robot humanoide, traduciendo objetivos de alto nivel en trayectorias ejecutables y comandos precisos para actuadores. Integra algoritmos de planificación de rutas con controladores en tiempo real para lograr movimientos coordinados, seguros y eficientes.


## PARTE I — Plan de Investigación (PI)

### 1. Antecedentes y contexto

Si el módulo de visión dota al robot de la capacidad de percibir y el módulo de localización y mapeo le permite saber dónde está y representar su entorno, este tercer módulo aborda el problema central que los conecta: **cómo traducir un objetivo de alto nivel en movimiento real**.

Cuando un ser humano decide ir a una habitación, no piensa en cada músculo que debe contraer ni en el ángulo exacto de cada articulación. Sin embargo, el sistema nervioso central ejecuta de forma automática y coordinada cientos de decisiones simultáneas a distintos niveles: desde la planificación general de la ruta hasta el control milimétrico de cada grupo muscular. Este proceso jerárquico —desde la intención hasta la acción— es exactamente lo que este módulo busca replicar en un robot de servicio.

La planificación y el control constituyen el **cerebro motor** del robot: el sistema que, partiendo de un objetivo, genera una trayectoria ejecutable y la lleva a cabo de forma precisa, segura y eficiente, en tiempo real.

---

### 2. Planteamiento del problema

Un robot que sabe dónde está y conoce su entorno todavía no es capaz de moverse de forma autónoma si no dispone de un sistema que resuelva tres problemas encadenados:

1. **¿Qué ruta seguir?** → Planificación global: calcular el camino óptimo desde el origen hasta el destino.
2. **¿Cómo adaptarse durante el trayecto?** → Planificación local: reaccionar a obstáculos dinámicos no previstos en el mapa.
3. **¿Cómo ejecutar el movimiento con precisión?** → Control: traducir la trayectoria planificada en comandos concretos para cada motor o articulación.

La pregunta de investigación central de este módulo es:

> ¿Cómo diseñar una arquitectura jerárquica de planificación y control que permita a un robot de servicio traducir objetivos de alto nivel en movimientos coordinados, precisos y seguros, integrando planificación global, adaptación local y control de actuadores en tiempo real?

---

### 3. Objetivos de investigación

**Objetivo general:**  
Diseñar e implementar una arquitectura jerárquica de planificación y control que cubra desde la generación de rutas globales hasta el control de bajo nivel de actuadores, garantizando movimientos coordinados, seguros y eficientes en entornos reales.

**Objetivos específicos:**

1. Estudiar y comparar los algoritmos de planificación global más utilizados en robótica móvil (A\*, RRT\*) y seleccionar el más adecuado según el tipo de entorno y las restricciones del robot.

2. Analizar los métodos de planificación local para evitación de obstáculos dinámicos en tiempo real, evaluando su latencia e integración con la planificación global.

3. Investigar las técnicas de optimización y suavizado de trayectorias que transforman rutas discretas en movimientos fluidos y ejecutables por los actuadores físicos del robot.

4. Explorar los controladores de alto nivel —especialmente el Control Predictivo por Modelo (MPC) y la cinemática inversa— como mecanismos de traducción entre trayectorias deseadas y comandos articulares.

5. Implementar y validar controladores de bajo nivel (PID) para el control preciso de cada articulación o motor del robot, evaluando su estabilidad y respuesta ante perturbaciones.

6. Integrar los distintos niveles de la arquitectura jerárquica y validar el sistema completo en escenarios de navegación y manipulación reales.

---

### 4. Hipótesis de trabajo

Una arquitectura jerárquica de planificación y control que combine planificación global (A\* o RRT\*), planificación local reactiva, optimización de trayectorias y controladores PID por articulación —coordinados por un controlador MPC de alto nivel— permite a un robot de servicio ejecutar tareas de navegación y manipulación de forma autónoma, segura y eficiente en entornos dinámicos reales.

---

### 5. Marco conceptual

#### 5.1 La arquitectura jerárquica: del objetivo a la acción

El sistema de planificación y control funciona en capas, cada una con su propio nivel de abstracción y velocidad de operación. Este diseño refleja cómo los seres vivos organizamos el movimiento: desde la decisión consciente de alto nivel hasta el reflejo automático de bajo nivel.

```
Objetivo de alto nivel (ej: "ir a la cocina")
         ↓
[PLANIFICACIÓN GLOBAL] → Ruta A* o RRT*
         ↓
[PLANIFICACIÓN LOCAL] → Evita obstáculos dinámicos
         ↓
[OPTIMIZACIÓN DE TRAYECTORIA] → Suaviza y optimiza movimiento
         ↓
[CONTROL DE ALTO NIVEL] → MPC, cinemática inversa
         ↓
[CONTROL DE BAJO NIVEL] → PID para cada articulación
         ↓
Actuadores (motores, servos)
```

Cada capa recibe información de la capa superior y retroalimentación de la capa inferior, creando un sistema de control en bucle cerrado en todos los niveles.

---

#### 5.2 Planificación global: encontrar la mejor ruta

La planificación global trabaja sobre el mapa generado por el módulo SLAM y calcula la ruta óptima desde la posición actual del robot hasta su destino. Opera a **baja frecuencia** (no necesita recalcularse en cada ciclo) pero debe ser eficiente y garantizar que la ruta encontrada sea la mejor posible.

Los dos algoritmos principales en robótica son:

**A\* (A-estrella)**  
Algoritmo de búsqueda heurística sobre un mapa de cuadrícula. En cada paso evalúa el coste real del camino recorrido más una estimación del coste restante hasta el objetivo (heurística). Garantiza encontrar el camino óptimo si la heurística es admisible. Es el más utilizado en entornos interiores con mapas de ocupación.

**RRT\* (Rapidly-exploring Random Tree)**  
Algoritmo de muestreo aleatorio del espacio de configuraciones. Construye un árbol de posiciones exploradas de forma aleatoria y lo va optimizando a medida que crece. Es especialmente adecuado para espacios de configuración de alta dimensión, como los de robots con múltiples articulaciones o para planificación en 3D.

| Algoritmo | Tipo | Ventajas | Limitaciones |
|---|---|---|---|
| **A\*** | Búsqueda en grafo | Óptimo, completo, eficiente en 2D | Escala mal en espacios de alta dimensión |
| **Dijkstra** | Búsqueda en grafo | Garantiza camino más corto | Más lento que A\* al no usar heurística |
| **RRT** | Muestreo aleatorio | Eficiente en alta dimensión | No garantiza optimalidad |
| **RRT\*** | Muestreo + optimización | Converge a la solución óptima | Mayor coste computacional que RRT |

> La analogía con el descenso de gradiente es directa en el caso de los planificadores basados en campos potenciales: el objetivo actúa como un mínimo de energía hacia el que el robot "desciende", mientras que los obstáculos generan barreras de potencial que lo repelen. El robot sigue el gradiente del campo de fuerzas resultante.

---

#### 5.3 Planificación local: reaccionar en tiempo real

La planificación global asume que el mapa es estático. En entornos reales, siempre aparecen **obstáculos dinámicos** no previstos: personas que caminan, puertas que se abren, objetos desplazados. La planificación local opera a **alta frecuencia** y adapta la ruta en tiempo real sin necesidad de recalcular el plan global.

Los algoritmos más utilizados son:

- **DWA** (*Dynamic Window Approach*): evalúa el espacio de velocidades alcanzables por el robot en el siguiente instante y selecciona la combinación de velocidad lineal y angular que maximiza el progreso hacia el objetivo mientras evita colisiones.
- **TEB** (*Timed Elastic Band*): modela la trayectoria como una banda elástica que se deforma para evitar obstáculos, optimizando simultáneamente tiempo, suavidad y distancia de seguridad.

---

#### 5.4 Optimización y suavizado de trayectorias

Los algoritmos de planificación generan rutas como secuencias de puntos discretos. Antes de enviarlos al controlador, es necesario **suavizar** estas rutas para que el movimiento resultante sea físicamente ejecutable (sin cambios bruscos de dirección) y mecánicamente eficiente (minimizando el desgaste de los actuadores).

Técnicas habituales:

- **Splines cúbicos:** interpolación suave entre los puntos de la ruta preservando la continuidad de velocidad y aceleración.
- **Optimización de trayectoria (CHOMP, STOMP):** métodos de optimización que modifican la trayectoria completa minimizando una función de coste que combina suavidad y evitación de obstáculos.
- **Perfiles de velocidad trapezoidal o S-curve:** definen cómo varía la velocidad a lo largo de la trayectoria, respetando los límites físicos de aceleración y jerk del robot.

---

#### 5.5 Control de alto nivel: MPC y cinemática inversa

Una vez que se dispone de una trayectoria suavizada, el controlador de alto nivel se encarga de **seguirla con precisión**, teniendo en cuenta la dinámica del robot y anticipando su comportamiento futuro.

**Control Predictivo por Modelo (MPC)**  
El MPC es uno de los controladores más potentes para sistemas robóticos complejos. Funciona resolviendo en cada ciclo un problema de optimización a corto plazo: dado el estado actual del robot y el modelo de su dinámica, calcula la secuencia de comandos que minimiza el error de seguimiento de trayectoria durante un horizonte temporal futuro. Solo ejecuta el primer paso de esa secuencia y repite el proceso en el siguiente ciclo.

> El MPC es la versión de control del descenso de gradiente aplicado en tiempo real: en cada instante optimiza la siguiente acción mirando un poco hacia adelante, en lugar de reaccionar solo al error presente.

**Cinemática inversa**  
Para robots articulados (brazos, humanoides), la cinemática inversa resuelve el problema de calcular los ángulos de cada articulación necesarios para que el extremo del robot (la mano, la herramienta) alcance una posición y orientación deseada en el espacio. Es la traducción entre el espacio cartesiano (coordenadas xyz) y el espacio articular (ángulos de cada motor).

---

#### 5.6 Control de bajo nivel: PID por articulación

En la base de la arquitectura se encuentran los controladores de bajo nivel, uno por cada motor o articulación del robot. Su función es ejecutar con precisión el comando que reciben del nivel superior, corrigiendo en tiempo real las desviaciones debidas a fricción, cargas externas o perturbaciones mecánicas.

El controlador más utilizado es el **PID** (*Proportional-Integral-Derivative*):

- **Término proporcional (P):** corrige el error actual entre la posición deseada y la real.
- **Término integral (I):** elimina el error acumulado a lo largo del tiempo (errores estacionarios).
- **Término derivativo (D):** anticipa la tendencia del error y amortigua oscilaciones.

La sintonización correcta de los parámetros PID (Kp, Ki, Kd) es crítica para que el movimiento sea estable, preciso y sin oscilaciones. En robots modernos se utilizan técnicas de autosintonización o control adaptativo para ajustar estos parámetros dinámicamente.

---

### 6. Metodología de investigación

| Fase | Descripción |
|---|---|
| **Fase 1 — Revisión del estado del arte** | Análisis de algoritmos de planificación global y local, técnicas de optimización de trayectorias y controladores MPC y PID aplicados a robótica. Fuentes: IEEE T-RO, ICRA, IROS. |
| **Fase 2 — Selección de la arquitectura** | Definición de la arquitectura jerárquica más adecuada para el robot de servicio objetivo, seleccionando los algoritmos de cada capa según restricciones de hardware y caso de uso. |
| **Fase 3 — Implementación en simulador** | Desarrollo de la pila de planificación y control en ROS2 + Gazebo. Validación de cada capa de forma independiente antes de la integración. |
| **Fase 4 — Integración jerárquica** | Conexión de las capas de planificación global, local, optimización y control. Validación del flujo completo desde objetivo hasta actuador en simulador. |
| **Fase 5 — Validación en hardware real** | Despliegue en el robot físico. Sintonización de controladores PID y ajuste de parámetros MPC. Evaluación con métricas de precisión, suavidad y tiempo de ejecución. |

---

### 7. Variables de estudio

- **Variable independiente:** algoritmo de planificación global seleccionado (A\* vs. RRT\*) y tipo de controlador de alto nivel (MPC vs. controlador geométrico simple).
- **Variable dependiente:** precisión de seguimiento de trayectoria, tiempo de cómputo por ciclo, suavidad del movimiento y tasa de éxito ante obstáculos dinámicos.
- **Variable de control:** entorno de prueba estandarizado, velocidad máxima del robot definida y mismo conjunto de escenarios de prueba para todos los algoritmos evaluados.

---

## PARTE II — Plan de Formación Personal (PFP)

### 1. Justificación

El diseño de sistemas de planificación y control requiere competencias tanto teóricas —álgebra lineal, teoría de control, optimización— como prácticas —implementación en ROS2, sintonización de controladores, trabajo con simuladores dinámicos—. La formación en este módulo parte de los fundamentos matemáticos del control y avanza hasta la implementación y validación de una arquitectura jerárquica completa integrada con los módulos anteriores.

---

### 2. Competencias a desarrollar

#### Bloque A — Fundamentos de teoría de control
- Sistemas dinámicos: modelado en espacio de estados, funciones de transferencia.
- Estabilidad de sistemas de control: criterios de Routh-Hurwitz, análisis de Bode.
- Diseño y sintonización de controladores **PID**: métodos de Ziegler-Nichols, autosintonización.
- Control en bucle cerrado: retroalimentación, perturbaciones y robustez.

#### Bloque B — Planificación de movimiento
- Algoritmos de búsqueda: **A\*** y variantes, implementación sobre OccupancyGrid.
- Planificación por muestreo: **RRT, RRT\***, espacios de configuración de alta dimensión.
- Planificación local reactiva: **DWA, TEB**, integración con Nav2 en ROS2.
- Campos de potencial artificial: gradiente atractivo-repulsivo para navegación.

#### Bloque C — Optimización de trayectorias
- Interpolación y suavizado: splines cúbicos, Bézier, B-splines.
- Perfiles de velocidad: trapezoidal, S-curve, respeto de límites cinemáticos.
- Métodos de optimización de trayectoria: **CHOMP, STOMP**, función de coste combinada.
- Planificación en el espacio articular vs. espacio cartesiano.

#### Bloque D — Control avanzado: MPC y cinemática inversa
- **Control Predictivo por Modelo (MPC)**: formulación del problema de optimización, horizonte de predicción, implementación con CasADi o acados.
- **Cinemática directa e inversa**: cadenas cinemáticas, Jacobiano, métodos numéricos (Jacobiano transpuesto, pseudoinversa).
- Dinámica de robots: ecuaciones de Euler-Lagrange, matriz de masa, términos de Coriolis.
- MoveIt2: framework de planificación y control de brazos robóticos en ROS2.

#### Bloque E — Integración en ROS2 y hardware
- Nav2: arquitectura completa, configuración de planificadores global y local, *behavior trees*.
- Control de actuadores en ROS2: `ros2_control`, interfaces de hardware, controladores de posición y velocidad.
- Sintonización experimental de PID en hardware real: herramientas de diagnóstico y análisis de señales.
- Integración del pipeline completo: SLAM (Módulo 2) + Nav2 + `ros2_control` + actuadores.

---

### 3. Itinerario formativo

| Módulo | Contenido | Recursos sugeridos |
|---|---|---|
| **Módulo 1** — Teoría de control | PID, estabilidad, sistemas dinámicos | "Modern Control Engineering" (Ogata); curso Control Systems (Coursera) |
| **Módulo 2** — Planificación global | A\*, RRT\*, campos potenciales | "Planning Algorithms" (LaValle) — acceso libre online; nav2 docs |
| **Módulo 3** — Planificación local y Nav2 | DWA, TEB, Nav2 en ROS2 | navigation.ros.org; tutoriales Nav2 (The Construct) |
| **Módulo 4** — Optimización de trayectorias | Splines, CHOMP, perfiles de velocidad | MoveIt2 docs; paper CHOMP (Ratliff et al.) |
| **Módulo 5** — MPC y cinemática inversa | MPC, Jacobiano, MoveIt2 | acados docs; "Robotics: Modelling, Planning and Control" (Siciliano) |
| **Módulo 6** — Integración hardware | ros2_control, sintonización PID real | ros2_control docs; NVIDIA Isaac ROS |

---

### 4. Indicadores de logro

Al finalizar el plan de formación, se habrán alcanzado los siguientes hitos:

1. Implementación funcional de un planificador A\* sobre un mapa de ocupación 2D con visualización en RViz2.
2. Configuración y validación del stack Nav2 completo en simulador Gazebo, con evitación de obstáculos dinámicos.
3. Implementación de un controlador PID sintonizado para al menos una articulación del robot, con análisis de respuesta al escalón.
4. Integración del pipeline completo (SLAM + Nav2 + control de actuadores) en ROS2, operativo en simulador y hardware real.
5. Documentación técnica de la arquitectura de control: diagramas de bloques, parámetros de configuración y análisis de resultados.

---

### 5. Relación entre formación e investigación

| Objetivo de investigación | Competencia formativa asociada |
|---|---|
| Comparar algoritmos de planificación global | Bloque B — Planificación de movimiento |
| Analizar planificación local para obstáculos dinámicos | Bloque B + Bloque E — Nav2 |
| Investigar optimización y suavizado de trayectorias | Bloque C — Optimización de trayectorias |
| Explorar MPC y cinemática inversa | Bloque D — Control avanzado |
| Implementar y validar controladores PID | Bloque A + Bloque E — Hardware |
| Integrar arquitectura jerárquica completa | Bloque E — Integración ROS2 |

---

### 6. Conexión con los módulos anteriores

Este módulo cierra el ciclo de autonomía del robot integrando las capacidades de los módulos anteriores:

- El sistema de **visión** (Módulo 1) proporciona información sobre objetos y obstáculos en el entorno en tiempo real, que el planificador local usa para la evitación dinámica.
- El sistema **SLAM** (Módulo 2) genera el mapa sobre el que opera el planificador global y mantiene actualizada la posición del robot, que el controlador MPC usa como estado de referencia.
- Este módulo añade la capa de **ejecución**: convierte toda esa información en movimiento real, coordinado y preciso.

La arquitectura completa del robot, con los tres módulos integrados, queda:

```
Sensores (cámara + LiDAR + encoders)
         ↓
[Módulo 1] Visión → detección de objetos y obstáculos
[Módulo 2] SLAM  → localización + mapa del entorno
         ↓
[Módulo 3] Planificación global (A* / RRT*)
         ↓
[Módulo 3] Planificación local (DWA / TEB)
         ↓
[Módulo 3] Optimización de trayectoria
         ↓
[Módulo 3] Control de alto nivel (MPC + cinemática inversa)
         ↓
[Módulo 3] Control de bajo nivel (PID por articulación)
         ↓
Actuadores (motores, servos)
```


## Visión general

La planificación y el control trabajan en conjunto en una arquitectura jerárquica:

```
Objetivo de alto nivel (ej: "ir a la cocina")
         ↓
[PLANIFICACIÓN GLOBAL] → Ruta A* o RRT*
         ↓
[PLANIFICACIÓN LOCAL] → Evita obstáculos dinámicos
         ↓
[OPTIMIZACIÓN DE TRAYECTORIA] → Suaviza y optimiza movimiento
         ↓
[CONTROL DE ALTO NIVEL] → MPC, cinemática inversa
         ↓
[CONTROL DE BAJO NIVEL] → PID para cada articulación
         ↓
Actuadores (motores, servos)
```

---

## Estructura del directorio

```
04_Planificacion_Control/
├── README.md (este archivo)
│
├── planificacion/                  # Algoritmos de planificación
│   ├── global/                    # Planificación global (A*, D*, RRT*)
│   │   ├── a_star/               # Algoritmo A*
│   │   ├── d_star/               # D* y D* Lite
│   │   ├── rrt/                  # RRT y RRT*
│   │   ├── prm/                  # Probabilistic Roadmap
│   │   └── dijkstra/             # Dijkstra básico
│   │
│   ├── local/                     # Planificación local
│   │   ├── dwa/                  # Dynamic Window Approach
│   │   ├── teb/                  # Timed Elastic Band
│   │   ├── vfh/                  # Vector Field Histogram
│   │   └── potential_fields/     # Campos potenciales
│   │
│   ├── trajectory_optimization/   # Optimización de trayectorias
│   │   ├── chomp/                # CHOMP (Covariant Hamiltonian)
│   │   ├── trajopt/              # TrajOpt
│   │   ├── spline_fitting/       # Ajuste con splines
│   │   └── minimum_jerk/         # Trayectorias mínimo jerk
│   │
│   └── task_planning/             # Planificación de tareas
│       ├── behavior_trees/       # Árboles de comportamiento
│       ├── state_machines/       # Máquinas de estados
│       └── hierarchical/         # Planificación jerárquica
│
├── control/                        # Sistemas de control
│   ├── low_level/                # Control de bajo nivel
│   │   ├── pid/                  # Controladores PID
│   │   ├── pwm/                  # Control PWM para motores
│   │   ├── torque/               # Control de torque
│   │   └── velocity/             # Control de velocidad
│   │
│   ├── kinematics/               # Cinemática
│   │   ├── forward/              # Cinemática directa
│   │   ├── inverse/              # Cinemática inversa (IK)
│   │   ├── jacobian/             # Matrices jacobianas
│   │   └── denavit_hartenberg/  # Parámetros DH
│   │
│   ├── dynamics/                 # Dinámica
│   │   ├── forward_dynamics/    # Dinámica directa
│   │   ├── inverse_dynamics/    # Dinámica inversa
│   │   └── lagrangian/          # Formulación lagrangiana
│   │
│   ├── advanced/                 # Control avanzado
│   │   ├── mpc/                 # Model Predictive Control
│   │   ├── adaptive/            # Control adaptativo
│   │   ├── robust/              # Control robusto
│   │   └── optimal/             # Control óptimo (LQR)
│   │
│   └── balance/                  # Control de equilibrio
│       ├── zmp/                 # Zero Moment Point
│       ├── capture_point/       # Capture Point
│       └── inverted_pendulum/   # Péndulo invertido
│
├── simulaciones/                   # Entornos de prueba
│   ├── gazebo/                   # Simulaciones en Gazebo
│   ├── pybullet/                 # PyBullet physics
│   ├── scenarios/                # Escenarios de prueba
│   └── benchmarks/               # Tests de rendimiento
│
└── notebooks/                      # Notebooks de demostración
    ├── path_planning_astar.ipynb
    ├── rrt_visualization.ipynb
    ├── pid_tuning.ipynb
    ├── inverse_kinematics.ipynb
    ├── mpc_demo.ipynb
    └── trajectory_optimization.ipynb
```

---

## Planificación

### 1. Planificación global

Encuentra rutas óptimas en mapas conocidos desde posición inicial hasta objetivo.

**Algoritmos principales:**
- **A\***: Heurística + costo real, garantiza optimalidad
- **RRT (Rapidly-exploring Random Tree)**: Muestreo aleatorio, bueno en espacios de alta dimensión
- **RRT\***: Versión asintóticamente óptima de RRT
- **PRM (Probabilistic Roadmap)**: Construye grafo de configuraciones libres

**Ejemplo: A\* en Python**
```python
import numpy as np
from queue import PriorityQueue

def heuristic(a, b):
    """Distancia euclidiana"""
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def a_star(grid, start, goal):
    """Implementación de A*"""
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while not frontier.empty():
        current = frontier.get()[1]
        
        if current == goal:
            break
            
        for next in neighbors(current, grid):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current
    
    return reconstruct_path(came_from, start, goal)
```

### 2. Planificación local

Evita obstáculos dinámicos y ajusta la ruta en tiempo real.

**Algoritmos:**
- **DWA (Dynamic Window Approach)**: Evalúa velocidades admisibles
- **TEB (Timed Elastic Band)**: Optimiza trayectoria en tiempo
- **VFH (Vector Field Histogram)**: Basado en histogramas de obstáculos

---

## Control

### 1. Control PID (bajo nivel)

Control básico para cada articulación:

```python
class PIDController:
    def __init__(self, kp, ki, kd, dt):
        self.kp = kp  # Proporcional
        self.ki = ki  # Integral
        self.kd = kd  # Derivativo
        self.dt = dt
        self.integral = 0
        self.prev_error = 0
    
    def update(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        
        output = (self.kp * error + 
                 self.ki * self.integral + 
                 self.kd * derivative)
        
        self.prev_error = error
        return output
```

### 2. Cinemática Inversa

Calcula ángulos de articulaciones dado una posición/orientación deseada del efector final.

**Métodos:**
- **Analítico**: Solución cerrada (rápido, limitado a geometrías simples)
- **Jacobiano**: Iterativo, funciona en configuraciones complejas
- **CCD (Cyclic Coordinate Descent)**: Heurístico, simple y efectivo

### 3. Model Predictive Control (MPC)

Control avanzado que optimiza secuencia de acciones futuras:

```python
import cvxpy as cp

def mpc_controller(x0, A, B, Q, R, N=10):
    """
    MPC básico para sistema lineal
    x_{k+1} = Ax_k + Bu_k
    """
    n = A.shape[0]  # Estados
    m = B.shape[1]  # Entradas
    
    x = cp.Variable((n, N+1))
    u = cp.Variable((m, N))
    
    cost = 0
    constraints = [x[:, 0] == x0]
    
    for k in range(N):
        cost += cp.quad_form(x[:, k], Q) + cp.quad_form(u[:, k], R)
        constraints += [x[:, k+1] == A @ x[:, k] + B @ u[:, k]]
    
    problem = cp.Problem(cp.Minimize(cost), constraints)
    problem.solve()
    
    return u[:, 0].value  # Retorna primer control
```

---

## Integración con otros módulos

- **[02_Percepcion_Vision](../02_Percepcion_Vision/)**: Recibe datos sensoriales para detectar obstáculos
- **[03_Localizacion_Mapeo](../03_Localizacion_Mapeo/)**: Usa mapas para planificación global
- **[05_Aprendizaje_IA](../05_Aprendizaje_IA/)**: Aprendizaje por refuerzo para políticas de control
- **[00_Fundamentos](../00_Fundamentos/programacion_control.md)**: Teoría de control y programación

---

## Recursos y herramientas

### Librerías principales
```python
import numpy as np
import scipy
from control import *           # Python Control Systems Library
import cvxpy as cp             # Optimización convexa
import casadi                  # Optimización no lineal
import pinocchio              # Dinámica de robots
```

### Simuladores
- **Gazebo**: Simulación física realista
- **PyBullet**: Física rápida para RL
- **MuJoCo**: Simulación de contactos precisa
- **CoppeliaSim (V-REP)**: Versátil para prototipos

---

## Próximos pasos

1. Implementar A* para navegación básica
2. Desarrollar controladores PID para articulaciones
3. Calibrar parámetros cinemáticos del robot
4. Integrar planificador local (DWA) con global
5. Implementar MPC para locomoción bípeda
6. Validar en simulación antes de hardware real

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
