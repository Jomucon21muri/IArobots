# Fundamentos de programación y control para robótica humanoide

## Resumen ejecutivo

La programación y control constituyen el cerebro cognitivo del robot humanoide, traduciendo objetivos de alto nivel en comandos específicos de actuadores. Este documento presenta los fundamentos teóricos y prácticos para implementar sistemas de control robótico a nivel doctoral, abarcando desde control de bajo nivel hasta planificación de movimiento y arquitecturas de software.

## 1. Fundamentos de programación para robótica

### 1.1 Lenguajes de programación relevantes

#### 1.1.1 C++ para sistemas embebidos

**Características clave**:
- Control de bajo nivel y acceso directo a hardware
- Alta eficiencia computacional (crítico en sistemas tiempo-real)
- Gestión manual de memoria
- Amplio uso en ROS y librerías robóticas

**Ejemplo: Control de servomotor con interrupciones**:

```cpp
#include <Arduino.h>

// Variables globales para control PWM por software
volatile uint16_t servo_position[16];  // Posiciones en microsegundos
volatile uint8_t servo_counter = 0;

// Timer interrupt para generar señales PWM precisas
ISR(TIMER1_COMPA_vect) {
    static unsigned long pulse_start = 0;
    static uint8_t current_servo = 0;
    
    unsigned long current_time = micros();
    
    if (current_time - pulse_start >= 20000) {  // Nuevo ciclo 20ms
        pulse_start = current_time;
        current_servo = 0;
        digitalWrite(SERVO_PINS[0], HIGH);
    }
    
    if (current_time - pulse_start >= servo_position[current_servo]) {
        digitalWrite(SERVO_PINS[current_servo], LOW);
        current_servo++;
        if (current_servo < NUM_SERVOS) {
            digitalWrite(SERVO_PINS[current_servo], HIGH);
        }
    }
}

// Clase para gestión de múltiples servos
class ServoController {
private:
    static const uint8_t MAX_SERVOS = 16;
    uint16_t positions[MAX_SERVOS];
    uint16_t min_pulse[MAX_SERVOS];
    uint16_t max_pulse[MAX_SERVOS];
    
public:
    ServoController() {
        for (uint8_t i = 0; i < MAX_SERVOS; i++) {
            min_pulse[i] = 544;   // 0° (~0.544ms)
            max_pulse[i] = 2400;  // 180° (~2.4ms)
            positions[i] = 1500;  // Centro (90°)
        }
    }
    
    void setAngle(uint8_t servo_id, float angle_degrees) {
        angle_degrees = constrain(angle_degrees, 0, 180);
        positions[servo_id] = map(
            angle_degrees * 10,  // Multiplicar por 10 para mejor resolución
            0, 1800,
            min_pulse[servo_id], max_pulse[servo_id]
        );
    }
    
    void setSpeed(uint8_t servo_id, float target_angle, float speed_deg_per_sec) {
        // Implementar movimiento suave con rampa de velocidad
        float current_angle = getAngle(servo_id);
        float delta = target_angle - current_angle;
        float step = speed_deg_per_sec * 0.02;  // 20ms update rate
        
        if (abs(delta) < step) {
            setAngle(servo_id, target_angle);
        } else {
            setAngle(servo_id, current_angle + (delta > 0 ? step : -step));
        }
    }
    
    float getAngle(uint8_t servo_id) {
        return map(
            positions[servo_id],
            min_pulse[servo_id], max_pulse[servo_id],
            0, 180
        );
    }
    
    void calibrate(uint8_t servo_id, uint16_t min_us, uint16_t max_us) {
        min_pulse[servo_id] = min_us;
        max_pulse[servo_id] = max_us;
    }
};
```

#### 1.1.2 Python para algoritmos y prototipado rápido

**Ventajas**:
- Sintaxis clara y expresiva
- Vasto ecosistema de librerías (NumPy, SciPy, OpenCV, TensorFlow)
- Ideal para desarrollo y experimentación rápida
- Excelente para IA/ML

