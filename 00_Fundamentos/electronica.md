# Fundamentos de electrónica y electricidad para robótica humanoide

## Resumen ejecutivo

El sistema electrónico de un robot humanoide constituye el sistema nervioso artificial que permite la percepción sensorial, el procesamiento de información y el control de actuadores. Este documento presenta los fundamentos teóricos y prácticos necesarios para diseñar, implementar y validar circuitos electrónicos para sistemas robóticos complejos a nivel de investigación doctoral.

## 1. Fundamentos de electricidad y circuitos

### 1.1 Leyes fundamentales

#### 1.1.1 Ley de Ohm

La relación fundamental entre voltaje, corriente y resistencia:

$$V = I \cdot R$$

Donde:
- $V$ = Voltaje (Volts, V)
- $I$ = Corriente (Amperes, A)
- $R$ = Resistencia (Ohms, Ω)

**Forma alternativas**:
$$I = \frac{V}{R} \quad\quad R = \frac{V}{I}$$

**Potencia disipada**:
$$P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}$$

**Aplicación práctica**: Dimensionamiento de resistencias limitadoras de corriente para LEDs.

```python
def calcular_resistencia_led(v_fuente, v_led, i_led_ma):
    """
    Calcula resistencia limitadora para LED
    
    Args:
        v_fuente: Voltaje de alimentación (V)
        v_led: Caída de voltaje del LED (V) [Rojo: 1.8-2.2, Azul: 3.0-3.4]
        i_led_ma: Corriente deseada del LED (mA) [típico: 20 mA]
    
    Returns:
        R: Resistencia (Ω)
        P: Potencia disipada (W)
        R_comercial: Valor comercial más cercano
    """
    i_led_a = i_led_ma / 1000  # Convertir a Amperes
    
    # Ley de Ohm
    R = (v_fuente - v_led) / i_led_a
    
    # Potencia disipada
    P = (v_fuente - v_led) * i_led_a
    
    # Valores comerciales E12 series
    valores_comerciales = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
                          100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
                          1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600]
    
    # Encontrar valor comercial más cercano (redondear arriba para seguridad)
    R_comercial = min([v for v in valores_comerciales if v >= R], 
                      key=lambda x: abs(x - R))
    
    return R, P, R_comercial

# Ejemplo: LED indicador en sistema 5V
R, P, R_com = calcular_resistencia_led(v_fuente=5, v_led=2.0, i_led_ma=20)
print(f"Resistencia calculada: {R:.1f} Ω")
print(f"Resistencia comercial: {R_com} Ω (usar 1/4W)")
print(f"Potencia disipada: {P*1000:.1f} mW")
```

#### 1.1.2 Leyes de Kirchhoff

**Primera Ley (Ley de Corrientes - KCL)**:
La suma algebraica de corrientes en un nodo es cero:

$$\sum I_{entrando} = \sum I_{saliendo}$$

**Segunda Ley (Ley de Voltajes - KVL)**:
La suma algebraica de voltajes en una malla cerrada es cero:

$$\sum V = 0$$

**Aplicación**: Análisis de divisores de voltaje y corriente.

**Divisor de voltaje**:
$$V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}$$

```python
def divisor_voltaje(v_in, r1, r2, r_carga=float('inf')):
    """
    Calcula salida de divisor de voltaje considerando carga
    
    Args:
        v_in: Voltaje de entrada (V)
        r1: Resistencia superior (Ω)
        r2: Resistencia inferior (Ω)
        r_carga: Resistencia de carga (Ω), infinito si no hay carga
    
    Returns:
        v_out: Voltaje de salida (V)
        i_total: Corriente total del divisor (mA)
    """
    # Resistencia equivalente de R2 en paralelo con carga
    if r_carga != float('inf'):
        r2_eq = (r2 * r_carga) / (r2 + r_carga)
    else:
        r2_eq = r2
    
    v_out = v_in * r2_eq / (r1 + r2_eq)
    i_total = v_in / (r1 + r2_eq) * 1000  # mA
    
    return v_out, i_total

# Ejemplo: Reducir 5V a 3.3V para lógica TTL
v_out, i = divisor_voltaje(5, r1=1700, r2=3300)
print(f"Salida: {v_out:.2f} V")
print(f"Corriente: {i:.2f} mA")
```

#### 1.1.3 Teoremas de red

**Teorema de Thévenin**:
Cualquier red lineal bilateral puede reemplazarse por:
- Una fuente de voltaje $V_{th}$
- Una resistencia en serie $R_{th}$

**Teorema de Norton**:
Equivalente usando fuente de corriente $I_N$ y resistencia paralela $R_N$.

### 1.2 Componentes pasivos

#### 1.2.1 Resistencias

**Tipos**:
- **Carbón**: Económicas, ±5-10%, ruidosas
- **Película metálica**: Precisas, ±1%, bajo ruido
- **Wire-wound**: Alta potencia, inductancia parásita
- **SMD**: Compactas, automatización

**Código de colores**:
```
Negro: 0    Marrón: 1    Rojo: 2       Naranja: 3
Amarillo: 4  Verde: 5    Azul: 6       Violeta: 7
Gris: 8     Blanco: 9    
Oro: ±5%    Plata: ±10%
```

**Potencia nominal**:
- 1/8 W, 1/4 W (común en señales)
- 1/2 W, 1 W (potencias medias)
- 5 W+ (alta potencia, wire-wound)

Regla: Usar resistencia con potencia nominal ≥ 2× potencia calculada.

#### 1.2.2 Condensadores

**Capacitancia**: Capacidad de almacenar carga.

$$C = \frac{Q}{V} \quad [Faradios]$$

**Energía almacenada**:
$$E = \frac{1}{2}CV^2$$

**Tipos y aplicaciones**:

| Tipo | Rango | Características | Aplicaciones |
|------|-------|----------------|--------------|
| Cerámico | 1pF - 10µF | Bajo ESR, NPO/X7R/Y5V | Desacoplo, alta frecuencia |
| Electrolítico | 1µF - 10,000µF | Polarizado, alta capacitancia | Filtrado fuente, bulk |
| Tántalo | 0.1µF - 1000µF | Polarizado, baja ESR | Audio, filtrado |
| Film | 100pF - 10µF | Precisos, no polarizados | Audio, timing |
| Supercapacitor | 0.1F - 3000F | Muy alta capacitancia | Backup energía |

**Reactancia capacitiva**:
$$X_C = \frac{1}{2\pi f C}$$

A mayor frecuencia, menor impedancia → Condensadores "cortocircuitan" AC.

**Aplicación: Desacoplo de fuentes**:

```python
def calcular_capacitor_desacoplo(i_pico_a, delta_v_max, tiempo_switching_ns):
    """
    Calcula capacitor de desacoplo para circuito digital
    
    Args:
        i_pico_a: Corriente pico transitoria (A)
        delta_v_max: Caída de voltaje máxima permitida (V)
        tiempo_switching_ns: Tiempo de conmutación (ns)
    
    Returns:
        C_min: Capacitancia mínima (µF)
    """
    t_sec = tiempo_switching_ns * 1e-9
    
    # Q = C * ΔV = I * Δt
    C_faradios = (i_pico_a * t_sec) / delta_v_max
    C_microfaradios = C_faradios * 1e6
    
    return C_microfaradios

# Ejemplo: Raspberry Pi con picos de 2A en 10ns
C = calcular_capacitor_desacoplo(i_pico_a=2, delta_v_max=0.1, tiempo_switching_ns=10)
print(f"Capacitor mínimo: {C:.2f} µF")
print("Usar: 100µF electrolítico + 0.1µF cerámico en paralelo")
```

#### 1.2.3 Inductores

**Inductancia**: Oposición al cambio de corriente.

$$V_L = L \frac{dI}{dt}$$

**Energía almacenada**:
$$E = \frac{1}{2}LI^2$$

**Reactancia inductiva**:
$$X_L = 2\pi f L$$

A mayor frecuencia, mayor impedancia → Inductores "bloquean" AC.

**Aplicaciones**:
- Filtros LC
- Convertidores DC-DC (Buck, Boost)
- Supresión EMI

### 1.3 Componentes activos

#### 1.3.1 Diodos

**Función**: Permitir flujo de corriente en una dirección.

**Ecuación de Shockley**:
$$I = I_S \left(e^{\frac{V}{nV_T}} - 1\right)$$

Donde $V_T = \frac{kT}{q} \approx 26\text{ mV}$ a temperatura ambiente.

**Tipos**:
- **Rectificador estándar** (1N4001-7): Rectificación AC
- **Schottky**: Baja caída de voltaje (~0.3V), alta velocidad
- **Zener**: Regulación de voltaje (voltaje de ruptura controlado)
- **LED**: Emisión de luz

**Protección con diodo flyback**:

```python
def diodo_flyback_para_relay(v_bobina, i_bobina, inductancia_mh):
    """
    Especifica diodo de protección para bobina inductiva
    
    Args:
        v_bobina: Voltaje de la bobina (V)
        i_bobina: Corriente de la bobina (A)
        inductancia_mh: Inductancia de la bobina (mH)
    
    Returns:
        especificaciones del diodo
    """
    # Pico de voltaje reverso: V_pico = V_bobina + V_diodo
    v_reverso_pico = v_bobina + 1  # +1V por caída del diodo
    
    # Corriente pico (igual a corriente de la bobina)
    i_pico = i_bobina
    
    # Energía a disipar
    L_henrios = inductancia_mh / 1000
    energia_julios = 0.5 * L_henrios * (i_bobina ** 2)
    
    return {
        'v_reverso_min': v_reverso_pico * 1.5,  # Factor de seguridad
        'i_forward_avg': i_pico,
        'tipo_recomendado': '1N4148' if i_bobina < 0.2 else '1N4007',
        'energia_disipada_mj': energia_julios * 1000
    }

# Ejemplo: Relé 12V, 50mA
specs = diodo_flyback_para_relay(12, 0.05, 100)
print(f"Diodo: {specs['tipo_recomendado']}")
print(f"Voltaje reverso mínimo: {specs['v_reverso_min']:.1f} V")
```

#### 1.3.2 Transistores

**BJT (Bipolar Junction Transistor)**:

Tres regiones de operación:
1. **Corte**: $I_B = 0$, transistor OFF ($V_{BE} < 0.7V$)
2. **Activa**: Amplificación, $I_C = \beta I_B$
3. **Saturación**: Transistor ON ($V_{CE,sat} \approx 0.2V$)

**Ganancia de corriente**:
$$\beta = h_{FE} = \frac{I_C}{I_B}$$

Típicamente $\beta = 50$ - 300.

**Diseño de switch BJT**:

```python
def diseñar_switch_bjt(v_cc, i_carga_ma, v_control=3.3, beta=100):
    """
    Diseña circuito de switch con BJT (NPN)
    
    Args:
        v_cc: Voltaje de colector (V)
        i_carga_ma: Corriente de carga (mA)
        v_control: Voltaje de señal de control (V)
        beta: Ganancia del transistor
    
    Returns:
        Rb: Resistencia de base (Ω)
        transistor_recomendado: Modelo
    """
    i_carga_a = i_carga_ma / 1000
    
    # Corriente de base para saturación (factor 10x de seguridad)
    i_base_sat = (i_carga_a / beta) * 10
    
    # Resistencia de base (asumiendo V_BE = 0.7V)
    v_rb = v_control - 0.7
    Rb = v_rb / i_base_sat
    
    # Seleccionar transistor
    if i_carga_ma < 100:
        transistor = '2N3904 (NPN, 200mA)'
    elif i_carga_ma < 600:
        transistor = '2N2222 (NPN, 600mA)'
    elif i_carga_ma < 1000:
        transistor = 'TIP31C (NPN, 3A)'
    else:
        transistor = 'TIP102 (Darlington, 8A)'
    
    return {
        'Rb': Rb,
        'Rb_comercial': round(Rb, -2),  # Redondear a 100Ω
        'transistor': transistor,
        'i_base_ma': i_base_sat * 1000
    }

# Ejemplo: Controlar motor DC 100mA desde GPIO 3.3V
result = diseñar_switch_bjt(v_cc=6, i_carga_ma=100, v_control=3.3)
print(f"Resistencia base: {result['Rb_comercial']:.0f} Ω")
print(f"Transistor: {result['transistor']}")
print(f"Corriente de base: {result['i_base_ma']:.2f} mA")
```

