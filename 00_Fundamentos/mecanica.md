# Fundamentos de mecánica y diseño mecánico para robótica humanoide

## Resumen ejecutivo

El diseño mecánico de un robot humanoide constituye la base estructural sobre la cual se integran todos los demás sistemas. Este documento presenta los fundamentos teóricos y aplicados necesarios para el diseño, análisis y construcción de la estructura mecánica de robots humanoides, con énfasis en la replicación de movimientos antropomórficos y la optimización estructural.

## 1. Fundamentos teóricos de mecánica aplicada

### 1.1 Principios básicos de mecánica

La mecánica clásica newtoniana gobierna el comportamiento físico del robot humanoide. Los principios fundamentales incluyen:

#### 1.1.1 Leyes del movimiento de Newton

**Primera Ley (Inercia)**:
Un cuerpo permanece en su estado de reposo o movimiento rectilíneo uniforme a menos que actúe sobre él una fuerza neta.

Aplicación: El robot debe superar su propia inercia para iniciar el movimiento, requiriendo actuadores con torque suficiente.

**Segunda Ley (Fuerza y Aceleración)**:
$$F = ma$$

Donde:
- $F$ = Fuerza neta (N)
- $m$ = Masa del sistema (kg)
- $a$ = Aceleración resultante (m/s²)

Aplicación: Cálculo de torques requeridos en articulaciones para movimientos con aceleraciones específicas.

**Tercera Ley (Acción-Reacción)**:
Para cada acción existe una reacción igual y opuesta.

Aplicación: Fuerzas de contacto pie-suelo durante la marcha bípeda, diseño de sistemas de agarre.

#### 1.1.2 Torque y momento de fuerza

El torque ($\tau$) es la tendencia de una fuerza a producir rotación alrededor de un eje:

$$\tau = r \times F = rF\sin(\theta)$$

Donde:
- $r$ = Vector de posición desde el eje de rotación
- $F$ = Fuerza aplicada
- $\theta$ = Ángulo entre $r$ y $F$

**Ecuación de movimiento rotacional**:
$$\tau = I\alpha$$

Donde:
- $I$ = Momento de inercia (kg·m²)
- $\alpha$ = Aceleración angular (rad/s²)

**Cálculo para articulación de codo**:

Consideremos un antebrazo de masa $m = 0.5$ kg, longitud $L = 0.3$ m, levantando un objeto de $m_{obj} = 0.2$ kg:

```python
import numpy as np

def calcular_torque_codo(masa_brazo, longitud, masa_objeto, angulo_grados):
    """
    Calcula el torque requerido en la articulación del codo
    
    Args:
        masa_brazo: Masa del antebrazo (kg)
        longitud: Longitud del antebrazo (m)
        masa_objeto: Masa del objeto sujetado (kg)
        angulo_grados: Ángulo del brazo respecto a la horizontal (grados)
    
    Returns:
        torque: Torque requerido (N·m)
    """
    g = 9.81  # Aceleración gravitacional (m/s²)
    angulo_rad = np.radians(angulo_grados)
    
    # Centro de masa del brazo está en L/2
    torque_brazo = masa_brazo * g * (longitud / 2) * np.cos(angulo_rad)
    
    # Objeto está en el extremo
    torque_objeto = masa_objeto * g * longitud * np.cos(angulo_rad)
    
    torque_total = torque_brazo + torque_objeto
    
    return torque_total

# Ejemplo: brazo horizontal (90°)
torque_requerido = calcular_torque_codo(0.5, 0.3, 0.2, 90)
print(f"Torque requerido: {torque_requerido:.3f} N·m")
print(f"En kg·cm: {torque_requerido * 100 / 9.81:.2f} kg·cm")
```

Output esperado: ~2.1 N·m ≈ 21.4 kg·cm

#### 1.1.3 Fricción y eficiencia mecánica

**Fricción estática**: $f_s \leq \mu_s N$
**Fricción cinética**: $f_k = \mu_k N$

Donde:
- $\mu_s, \mu_k$ = Coeficientes de fricción estática y cinética
- $N$ = Fuerza normal

**Impacto en el diseño**:
- Selección de rodamientos vs. bujes
- Lubricación de articulaciones
- Pérdidas de eficiencia en transmisiones

**Eficiencia mecánica**:
$$\eta = \frac{P_{salida}}{P_{entrada}} = \frac{\tau_{salida} \omega_{salida}}{\tau_{entrada} \omega_{entrada}}$$

Valores típicos:
- Engranajes rectos: 95-98%
- Engranajes cónicos: 93-97%
- Transmisión por correa: 90-95%
- Husillo de bolas: 85-95%