**Ejemplo: Control cinemático de brazo robótico**:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class BrazoRobotico:
    """
    Modelo cinemático y de control para brazo robótico planar 3-DOF
    """
    
    def __init__(self, longitudes=[0.15, 0.20, 0.15]):
        """
        Args:
            longitudes: [L1, L2, L3] en metros
        """
        self.L = np.array(longitudes)
        self.num_joints = len(longitudes)
        self.theta = np.zeros(self.num_joints)  # Ángulos actuales (rad)
        self.theta_dot = np.zeros(self.num_joints)  # Velocidades actuales
        
        # Límites articulares (rad)
        self.theta_min = np.array([-np.pi, -np.pi/2, -3*np.pi/4])
        self.theta_max = np.array([np.pi, np.pi/2, 3*np.pi/4])
        
        # Velocidades y aceleraciones máximas
        self.theta_dot_max = np.array([2.0, 2.0, 3.0])  # rad/s
        self.theta_ddot_max = np.array([5.0, 5.0, 7.0])  # rad/s²
    
    def cinematica_directa(self, theta=None):
        """
        Calcula posición del efector final
        
        Args:
            theta: Ángulos articulares [rad]. Si None, usa self.theta
        
        Returns:
            posicion: [x, y] del efector final
        """
        if theta is None:
            theta = self.theta
        
        x = 0
        y = 0
        angle_sum = 0
        
        for i in range(self.num_joints):
            angle_sum += theta[i]
            x += self.L[i] * np.cos(angle_sum)
            y += self.L[i] * np.sin(angle_sum)
        
        return np.array([x, y])
    
    def jacobiano(self, theta=None):
        """
        Calcula matriz Jacobiana J = ∂(x,y)/∂(θ₁,θ₂,θ₃)
        
        Returns:
            J: Matriz 2×n (velocidad cartesiana = J × velocidad articular)
        """
        if theta is None:
            theta = self.theta
        
        J = np.zeros((2, self.num_joints))
        
        for i in range(self.num_joints):
            angle_sum = np.sum(theta[:i+1])
            
            # Contribución de cada articulación a la velocidad del efector
            for j in range(i+1):
                angle_sum_j = np.sum(theta[:j+1])
                J[0, j] -= self.L[i] * np.sin(angle_sum_j)  # ∂x/∂θⱼ
                J[1, j] += self.L[i] * np.cos(angle_sum_j)  # ∂y/∂θⱼ
        
        return J
    
    def cinematica_inversa_numerica(self, target, theta_init=None, method='SLSQP'):
        """
        Resuelve cinemática inversa mediante optimización numérica
        
        Args:
            target: [x, y] posición objetivo
            theta_init: Ángulos iniciales para iteración
            method: Método de optimización ('SLSQP', 'trust-constr')
        
        Returns:
            theta: Solución de ángulos articulares
            success: Boolean indicando éxito
            error: Error de posición
        """
        if theta_init is None:
            theta_init = self.theta
        
        def objetivo(theta):
            """Función objetivo: distancia al target"""
            pos = self.cinematica_directa(theta)
            return np.linalg.norm(pos - target)
        
        # Restricciones: límites articulares
        bounds = [(self.theta_min[i], self.theta_max[i]) 
                  for i in range(self.num_joints)]
        
        # Optimizar
        result = minimize(
            objetivo,
            theta_init,
            method=method,
            bounds=bounds,
            options={'maxiter': 100}
        )
        
        return result.x, result.success, result.fun
    
    def control_velocidad_cartesiana(self, v_cartesiana, alpha=0.1):
        """
        Control de velocidad cartesiana usando Jacobiano
        θ̇ = J⁻¹ × ẋ  (o pseudo-inversa si J no es cuadrada)
        
        Args:
            v_cartesiana: [vx, vy] velocidad deseada del efector
            alpha: Factor de amortiguamiento (damped least squares)
        
        Returns:
            theta_dot: Velocidades articulares requeridas
        """
        J = self.jacobiano()
        
        # Pseudo-inversa con amortiguamiento (evita singularidades)
        JJT = J @ J.T + alpha**2 * np.eye(2)
        J_pinv = J.T @ np.linalg.inv(JJT)
        
        theta_dot = J_pinv @ v_cartesiana
        
        # Saturar velocidades
        theta_dot = np.clip(theta_dot, -self.theta_dot_max, self.theta_dot_max)
        
        return theta_dot
    
    def planificar_trayectoria(self, target, duration, n_points=50):
        """
        Planifica trayectoria suave desde posición actual a target
        Usa interpolación quintica (aceleración continua)
        
        Args:
            target: [x, y] posición final
            duration: Duración del movimiento (segundos)
            n_points: Número de puntos en la trayectoria
        
        Returns:
            trayectoria: Array [n_points × 2] de posiciones
            tiempos: Array de tiempos correspondientes
        """
        # Posición inicial
        pos_inicial = self.cinematica_directa()
        
        # Generar trayectoria quintica (s(t) = a₀ + a₁t + ... + a₅t⁵)
        t = np.linspace(0, duration, n_points)
        s = self._polinomio_quintico(t, duration)
        
        # Interpolar linealmente en espacio cartesiano
        trayectoria = np.outer(1 - s, pos_inicial) + np.outer(s, target)
        
        return trayectoria, t
    
    def _polinomio_quintico(self, t, T):
        """
        Polinomio quintico normalizado con condiciones:
        s(0)=0, ṡ(0)=0, s̈(0)=0, s(T)=1, ṡ(T)=0, s̈(T)=0
        """
        tau = t / T  # Normalizar tiempo
        s = 10*tau**3 - 15*tau**4 + 6*tau**5
        return s
    
    def visualizar(self, ax=None):
        """Visualiza configuración actual del brazo"""
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 8))
        
        # Calcular posiciones de todas las articulaciones
        x_joints = [0]
        y_joints = [0]
        angle_sum = 0
        
        for i in range(self.num_joints):
            angle_sum += self.theta[i]
            x_joints.append(x_joints[-1] + self.L[i] * np.cos(angle_sum))
            y_joints.append(y_joints[-1] + self.L[i] * np.sin(angle_sum))
        
        # Dibujar eslabones
        ax.plot(x_joints, y_joints, 'o-', linewidth=3, markersize=10)
        
        # Dibujar espacio de trabajo
        alcance_max = np.sum(self.L)
        circle = plt.Circle((0, 0), alcance_max, fill=False, 
                           linestyle='--', color='gray', alpha=0.3)
        ax.add_patch(circle)
        
        ax.set_xlim(-alcance_max*1.1, alcance_max*1.1)
        ax.set_ylim(-alcance_max*1.1, alcance_max*1.1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        
        return ax

# Ejemplo de uso
if __name__ == "__main__":
    # Crear brazo robótico
    brazo = BrazoRobotico(longitudes=[0.15, 0.20, 0.15])
    
    # 1. Cinemática directa
    brazo.theta = np.array([0, np.pi/4, -np.pi/4])
    pos = brazo.cinematica_directa()
    print(f"Posición efector final: {pos}")
    
    # 2. Cinemática inversa
    target = np.array([0.30, 0.25])
    theta_solucion, exito, error = brazo.cinematica_inversa_numerica(target)
    if exito:
        print(f"Solución IK: θ = {np.degrees(theta_solucion)}°")
        print(f"Error: {error*1000:.2f} mm")
    
    # 3. Control de velocidad
    v_deseada = np.array([0.1, 0.05])  # m/s
    theta_dot = brazo.control_velocidad_cartesiana(v_deseada)
    print(f"Velocidades articulares: {np.degrees(theta_dot)}°/s")
    
    # 4. Planificación de trayectoria
    trayectoria, tiempos = brazo.planificar_trayectoria(target, duration=2.0)
    
    # 5. Visualización
    brazo.visualizar()
    plt.title('Configuración del Brazo Robótico')
    plt.show()
```

#### 1.1.3 ROS (Robot Operating System)

**Conceptos fundamentales**:
- **Nodos**: Procesos independientes que realizan tareas específicas
- **Topics**: Canales de comunicación pub/sub para mensajes
- **Services**: Llamadas RPC síncronas
- **Actions**: Tareas asíncronas con feedback
- **TF**: Sistema de transformadas espaciales

**Ejemplo: Nodo ROS en Python**:

```python
#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray
import numpy as np

class ControladorRobotHumanoide:
    """
    Nodo ROS para control de robot humanoide
    """
    
    def __init__(self):
        # Inicializar nodo
        rospy.init_node('controlador_humanoide', anonymous=False)
        
        # Parámetros
        self.rate_hz = rospy.get_param('~control_rate', 50)
        self.num_joints = rospy.get_param('~num_joints', 20)
        
        # Estado interno
        self.joint_positions = np.zeros(self.num_joints)
        self.joint_velocities = np.zeros(self.num_joints)
        self.cmd_vel = Twist()
        
        # Publishers
        self.pub_joint_command = rospy.Publisher(
            '/joint_command',
            Float32MultiArray,
            queue_size=10
        )
        
        self.pub_joint_state = rospy.Publisher(
            '/joint_states',
            JointState,
            queue_size=10
        )
        
        # Subscribers
        rospy.Subscriber('/cmd_vel', Twist, self.callback_cmd_vel)
        rospy.Subscriber('/joint_states_raw', JointState, 
                        self.callback_joint_states)
        
        # Timer para control loop
        self.timer = rospy.Timer(
            rospy.Duration(1.0 / self.rate_hz),
            self.control_loop
        )
        
        rospy.loginfo("Controlador humanoide inicializado")
    
    def callback_cmd_vel(self, msg):
        """Recibe comandos de velocidad para locomoción"""
        self.cmd_vel = msg
        rospy.logdebug(f"Cmd vel: linear={msg.linear.x}, angular={msg.angular.z}")
    
    def callback_joint_states(self, msg):
        """Recibe estado actual de articulaciones"""
        self.joint_positions = np.array(msg.position)
        self.joint_velocities = np.array(msg.velocity)
    
    def control_loop(self, event):
        """Loop principal de control ejecutado a frecuencia fija"""
        
        # 1. Generar patrón de marcha basado en cmd_vel
        joint_targets = self.generar_patron_marcha(
            self.cmd_vel.linear.x,
            self.cmd_vel.angular.z
        )
        
        # 2. Control PID de articulaciones
        joint_commands = self.control_pid(joint_targets)
        
        # 3. Publicar comandos
        msg_command = Float32MultiArray()
        msg_command.data = joint_commands.tolist()
        self.pub_joint_command.publish(msg_command)
        
        # 4. Publicar estado (para visualización)
        msg_state = JointState()
        msg_state.header.stamp = rospy.Time.now()
        msg_state.name = [f"joint_{i}" for i in range(self.num_joints)]
        msg_state.position = self.joint_positions.tolist()
        msg_state.velocity = self.joint_velocities.tolist()
        self.pub_joint_state.publish(msg_state)
    
    def generar_patron_marcha(self, vel_lineal, vel_angular):
        """
        Genera trayectorias de articulaciones para locomoción bípeda
        
        Args:
            vel_lineal: Velocidad deseada hacia adelante (m/s)
            vel_angular: Velocidad de rotación (rad/s)
        
        Returns:
            joint_targets: Array de posiciones objetivo [rad]
        """
        t = rospy.Time.now().to_sec()
        freq_marcha = 1.0  # Hz (pasos por segundo)
        
        # Fase de marcha (0 a 2π)
        fase = 2 * np.pi * freq_marcha * t
        
        # Amplitudes basadas en velocidad deseada
        amp_cadera = 0.3 * vel_lineal  # rad
        amp_rodilla = 0.5 * vel_lineal
        
        joint_targets = np.zeros(self.num_joints)
        
        # Pierna derecha (joints 0-5)
        joint_targets[0] = amp_cadera * np.sin(fase)           # Cadera flexión
        joint_targets[1] = amp_rodilla * max(0, np.sin(fase))  # Rodilla
        joint_targets[2] = -0.2 * amp_cadera * np.sin(fase)    # Tobillo
        
        # Pierna izquierda (joints 6-11) - fase opuesta
        joint_targets[6] = amp_cadera * np.sin(fase + np.pi)
        joint_targets[7] = amp_rodilla * max(0, np.sin(fase + np.pi))
        joint_targets[8] = -0.2 * amp_cadera * np.sin(fase + np.pi)
        
        # Brazos balanceo (joints 12-17) - compensar movimiento piernas
        joint_targets[12] = -0.5 * amp_cadera * np.sin(fase + np.pi)  # Brazo derecho
        joint_targets[13] = -0.5 * amp_cadera * np.sin(fase)          # Brazo izquierdo
        
        return joint_targets
    
    def control_pid(self, targets):
        """
        Control PID de articulaciones
        
        Args:
            targets: Posiciones objetivo [rad]
        
        Returns:
            commands: Torques de comando
        """
        # Parámetros PID (simplificados)
        Kp = 10.0
        Kd = 1.0
        
        error_pos = targets - self.joint_positions
        error_vel = -self.joint_velocities
        
        commands = Kp * error_pos + Kd * error_vel
        
        # Limitar torques
        max_torque = 5.0  # N·m
        commands = np.clip(commands, -max_torque, max_torque)
        
        return commands
    
    def run(self):
        """Mantiene el nodo vivo"""
        rospy.spin()

if __name__ == '__main__':
    try:
        controlador = ControladorRobotHumanoide()
        controlador.run()
    except rospy.ROSInterruptException:
        pass
```

### 1.2 Paradigmas de programación

#### 1.2.1 Programación orientada a objetos (POO)

**Principios SOLID**:
1. **Single Responsibility**: Cada clase una sola responsabilidad
2. **Open/Closed**: Abierto a extensión, cerrado a modificación
3. **Liskov Substitution**: Subclases sustituibles por superclases
4. **Interface Segregation**: Interfaces específicas, no generales
5. **Dependency Inversion**: Depender de abstracciones, no implementaciones

**Ejemplo: Jerarquía de sensores**:

```python
from abc import ABC, abstractmethod
import numpy as np

class Sensor(ABC):
    """Clase base abstracta para todos los sensores"""
    
    def __init__(self, nombre, frecuencia_hz=100):
        self.nombre = nombre
        self.frecuencia = frecuencia_hz
        self.ultima_lectura = None
        self.timestamp = 0
    
    @abstractmethod
    def leer(self):
        """Método abstracto: debe ser implementado por subclases"""
        pass
    
    def calibrar(self, muestras=100):
        """Calibración genérica usando múltiples muestras"""
        lecturas = []
        for _ in range(muestras):
            lecturas.append(self.leer())
        return np.mean(lecturas, axis=0)

class IMU(Sensor):
    """Unidad de Medición Inercial - acelerómetro + giroscopio"""
    
    def __init__(self, nombre="IMU", i2c_address=0x68):
        super().__init__(nombre, frecuencia_hz=200)
        self.address = i2c_address
        self.accel_offset = np.zeros(3)
        self.gyro_offset = np.zeros(3)
    
    def leer(self):
        """Lee aceleración y velocidad angular"""
        # Simulado: en realidad leería del hardware vía I2C
        accel = np.random.randn(3) * 0.1  # m/s²
        gyro = np.random.randn(3) * 0.05  # rad/s
        
        self.ultima_lectura = {
            'aceleracion': accel - self.accel_offset,
            'giroscopo': gyro - self.gyro_offset
        }
        
        return self.ultima_lectura
    
    def calibrar(self, muestras=100):
        """Calibra offsets en reposo"""
        print(f"Calibrando {self.nombre}... Mantener inmóvil")
        
        accel_muestras = []
        gyro_muestras = []
        
        for _ in range(muestras):
            lectura = self.leer()
            accel_muestras.append(lectura['aceleracion'])
            gyro_muestras.append(lectura['giroscopo'])
        
        self.accel_offset = np.mean(accel_muestras, axis=0)
        self.accel_offset[2] -= 9.81  # Compensar gravedad en Z
        self.gyro_offset = np.mean(gyro_muestras, axis=0)
        
        print(f"Calibración completada. Offsets: accel={self.accel_offset}, gyro={self.gyro_offset}")

class Ultrasonico(Sensor):
    """Sensor ultrasónico de distancia"""
    
    def __init__(self, nombre="US", pin_trigger=12, pin_echo=13):
        super().__init__(nombre, frecuencia_hz=20)
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        self.distancia_max = 4.0  # metros
    
    def leer(self):
        """Lee distancia en metros"""
        # Simulado: en realidad mediría tiempo de vuelo del pulso
        import random
        distancia = random.uniform(0.1, self.distancia_max)
        
        self.ultima_lectura = {'distancia': distancia}
        return self.ultima_lectura

class FusionSensorial:
    """Fusiona datos de múltiples sensores"""
    
    def __init__(self):
        self.sensores = []
    
    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)
    
    def leer_todos(self):
        """Lee todos los sensores y retorna diccionario unificado"""
        datos = {}
        for sensor in self.sensores:
            lectura = sensor.leer()
            datos[sensor.nombre] = lectura
        return datos
    
    def calibrar_todos(self):
        """Calibra todos los sensores"""
        for sensor in self.sensores:
            sensor.calibrar()