**MOSFET (Metal-Oxide-Semiconductor FET)**:

Ventajas sobre BJT:
- Control por voltaje (no requiere corriente de base continua)
- Conmutación más rápida
- Menor disipación de potencia

**Parámetros clave**:
- $V_{GS(th)}$: Voltaje umbral de activación (typ. 2-4V)
- $R_{DS(on)}$: Resistencia en conducción (typ. 0.01-0.1Ω)
- $I_D$: Corriente de drenador máxima

**Tipos**:
- **N-Channel**: Más común, para lado bajo (low-side switching)
- **P-Channel**: Para lado alto (high-side switching)

**Ejemplo de aplicación - Control de motor**:

```python
def seleccionar_mosfet_motor(v_motor, i_motor_a, pwm_freq_khz):
    """
    Selecciona MOSFET para control PWM de motor DC
    
    Args:
        v_motor: Voltaje del motor (V)
        i_motor_a: Corriente del motor (A)
        pwm_freq_khz: Frecuencia PWM (kHz)
    
    Returns:
        Especificaciones del MOSFET
    """
    # Voltaje drain-source mínimo (factor 2x seguridad)
    v_dss_min = v_motor * 2
    
    # Corriente continua mínima (factor 1.5x seguridad)
    i_d_min = i_motor_a * 1.5
    
    # Resistencia RDS(on) para no exceder 1W de disipación
    p_max_disipacion = 1  # W
    r_ds_on_max = p_max_disipacion / (i_motor_a ** 2)
    
    # Tiempo de conmutación (influye en pérdidas)
    t_switch_max_ns = 1000 / pwm_freq_khz  # Simplificado
    
    # Recomendaciones
    if i_motor_a < 1:
        mosfet = 'IRLZ44N (N-ch, 55V, 47A, RDS=0.022Ω)'
    elif i_motor_a < 5:
        mosfet = 'IRF540N (N-ch, 100V, 33A, RDS=0.044Ω)'
    elif i_motor_a < 15:
        mosfet = 'IRFB3077 (N-ch, 75V, 210A, RDS=0.003Ω)'
    else:
        mosfet = 'Usar H-Bridge integrado (VNH5019, BTS7960)'
    
    return {
        'V_DSS_min': v_dss_min,
        'I_D_min': i_d_min,
        'RDS_on_max': r_ds_on_max,
        'mosfet_recomendado': mosfet
    }

# Ejemplo: Motor 12V, 3A
specs = seleccionar_mosfet_motor(12, 3, 20)
print(f"MOSFET: {specs['mosfet_recomendado']}")
print(f"RDS(on) máximo: {specs['RDS_on_max']:.4f} Ω")
```

## 2. Microcontroladores y procesadores

### 2.1 Arquitectura de microcontroladores

**Componentes principales**:
- **CPU**: Unidad central de procesamiento
- **Memoria Flash**: Programa ejecutable
- **RAM**: Variables temporales
- **Periféricos**: GPIO, ADC, UART, I2C, SPI, PWM, Timers

**Comparativa para robótica**:

| MCU | CPU | Velocidad | Flash | RAM | GPIO | ADC | Precio | Aplicación |
|-----|-----|-----------|-------|-----|------|-----|--------|------------|
| **Arduino Uno** (ATmega328P) | 8-bit AVR | 16 MHz | 32 KB | 2 KB | 14 | 6×10-bit | $5 | Prototipado, sensores |
| **Arduino Mega** (ATmega2560) | 8-bit AVR | 16 MHz | 256 KB | 8 KB | 54 | 16×10-bit | $10 | Muchos servos, I/O |
| **Teensy 4.0** (ARM Cortex-M7) | 32-bit | 600 MHz | 2 MB | 1 MB | 40 | 14×12-bit | $20 | Alto rendimiento |
| **ESP32** | 32-bit Xtensa dual-core | 240 MHz | 4 MB | 520 KB | 34 | 18×12-bit | $3 | WiFi/BT, IoT |
| **STM32F4** (Nucleo) | 32-bit ARM Cortex-M4 | 168 MHz | 512 KB | 128 KB | 82 | 16×12-bit | $15 | Profesional, DSP |
| **Raspberry Pi 4** (BCM2711) | 64-bit ARM Cortex-A72 quad-core | 1.5 GHz | SD Card | 4-8 GB | 40 | 0 (usar ADC ext) | $35-55 | Linux, visión, IA |

### 2.2 Protocolos de comunicación

#### 2.2.1 UART (Universal Asynchronous Receiver-Transmitter)

**Características**:
- Comunicación serial asíncrona
- Requiere acordar baud rate (9600, 115200, etc.)
- 2 cables: TX, RX (+ GND)
- Distancia corta (<15m sin driver RS-232)

**Formato de trama**:
```
[Start bit | Data bits (5-9) | Parity bit (opt) | Stop bit(s)]
```

