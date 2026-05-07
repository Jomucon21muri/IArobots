# Integración de hardware - robot humanoide

## Propósito

Esta carpeta documenta todos los aspectos de hardware del robot humanoide, incluyendo diseño mecánico, electrónica, materiales, energía y mecatrónica. Es el núcleo físico del proyecto.

## Áreas de conocimiento cubiertas

Este módulo integra los siguientes pilares de conocimiento (ver [recursos_conocimientos.md](../01_Proyecto/recursos_conocimientos.md)):

1. **Mecánica y Diseño Mecánico**: Estructura, articulaciones, CAD
2. **Electrónica y Electricidad**: Circuitos, sensores, actuadores
3. **Mecatrónica**: Integración mecánica-electrónica
4. **Materiales y Fabricación**: Selección de materiales, impresión 3D, mecanizado
5. **Baterías y Energía**: Gestión de energía, autonomía

## Estructura del directorio

```
06_Integracion_Hardware/
├── README.md (este archivo)
├── mecanica/
│   ├── disenos_cad/        # Modelos 3D (SolidWorks, Fusion 360)
│   ├── articulaciones/     # Diseño de articulaciones específicas
│   ├── estructura/         # Chasis y estructura principal
│   └── materiales.md       # Especificaciones de materiales
├── electronica/
│   ├── esquemas/           # Esquemas de circuitos (KiCad, Fritzing)
│   ├── pcb/                # Diseños de PCB personalizados
│   ├── bom/                # Bill of Materials
│   └── datasheets/         # Hojas de datos de componentes
├── drivers/
│   ├── motores/            # Control de servos y motores DC
│   ├── sensores/           # Drivers de IMU, encoders, etc.
│   └── comunicacion/       # UART, SPI, I2C, CAN
├── wiring/
│   ├── diagramas/          # Diagramas de cableado completo
│   ├── power_distribution/ # Distribución de energía
│   └── guias_montaje/      # Guías paso a paso
├── firmware/
│   ├── arduino/            # Firmware para Arduino
│   ├── stm32/              # Firmware para STM32
│   └── esp32/              # Firmware para ESP32 (WiFi/BT)
├── energia/
│   ├── baterias/           # Especificaciones y gestión de baterías
│   ├── reguladores/        # Circuitos de regulación de voltaje
│   └── monitoreo/          # Sistema de monitoreo de energía
├── fabricacion/
│   ├── impresion_3d/       # Archivos STL, perfiles de impresión
│   ├── mecanizado/         # G-code para CNC
│   └── ensamblaje/         # Procedimientos de ensamblaje
└── safety/
    ├── checklists/         # Listas de verificación
    ├── protocolos/         # Protocolos de seguridad
    └── emergency_procedures/ # Procedimientos de emergencia
```

## Componentes principales del robot humanoide

### Sistema mecánico

**Grados de Libertad (DOF)**:
- Cabeza: 2-3 DOF (pan, tilt, roll opcional)
- Cada brazo: 6-7 DOF (hombro 3, codo 1, muñeca 2-3)
- Torso: 1-3 DOF (flexión, rotación)
- Cada pierna: 6 DOF (cadera 3, rodilla 1, tobillo 2)
- **Total**: ~25-30 DOF

**Materiales**:
- Estructura: Aluminio 6061-T6, fibra de carbono
- Articulaciones: Rodamientos de bolas, bujes de bronce
- Carcasas: PLA, ABS, PETG (impresión 3D)
- Partes móviles: Nylon, TPU (flexible)

### Sistema electrónico

**Cerebro**:
- **Principal**: Raspberry Pi 4 (8GB) o Nvidia Jetson Nano
- **Co-procesador**: Arduino Mega 2560 / STM32
- **Comunicación**: ESP32 (WiFi/Bluetooth)

**Actuadores**:
- Servomotores digitales (20-30 unidades)
  - Torque: 10-25 kg·cm
  - Protocolo: PWM, UART (Dynamixel)
- Motores DC brushless (opcional para ruedas/movilidad)