# Uso
sistema = FusionSensorial()
sistema.agregar_sensor(IMU("IMU_Torso"))
sistema.agregar_sensor(Ultrasonico("US_Frontal"))

# Calibrar
sistema.calibrar_todos()

# Leer
datos = sistema.leer_todos()
print(datos)
```

#### 1.2.2 Programación reactiva y event-driven

Para sistemas robóticos con múltiples fuentes de eventos asíncronos.

```python
import asyncio
from typing import Callable, Any

class EventBus:
    """Bus de eventos para comunicación entre módulos"""
    
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_type: str, callback: Callable):
        """Suscribe callback a tipo de evento"""
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
    
    async def publish(self, event_type: str, data: Any):
        """Publica evento a todos los suscriptores"""
        if event_type in self.subscribers:
            tasks = [callback(data) for callback in self.subscribers[event_type]]
            await asyncio.gather(*tasks)

# Ejemplo de uso
async def on_obstacle_detected(data):
    print(f"Obstáculo detectado a {data['distance']:.2f}m - Deteniendo")
    # Aquí iría código para detener motores

async def on_battery_low(data):
    print(f"Batería baja: {data['percentage']}% - Regresando a base")
    # Aquí iría código para navegación a estación de carga

bus = EventBus()
bus.subscribe('obstacle_detected', on_obstacle_detected)
bus.subscribe('battery_low', on_battery_low)