**Código Arduino**:
```cpp
// Arduino - Comunicación UART
void setup() {
    Serial.begin(115200);  // Inicializar a 115200 baud
}

void loop() {
    if (Serial.available() > 0) {
        char comando = Serial.read();
        
        if (comando == 'A') {
            // Mover brazo
            Serial.println("OK: Brazo movido");
        }
    }
    
    // Enviar telemetría
    float temperatura = leerTemperatura();
    Serial.print("TEMP:");
    Serial.println(temperatura);
    
    delay(100);
}
```

#### 2.2.2 I2C (Inter-Integrated Circuit)

**Características**:
- Bus de 2 cables: SDA (datos), SCL (reloj)
- Múltiples dispositivos (hasta 127) en un bus
- Master-slave
- Velocidad: 100 kHz (Standard), 400 kHz (Fast), 3.4 MHz (High-speed)
- Distancia corta (<1m típico)

**Direccionamiento**: Cada dispositivo tiene dirección de 7 bits (0x00 - 0x7F).

**Ejemplo - Lectura de IMU (MPU6050)**:

```cpp
#include <Wire.h>

#define MPU6050_ADDR 0x68
#define PWR_MGMT_1   0x6B
#define ACCEL_XOUT_H 0x3B

void setup() {
    Wire.begin();
    Serial.begin(115200);
    
    // Despertar MPU6050
    Wire.beginTransmission(MPU6050_ADDR);
    Wire.write(PWR_MGMT_1);
    Wire.write(0);  // Salir de sleep mode
    Wire.endTransmission(true);
}

void loop() {
    // Leer acelerómetro (6 bytes: X, Y, Z en 16-bit)
    Wire.beginTransmission(MPU6050_ADDR);
    Wire.write(ACCEL_XOUT_H);
    Wire.endTransmission(false);
    Wire.requestFrom(MPU6050_ADDR, 6, true);
    
    int16_t accelX = Wire.read() << 8 | Wire.read();
    int16_t accelY = Wire.read() << 8 | Wire.read();
    int16_t accelZ = Wire.read() << 8 | Wire.read();
    
    // Convertir a g (suponiendo rango ±2g)
    float ax = accelX / 16384.0;
    float ay = accelY / 16384.0;
    float az = accelZ / 16384.0;
    
    Serial.print("Accel: ");
    Serial.print(ax); Serial.print(", ");
    Serial.print(ay); Serial.print(", ");
    Serial.println(az);
    
    delay(100);
}
```

#### 2.2.3 SPI (Serial Peripheral Interface)

**Características**:
- Bus de 4 cables: MOSI, MISO, SCK, CS/SS
- Full-duplex (transmisión simultánea en ambas direcciones)
- Master-slave (múltiples slaves con diferentes CS)
- Alta velocidad (10+ MHz)
- Distancia corta (<30 cm típico)

**Ventajas vs. I2C**:
- Más rápido
- Hardware más simple
- Full-duplex

**Desventajas**:
- Más cables (1 CS por dispositivo esclavo)

**Ejemplo - Lector de tarjeta SD**:

```cpp
#include <SPI.h>
#include <SD.h>

const int chipSelect = 10;  // Pin CS

void setup() {
    Serial.begin(115200);
    
    if (!SD.begin(chipSelect)) {
        Serial.println("Error al inicializar SD");
        return;
    }
    
    // Escribir datos
    File dataFile = SD.open("log.txt", FILE_WRITE);
    if (dataFile) {
        dataFile.println("Timestamp, Sensor1, Sensor2");
        dataFile.close();
    }
}

void loop() {
    File dataFile = SD.open("log.txt", FILE_WRITE);
    if (dataFile) {
        dataFile.print(millis());
        dataFile.print(", ");
        dataFile.print(analogRead(A0));
        dataFile.print(", ");
        dataFile.println(analogRead(A1));
        dataFile.close();
    }
    delay(1000);
}
```

#### 2.2.4 CAN Bus (Controller Area Network)

**Características**:
- Robusto, usado en automotriz y aplicaciones industriales
- Detección y correcci de errores
- Priorización de mensajes
- Bus diferencial (CAN_H, CAN_L)
- Distancia larga (hasta 1 km a 50 kbps)
- Velocidad: hasta 1 Mbps

**Aplicación en robótica**:
- Comunicación entre múltiples módulos distribuidos
- Entorno con ruido electromagnético
- Sistemas críticos de seguridad

### 2.3 Conversión analógico-digital (ADC)

**Función**: Convertir señal analógica continua a valor digital discreto.

**Parámetros clave**:
- **Resolución**: Número de bits (8, 10, 12, 16-bit)
- **Rango**: Voltaje mínimo y máximo (0-5V, 0-3.3V)
- **Velocidad de muestreo**: Samples per second (SPS)
- **Linealidad**: INL (Integral Non-Linearity), DNL (Differential NL)

**Cuantización**:

Para ADC de $n$ bits con rango $V_{ref}$:

$$LSB = \frac{V_{ref}}{2^n}$$

$$V_{medido} = \frac{valor\_digital \times V_{ref}}{2^n}$$

**Ejemplo**:
- Arduino Uno: 10-bit ADC, Vref = 5V
- LSB = 5V / 1024 = 4.88 mV
- Lectura de 512 → 512 × 4.88 mV = 2.5 V

**Código de lectura calibrada**:

```python
class ADC_Calibrado:
    """Clase para lectura calibrada de ADC"""
    
    def __init__(self, bits=10, vref=5.0, offset=0, ganancia=1.0):
        self.bits = bits
        self.vref = vref
        self.max_digital = 2**bits - 1
        self.lsb = vref / (2**bits)
        self.offset = offset
        self.ganancia = ganancia
    
    def leer_voltaje(self, valor_digital):
        """Convierte lectura digital a voltaje real"""
        v_raw = (valor_digital / self.max_digital) * self.vref
        v_calibrado = (v_raw - self.offset) * self.ganancia
        return v_calibrado
    
    def calibrar(self, valores_conocidos, lecturas_digitales):
        """
        Calibración de dos puntos
        
        Args:
            valores_conocidos: [V_low, V_high] voltajes reales medidos
            lecturas_digitales: [D_low, D_high] valores ADC correspondientes
        """
        v_low, v_high = valores_conocidos
        d_low, d_high = lecturas_digitales
        
        # Convertir a voltajes sin calibrar
        v_low_raw = (d_low / self.max_digital) * self.vref
        v_high_raw = (d_high / self.max_digital) * self.vref
        
        # Calcular ganancia y offset
        self.ganancia = (v_high - v_low) / (v_high_raw - v_low_raw)
        self.offset = v_low_raw - (v_low / self.ganancia)
        
        print(f"Calibración completada:")
        print(f"  Ganancia: {self.ganancia:.4f}")
        print(f"  Offset: {self.offset:.4f} V")

# Ejemplo de uso
adc = ADC_Calibrado(bits=10, vref=5.0)

# Calibración con multímetro
# Medimos 0V → ADC lee 5 (debería ser 0)
# Medimos 5V → ADC lee 1020 (debería ser 1023)
adc.calibrar(valores_conocidos=[0, 5.0], lecturas_digitales=[5, 1020])

# Lectura calibrada
lectura_raw = 512  # Ejemplo: lectura del Arduino
voltaje_real = adc.leer_voltaje(lectura_raw)
print(f"Voltaje calibrado: {voltaje_real:.3f} V")
```

### 2.4 Modulación por ancho de pulso (PWM)

**Función**: Generar señal analógica promedio mediante pulsos digitales.

**Parámetros**:
- **Frecuencia**: Ciclos por segundo (Hz)
- **Duty Cycle**: Porcentaje de tiempo en HIGH (0-100%)

$$V_{avg} = V_{max} \times \frac{Duty\_Cycle}{100}$$

**Aplicaciones**:
- Control de velocidad de motores DC
- Control de brillo de LEDs
- Generación de señales analógicas (con filtro LC)
- Control de servomotores

**Servomotores**:
- PWM de 50 Hz (período 20 ms)
- Pulso de 1 ms → 0° (o -90°)
- Pulso de 1.5 ms → 90° (centro)
- Pulso de 2 ms → 180° (o +90°)

```cpp
#include <Servo.h>

Servo miServo;

void setup() {
    miServo.attach(9);  // Pin 9
}

void loop() {
    // Barrido de 0° a 180°
    for (int angulo = 0; angulo <= 180; angulo++) {
        miServo.write(angulo);
        delay(15);
    }
    
    for (int angulo = 180; angulo >= 0; angulo--) {
        miServo.write(angulo);
        delay(15);
    }
}
```

**Control PWM de motor DC con driver L298N**:

```cpp
// Pines del L298N
const int ENA = 9;   // PWM para control de velocidad Motor A
const int IN1 = 8;   // Dirección Motor A
const int IN2 = 7;

void setup() {
    pinMode(ENA, OUTPUT);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
}

void motorControl(int velocidad) {
    /*
    velocidad: -255 (reversa máxima) a +255 (adelante máxima)
    */
    if (velocidad > 0) {
        // Adelante
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        analogWrite(ENA, velocidad);
    } else if (velocidad < 0) {
        // Reversa
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        analogWrite(ENA, -velocidad);
    } else {
        // Freno
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        analogWrite(ENA, 0);
    }
}

void loop() {
    // Acelerar adelante
    for (int v = 0; v <= 255; v += 5) {
        motorControl(v);
        delay(50);
    }
    
    delay(1000);
    
    // Acelerar reversa
    for (int v = 0; v >= -255; v -= 5) {
        motorControl(v);
        delay(50);
    }
    
    motorControl(0);  // Detener
    delay(2000);
}
```

## 3. Fuentes de alimentación y gestión de energía

### 3.1 Reguladores de voltaje

#### 3.1.1 Reguladores lineales

**Principio**: Disipar exceso de voltaje como calor.

**Ventajas**:
- Simple, pocos componentes externos
- Bajo ruido
- Respuesta rápida

**Desventajas**:
- Baja eficiencia: $\eta = \frac{V_{out}}{V_{in}}$
- Disipación de calor: $P_D = (V_{in} - V_{out}) \times I_{out}$

**Familias comunes**:
- **78xx** (positivo): 7805 (5V), 7809 (9V), 7812 (12V)
- **79xx** (negativo): 7905 (-5V), 7912 (-12V)
- **LDO** (Low Dropout): LM1117, AMS1117, LD1117

**Ejemplo de cálculo de disipación**:

```python
def calcular_disipador_regulador(v_in, v_out, i_out, r_theta_ja=50):
    """
    Determina si se necesita disipador para regulador lineal
    
    Args:
        v_in: Voltaje de entrada (V)
        v_out: Voltaje de salida (V)
        i_out: Corriente de salida (A)
        r_theta_ja: Resistencia térmica junction-to-ambient sin disipador (°C/W)
    
    Returns:
        Especificaciones térmicas
    """
    # Potencia disipada
    p_diss = (v_in - v_out) * i_out
    
    # Eficiencia
    eficiencia = (v_out / v_in) * 100
    
    # Temperatura del chip (asumiendo 25°C ambiente)
    t_ambiente = 25
    t_junction_max = 125  # Típico para 78xx
    
    delta_t = p_diss * r_theta_ja
    t_junction = t_ambiente + delta_t
    
    necesita_disipador = t_junction > 70  # Usar 70°C como límite conservador
    
    if necesita_disipador:
        # Resistencia térmica del disipador requerida
        r_theta_ja_max = (t_junction_max - t_ambiente) / p_diss - 5  # -5 es R_theta_jc típico
        recomendacion = f"Usar disipador con R_θ ≤ {r_theta_ja_max:.1f} °C/W"
    else:
        recomendacion = "No requiere disipador"
    
    return {
        'potencia_disipada_w': p_diss,
        'eficiencia_pct': eficiencia,
        'temp_junction_c': t_junction,
        'necesita_disipador': necesita_disipador,
        'recomendacion': recomendacion
    }

# Ejemplo: 7805 convirtiendo 12V a 5V, 1A
resultado = calcular_disipador_regulador(12, 5, 1.0)
print(f"Potencia disipada: {resultado['potencia_disipada_w']:.2f} W")
print(f"Eficiencia: {resultado['eficiencia_pct']:.1f}%")
print(f"Temperatura del chip: {resultado['temp_junction_c']:.1f}°C")
print(f"Recomendación: {resultado['recomendacion']}")
```

