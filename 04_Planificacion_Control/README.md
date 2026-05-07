# Planificación y control - cerebro motor del robot

## Propósito

Este módulo implementa el **sistema de planificación y control** del robot humanoide, traduciendo objetivos de alto nivel en trayectorias ejecutables y comandos precisos para actuadores. Integra algoritmos de planificación de rutas con controladores en tiempo real para lograr movimientos coordinados, seguros y eficientes.

---

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