# Simularsensores publicando eventos
async def sensor_loop():
    while True:
        await asyncio.sleep(1)
        # Simular detección de obstáculo
        await bus.publish('obstacle_detected', {'distance': 0.3})

async Main():
    await sensor_loop()

# asyncio.run(main())
```

## 2. Teoría de control

### 2.1 Control PID

El controlador PID es el algoritmo de control más utilizado en la industria.

**Ecuación continua**:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

**Forma discreta** (para microcontroladores):
$$u[k] = K_p e[k] + K_i \sum_{i=0}^k e[i]\Delta t + K_d \frac{e[k]-e[k-1]}{\Delta t}$$

Donde:
- $e(t) = r(t) - y(t)$ es el error (referencia - medición)
- $K_p$ = Ganancia proporcional
- $K_i$ = Ganancia integral
- $K_d$ = Ganancia derivativa

**Implementación en C++ con anti-windup**:

```cpp
class PIDController {
private:
    float Kp, Ki, Kd;
    float integral;
    float prev_error;
    float output_min, output_max;
    float dt;  // Tiempo de muestreo
    
public:
    PIDController(float kp, float ki, float kd, float sample_time,
                 float out_min = -255, float out_max = 255)
        : Kp(kp), Ki(ki), Kd(kd), dt(sample_time),
          output_min(out_min), output_max(out_max),
          integral(0), prev_error(0) {}
    
    float compute(float setpoint, float measured_value) {
        // Calcular error
        float error = setpoint - measured_value;
        
        // Término proporcional
        float P = Kp * error;
        
        // Término integral con anti-windup
        integral += error * dt;
        // Limitar integral para prevenir windup
        float max_integral = (output_max - output_min) / Ki;
        integral = constrain(integral, -max_integral, max_integral);
        float I = Ki * integral;
        
        // Término derivativo (con filtro para reducir ruido)
        float derivative = (error - prev_error) / dt;
        float D = Kd * derivative;
        
        // Salida total
        float output = P + I + D;
        
        // Saturar salida
        output = constrain(output, output_min, output_max);
        
        // Anti-windup: si salida saturada, no acumular integral
        if (output >= output_max || output <= output_min) {
            integral -= error * dt;  // Revertir acumulación
        }
        
        // Actualizar para próxima iteración
        prev_error = error;
        
        return output;
    }
    