#### 3.1.2 Convertidores DC-DC conmutados

**Ventajas**:
- Alta eficiencia (85-95%)
- Menor disipación de calor
- Pueden aumentar voltaje (Boost) o disminuir (Buck)

**Tipos**:

1. **Buck (Step-Down)**:
   - $V_{out} < V_{in}$
   - Ejemplo: 12V → 5V

2. **Boost (Step-Up)**:
   - $V_{out} > V_{in}$
   - Ejemplo: 3.7V (batería Li-Ion) → 5V

3. **Buck-Boost**:
   - $V_{out}$ puede ser mayor o menor que $V_{in}$

4. **Inversor**:
   - Generate voltaje negativo

**Selección de componentes para módulo Buck**:

```python
def diseñar_buck_converter(v_in, v_out, i_out, freq_khz=100):
    """
    Dimensiona componentes para Buck converter
    
    Args:
        v_in: Voltaje de entrada (V)
        v_out: Voltaje de salida (V)
        i_out: Corriente de salida (A)
        freq_khz: Frecuencia de switching (kHz)
    
    Returns:
        Especificaciones de componentes
    """
    # Duty cycle
    D = v_out / v_in
    
    # Ripple de corriente (típicamente 20-40% de Iout)
    delta_i_L = 0.3 * i_out
    
    # Inductancia
    f_hz = freq_khz * 1000
    L_henrios = (v_in - v_out) * D / (delta_i_L * f_hz)
    L_microhenrios = L_henrios * 1e6
    
    # Capacitor de salida (para ripple de voltaje <50mV)
    delta_v_ripple = 0.05  # 50 mV
    C_faradios = delta_i_L / (8 * f_hz * delta_v_ripple)
    C_microfaradios = C_faradios * 1e6
    
    # Diodo/MOSFET de free-wheeling
    v_diodo_min = v_in * 1.5
    i_diodo_avg = i_out * (1 - D)
    
    return {
        'duty_cycle': D * 100,
        'inductancia_uH': L_microhenrios,
        'capacitor_uF': C_microfaradios,
        'diodo_specs': {
            'v_reverso_min': v_diodo_min,
            'i_avg': i_diodo_avg
        }
    }

# Ejemplo: 12V → 5V, 2A
specs = diseñar_buck_converter(12, 5, 2.0, freq_khz=100)
print(f"Duty Cycle: {specs['duty_cycle']:.1f}%")
print(f"Inductancia: {specs['inductancia_uH']:.1f} µH (usar 47µH o 100µH estándar)")
print(f"Capacitor: {specs['capacitor_uF']:.1f} µF (usar 100µF electrolítico + 0.1µF cerámico)")
```

**Módulos Buck/Boost comerciales**:
- **LM2596** (Buck): 3-40V in → 1.5-35V out, 3A
- **XL4015** (Buck): 8-36V in → 1.25-32V out, 5A
- **MT3608** (Boost): 2-24V in → 5-28V out, 2A
- **LTC3780** (Buck-Boost): 5-32V in → 1-30V out, 10A

### 3.2 Baterías para robótica

#### 3.2.1 Tipos de baterías

**Comparativa**:

| Tipo | Voltaje nominal | Densidad energía (Wh/kg) | C-rate típico | Ciclos | Seguridad | Costo |
|------|----------------|--------------------------|---------------|--------|-----------|-------|
| **Li-Po** | 3.7V/celda | 150-200 | 20-30C | 300-500 | Peligro | $$ |
| **Li-Ion 18650** | 3.7V/celda | 150-250 | 1-3C | 500-1000 | Moderado | $$ |
| **LiFePO4** | 3.2V/celda | 90-120 | 3-5C | 2000-5000 | Alta | $$$ |
| **NiMH** | 1.2V/celda | 60-80 | 1-2C | 500-1000 | Alta | $ |
| **Lead-Acid** | 2V/celda | 30-50 | 0.2C | 200-300 | Alta | $ |

**Nomenclatura LiPo**:
- **3S**: 3 celdas en serie → 11.1V nominal (12.6V cargada)
- **2200mAh**: Capacidad (carga almacenada)
- **25C**: Tasa de descarga → Corriente máxima = 2.2A × 25 = 55A

#### 3.2.2 Battery Management System (BMS)

**Funciones críticas**:
1. **Balanceo de celdas**: Igualar carga entre celdas
2. **Protección sobre-carga**: Vcell_max = 4.2V
3. **Protección sobre-descarga**: Vcell_min = 3.0V (2.7V absoluto)
4. **Protección sobre-corriente**: Limitar picos
5. **Protección sobre-temperatura**: Desconectar si T > 60°C

**Implementación de monitor de batería**:

```python
import time

class BatteryMonitor:
    """Sistema de monitoreo de batería LiPo"""
    
    def __init__(self, n_cells=3, capacity_mah=5000):
        self.n_cells = n_cells
        self.capacity_mah = capacity_mah
        self.v_cell_min = 3.0
        self.v_cell_max = 4.2
        self.v_cell_nominal = 3.7
        self.v_cell_storage = 3.8
        
        # Estado
        self.cell_voltages = [self.v_cell_nominal] * n_cells
        self.current_ma = 0
        self.temperature_c = 25
    
    def update_cell_voltages(self, voltages):
        """Actualiza voltajes de celdas"""
        if len(voltages) != self.n_cells:
            raise ValueError(f"Se esperaban {self.n_cells} voltajes")
        self.cell_voltages = voltages
    
    def get_total_voltage(self):
        """Voltaje total del pack"""
        return sum(self.cell_voltages)
    
    def get_charge_percentage(self):
        """Estima porcentaje de carga basado en voltaje"""
        avg_voltage = sum(self.cell_voltages) / self.n_cells
        
        # Curva simplificada de descarga LiPo
        if avg_voltage >= 4.2:
            return 100
        elif avg_voltage >= 3.7:
            return 50 + (avg_voltage - 3.7) * 100
        elif avg_voltage >= 3.0:
            return (avg_voltage - 3.0) / 0.7 * 50
        else:
            return 0
    
    def check_health(self):
        """Verifica estado de salud de la batería"""
        warnings = []
        critical = []
        
        # Chequear voltajes individuales
        for i, v in enumerate(self.cell_voltages):
            if v < self.v_cell_min:
                critical.append(f"Celda {i+1}: Sobre-descargada ({v:.2f}V)")
            elif v < 3.3:
                warnings.append(f"Celda {i+1}: Batería baja ({v:.2f}V)")
            elif v > self.v_cell_max:
                critical.append(f"Celda {i+1}: Sobre-cargada ({v:.2f}V)")
        
        # Chequear desbalance
        v_max = max(self.cell_voltages)
        v_min = min(self.cell_voltages)
        delta_v = v_max - v_min
        if delta_v > 0.1:
            warnings.append(f"Desbalance de celdas: {delta_v:.3f}V")
        
        # Chequear temperatura
        if self.temperature_c > 60:
            critical.append(f"Sobre-temperatura: {self.temperature_c}°C")
        elif self.temperature_c > 45:
            warnings.append(f"Temperatura elevada: {self.temperature_c}°C")
        
        return {
            'healthy': len(critical) == 0,
            'warnings': warnings,
            'critical': critical
        }
    
    def estimate_remaining_time(self, avg_current_ma):
        """Estima tiempo restante en minutos"""
        charge_pct = self.get_charge_percentage()
        remaining_mah = (charge_pct / 100) * self.capacity_mah
        
        if avg_current_ma > 0:
            hours = remaining_mah / avg_current_ma
            return hours * 60  # Convertir a minutos
        return float('inf')
    
    def should_return_to_dock(self, threshold_pct=20):
        """Decide si debe regresar a estación de carga"""
        return self.get_charge_percentage() < threshold_pct

# Ejemplo de uso
bms = BatteryMonitor(n_cells=3, capacity_mah=5000)
bms.update_cell_voltages([3.85, 3.87, 3.82])  # Voltajes leídos
bms.current_ma = 1200  # Consumo actual
bms.temperature_c = 32

print(f"Voltaje total: {bms.get_total_voltage():.2f} V")
print(f"Carga: {bms.get_charge_percentage():.1f}%")
print(f"Tiempo restante: {bms.estimate_remaining_time(1200):.1f} min")

health = bms.check_health()
if not health['healthy']:
    print("CRÍTICO:", health['critical'])
if health['warnings']:
    print("Advertencias:", health['warnings'])
```

### 3.3 Distribución de energía

**Arquitectura típica para robot humanoide**:

```
Batería LiPo 3S (11.1V)
    │
    ├─→ BMS (protección y balanceo)
    │
    ├─→ Switch principal + fusible (20A)
    │
    ├─→ Buck 5V/3A → Raspberry Pi
    │   └─→ Decoupling: 470µF + 0.1µF
    │
    ├─→ Buck 6V/10A → Servomotores
    │   └─→ Bulk capacitor: 2200µF
    │
    ├─→ Buck 5V/1A → Sensores + Arduino
    │   └─→ Decoupling: 100µF + 0.1µF
    │
    └─→ Monitor de voltaje/corriente (INA219)
```

**Consejos de distribución**:
1. **Cables adecuados**: AWG según corriente
   - 22 AWG: hasta 5A
   - 18 AWG: hasta 10A
   - 14 AWG: hasta 20A
2. **Conectores robustos**: XT60, XT90, Deans para alta corriente
3. **Fusibles**: En cada rama principal
4. **Decoupling local**: Condensador cerca de cada IC
5. **Ground plane**: Retorno común robusto

## 4. Control de actuadores

### 4.1 Servomotores

**Tipos**:
1. **Servos analógicos**: Control PWM 50Hz, precisión ~1°
2. **Servos digitales**: Mayor torque, precisión, velocidad
3. **Servos de rotación continua**: Motor DC con encoder, control de velocidad

**Ejemplo de control multi-servo con PCA9685**:

```cpp
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150  // Pulso mínimo (aprox. 1ms)
#define SERVOMAX  600  // Pulso máximo (aprox. 2ms)

void setup() {
    pwm.begin();
    pwm.setPWMFreq(50);  // 50 Hz para servos
    delay(10);
}

void setServoAngle(uint8_t servo_num, uint8_t angulo) {
    // Convertir ángulo (0-180°) a pulso PWM
    uint16_t pulso = map(angulo, 0, 180, SERVOMIN, SERVOMAX);
    pwm.setPWM(servo_num, 0, pulso);
}

void loop() {
    // Ejemplo: barrido coordinado de 3 servos
    for (int angulo = 0; angulo <= 180; angulo += 5) {
        setServoAngle(0, angulo);           // Servo 0
        setServoAngle(1, 180 - angulo);     // Servo 1 (invertido)
        setServoAngle(2, angulo / 2);       // Servo 2 (mitad velocidad)
        delay(50);
    }
}
```

### 4.2 Motores DC y drivers