**Sensores**:
- **IMU**: MPU6050 / BNO055 (orientación, aceleración)
- **Cámaras**: Raspberry Pi Camera v2 o webcam USB (estéreo opcional)
- **Ultrasonido**: HC-SR04 (detección obstáculos)
- **Encoders**: En articulaciones críticas
- **Sensores de fuerza**: FSR en pies, manos
- **Micrófonos**: Para reconocimiento de voz
- **Altavoces**: Para síntesis de voz

**Alimentación**:
- Batería LiPo 3S (11.1V) 5000mAh 20C
- BMS (Battery Management System)
- Reguladores Buck:
  - 5V @ 3A (Raspberry Pi, sensores)
  - 6V @ 10A (Servomotores)
- Sistema de monitoreo (INA219)

### Conectividad

**Protocolos Internos**:
- I2C: Sensores (IMU, display)
- SPI: Alta velocidad (si necesario)
- UART: Servos avanzados (Dynamixel)
- PWM: Servos estándar

**Protocolos Externos**:
- WiFi: Control remoto, telemetría
- Bluetooth: Periféricos, gamepad
- Ethernet: Opcional para conexión estable

## Guías de construcción

### Fase 1: diseño (meses 3-4)

1. **Diseño CAD**:
   - Crear modelo completo en SolidWorks/Fusion 360
   - Validar interferencias y rangos de movimiento
   - Generar planos de fabricación

2. **Diseño Eléctrico**:
   - Esquema completo del sistema
   - Cálculo de consumo energético
   - Selección de componentes

3. **Simulación**:
   - Análisis de elementos finitos (FEA) en partes críticas
   - Simulación cinemática en Gazebo/PyBullet

### Fase 2: fabricación (meses 5-6)

1. **Impresión 3D**:
   - Configuración óptima por material
   - Orientación para máxima resistencia
   - Post-procesamiento (lijado, acetona para ABS)

2. **Mecanizado** (si aplica):
   - Piezas metálicas en CNC
   - Tolerancias ajustadas

3. **Ensamblaje Mecánico**:
   - Seguir guía de ensamblaje
   - Verificar alineación de articulaciones
   - Instalación de rodamientos

### Fase 3: electrónica (mes 6)

1. **Montaje de Componentes**:
   - Soldar PCB si hay diseños personalizados
   - Montar microcontroladores y sensores
   - Instalar actuadores

2. **Cableado**:
   - Seguir diagrama de cableado
   - Cable management limpio
   - Etiquetado claro

3. **Pruebas Iniciales**:
   - Verificar continuidad
   - Test de alimentación (sin motores)
   - Verificar comunicación de sensores

### Fase 4: integración (mes 6)

1. **Prueba de Motores**:
   - Un motor a la vez
   - Verificar dirección y rango
   - Calibración

2. **Prueba de Sensores**:
   - Lectura de cada sensor
   - Calibración (especialmente IMU)
   - Fusión sensorial básica

3. **Sistema Completo**:
   - Integración gradual
   - Pruebas de estrés
   - Validación de seguridad

## Checklist de seguridad pre-prueba

**ADVERTENCIA: OBLIGATORIO antes de cada sesión de pruebas**:

- [ ] **Batería**: Verificar voltaje, conexiones seguras
- [ ] **E-stop**: Botón de parada de emergencia accesible y funcional
- [ ] **Cableado**: Sin cables sueltos o pelados
- [ ] **Estructura**: Sin grietas o piezas flojas
- [ ] **Software**: Emergency stop implementado en código
- [ ] **Área**: Espacio despejado, sin personas cerca
- [ ] **Supervisión**: Nunca dejar operando sin supervisión
- [ ] **Logs**: Sistema de logging activado
- [ ] **Límites**: Rangos de movimiento configurados y probados
- [ ] **Comunicación**: Canal de comunicación confiable (no intermitente)

## Especificaciones técnicas objetivo