    void reset() {
        integral = 0;
        prev_error = 0;
    }
    
    void setGains(float kp, float ki, float kd) {
        Kp = kp;
        Ki = ki;
        Kd = kd;
    }
};

// Ejemplo de uso: Control de posición de motor
PIDController positionPID(2.0, 0.5, 0.1, 0.01);  // Kp, Ki,Kd, dt=10ms

void loop() {
    float target_position = 1000;  // Pulsos de encoder
    float current_position = readEncoder();
    
    float control_output = positionPID.compute(target_position, current_position);
    
    setMotorPWM(control_output);
    
    delay(10);  // 100 Hz control loop
}
```

**Sintonización PID - Método de Ziegler-Nichols**:

1. Establecer Ki=0, Kd=0
2. Incrementar Kp hasta que el sistema oscile con amplitud constante (Kp crítico = Ku)
3. Medir período de oscilación Tu
4. Calcular ganancias:
   - $K_p = 0.6 K_u$
   - $K_i = \frac{2K_p}{T_u}$
   - $K_d = \frac{K_p T_u}{8}$

```python
def ziegler_nichols(Ku, Tu):
    """
    Calcula ganancias PID usando método Ziegler-Nichols
    
    Args:
        Ku: Ganancia proporcional crítica (cuando sistema oscila)
        Tu: Período de oscilación (segundos)
    
    Returns:
        (Kp, Ki, Kd)
    """
    Kp = 0.6 * Ku
    Ki = 2 * Kp / Tu
    Kd = Kp * Tu / 8
    
    return Kp, Ki, Kd

# Ejemplo
Ku_critico = 5.0
Tu_oscilacion = 0.5  # segundos
Kp, Ki, Kd = ziegler_nichols(Ku_critico, Tu_oscilacion)
print(f"Ganancias PID: Kp={Kp:.2f}, Ki={Ki:.2f}, Kd={Kd:.2f}")
```

### 2.2 Control en espacio de estados

Representación moderna de sistemas dinámicos:

$$\dot{x} = Ax + Bu$$
$$y = Cx + Du$$

Donde:
- $x$ = Vector de estado
- $u$ = Vector de entrada (control)
- $y$ = Vector de salida
- $A, B, C, D$ = Matrices del sistema

**Ejemplo: Péndulo invertido**:

```python
import numpy as np
import control as ct
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class PenduloInvertido:
    """
    Modelo de péndulo invertido sobre carro
    Estado: x = [posición_carro, velocidad_carro, ángulo_péndulo, velocidad_angular]
    """
    
    def __init__(self, M=1.0, m=0.1, L=0.5, g=9.81, b=0.1):
        """
        Args:
            M: Masa del carro (kg)
            m: Masa del péndulo (kg)
            L: Longitud del péndulo (m)
            g: Gravedad (m/s²)
            b: Coeficiente de fricción
        """
        self.M = M
        self.m = m
        self.L = L
        self.g = g
        self.b = b
        
        # Linealización alrededor de punto de equilibrio θ=0
        self.A, self.B, self.C, self.D = self._linearizar()
    
    def _linearizar(self):
        """Linealiza sistema alrededor del equilibrio vertical"""
        M, m, L, g, b = self.M, self.m, self.L, self.g, self.b
        
        p = M + m
        
        A = np.array([
            [0, 1, 0, 0],
            [0, -b/p, m*g/p, 0],
            [0, 0, 0, 1],
            [0, -b/(L*p), (M+m)*g/(L*p), 0]
        ])
        
        B = np.array([
            [0],
            [1/p],
            [0],
            [1/(L*p)]
        ])
        
        C = np.array([[1, 0, 0, 0],    # Posición del carro
                      [0, 0, 1, 0]])   # Ángulo del péndulo
        
        D = np.zeros((2, 1))
        
        return A, B, C, D
    
    def diseñar_lqr(self, Q, R):
        """
        Diseña controlador LQR (Linear Quadratic Regulator)
        Minimiza: J = ∫(x'Qx + u'Ru)dt
        
        Args:
            Q: Matriz de pesos de estados (4×4)
            R: Matriz de pesos de control (1×1)
        
        Returns:
            K: Ganancias de retroalimentación de estado
        """
        # Resolver ecuación algebraica de Riccati
        sys = ct.ss(self.A, self.B, self.C, self.D)
        K, S, E = ct.lqr(sys, Q, R)
        
        return K
    
    def simular(self, x0, K, t_final=10, dt=0.01):
        """
        Simula sistema con controlador LQR
        
        Args:
            x0: Estado inicial [x, ẋ, θ, θ̇]
            K: Ganancias LQR
            t_final: Tiempo de simulación
            dt: Paso de tiempo
        
        Returns:
            t, x, u: Tiempo, estados, controles
        """
        t = np.arange(0, t_final, dt)
        n_steps = len(t)
        
        x = np.zeros((n_steps, 4))
        u = np.zeros(n_steps)
        x[0] = x0
        
        for i in range(n_steps - 1):
            # Control: u = -Kx (retroalimentación de estado)
            u[i] = -K @ x[i]
            
            # Dinámica: ẋ = Ax + Bu
            x_dot = self.A @ x[i] + self.B.flatten() * u[i]
            x[i+1] = x[i] + x_dot * dt
        
        return t, x, u

# Ejemplo de uso
pendulo = PenduloInvertido()

# Pesos para LQR (ajustar según prioridades)
Q = np.diag([10, 1, 100, 1])  # Priorizar posición carro y ángulo péndulo
R = np.array([[0.1]])  # Penalizar esfuerzo de control

# Diseñar controlador
K = pendulo.diseñar_lqr(Q, R)
print(f"Ganancias LQR: K = {K}")

# Simular desde condición inicial desbalanceada
x0 = np.array([0, 0, 0.2, 0])  # θ₀ = 0.2 rad (~11°)
t, x, u = pendulo.simular(x0, K, t_final=5)