**Controladores H-Bridge**:
- **L298N**: Hasta 2A por canal, económico
- **L293D**: Hasta 600mA, integrado
- **DRV8833**: Hasta 1.5A, eficiente
- **VNH5019**: Hasta 12A, alta potencia
- **BTS7960**: Hasta 43A, muy alta potencia

**Control bidireccional con encoder**:

```cpp
// Pines
const int MOTOR_PWM = 9;
const int MOTOR_DIR = 8;
const int ENCODER_A = 2;  // Interrupción
const int ENCODER_B = 3;

volatile long encoder_count = 0;

void setup() {
    pinMode(MOTOR_PWM, OUTPUT);
    pinMode(MOTOR_DIR, OUTPUT);
    pinMode(ENCODER_A, INPUT_PULLUP);
    pinMode(ENCODER_B, INPUT_PULLUP);
    
    attachInterrupt(digitalPinToInterrupt(ENCODER_A), encoderISR, CHANGE);
    Serial.begin(115200);
}

void encoderISR() {
    // Leer estado de ambos canales
    bool A = digitalRead(ENCODER_A);
    bool B = digitalRead(ENCODER_B);
    
    // Determinar dirección (simplificado)
    if (A == B) {
        encoder_count++;
    } else {
        encoder_count--;
    }
}

void setMotor(int velocidad) {
    // velocidad: -255 a +255
    if (velocidad > 0) {
        digitalWrite(MOTOR_DIR, HIGH);
        analogWrite(MOTOR_PWM, velocidad);
    } else {
        digitalWrite(MOTOR_DIR, LOW);
        analogWrite(MOTOR_PWM, -velocidad);
    }
}

void loop() {
    // Control simple P (proporcional)
    long target_position = 1000;  // Pulsos de encoder
    long error = target_position - encoder_count;
    
    float Kp = 0.5;
    int control = Kp * error;
    control = constrain(control, -255, 255);
    
    setMotor(control);
    
    Serial.print("Pos: ");
    Serial.print(encoder_count);
    Serial.print(" Error: ");
    Serial.println(error);
    
    delay(10);
}
```

## 5. Diseño de PCBs

### 5.1 Software de diseño

**Opciones**:
- **KiCad**: Open-source, profesional, gratuito
- **Eagle**: (Autodesk), versión gratuita limitada
- **EasyEDA**: Web-based, integración con JLCPCB
- **Altium Designer**: Profesional, costoso

### 5.2 Reglas de diseño (design rules)

**Anchos de pistas según corriente** (cobre 1 oz/ft², 35µm):

| Corriente | Ancho mínimo (externa) | Ancho mínimo (interna) |
|-----------|----------------------|----------------------|
| 0.5 A | 0.3 mm (12 mil) | 0.5 mm (20 mil) |
| 1 A | 0.6 mm (24 mil) | 1.0 mm (40 mil) |
| 2 A | 1.2 mm (47 mil) | 2.0 mm (80 mil) |
| 3 A | 1.8 mm (71 mil) | 3.0 mm (120 mil) |
| 5 A | 3.0 mm (118 mil) | 5.0 mm (197 mil) |

**Separación (clearance)**:
- Señales baja tensión (<50V): 0.2 mm (8 mil)
- Líneas de potencia: 0.5 mm (20 mil)
- Alta tensión (>100V): 1 mm+ según normativas

**Vías (vias)**:
- Diámetro taladro: 0.3-0.8 mm típico
- Diámetro pad: Taladro + 0.3 mm
- Corriente por vía: ~1A (depende del plateado)

### 5.3 Best practices

1. **Ground planes**: Usar GND como plano continuo
2. **Decoupling**: Capacitor cerca (< 5mm) de cada IC
3. **Routing crítico**: Señales de alta frecuencia cortas y directas
4. **Señales diferenciales**: Misma longitud, paralelas
5. **Protección ESD**: Diodos TVS en entradas expuestas
6. **Testpoints**: Para debugging y calibración

## 6. Seguridad eléctrica

### 6.1 Riesgos y protecciones

**Sobrecorriente**: Fusibles, breakers, PTC resettables
**Sobrevoltaje**: Diodos Zener, TVS, varistores (MOV)
**Polaridad inversa**: Diodo serie, MOSFET P-channel
**Cortocircuito**: Current limiting, circuit breakers
**ESD**: Diodos TVS, ground straps, packaging antiestático

### 6.2 Checklists de seguridad

**Antes de energizar**:
- [ ] Verificar polaridad de batería
- [ ] Medir voltajes con multímetro
- [ ] Verificar continuidad de GND
- [ ] No hay cortocircuitos (resistencia >1kΩ entre VCC y GND)
- [ ] Fusibles instalados
- [ ] Emergency stop accesible

**Durante operación**:
- [ ] Monitorear temperatura de componentes
- [ ] Observar corrientes anormales
- [ ] Escuchar ruidos inusuales
- [ ] Verificar voltajes estables

## Referencias

### Libros
- "The Art of Electronics" - Horowitz & Hill
- "Practical Electronics for Inventors" - Scherz & Monk
- "Make: Electronics" - Charles Platt

### Recursos online
- Electronics-Tutorials.ws
- AllAboutCircuits.com
- Texas Instruments Application Notes
- Adafruit Learn

### Herramientas
- **Simuladores**: LTSpice, Proteus, TINA-TI
- **Calculadoras**: Digi-Key, Mouser, DigiCalc App
- **Datasheets**: Octopart, componentsearchengine.com

---

## Conclusión

El dominio de la electrónica es fundamental para la construcción exitosa de robots humanoides. La integración apropiada de microcontroladores, sensores, actuadores, alimentación y comunicaciones constituye el sistema nervioso del robot, permitiéndole percibir el entorno y ejecutar acciones coordinadas de manera confiable y segura.

**Próximo módulo**: [Programación y Control](../04_Planificacion_Control/) para implementar algoritmos de control que aprovechen el hardware electrónico.