| Parámetro | Valor Objetivo |
|-----------|----------------|
| Altura | 150-180 cm |
| Peso | 8-15 kg |
| DOF Total | 25-30 |
| Autonomía | 2-4 horas (uso moderado) |
| Velocidad marcha | 0.5-1.5 km/h |
| Carga útil (brazos) | 0.5-2 kg por brazo |
| Tiempo respuesta | <100 ms |
| Comunicación | WiFi 2.4/5GHz, BT 5.0 |

---

## Sistema de energía (metabolismo artificial)

El sistema de energía del robot humanoide simula el metabolismo biológico, gestionando la obtención, almacenamiento, distribución y optimización de energía para todas sus funciones.

### 1. Generación y almacenamiento de energía

#### Qué se simula
- Cómo el robot obtiene y gestiona su energía (equivalente a la alimentación en humanos)
- Balance entre capacidad de batería y consumo de sistemas
- Autonomía operacional

#### Hardware implementado

**Baterías principales**:
- **Tipo**: LiPo 3S (11.1V nominal, 12.6V cargada)
- **Capacidad**: 5000-8000 mAh
- **Tasa de descarga**: 20C-30C
- **Ubicación**: Centro de masa del torso (estabilidad)

**Alternativas y mejoras**:
```
┌─────────────────────────────────────────────────────┐
│  Tipo de batería  │ Ventajas          │ Desventajas │
├───────────────────┼───────────────────┼─────────────┤
│ LiPo              │ Alta densidad     │ Peligrosa   │
│ Li-Ion 18650      │ Más segura        │ Menos C     │
│ LiFePO4           │ Muy segura        │ Más pesada  │
│ Supercapacitores  │ Carga ultrarrápida│ Baja cap.   │
└─────────────────────────────────────────────────────┘
```

#### Software de gestión

**Battery Management System (BMS) personalizado**:
```python
import time

class BatteryManagementSystem:
    def __init__(self, cells=3, capacity_mah=5000):
        self.cells = cells
        self.capacity = capacity_mah
        self.voltage_min = 3.3  # Por celda
        self.voltage_max = 4.2  # Por celda
        self.current_voltage = [4.1, 4.1, 4.1]  # Voltaje inicial
        self.consumption_log = []
        
    def get_total_voltage(self):
        return sum(self.current_voltage)
    
    def get_charge_percentage(self):
        avg_voltage = sum(self.current_voltage) / self.cells
        # Curva de descarga simplificada
        percentage = ((avg_voltage - self.voltage_min) / 
                      (self.voltage_max - self.voltage_min)) * 100
        return max(0, min(100, percentage))
    
    def estimate_remaining_time(self, current_ma):
        """Estima tiempo restante en minutos"""
        charge_pct = self.get_charge_percentage()
        remaining_mah = (charge_pct / 100) * self.capacity
        if current_ma > 0:
            hours = remaining_mah / current_ma
            return hours * 60  # minutos
        return float('inf')
    
    def should_return_to_dock(self, threshold=20):
        """Decide si debe volver a la estación de carga"""
        return self.get_charge_percentage() < threshold
    
    def log_consumption(self, task_name, power_watts, duration_sec):
        """Registra consumo por tarea"""
        energy_wh = (power_watts * duration_sec) / 3600
        self.consumption_log.append({
            'task': task_name,
            'energy_wh': energy_wh,
            'timestamp': time.time()
        })

# Uso en ROS
import rospy
from sensor_msgs.msg import BatteryState

class BatteryMonitor:
    def __init__(self):
        self.bms = BatteryManagementSystem()
        self.pub = rospy.Publisher('/battery_state', BatteryState, queue_size=10)
        
    def publish_state(self):
        msg = BatteryState()
        msg.voltage = self.bms.get_total_voltage()
        msg.percentage = self.bms.get_charge_percentage()
        msg.power_supply_status = BatteryState.POWER_SUPPLY_STATUS_DISCHARGING
        self.pub.publish(msg)
```

#### Simulación de consumo en Gazebo