# Visualizar
fig, axes = plt.subplots(3, 1, figsize=(10, 8))
axes[0].plot(t, x[:, 0])
axes[0].set_ylabel('Posición carro (m)')
axes[0].grid(True)

axes[1].plot(t, np.degrees(x[:, 2]))
axes[1].set_ylabel('Ángulo péndulo (°)')
axes[1].axhline(0, color='r', linestyle='--', alpha=0.3)
axes[1].grid(True)

axes[2].plot(t, u)
axes[2].set_ylabel('Fuerza control (N)')
axes[2].set_xlabel('Tiempo (s)')
axes[2].grid(True)

plt.tight_layout()
plt.savefig('lqr_pendulo.png')
print("Gráfica guardada como 'lqr_pendulo.png'")
```

### 2.3 Control predictivo por modelo (MPC)

Control avanzado que considera restricciones y optimiza trayectoria futura.

**Concepto**: En cada paso:
1. Predice comportamiento futuro del sistema (horizonte N)
2. Optimiza secuencia de controles minimizando función de costo
3. Aplica solo el primer control
4. Repite (receding horizon)

**Implementación simplificada**:

```python
from scipy.optimize import minimize
import numpy as np

class MPCController:
    """Model Predictive Controller simplificado"""
    
    def __init__(self, A, B, Q, R, horizon=10):
        """
        Args:
            A, B: Matrices del sistema discreto
            Q: Peso de estados en función de costo
            R: Peso de control en función de costo
            horizon: Horizonte de predicción (pasos)
        """
        self.A = A
        self.B = B
        self.Q = Q
        self.R = R
        self.N = horizon
        
        self.n_states = A.shape[0]
        self.n_inputs = B.shape[1]
    
    def costo(self, U, x0, x_ref):
        """
        Función de costo a minimizar
        J = Σ(||x-x_ref||²_Q + ||u||²_R)
        
        Args:
            U: Secuencia de controles [u₀, u₁, ..., u_{N-1}]
            x0: Estado inicial
            x_ref: Trayectoria de referencia
        
        Returns:
            costo: Valor escalar del costo
        """
        U = U.reshape((self.N, self.n_inputs))
        x = x0.copy()
        J = 0
        
        for k in range(self.N):
            # Costo de estado
            error_x = x - x_ref[k]
            J += error_x.T @ self.Q @ error_x
            
            # Costo de control
            u = U[k]
            J += u.T @ self.R @ u
            
            # Predecir siguiente estado
            x = self.A @ x + self.B @ u
        
        return J
    
    def compute(self, x_current, x_ref, u_min=-np.inf, u_max=np.inf):
        """
        Calcula control óptimo
        
        Args:
            x_current: Estado actual
            x_ref: Trayectoria de referencia [N × n_states]
            u_min, u_max: Límites de control
        
        Returns:
            u_optimal: Primer control de la secuencia óptima
        """
        # Condición inicial para optimización
        U0 = np.zeros(self.N * self.n_inputs)
        
        # Restricciones de acerca
        bounds = [(u_min, u_max)] * (self.N * self.n_inputs)
        
        # Optimizar
        result = minimize(
            fun=lambda U: self.costo(U, x_current, x_ref),
            x0=U0,
            method='SLSQP',
            bounds=bounds
        )
        
        # Extraer primer control
        U_opt = result.x.reshape((self.N, self.n_inputs))
        u_optimal = U_opt[0]
        
        return u_optimal

# Ejemplo: MPC para seguimiento de trayectoria
# Sistema: ẋ = Ax + Bu (masa-resorte-amortiguador)
A = np.array([[0, 1], [-2, -0.5]])
B = np.array([[0], [1]])

# Discretizar (usando aproximación Euler con dt=0.1)
dt = 0.1
A_d = np.eye(2) + A * dt
B_d = B * dt

# Crear controlador MPC
Q = np.diag([10, 1])  # Penalizar posición más que velocidad
R = np.array([[0.1]])
mpc = MPCController(A_d, B_d, Q, R, horizon=20)

# Trayectoria de referencia (senoidal)
N_total = 200
t = np.arange(N_total) * dt
x_ref_traj = np.column_stack([
    np.sin(t),        # Posición
    np.cos(t)         # Velocidad
])

# Simulación con MPC
x = np.array([0, 0])  # Estado inicial
x_history = [x.copy()]
u_history = []

for k in range(N_total - 20):
    # Obtener ventana de referencia futura
    x_ref_window = x_ref_traj[k:k+20]
    
    # Calcular control
    u = mpc.compute(x, x_ref_window, u_min=-5, u_max=5)
    u_history.append(u[0])
    
    # Aplicar control y simular
    x = A_d @ x + B_d.flatten() * u
    x_history.append(x.copy())

x_history = np.array(x_history)
u_history = np.array(u_history)

# Visualizar
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t[:len(x_history)], x_history[:, 0], label='Posición real')
plt.plot(t[:len(x_history)], x_ref_traj[:len(x_history), 0], 
         '--', label='Referencia')
plt.ylabel('Posición')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t[:len(u_history)], u_history)
plt.ylabel('Control u')
plt.xlabel('Tiempo (s)')
plt.grid(True)

plt.tight_layout()
plt.savefig('mpc_tracking.png')
print("Gráfica MPC guardada")
```

## 3. Diseño ergonómico y biomecánica

### 3.1 Biomecánica del movimiento humano

**Objetivos**:
- Replicar movimientos naturales
- Evitar configuraciones singulares
- Optimizar eficiencia energética

**Análisis de marcha humana**:

```python
import numpy as np
import matplotlib.pyplot as plt