### 1.2 Cinemática y dinámica

#### 1.2.1 Cinemática directa

La cinemática estudia el movimiento sin considerar las fuerzas que lo causan.

**Convención de Denavit-Hartenberg (DH)**:

Para cada articulación $i$, se definen 4 parámetros:
- $a_i$: Longitud del eslabón
- $\alpha_i$: Ángulo de torsión del eslabón
- $d_i$: Desplazamiento del eslabón
- $\theta_i$: Ángulo de la articulación

**Matriz de transformación homogénea**:

$$T_i^{i-1} = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\
\sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

**Implementación para brazo 3-DOF**:

```python
import numpy as np
from scipy.spatial.transform import Rotation

class BrazoRobot3DOF:
    """
    Modelo cinemático de brazo robótico con 3 grados de libertad
    usando convención Denavit-Hartenberg
    """
    
    def __init__(self, L1=0.15, L2=0.20, L3=0.15):
        """
        Args:
            L1, L2, L3: Longitudes de los eslabones (m)
        """
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        
        # Parámetros DH: [a, alpha, d, theta]
        # theta es variable, los demás son constantes
        self.dh_params = [
            [0, np.pi/2, L1, 0],  # Articulación hombro (rotación Y)
            [L2, 0, 0, 0],         # Articulación codo
            [L3, 0, 0, 0]          # Articulación muñeca
        ]
    
    def matriz_dh(self, a, alpha, d, theta):
        """Matriz de transformación DH para una articulación"""
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
    
    def cinematica_directa(self, theta1, theta2, theta3):
        """
        Calcula la posición del efector final dados los ángulos de articulaciones
        
        Args:
            theta1, theta2, theta3: Ángulos articulares (radianes)
        
        Returns:
            posicion: [x, y, z] del efector final
            orientacion: Matriz de rotación 3x3
        """
        # Actualizar valores de theta
        thetas = [theta1, theta2, theta3]
        
        # Calcular transformación compuesta
        T = np.eye(4)
        for i, (a, alpha, d, _) in enumerate(self.dh_params):
            T_i = self.matriz_dh(a, alpha, d, thetas[i])
            T = T @ T_i
        
        posicion = T[0:3, 3]
        orientacion = T[0:3, 0:3]
        
        return posicion, orientacion
    
    def alcance_maximo(self):
        """Calcula el alcance máximo del brazo"""
        return self.L1 + self.L2 + self.L3
    
    def workspace_analysis(self, n_samples=50):
        """
        Analiza el espacio de trabajo alcanzable
        
        Returns:
            puntos: Array de puntos alcanzables [N, 3]
        """
        puntos = []
        
        for theta1 in np.linspace(-np.pi, np.pi, n_samples):
            for theta2 in np.linspace(-np.pi, np.pi, n_samples):
                for theta3 in np.linspace(-np.pi, np.pi, n_samples):
                    pos, _ = self.cinematica_directa(theta1, theta2, theta3)
                    puntos.append(pos)
        
        return np.array(puntos)

# Ejemplo de uso
brazo = BrazoRobot3DOF(L1=0.15, L2=0.20, L3=0.15)

# Posición con todos los ángulos en 0
pos, rot = brazo.cinematica_directa(0, 0, 0)
print(f"Posición (0,0,0): {pos}")
print(f"Alcance máximo: {brazo.alcance_maximo():.3f} m")

# Configuración en "L"
pos_l, _ = brazo.cinematica_directa(0, np.pi/2, 0)
print(f"Posición en 'L': {pos_l}")
```

#### 1.2.2 Cinemática inversa

Problema: Dados la posición y orientación deseadas del efector final, calcular los ángulos articulares necesarios.

**Métodos de solución**:

1. **Analítico** (para configuraciones simples)
2. **Numérico** (Jacobiano, Newton-Raphson)
3. **Geométrico** (descomposición de cadena cinemática)

**Implementación usando Jacobiano**:

```python
def cinematica_inversa_numerica(self, target_pos, theta_init=None, 
                                 max_iter=100, tol=1e-4):
    """
    Cinemática inversa usando método del Jacobiano
    
    Args:
        target_pos: Posición deseada [x, y, z]
        theta_init: Ángulos iniciales (si None, usa [0,0,0])
        max_iter: Iteraciones máximas
        tol: Tolerancia de error
    
    Returns:
        theta: Ángulos articulares solución
        exito: Boolean indicando convergencia
    """
    if theta_init is None:
        theta = np.array([0.0, 0.0, 0.0])
    else:
        theta = np.array(theta_init)
    
    for iteration in range(max_iter):
        # Calcular posición actual
        pos_actual, _ = self.cinematica_directa(*theta)
        
        # Error de posición
        error = target_pos - pos_actual
        error_norm = np.linalg.norm(error)
        
        if error_norm < tol:
            return theta, True
        
        # Calcular Jacobiano numérico
        J = self._jacobiano_numerico(theta)
        
        # Pseudo-inversa del Jacobiano
        J_pinv = np.linalg.pinv(J)
        
        # Actualizar ángulos
        delta_theta = J_pinv @ error
        theta += delta_theta * 0.1  # Factor de amortiguamiento
        
        # Limitar rango articular
        theta = np.clip(theta, -np.pi, np.pi)
    
    return theta, False

def _jacobiano_numerico(self, theta, epsilon=1e-6):
    """Calcula el Jacobiano usando diferencias finitas"""
    J = np.zeros((3, 3))
    pos_base, _ = self.cinematica_directa(*theta)
    
    for i in range(3):
        theta_perturb = theta.copy()
        theta_perturb[i] += epsilon
        pos_perturb, _ = self.cinematica_directa(*theta_perturb)
        J[:, i] = (pos_perturb - pos_base) / epsilon
    
    return J

# Añadir métodos a la clase BrazoRobot3DOF
BrazoRobot3DOF.cinematica_inversa_numerica = cinematica_inversa_numerica
BrazoRobot3DOF._jacobiano_numerico = _jacobiano_numerico

# Ejemplo de uso
brazo = BrazoRobot3DOF()
target = np.array([0.3, 0.2, 0.15])
theta_solucion, exito = brazo.cinematica_inversa_numerica(target)

if exito:
    print(f"Solución encontrada: {np.degrees(theta_solucion)}")
    pos_verificacion, _ = brazo.cinematica_directa(*theta_solucion)
    print(f"Verificación: {pos_verificacion}")
    print(f"Error: {np.linalg.norm(target - pos_verificacion):.6f} m")
else:
    print("No se encontró solución")
```

#### 1.2.3 Dinámica de robots

La dinámica relaciona fuerzas/torques con movimientos. Dos formulaciones principales:

**1. Ecuaciones de Euler-Lagrange**:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = \tau_i$$

Donde $L = T - V$ (Lagrangiano = energía cinética - energía potencial)

**2. Formulación de Newton-Euler**:

$$\tau = M(q)\ddot{q} + C(q,\dot{q})\dot{q} + g(q)$$

Donde:
- $M(q)$ = Matriz de inercia
- $C(q,\dot{q})$ = Fuerzas de Coriolis y centrífugas
- $g(q)$ = Vector de gravedad

**Implementación simplificada para 1-DOF**:

```python
class ArticulacionDinamica:
    """Modelo dinámico de una articulación simple"""
    
    def __init__(self, masa, longitud, friccion=0.1):
        self.m = masa          # kg
        self.L = longitud      # m
        self.b = friccion      # N·m·s/rad
        self.g = 9.81          # m/s²
        
        # Momento de inercia (barra homogénea)
        self.I = (1/3) * self.m * self.L**2
    
    def ecuacion_movimiento(self, theta, theta_dot, torque):
        """
        Calcula la aceleración angular dada configuración actual y torque
        
        d²θ/dt² = (τ - mgL/2·sin(θ) - b·dθ/dt) / I
        """
        torque_gravedad = (self.m * self.g * self.L / 2) * np.sin(theta)
        torque_friccion = self.b * theta_dot
        
        theta_ddot = (torque - torque_gravedad - torque_friccion) / self.I
        
        return theta_ddot
    
    def simular(self, theta0, theta_dot0, torque_func, t_final, dt=0.001):
        """
        Simula el movimiento de la articulación
        
        Args:
            theta0: Ángulo inicial (rad)
            theta_dot0: Velocidad angular inicial (rad/s)
            torque_func: Función que devuelve torque dado tiempo t
            t_final: Tiempo final de simulación (s)
            dt: Paso de tiempo (s)
        
        Returns:
            tiempo, theta, theta_dot, theta_ddot
        """
        n_steps = int(t_final / dt)
        t = np.linspace(0, t_final, n_steps)
        
        theta = np.zeros(n_steps)
        theta_dot = np.zeros(n_steps)
        theta_ddot = np.zeros(n_steps)
        
        theta[0] = theta0
        theta_dot[0] = theta_dot0
        
        for i in range(1, n_steps):
            # Calcular aceleración
            torque = torque_func(t[i-1])
            theta_ddot[i-1] = self.ecuacion_movimiento(
                theta[i-1], theta_dot[i-1], torque
            )
            
            # Integración (Euler)
            theta_dot[i] = theta_dot[i-1] + theta_ddot[i-1] * dt
            theta[i] = theta[i-1] + theta_dot[i-1] * dt
        
        return t, theta, theta_dot, theta_ddot

# Ejemplo: aplicar torque constante
articulacion = ArticulacionDinamica(masa=0.5, longitud=0.3)

# Torque de escalón
def torque_escalon(t):
    return 2.0 if t > 0.1 else 0.0

t, theta, theta_dot, theta_ddot = articulacion.simular(
    theta0=np.pi/2,  # Inicio horizontal
    theta_dot0=0,
    torque_func=torque_escalon,
    t_final=2.0
)

print(f"Posición final: {np.degrees(theta[-1]):.2f}°")
print(f"Velocidad final: {theta_dot[-1]:.2f} rad/s")
```