```python
# Plugin de Gazebo para simular descarga de batería
class BatteryPlugin:
    def __init__(self):
        self.initial_charge = 100.0  # %
        self.current_charge = 100.0
        
        # Consumo por sistema (Watts)
        self.power_consumption = {
            'raspberry_pi': 5.0,
            'servos_idle': 2.0,
            'servos_moving': 30.0,
            'camera': 2.5,
            'sensors': 1.0,
            'wifi': 1.5
        }
    
    def update(self, dt, robot_state):
        """Actualiza carga según actividad"""
        total_power = self.power_consumption['raspberry_pi']
        total_power += self.power_consumption['sensors']
        total_power += self.power_consumption['wifi']
        
        if robot_state['moving']:
            total_power += self.power_consumption['servos_moving']
        else:
            total_power += self.power_consumption['servos_idle']
        
        if robot_state['camera_active']:
            total_power += self.power_consumption['camera']
        
        # Calcular descarga (asumiendo batería de 11.1V 5000mAh = 55.5Wh)
        battery_capacity_wh = 55.5
        charge_consumed = (total_power * dt / 3600) / battery_capacity_wh * 100
        self.current_charge -= charge_consumed
        
        return self.current_charge
```

---

### 2. Regulación energética (homeostasis)

#### Qué se simula
- Balance energético dinámico según las tareas realizadas
- Asignación inteligente de recursos
- Modos de ahorro de energía

#### Estrategias de optimización

**Modos de operación**:

```python
from enum import Enum

class PowerMode(Enum):
    PERFORMANCE = 1    # Máximo rendimiento
    BALANCED = 2       # Balance rendimiento/eficiencia
    POWER_SAVE = 3     # Máximo ahorro
    EMERGENCY = 4      # Modo crítico (<10% batería)

class PowerManager:
    def __init__(self):
        self.mode = PowerMode.BALANCED
        self.battery = BatteryManagementSystem()
        
    def adjust_mode(self):
        """Ajusta modo automáticamente según batería"""
        charge = self.battery.get_charge_percentage()
        
        if charge < 10:
            self.mode = PowerMode.EMERGENCY
            self.emergency_actions()
        elif charge < 25:
            self.mode = PowerMode.POWER_SAVE
        elif charge > 60:
            self.mode = PowerMode.PERFORMANCE
        else:
            self.mode = PowerMode.BALANCED
    
    def get_cpu_frequency(self):
        """Ajusta frecuencia de CPU según modo"""
        freq_map = {
            PowerMode.PERFORMANCE: 1500,  # MHz
            PowerMode.BALANCED: 1200,
            PowerMode.POWER_SAVE: 800,
            PowerMode.EMERGENCY: 600
        }
        return freq_map[self.mode]
    
    def get_servo_refresh_rate(self):
        """Ajusta tasa de actualización de servos"""
        rate_map = {
            PowerMode.PERFORMANCE: 50,  # Hz
            PowerMode.BALANCED: 30,
            PowerMode.POWER_SAVE: 20,
            PowerMode.EMERGENCY: 10
        }
        return rate_map[self.mode]
    
    def can_execute_task(self, task_name, estimated_energy_wh):
        """Decide si hay suficiente energía para una tarea"""
        remaining_energy = (self.battery.get_charge_percentage() / 100) * 55.5  # Wh
        safety_margin = 10  # Wh
        
        return remaining_energy > (estimated_energy_wh + safety_margin)
    
    def emergency_actions(self):
        """Acciones en modo emergencia"""
        print("ADVERTENCIA: MODO EMERGENCIA ACTIVADO")
        # 1. Desactivar cámara
        # 2. Reducir frecuencia de sensores
        # 3. Desactivar WiFi (solo emergencia local)
        # 4. Posición segura (sentado)
        # 5. Buscar estación de carga
        pass

# Integración con planificador de tareas
class TaskScheduler:
    def __init__(self):
        self.power_manager = PowerManager()
        self.task_queue = []
    
    def schedule_task(self, task):
        """Programa tarea considerando energía disponible"""
        if self.power_manager.can_execute_task(task.name, task.energy_cost):
            self.task_queue.append(task)
            return True
        else:
            print(f"ERROR: Tarea {task.name} pospuesta por falta de energía")
            return False
```

#### Predicción de consumo con IA