class GaitGenerator:
    """Generador de patrones de marcha bípeda"""
    
    def __init__(self, step_length=0.4, step_height=0.05, step_duration=0.8):
        """
        Args:
            step_length: Longitud de paso (m)
            step_height: Altura máxima del pie (m)
            step_duration: Duración de un paso completo (s)
        """
        self.L_step = step_length
        self.H_step = step_height
        self.T_step = step_duration
    
    def trajectory_swing_foot(self, t_norm):
        """
        Trayectoria del pie durante fase de balanceo (swing phase)
        
        Args:
            t_norm: Tiempo normalizado [0, 1] dentro del paso
        
        Returns:
            (x, z): Posición del pie respecto al centro de masa
        """
        # Trayectoria horizontal (lineal)
        x = self.L_step * t_norm
        
        # Trayectoria vertical (parábola)
        z = 4 * self.H_step * t_norm * (1 - t_norm)
        
        return x, z
    
    def joint_angles_leg(self, x_foot, z_foot, L_thigh=0.4, L_shank=0.4):
        """
        Cinemática inversa para ángulos de cadera, rodilla, tobillo
        
        Args:
            x_foot, z_foot: Posición del pie
            L_thigh: Longitud del muslo (m)
            L_shank: Longitud de la pierna (m)
        
        Returns:
            (theta_hip, theta_knee, theta_ankle): Ángulos articulares (rad)
        """
        # Distancia del pivote de cadera al pie
        r = np.sqrt(x_foot**2 + z_foot**2)
        
        # Ley de cosenos para ángulo de rodilla
        cos_knee = (L_thigh**2 + L_shank**2 - r**2) / (2 * L_thigh * L_shank)
        cos_knee = np.clip(cos_knee, -1, 1)  # Evitar errores numéricos
        theta_knee = np.arccos(cos_knee)
        
        # Geometría para ángulo de cadera
        alpha = np.arctan2(z_foot, x_foot)
        beta = np.arcsin(L_shank * np.sin(theta_knee) / r)
        theta_hip = alpha + beta
        
        # Tobillo (mantener pie horizontal)
        theta_ankle = -(theta_hip + theta_knee - np.pi)
        
        return theta_hip, theta_knee, theta_ankle
    
    def generate_full_gait_cycle(self, velocity=0.5, n_samples=100):
        """
        Genera ciclo completo de marcha para ambas piernas
        
        Args:
            velocity: Velocidad de marcha (m/s)
            n_samples: Número de muestras en el ciclo
        
        Returns:
            t, angles_right, angles_left: Tiempos y ángulos articulares
        """
        # Ajustar parámetros según velocidad
        self.L_step = velocity * self.T_step
        
        t = np.linspace(0, self.T_step, n_samples)
        angles_right = np.zeros((n_samples, 3))  # [cadera, rodilla, tobillo]
        angles_left = np.zeros((n_samples, 3))
        
        for i, time in enumerate(t):
            phase = time / self.T_step  # [0, 1]
            
            # Pierna derecha (0-0.5: swing, 0.5-1.0: stance)
            if phase < 0.5:
                # Fase de balanceo
                x, z = self.trajectory_swing_foot(phase * 2)
                x -= self.L_step / 2  # Centrar
            else:
                # Fase de apoyo (pie en el suelo moviéndose atrás)
                x = self.L_step / 2 - self.L_step * (phase - 0.5) * 2
                z = 0
            
            angles_right[i] = self.joint_angles_leg(x, -z)
            
            # Pierna izquierda (fase opuesta, +180°)
            phase_left = (phase + 0.5) % 1.0
            if phase_left < 0.5:
                x_l, z_l = self.trajectory_swing_foot(phase_left * 2)
                x_l -= self.L_step / 2
            else:
                x_l = self.L_step / 2 - self.L_step * (phase_left - 0.5) * 2
                z_l = 0
            
            angles_left[i] = self.joint_angles_leg(x_l, -z_l)
        
        return t, angles_right, angles_left
    
    def visualize(self):
        """Visualiza ciclo de marcha"""
        t, angles_r, angles_l = self.generate_full_gait_cycle()
        
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        
        labels = ['Cadera', 'Rodilla', 'Tobillo']
        for i in range(3):
            axes[i].plot(t, np.degrees(angles_r[:, i]), 'b-', label='Pierna Derecha')
            axes[i].plot(t, np.degrees(angles_l[:, i]), 'r--', label='Pierna Izquierda')
            axes[i].set_ylabel(f'{labels[i]} (°)')
            axes[i].grid(True, alpha=0.3)
            axes[i].legend()
        
        axes[2].set_xlabel('Tiempo (s)')
        plt.suptitle('Ángulos Articulares durante Ciclo de Marcha')
        plt.tight_layout()
        plt.savefig('gait_pattern.png')
        print("Patrón de marcha guardado como 'gait_pattern.png'")

# Ejemplo de uso
gait = GaitGenerator(step_length=0.5, step_height=0.05, step_duration=0.8)
gait.visualize()
```

### 3.2 Centro de masa y estabilidad

**Zero Moment Point (ZMP)**:
Criterio fundamental para estabilidad en locomoción bípeda.

```python
def calcular_zmp(fuerzas_pies, posiciones_pies):
    """
    Calcula Zero Moment Point (ZMP)
    
    Args:
        fuerzas_pies: [(Fx_L, Fy_L, Fz_L), (Fx_R, Fy_R, Fz_R)]
        posiciones_pies: [(x_L, y_L), (x_R, y_R)]
    
    Returns:
        (x_zmp, y_zmp): Posición del ZMP
    """
    # Descomponer fuerzas y posiciones
    F_L = np.array(fuerzas_pies[0])
    F_R = np.array(fuerzas_pies[1])
    pos_L = np.array(posiciones_pies[0])
    pos_R = np.array(posiciones_pies[1])
    
    # Fuerza total vertical
    Fz_total = F_L[2] + F_R[2]
    
    if Fz_total < 0.1:  # Evitar división por cero
        return None
    
    # ZMP es el promedio ponderado de las posiciones de los pies
    x_zmp = (F_L[2] * pos_L[0] + F_R[2] * pos_R[0]) / Fz_total
    y_zmp = (F_L[2] * pos_L[1] + F_R[2] * pos_R[1]) / Fz_total
    
    return x_zmp, y_zmp

def estabilidad_estatica(zmp, poligono_soporte):
    """
    Verifica si el robot es estáticamente estable
    
    Args:
        zmp: (x, y) posición del ZMP
        poligono_soporte: Lista de vértices del polígono formado por pies
    
    Returns:
        estable: Boolean
    """
    from matplotlib.path import Path
    
    path = Path(poligono_soporte)
    return path.contains_point(zmp)