## 2. Diseño de articulaciones

### 2.1 Tipos de articulaciones

Las articulaciones son las conexiones móviles entre eslabones. Principales tipos:

#### 2.1.1 Articulación de revolución (R)

**Características**:
- 1 grado de libertad (rotación alrededor de un eje)
- Más común en robots humanoides
- Ejemplos: codo, rodilla (flexión/extensión)

**Diseño típico**:
```
┌─────────────────────────────────────┐
│   Componentes de articulación R     │
├─────────────────────────────────────┤
│ 1. Servomotor (actuador)            │
│ 2. Rodamiento de bolas (2 unidades) │
│ 3. Eje de rotación (acero)          │
│ 4. Estructura de soporte            │
│ 5. Encoder de posición (opcional)   │
└─────────────────────────────────────┘
```

**Consideraciones de diseño**:
- Rango de movimiento (ROM): Definir límites biomecánicamente realistas
- Torque requerido: Calcular usando análisis dinámico
- Rigidez: Minimizar flexibilidad no deseada
- Backlash: Reducir juego mecánico (<0.5°)

#### 2.1.2 Articulación prismática (P)

**Características**:
- 1 DOF (traslación lineal)
- Menos común en humanoides, más en manipuladores industriales
- Ejemplo: Extensión telescópica de brazo

#### 2.1.3 Articulación esférica (S)

**Características**:
- 3 DOF (rotación en 3 ejes)
- Compleja de implementar mecánicamente
- Ejemplo: Hombro humano (abducción/aducción, flexión/extensión, rotación interna/externa)

**Implementación práctica**:
- Usar 3 articulaciones R en configuración ortogonal
- Evitar singularidades (gimbal lock)

### 2.2 Diseño biomimético de articulaciones

Los robots humanoides buscan replicar los rangos de movimiento humanos:

**Tabla de rangos articulares humanos**:

| Articulación | Movimiento | Rango típico | Implementación robótica |
|-------------|-----------|--------------|------------------------|
| Cuello | Flexión/extensión | 0-60° | 1 DOF (servo digital) |
| | Rotación lateral | ±70° | 1 DOF |
| | Inclinación | ±45° | 1 DOF (opcional) |
| Hombro | Flexión/extensión | 0-180° | 1 DOF |
| | Abducción/aducción | 0-180° | 1 DOF |
| | Rotación int/ext | ±90° | 1 DOF |
| Codo | Flexión | 0-150° | 1 DOF |
| | Pronación/supinación | ±90° | 1 DOF (muñeca) |
| Muñeca | Flexión dorsivolar | ±70° | 1-2 DOF |
| | Desviación radial/ulnar | ±30° | 1 DOF (opcional) |
| Cadera | Flexión/extensión | -15 a 120° | 1 DOF |
| | Abducción/aducción | ±45° | 1 DOF |
| | Rotación int/ext | ±45° | 1 DOF |
| Rodilla | Flexión | 0-140° | 1 DOF |
| Tobillo | Dorsiflexión/plantarflexión | -20 a 45° | 1 DOF |
| | Inversión/eversión | ±30° | 1 DOF (opcional) |

### 2.3 Selección de rodamientos y bujes

**Rodamientos de bolas**:
- Fricción ultra-baja ($\mu \approx 0.001$)
- Alta precisión
- Mayor costo
- Uso: Articulaciones principales

**Bujes de bronce/plástico**:
- Fricción moderada ($\mu \approx 0.05-0.15$)
- Menor costo
- Requiere lubricación
- Uso: Articulaciones secundarias, prototipos

**Dimensionamiento de rodamientos**:

```python
def seleccionar_rodamiento(diametro_eje_mm, carga_radial_N, 
                          carga_axial_N, rpm):
    """
    Guía básica para seleccionar rodamiento
    
    Returns:
        tipo_recomendado: String con recomendación
        carga_dinamica_requerida: C10 en N
    """
    # Carga equivalente (fórmula simplificada)
    P = carga_radial_N + 0.5 * carga_axial_N
    
    # Vida útil deseada en millones de revoluciones
    L10 = 1  # 1 millón de revoluciones (ajustable)
    
    # Capacidad de carga dinámica requerida
    C10 = P * (L10 ** (1/3))
    
    # Recomendación según diámetro
    if diametro_eje_mm <= 8:
        tipo = "608 (skate bearing) o 688"
    elif diametro_eje_mm <= 12:
        tipo = "6000 series o MR12"
    elif diametro_eje_mm <= 20:
        tipo = "6200 series"
    else:
        tipo = "6300 series o superior"
    
    return tipo, C10

# Ejemplo: articulación de codo
tipo, C10 = seleccionar_rodamiento(
    diametro_eje_mm=10,
    carga_radial_N=80,  # Peso de antebrazo + objeto
    carga_axial_N=10,
    rpm=30  # Movimiento lento
)
print(f"Rodamiento recomendado: {tipo}")
print(f"Capacidad de carga dinámica requerida: {C10:.1f} N")
```

## 3. Modelado 3D y CAD

### 3.1 Software CAD para robótica

**Opciones principales**:

1. **SolidWorks** (Comercial, ~$3,000/año)
   - Industria estándar
   - Excelente análisis FEA
   - Buena integración con fabricación

2. **Fusion 360** (Comercial/Gratuito para estudiantes)
   - Cloud-based
   - Buena curva de aprendizaje
   - CAM integrado

3. **FreeCAD** (Open-source, gratuito)
   - Capacidades completas
   - Módulo de robots
   - Comunidad activa

### 3.2 Flujo de trabajo de diseño

```
1. Concept Sketching
   └── Bocetos manuales, proporciones iniciales
   
2. CAD Modeling
   ├── Part Design: Diseñar cada pieza individual
   ├── Assembly: Ensamblar componentes
   └── Constraints: Definir restricciones de movimiento
   
3. Simulation
   ├── Motion Study: Verificar rangos de movimiento
   ├── FEA: Análisis de esfuerzos
   └── Interference Check: Detectar colisiones
   
4. Optimization
   ├── Topology Optimization: Reducir peso
   ├── Material Selection: Ajustar propiedades
   └── Iteration: Refinar diseño
   
5. Manufacturing Prep
   ├── Drawings: Planos técnicos
   ├── BOM: Lista de materiales
   └── Export: STL para 3D, DXF para CNC
```

### 3.3 Modelado paramétrico

Ventaja: Modificaciones rápidas ajustando parámetros

**Ejemplo de parámetros para brazo robótico**:

```
// Parámetros globales (en SolidWorks o Fusion 360)
L1_hombro_codo = 200 mm
L2_codo_muneca = 150 mm
diametro_eje = 10 mm
espesor_pared = 3 mm
altura_servo = 40 mm
longitud_servo = 20 mm

// Relaciones derivadas
alcance_maximo = L1_hombro_codo + L2_codo_muneca
factor_seguridad = 1.5
```

### 3.4 Análisis de elementos finitos (FEA)

**Objetivo**: Verificar que las piezas soportan cargas sin fallar

**Procedimiento típico**:

1. **Definir material**: Ejemplo, PLA (resistencia tensión ~50 MPa)
2. **Aplicar cargas**: Fuerzas, momentos, gravedad
3. **Definir restricciones**: Puntos fijos
4. **Mallar**: Discretizar geometría
5. **Solver**: Calcular esfuerzos y deformaciones
6. **Evaluar**: Factor de seguridad > 2 (conservador)

**Criterio de fallo (Von Mises)**:

$$\sigma_{VM} = \sqrt{\frac{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}{2}}$$

Si $\sigma_{VM} < \sigma_{yield} / FS$, la pieza es segura.

```python
def evaluar_fea_results(sigma_vm_max_mpa, material='PLA'):
    """
    Evalúa resultados de FEA
    
    Args:
        sigma_vm_max_mpa: Esfuerzo de Von Mises máximo (MPa)
        material: Material de la pieza
    
    Returns:
        factor_seguridad, aprueba
    """
    # Resistencia de fluencia de materiales comunes
    resistencias = {
        'PLA': 50,          # MPa
        'ABS': 40,          # MPa
        'PETG': 50,         # MPa
        'Nylon': 60,        # MPa
        'Aluminio 6061': 276,  # MPa
        'Acero 1045': 530   # MPa
    }
    
    sigma_yield = resistencias.get(material, 50)
    factor_seguridad = sigma_yield / sigma_vm_max_mpa
    aprueba = factor_seguridad >= 2.0
    
    return factor_seguridad, aprueba

# Ejemplo
fs, ok = evaluar_fea_results(18.5, material='PLA')
print(f"Factor de seguridad: {fs:.2f}")
print(f"Aprueba: {'SĂ­' if ok else 'NO - Rediseñar'}")
```