```python
import torch
import torch.nn as nn

class EnergyConsumptionPredictor(nn.Module):
    """Predice consumo futuro basado en tareas planificadas"""
    def __init__(self, input_size=10):
        super().__init__()
        self.lstm = nn.LSTM(input_size, 64, batch_first=True)
        self.fc = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),  # Predicción de consumo en Watts
            nn.ReLU()
        )
    
    def forward(self, x):
        # x: (batch, sequence_length, features)
        # features: [n_servos_activos, velocidad, carga_cpu, camara_on, ...]
        lstm_out, _ = self.lstm(x)
        prediction = self.fc(lstm_out[:, -1, :])
        return prediction

# Entrenamiento con datos históricos
def train_energy_predictor(model, historical_data):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()
    
    for epoch in range(100):
        for batch_features, batch_consumption in historical_data:
            optimizer.zero_grad()
            predicted = model(batch_features)
            loss = criterion(predicted, batch_consumption)
            loss.backward()
            optimizer.step()
```

---

### 3. Recuperación y eficiencia (metabolismo avanzado)

#### Qué se simula
- Capacidad de recuperar energía o usar fuentes alternativas
- Optimización del consumo en tiempo de ejecución
- Estrategias de recarga autónoma

#### Frenado regenerativo (para robots con movilidad con ruedas)

```python
class RegenerativeBraking:
    """Recupera energía durante desaceleración"""
    def __init__(self, motor_controller):
        self.motor = motor_controller
        self.energy_recovered = 0  # Wh
        
    def brake(self, current_speed, target_speed):
        """Frena y recupera energía"""
        if current_speed > target_speed:
            # Calcular energía cinética disponible
            kinetic_energy = 0.5 * self.motor.mass * (current_speed**2 - target_speed**2)
            
            # Eficiencia del sistema (típicamente 60-70%)
            efficiency = 0.65
            energy_recovered_j = kinetic_energy * efficiency
            energy_recovered_wh = energy_recovered_j / 3600
            
            self.energy_recovered += energy_recovered_wh
            
            # Enviar comando al motor para actuar como generador
            self.motor.set_mode('generator')
            self.motor.set_brake_force(self.calculate_brake_force(current_speed, target_speed))
            
            return energy_recovered_wh
        return 0
```

#### Dock de carga autónomo

```python
class ChargingDockController:
    """Controla la búsqueda y acoplamiento a estación de carga"""
    def __init__(self):
        self.dock_position = None
        self.is_charging = False
        self.charge_current = 0  # mA
        
    def locate_charging_dock(self):
        """Busca la estación de carga usando visión o balizas IR"""
        # Método 1: Visión por computadora (ArUco markers)
        # Método 2: Balizas infrarrojas
        # Método 3: Guía por ultrasonido
        pass
    
    def navigate_to_dock(self):
        """Navega autónomamente a la estación"""
        if self.dock_position:
            # Usar planificador de rutas
            # Alineación precisa con contactos
            pass
    
    def start_charging(self):
        """Inicia proceso de carga"""
        self.is_charging = True
        # Verificar contactos eléctricos
        # Monitorear corriente y temperatura
        # Balanceo de celdas si aplica
        pass
    
    def charging_behavior(self):
        """Comportamiento durante la carga"""
        # Modo de bajo consumo
        # Actualizar firmware si hay updates
        # Procesar datos del día
        # Entrenar modelos (si tiene GPU)
        pass
```

#### Energía solar (opcional avanzado)

```python
class SolarPanel:
    """Simula panel solar como fuente de energía auxiliar"""
    def __init__(self, area_m2=0.1, efficiency=0.15):
        self.area = area_m2
        self.efficiency = efficiency
        
    def get_power_output(self, solar_irradiance_w_m2, angle_deg=0):
        """
        Calcula potencia generada
        solar_irradiance: típicamente 400-1000 W/m² dependiendo de hora y clima
        """
        angle_factor = math.cos(math.radians(angle_deg))
        power_w = self.area * solar_irradiance_w_m2 * self.efficiency * angle_factor
        return max(0, power_w)
    
    def estimate_daily_generation(self, location_lat, season):
        """Estima generación diaria según ubicación"""
        # Simplificado: 5 horas de sol útil promedio
        avg_irradiance = 600  # W/m²
        useful_hours = 5
        daily_wh = self.get_power_output(avg_irradiance) * useful_hours
        return daily_wh

# Ejemplo: Panel de 0.1 m² (10cm x 10cm) genera ~15Wh/día
# Batería del robot: 55.5Wh → panel cubre ~27% del consumo diario en uso ligero
```