# Ejemplo
fuerzas = [(0, 0, 200), (0, 0, 150)]  # Izq, Der en Newtons
posiciones = [(0.0, 0.1), (0.0, -0.1)]  # Izq, Der en metros

zmp = calcular_zmp(fuerzas, posiciones)
print(f"ZMP en: {zmp}")

# Polígono de soporte (rectángulo entre pies)
poligono = [(-0.1, -0.15), (0.1, -0.15), (0.1, 0.15), (-0.1, 0.15)]
print(f"Estable: {estabilidad_estatica(zmp, poligono)}")
```

## 4. Interfaz de usuario y comportamiento

### 4.1 Máquinas de estados finitos (FSM)

Para gestionar comportamientos complejos del robot.

```python
from enum import Enum, auto

class EstadoRobot(Enum):
    """Estados posibles del robot humanoide"""
    IDLE = auto()
    CAMINANDO = auto()
    AGACHADO = auto()
    LEVANTANDOSE = auto()
    CAYENDO = auto()
    EMERGENCIA = auto()

class MaquinaEstadosRobot:
    """FSM para control de comportamiento del robot"""
    
    def __init__(self):
        self.estado_actual = EstadoRobot.IDLE
        self.historial = [self.estado_actual]
        
        # Transiciones válidas
        self.transiciones = {
            EstadoRobot.IDLE: [EstadoRobot.CAMINANDO, EstadoRobot.AGACHADO, EstadoRobot.EMERGENCIA],
            EstadoRobot.CAMINANDO: [EstadoRobot.IDLE, EstadoRobot.CAYENDO, EstadoRobot.EMERGENCIA],
            EstadoRobot.AGACHADO: [EstadoRobot.LEVANTANDOSE, EstadoRobot.EMERGENCIA],
            EstadoRobot.LEVANTANDOSE: [EstadoRobot.IDLE, EstadoRobot.EMERGENCIA],
            EstadoRobot.CAYENDO: [EstadoRobot.IDLE, EstadoRobot.EMERGENCIA],
            EstadoRobot.EMERGENCIA: [EstadoRobot.IDLE]  # Solo salida manual
        }
    
    def transicion(self, nuevo_estado):
        """Intenta transición a nuevo estado"""
        if nuevo_estado in self.transiciones[self.estado_actual]:
            print(f"Transición: {self.estado_actual.name} → {nuevo_estado.name}")
            self.estado_actual = nuevo_estado
            self.historial.append(nuevo_estado)
            
            # Ejecutar acciones asociadas al nuevo estado
            self._on_enter_state(nuevo_estado)
            return True
        else:
            print(f"Transición inválida: {self.estado_actual.name} → {nuevo_estado.name}")
            return False
    
    def _on_enter_state(self, estado):
        """Acciones al entrar a cada estado"""
        if estado == EstadoRobot.IDLE:
            print("  → Modo reposo: Servos relajados")
        elif estado == EstadoRobot.CAMINANDO:
            print("  → Iniciando locomoción")
        elif estado == EstadoRobot.EMERGENCIA:
            print("  → STOP! Deteniendo todos los actuadores")

# Ejemplo
fsm = MaquinaEstadosRobot()
fsm.transicion(EstadoRobot.CAMINANDO)
fsm.transicion(EstadoRobot.IDLE)
fsm.transicion(EstadoRobot.AGACHADO)
fsm.transicion(EstadoRobot.LEVANTANDOSE)
```

## 5. Simulación y testing

### 5.1 Test unitarios para código de control

```python
import unittest
import numpy as np

class TestCinematicaDirecta(unittest.TestCase):
    """Tests para cinemática directa del brazo"""
    
    def setUp(self):
        """Ejecutado antes de cada test"""
        self.brazo = BrazoRobotico(longitudes=[0.15, 0.20, 0.15])
    
    def test_posicion_extendida(self):
        """Test: brazo completamente extendido"""
        self.brazo.theta = np.array([0, 0, 0])
        pos = self.brazo.cinematica_directa()
        
        # Debe estar en (L1+L2+L3, 0)
        esperado = np.array([0.5, 0])
        np.testing.assert_array_almost_equal(pos, esperado, decimal=3)
    
    def test_configuracion_L(self):
        """Test: brazo en forma de L"""
        self.brazo.theta = np.array([0, np.pi/2, 0])
        pos = self.brazo.cinematica_directa()
        
        # Debe estar en (L1, L2+L3)
        esperado = np.array([0.15, 0.35])
        np.testing.assert_array_almost_equal(pos, esperado, decimal=3)
    
    def test_alcance_maximo(self):
        """Test: Verificar que nunca exceda alcance máximo"""
        for _ in range(100):
            # Configuraciones aleatorias
            theta_random = np.random.uniform(-np.pi, np.pi, 3)
            self.brazo.theta = theta_random
            pos = self.brazo.cinematica_directa()
            distancia = np.linalg.norm(pos)
            
            self.assertLessEqual(distancia, 0.51,  # 0.5 + tolerancia
                               "Posición excede alcance máximo")

# Ejecutar tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

## Referencias

- **Libros**:
  - "Modern Robotics" - Kevin Lynch & Frank Park
  - "Probabilistic Robotics" - Sebastian Thrun
  - "Humanoid Robotics: A Reference" - Ambarish Goswami & Prahlad Vadakkepat

- **Cursos Online**:
  - "Robot Mechanics and Control" - Seoul National University (Coursera)
  - ROS Tutorials - ros.org

- **Software**:
  - ROS/ROS2: Framework estándar
  - Gazebo/PyBullet: Simulación
  - MATLAB Robotics Toolbox

---

## Conclusión

El dominio de programación y control es esencial para transformar el hardware del robot humanoide en un sistema autónomo funcional. La combinación de algoritmos de control clásicos (PID), modernos (LQR, MPC), generación de trayectorias y arquitecturas de software robustas permite crear robots humanoides capaces de interactuar de manera segura y eficiente con entornos dinámicos.

**Próximo módulo**: [Aprendizaje automático](../05_Aprendizaje_IA/) para dotar al robot de capacidades de percepción y adaptación inteligentes.