## 4. Selección de materiales

### 4.1 Materiales para impresión 3D

**Comparativa de materiales termoplásticos**:

| Material | Densidad (g/cm³) | Resistencia tensión (MPa) | Módulo Young (GPa) | Temp. impresión (°C) | Costo relativo |
|---------|------------------|--------------------------|-------------------|---------------------|----------------|
| PLA | 1.24 | 50 | 3.5 | 190-220 | $ |
| ABS | 1.04 | 40 | 2.3 | 220-250 | $ |
| PETG | 1.27 | 50 | 2.1 | 220-250 | $$ |
| Nylon | 1.14 | 60 | 2.7 | 240-270 | $$$ |
| TPU (flexible) | 1.21 | 26 | 0.1 | 210-230 | $$ |
| Carbon Fiber PLA | 1.3 | 70 | 6.0 | 200-220 | $$$$ |

**Guía de selección por aplicación**:

```
Componentes estructurales principales: 
  → PLA reforzado con fibra de carbono, Nylon

Articulaciones y partes móviles:
  → PETG (resistente al impacto), Nylon (bajo fricción)

Carcasas protectoras:
  → ABS (buena resistencia, ligero)

Amortiguadores y juntas flexibles:
  → TPU, TPE (flexibles)

Prototipos rápidos:
  → PLA (fácil impresión, bajo costo)
```

### 4.2 Materiales metálicos

**Para piezas mecanizadas críticas**:

**Aluminio 6061-T6**:
- Densidad: 2.7 g/cm³
- Resistencia: 276 MPa
- Excelente relación resistencia/peso
- Fácil mecanizado
- Uso: Estructura principal, ejes

**Acero 1045**:
- Densidad: 7.85 g/cm³
- Resistencia: 530 MPa
- Mayor resistencia que aluminio
- Más pesado
- Uso: Ejes de alta carga, engranajes

**Latón/Bronce**:
- Buena maquinabilidad
- Bajo fricción
- Uso: Bujes, tuercas autoblocantes

### 4.3 Optimización de peso vs. resistencia

**Estrategias**:

1. **Topología Interna (Infill)**:
   - Sólido (100%): Máxima resistencia, pesado
   - Honeycomb (20-40%): Balance óptimo
   - Gyroid (30%): Isotrópico, buena resistencia

2. **Perfiles Estructurales**:
   - Vigas en I: Alta rigidez a flexión
   - Tubos: Alta resistencia torsional
   - Estructuras tipo sándwich: Ligeras y rígidas

3. **Optimización Topológica**:
   - Software: Fusion 360, nTopology, Altair Inspire
   - Reduce peso 30-60% manteniendo rigidez
   - Geometrías orgánicas

```python
def calcular_masa_pieza(volumen_cm3, material, infill=0.3):
    """
    Estima la masa de una pieza impresa en 3D
    
    Args:
        volumen_cm3: Volumen externo de la pieza
        material: Tipo de material ('PLA', 'ABS', etc.)
        infill: Porcentaje de relleno (0.0 a 1.0)
    
    Returns:
        masa_g: Masa estimada en gramos
    """
    densidades = {
        'PLA': 1.24,
        'ABS': 1.04,
        'PETG': 1.27,
        'Nylon': 1.14,
        'TPU': 1.21
    }
    
    densidad = densidades.get(material, 1.24)
    
    # Modelo simplificado: 2 paredes + infill
    espesor_pared_mm = 1.2  # Típico: 3 perímetros x 0.4mm
    area_superficial_estimada = 6 * (volumen_cm3 ** (2/3))  # Aproximación
    volumen_paredes = area_superficial_estimada * (espesor_pared_mm / 10)
    volumen_infill = (volumen_cm3 - volumen_paredes) * infill
    volumen_total_material = volumen_paredes + volumen_infill
    
    masa_g = volumen_total_material * densidad
    
    return masa_g

# Ejemplo: antebrazo del robot
volumen_antebrazo = 120  # cm³ (120 x 40 x 60 mm)
masa = calcular_masa_pieza(volumen_antebrazo, 'PETG', infill=0.25)
print(f"Masa estimada del antebrazo: {masa:.1f} g")
```

## 5. Tolerancias y ajustes

### 5.1 Sistema de ajustes ISO