#### Músculos artificiales (investigación futura)

```markdown
**Actuadores más eficientes que motores tradicionales**:

1. **Actuadores neumáticos**:
   - Ventajas: Ligeros, compliantes, seguros
   - Desventajas: Requieren compresor (consume energía)
   
2. **Polímeros electroactivos (EAP)**:
   - Consumo: 1/10 de un motor tradicional
   - Estado: Aún en investigación para robots grandes
   
3. **Aleaciones con memoria de forma (SMA)**:
   - Eficientes para movimientos lentos
   - Consumo: Moderado
   
4. **Comparación de consumo**:
   Servo estándar: ~10W en movimiento
   Músculo neumático: ~15W (incluyendo compresor)
   EAP teórico: ~1W
```

#### Dashboard de monitoreo energético

```python
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class EnergyDashboard:
    def __init__(self):
        self.history = {
            'time': [],
            'charge': [],
            'consumption': [],
            'mode': []
        }
    
    def plot_energy_status(self):
        """Visualiza estado energético"""
        fig, axs = plt.subplots(3, 1, figsize=(10, 8))
        
        # Gráfico 1: Nivel de batería
        axs[0].plot(self.history['time'], self.history['charge'], 'b-')
        axs[0].set_ylabel('Carga (%)')
        axs[0].set_title('Estado de Batería')
        axs[0].axhline(y=20, color='r', linestyle='--', label='Umbral crítico')
        axs[0].legend()
        
        # Gráfico 2: Consumo instantáneo
        axs[1].plot(self.history['time'], self.history['consumption'], 'g-')
        axs[1].set_ylabel('Potencia (W)')
        axs[1].set_title('Consumo Instantáneo')
        
        # Gráfico 3: Modo de operación
        modes = {'PERFORMANCE': 3, 'BALANCED': 2, 'POWER_SAVE': 1, 'EMERGENCY': 0}
        mode_values = [modes[m] for m in self.history['mode']]
        axs[2].step(self.history['time'], mode_values, 'r-', where='post')
        axs[2].set_ylabel('Modo')
        axs[2].set_xlabel('Tiempo')
        axs[2].set_title('Modo de Operación')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self):
        """Genera reporte de eficiencia energética"""
        total_time = (self.history['time'][-1] - self.history['time'][0]).seconds / 3600  # horas
        avg_consumption = sum(self.history['consumption']) / len(self.history['consumption'])
        total_energy = avg_consumption * total_time  # Wh
        
        report = f"""
        REPORTE ENERGÉTICO
        ═══════════════════════════════
        Tiempo de operación: {total_time:.2f} horas
        Consumo promedio: {avg_consumption:.2f} W
        Energía total consumida: {total_energy:.2f} Wh
        Carga inicial: {self.history['charge'][0]:.1f}%
        Carga final: {self.history['charge'][-1]:.1f}%
        Eficiencia: {(self.history['charge'][0] - self.history['charge'][-1]) / total_energy * 55.5:.2f} %/Wh
        """
        return report
```

---

### Integración con ROS

Topics relacionados con energía:

```bash
# Publicar estado de batería
rostopic pub /energy/battery_state sensor_msgs/BatteryState

# Suscribirse a modo de energía
rostopic echo /energy/power_mode

# Comandar retorno a dock
rostopic pub /energy/return_to_dock std_msgs/Bool "data: true"

# Monitorear consumo por sistema
rostopic echo /energy/system_consumption
```

---

### Referencias

**Papers recomendados**:
1. "Energy Management for Mobile Robots" (IEEE Robotics & Automation)
2. "Battery State Estimation for Mobile Robots" (Journal of Field Robotics)
3. "Autonomous Recharging for Service Robots" (IROS)