Las tolerancias determinan qué tan precisas deben ser las dimensiones.

**Tipos de ajuste**:

1. **Con holgura (Clearance fit)**: El agujero es siempre más grande que el eje
   - Ejemplo: H7/g6 para rodamientos que deben girar libremente
   
2. **Con apriete (Interference fit)**: El eje es siempre más grande que el agujero
   - Ejemplo: H7/p6 para ejes fijos en rodamientos
   
3. **Indeterminado (Transition fit)**: Puede haber holgura o apriete ligero
   - Ejemplo: H7/k6 para ajustes precisos

**Tablas de tolerancias (simplificadas)**:

Para un diámetro nominal de 10 mm:
- H7 (agujero): +0.015/0 mm → Diámetro real: 10.000 - 10.015 mm
- g6 (eje): -0.005/-0.014 mm → Diámetro real: 9.986 - 9.995 mm
- Holgura mínima: 10.000 - 9.995 = 0.005 mm
- Holgura máxima: 10.015 - 9.986 = 0.029 mm

### 5.2 Tolerancias en impresión 3D

**Precisión dimensional típica**:
- FDM (impresión de filamento): ±0.2 - 0.5 mm
- SLA (resina): ±0.05 - 0.1 mm

**Compensación en diseño CAD**:

```python
def compensar_ajuste_impresion3d(diametro_nominal, tipo_ajuste='deslizante'):
    """
    Ajusta dimensiones para impresión 3D
    
    Args:
        diametro_nominal: Diámetro deseado en mm
        tipo_ajuste: 'apretado', 'deslizante', 'libre'
    
    Returns:
        diametro_agujero, diametro_eje
    """
    # Compensaciones empíricas para FDM
    compensaciones = {
        'apretado': {'agujero': -0.1, 'eje': 0.1},     # Ajuste a presión
        'deslizante': {'agujero': 0.15, 'eje': -0.15},  # Desliza suave
        'libre': {'agujero': 0.3, 'eje': -0.3}          # Movimiento libre
    }
    
    comp = compensaciones.get(tipo_ajuste, compensaciones['deslizante'])
    
    diametro_agujero = diametro_nominal + comp['agujero']
    diametro_eje = diametro_nominal + comp['eje']
    
    return diametro_agujero, diametro_eje

# Ejemplo: Eje de 6mm para rodamiento 608
d_agujero, d_eje = compensar_ajuste_impresion3d(8, 'deslizante')
print(f"Diseñar agujero: Ø{d_agujero:.2f} mm")
print(f"Diseñar eje: Ø{d_eje:.2f} mm")
```

### 5.3 Post-procesamiento para mayor precisión

**Técnicas**:
- **Taladrado/escariado**: Mejora precisión de agujeros
- **Roscado**: Insertos metálicos para roscas durables
- **Lijado/pulido**: Mejora acabado superficial
- **Vapor de acetona** (solo ABS): Suaviza superficie

## 6. Fabricación y ensamblaje

### 6.1 Impresión 3D - best practices

**Configuración óptima (FDM)**:

```
Capa inicial: 0.2-0.3 mm (adherencia)
Capas subsecuentes: 0.1-0.2 mm (calidad vs. velocidad)
Perímetros: 3-4 (resistencia)
Infill: 20-30% (piezas estándar), 50%+ (alta carga)
Patrón infill: Gyroid, Grid, Honeycomb
Velocidad: 40-60 mm/s (calidad), 80-100 mm/s (rápido)
Temperatura: Según fabricante del filamento
Cama caliente: 50-60°C (PLA), 90-110°C (ABS)
Soportes: Sí, si hay overhangs >45°
Brim/Raft: Sí, para piezas grandes o con poca adherencia
```

**Orientación de impresión**:

Principio: Las capas son el punto débil.

```
Fuerza Óptima: Cargar en dirección PARALELA a las capas
Fuerza Débil: Cargar PERPENDICULAR a las capas

Ejemplo: Brazo robótico
  Imprimir verticalmente: Débil a flexión lateral
  Imprimir horizontalmente: Fuerte a flexión lateral
```

### 6.2 Mecanizado CNC

Para piezas metálicas críticas:

**Proceso típico**:
1. Diseñar pieza en CAD
2. Generar CAM (trayectorias de herramienta)
3. Post-procesar a G-code específico de máquina
4. Mecanizar en CNC
5. Inspección dimensional

**Operaciones comunes**:
- Torneado: Piezas cilíndricas (ejes)
- Fresado: Geometrías complejas
- Taladrado: Agujeros precisos
- Roscado: Roscas internas/externas

### 6.3 Ensamblaje