**Herramientas**:
- INA219: Sensor de corriente/voltaje
- Battery monitoring libraries: `ina219`, `Adafruit_CircuitPython`
- ROS package: `robot_battery_state`

---

## Herramientas necesarias

### Software
- **CAD**: SolidWorks, Fusion 360, FreeCAD
- **Electrónica**: KiCad, Fritzing, Eagle
- **Simulación**: Gazebo, PyBullet, V-REP
- **Firmware**: Arduino IDE, PlatformIO, STM32CubeIDE

### Hardware
- Impresora 3D (recomendado: Prusa i3 MK3S o similar)
- Estación de soldadura
- Multímetro digital
- Fuente de alimentación variable
- Juego de destornilladores
- Herramientas de crimping
- Osciloscopio (opcional pero útil)

## Bill of materials (BOM) estimado

Ver archivo detallado en `electronica/bom/bom_completo.csv`

**Costo estimado total**: $1,000 - $2,500 USD (dependiendo de componentes)

### Categorías principales:
- **Mecánica**: $200-400 (aluminio, filamento, tornillería)
- **Actuadores**: $300-600 (servos de calidad)
- **Electrónica**: $200-400 (microcontroladores, sensores, PCB)
- **Energía**: $100-200 (baterías, reguladores, BMS)
- **Herramientas**: $200-900 (si no se tienen)

## Proveedores recomendados

- **Electrónica**: Adafruit, SparkFun, Pololu, Digi-Key, Mouser
- **Mecánica**: McMaster-Carr, Misumi, OpenBuilds
- **Impresión 3D**: Prusa Research, Ultimaker, local makers
- **Actuadores**: Robotis (Dynamixel), Servo City, AliExpress (económico)

## Troubleshooting común

### Problema: Servo vibra o no mantiene posición
**Soluciones**:
- Verificar alimentación adecuada (voltaje y corriente)
- Añadir capacitor cerca del servo (100-470µF)
- Implementar deadband en control PID
- Verificar que señal PWM sea estable

### Problema: Raspberry Pi se reinicia
**Soluciones**:
- Alimentación insuficiente (usar fuente ≥3A)
- Caída de voltaje (cable corto y grueso)
- Motores causando ruido eléctrico (separar alimentaciones)

### Problema: Comunicación I2C falla
**Soluciones**:
- Verificar pull-up resistors (2.2-4.7kΩ)
- Cables cortos (<1m)
- Verificar direcciones I2C únicas
- Reducir velocidad de bus si hay ruido

### Problema: IMU da lecturas erráticas
**Soluciones**:
- Calibración en superficie nivelada
- Alejado de campos magnéticos (motores, imanes)
- Filtrado (complementary filter, Kalman)
- Montaje rígido (sin vibraciones)

## Próximos pasos

1. **Completar diseño CAD** de todas las piezas
2. **Validar BOM** y realizar pedidos
3. **Comenzar fabricación** de piezas no críticas
4. **Configurar entorno de desarrollo** (Arduino IDE, ROS, etc.)
5. **Crear prototipos pequeños** (probar una articulación completa)

## Referencias y recursos

### Proyectos open source similares
- InMoov: Robot humanoide DIY completo
- Poppy Project: Plataforma educativa modular
- THOR (UCLA): Robot humanoide open source
- Jimmy Robot: Versión simple y económica

### Tutoriales
- Adafruit Learn: Servo control, I2C, etc.
- SparkFun Tutorials: Sensores y actuadores
- ROS Tutorials: Integración con ROS

### Documentación
- Servo datasheets (torque curves, specifications)
- IMU sensor fusion algorithms
- Battery safety guidelines (LiPo)

### Comunidades
- r/robotics
- ROS Discourse
- Let's Make Robots forum
- Arduino Forum

---

**Nota de Seguridad**: Este robot tiene componentes móviles y eléctricos. Siempre seguir procedimientos de seguridad. En caso de duda, DETENER y consultar.

**Última actualización**: Febrero 2026