**Técnicas de unión**:

1. **Tornillos y tuercas**:
   - M3, M4, M5 más comunes en robótica pequeña
   - Usar arandelas de seguridad para evitar aflojamiento
   - Threadlocker (Loctite) para permanentes

2. **Insertos roscados** (para plástico):
   - Insertos térmicos (calentados e insertados)
   - Insertos a presión
   - MUCHO más resistentes que roscar directo en plástico

3. **Pegado**:
   - Cianoacrilato (super glue): PLA, ABS
   - Epoxy: Alta resistencia
   - Soldadura química: Acetona para ABS, cloroformo para PLA

4. **Snap-fits**:
   - Sin herramientas
   - Para ensamblaje/desensamblaje frecuente
   - Requiere diseño cuidadoso

**Orden de ensamblaje típico para robot humanoide**:

```
1. Subensamblar piernas (pie → tobillo → tibia → rodilla → fémur → cadera)
2. Subensamblar brazos (mano → muñeca → antebrazo → codo → brazo → hombro)
3. Ensamblar torso con estructura de energía
4. Montar piernas en cadera
5. Montar brazos en hombros
6. Instalar cabeza
7. Cableado
8. Instalación de covers/carcasas
```

## 7. Simulación y pruebas virtuales

### 7.1 Simulación en Gazebo/PyBullet

Antes de fabricar físicamente, validar en simulación:

**Ejemplo en PyBullet**:

```python
import pybullet as p
import pybullet_data
import time

# Inicializar simulación
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Cargar robot desde URDF
robot_id = p.loadURDF("mi_humanoid.urdf", [0, 0, 0.5])

# Obtener información de articulaciones
num_joints = p.getNumJoints(robot_id)
for i in range(num_joints):
    info = p.getJointInfo(robot_id, i)
    print(f"Joint {i}: {info[1].decode('utf-8')}, Type: {info[2]}")

# Control de articulaciones
for step in range(10000):
    # Ejemplo: mover brazo derecho
    p.setJointMotorControl2(
        robot_id,
        jointIndex=2,  # Hombro derecho
        controlMode=p.POSITION_CONTROL,
        targetPosition=1.57  # 90 grados
    )
    
    p.stepSimulation()
    time.sleep(1/240)  # 240 Hz

p.disconnect()
```

### 7.2 Verificación de colisiones

Detectar interferencias entre partes:

```python
def verificar_colisiones_self(robot_id):
    """Detecta auto-colisiones en configuración actual"""
    contact_points = p.getContactPoints(robot_id, robot_id)
    
    if len(contact_points) > 0:
        print("COLISIÓN DETECTADA:")
        for cp in contact_points:
            link_a = cp[3]
            link_b = cp[4]
            print(f"  Link {link_a} colisiona con Link {link_b}")
        return True
    return False
```

## 8. Referencias y recursos

### 8.1 Libros fundamentales

1. **"Robot Modeling and Control"** - Spong, Hutchinson, Vidyasagar
   - Cinemática, dinámica, control - nivel académico riguroso

2. **"Introduction to Robotics: Mechanics and Control"** - John J. Craig
   - Texto clásico, excelente para cinemática DH

3. **"Modern Robotics"** - Lynch y Park
   - Enfoque geométrico moderno, con software complementario

### 8.2 Software y herramientas

- **SolidWorks**: CAD profesional
- **Fusion 360**: CAD + CAM + simulación
- **FreeCAD**: Open-source alternativo
- **MATLAB Robotics Toolbox**: Cinemática y control
- **ROS (Robot Operating System)**: Framework de software
- **Gazebo / PyBullet**: Simulación física

### 8.3 Estándares relevantes

- **ISO 8373**: Vocabulario de robótica
- **ISO 9283**: Pruebas de performance de robots
- **ISO/TS 15066**: Robots colaborativos
- **DIN 51524**: Lubricantes para rodamientos

---

## Conclusiones

El diseño mecánico de un robot humanoide requiere una integración profunda de:

1. **Fundaments teóricos**: Mecánica newtoniana, cinemática, dinámica
2. **Herramientas CAD**: Modelado paramétrico, FEA, optimización
3. **Selección de materiales**: Balance peso-resistencia-costo
4. **Fabricación**: Impresión 3D, mecanizado, ensamblaje preciso
5. **Validación**: Simulación antes de construcción física

Este conocimiento constituye la base mecánica sobre la cual se construyen los sistemas electrónicos, de control e inteligencia artificial del robot humanoide completo.

**Próximos pasos**: Ver [electrónica](electronica.md) y [programación y control](programacion_control.md) para la integración de actuadores, sensores y sistemas embebidos.
