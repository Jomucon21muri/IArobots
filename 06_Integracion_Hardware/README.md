# Plan de Investigación y Plan de Formación Personal (PIyPFP)
## Integración de Hardware — El Núcleo Físico del Robot Humanoide

---

**Área temática:** Robótica Inteligente  
**Módulo:** 5 — Integración de Hardware, Mecatrónica y Sistemas de Energía  
**Conecta con:** Módulo 1 — Visión · Módulo 2 — SLAM · Módulo 3 — Planificación y Control · Módulo 4 — IA y ML  

---

## PARTE I — Plan de Investigación (PI)

### 1. Antecedentes y contexto

Los módulos anteriores han construido el sistema cognitivo del robot: percepción visual, orientación espacial, planificación de movimiento e inteligencia artificial. Sin embargo, toda esa inteligencia necesita un soporte físico sobre el que existir y actuar. Este módulo aborda el **núcleo físico del proyecto**: el diseño, fabricación e integración del hardware que hace posible que el robot exista como entidad real en el mundo.

La robótica humanoide plantea uno de los retos de ingeniería más complejos que existen: integrar en un único sistema físico las capacidades mecánicas, electrónicas y energéticas necesarias para que un conjunto de algoritmos se convierta en movimiento real, coordinado y seguro. A diferencia de los robots industriales, que operan en entornos controlados y estáticos, un robot humanoide debe funcionar en entornos diseñados para personas, lo que impone restricciones muy estrictas sobre su tamaño, peso, consumo energético y seguridad.

Este módulo investiga cómo diseñar e integrar los cinco pilares del hardware del robot: **mecánica y diseño estructural**, **electrónica y actuadores**, **mecatrónica** como disciplina integradora, **materiales y fabricación**, y **gestión de energía** como el metabolismo artificial del sistema.

---

### 2. Planteamiento del problema

Un robot humanoide funcional requiere resolver simultáneamente problemas de naturaleza muy distinta que deben estar perfectamente coordinados:

1. **¿Cómo estructurar el cuerpo del robot?** → Diseño mecánico con el número correcto de grados de libertad, materiales adecuados y articulaciones que soporten las cargas previstas.
2. **¿Cómo dotar al robot de percepción y actuación?** → Selección e integración de sensores, actuadores y el cerebro computacional que los coordina.
3. **¿Cómo fabricar las piezas necesarias?** → Combinación de impresión 3D, mecanizado y componentes comerciales para obtener un robot funcional con los medios disponibles.
4. **¿Cómo gestionar la energía de forma eficiente?** → Sistema de alimentación que garantice la autonomía necesaria distribuyendo la energía de forma segura a todos los subsistemas.
5. **¿Cómo garantizar la seguridad durante el desarrollo y uso?** → Protocolos y mecanismos de seguridad que protejan tanto al robot como a las personas en su entorno.

La pregunta de investigación central de este módulo es:

> ¿Cómo diseñar e integrar el hardware de un robot humanoide de 25-30 grados de libertad que combine un sistema mecánico eficiente, electrónica de control distribuida y gestión inteligente de energía, garantizando un funcionamiento seguro y autónomo durante 2-4 horas?

---

### 3. Objetivos de investigación

**Objetivo general:**  
Diseñar, fabricar e integrar el hardware completo del robot humanoide —incluyendo estructura mecánica, sistema electrónico, actuadores, sensores y gestión de energía— validando su funcionamiento como plataforma física capaz de soportar los sistemas de software desarrollados en los módulos anteriores.

**Objetivos específicos:**

1. Diseñar la arquitectura mecánica del robot humanoide definiendo los grados de libertad necesarios, la distribución de cargas y los materiales óptimos para cada componente estructural.

2. Seleccionar y caracterizar los actuadores (servomotores y motores DC) más adecuados para cada articulación, evaluando torque, protocolo de comunicación, consumo y fiabilidad.

3. Definir la arquitectura electrónica del sistema, incluyendo el cerebro computacional principal, los co-procesadores de control de bajo nivel y los protocolos de comunicación entre subsistemas.

4. Investigar y comparar las tecnologías de fabricación disponibles —impresión 3D, mecanizado CNC y componentes comerciales— para determinar la combinación óptima que garantice resistencia, precisión y coste razonable.

5. Diseñar el sistema de gestión de energía del robot, incluyendo la selección de baterías, distribución de voltajes, protección mediante BMS y monitoreo en tiempo real del consumo de cada subsistema.

6. Establecer protocolos de seguridad para las fases de fabricación, montaje y pruebas, incluyendo sistemas de parada de emergencia hardware y software.

---

### 4. Hipótesis de trabajo

Un robot humanoide de entre 25 y 30 grados de libertad construido con una estructura híbrida de aluminio 6061-T6 e impresión 3D, controlado mediante una arquitectura distribuida Raspberry Pi / STM32 y alimentado por una batería LiPo 3S con distribución regulada de voltaje, puede alcanzar una autonomía operativa de 2 a 4 horas con velocidad de respuesta inferior a 100 ms, siempre que el sistema de gestión de energía priorice dinámicamente los subsistemas según la tarea en ejecución.

---

### 5. Marco conceptual

#### 5.1 El cuerpo del robot: analogía con la anatomía humana

Al igual que el cuerpo humano combina un esqueleto rígido con articulaciones móviles, músculos actuadores, un sistema nervioso de comunicación y un sistema circulatorio de distribución de energía, el robot humanoide replica esta arquitectura en términos de ingeniería:

| Sistema biológico | Equivalente en el robot |
|---|---|
| Esqueleto | Estructura de aluminio y piezas impresas en 3D |
| Articulaciones | Rodamientos, bujes y servomotores |
| Músculos | Actuadores: servos digitales, motores DC brushless |
| Sistema nervioso | Red de comunicación: I2C, SPI, UART, CAN |
| Cerebro | Raspberry Pi 4 / Nvidia Jetson Nano |
| Reflejos | Co-procesador STM32 / Arduino para control de bajo nivel |
| Metabolismo | Sistema de baterías LiPo + BMS + reguladores Buck |

> Diseñar el hardware del robot es, en esencia, hacer ingeniería de un cuerpo artificial. Cada decisión de diseño —desde el material de una articulación hasta el protocolo de comunicación entre microcontroladores— tiene su equivalente en la evolución biológica: miles de millones de años optimizando la misma solución que nosotros intentamos replicar en meses.

---

#### 5.2 Sistema mecánico: grados de libertad y estructura

Los **grados de libertad** (DOF, *Degrees of Freedom*) determinan la capacidad de movimiento del robot. Cada DOF corresponde a un eje de rotación o traslación independiente. La distribución prevista para el robot humanoide es:

| Segmento | DOF | Movimientos |
|---|---|---|
| **Cabeza** | 2-3 | Pan (izquierda-derecha), Tilt (arriba-abajo), Roll (opcional) |
| **Cada brazo** | 6-7 | Hombro (3), Codo (1), Muñeca (2-3) |
| **Torso** | 1-3 | Flexión, rotación lateral |
| **Cada pierna** | 6 | Cadera (3), Rodilla (1), Tobillo (2) |
| **Total** | **25-30** | — |

La selección de materiales sigue una lógica de compromiso entre resistencia, peso y fabricabilidad:

- **Aluminio 6061-T6**: estructura principal y piezas sometidas a carga. Excelente relación resistencia/peso, mecanizable con CNC.
- **Fibra de carbono**: segmentos que requieren máxima rigidez con mínimo peso (opcional en versiones avanzadas).
- **PLA / ABS / PETG**: carcasas y piezas no estructurales fabricadas por impresión 3D.
- **Nylon y TPU**: piezas móviles que requieren cierta flexibilidad o resistencia al desgaste.
- **Rodamientos de bolas y bujes de bronce**: articulaciones que deben soportar cargas radiales con mínima fricción.

---

#### 5.3 Sistema electrónico: arquitectura distribuida

La electrónica del robot sigue una **arquitectura jerárquica distribuida** que refleja la del sistema nervioso: un cerebro central para el procesamiento de alto nivel y co-procesadores para el control reflejo de bajo nivel.

**Capa de procesamiento principal:**

- **Raspberry Pi 4 (8GB)** o **Nvidia Jetson Nano**: ejecuta ROS2, los módulos de IA, visión y SLAM. Es el nodo central de la arquitectura software.
- **Arduino Mega 2560 / STM32**: co-procesador para control de servos, lectura de sensores en tiempo real y bucles de control de bajo nivel. Opera a frecuencias más altas que el procesador principal.
- **ESP32**: módulo de comunicación WiFi y Bluetooth para telemetría, control remoto y comunicación con sistemas externos.

**Actuadores:**

Los servomotores son los músculos del robot. Se utilizan en dos categorías según la articulación:

| Tipo | Torque | Protocolo | Aplicación |
|---|---|---|---|
| Servos digitales estándar | 10-15 kg·cm | PWM | Articulaciones secundarias (muñeca, cabeza) |
| Servos digitales de alto torque | 20-25 kg·cm | PWM / UART | Articulaciones de carga (cadera, rodilla, hombro) |
| Dynamixel (serie AX/MX) | Variable | UART (TTL/RS485) | Articulaciones que requieren retroalimentación de posición |
| Motores DC brushless | — | PWM + ESC | Movilidad con ruedas (opcional) |

**Sensores:**

| Sensor | Modelo | Función |
|---|---|---|
| IMU | MPU6050 / BNO055 | Orientación, aceleración, fusión sensorial |
| Cámara | Raspberry Pi Camera v2 / webcam USB | Visión (Módulo 1) |
| Ultrasonido | HC-SR04 | Detección de obstáculos cercanos |
| Encoders | Magnéticos / ópticos | Posición precisa en articulaciones críticas |
| Sensores de fuerza | FSR (*Force Sensing Resistors*) | Contacto en pies y manos |
| Micrófono | USB / analógico | Reconocimiento de voz (Módulo 4 — NLP) |
| Monitor de corriente | INA219 | Monitoreo de consumo por subsistema |

---

#### 5.4 Protocolos de comunicación interna

La comunicación entre los distintos componentes electrónicos sigue una jerarquía de velocidad y distancia:

| Protocolo | Velocidad | Uso en el robot |
|---|---|---|
| **I2C** | Hasta 400 kHz | Sensores (IMU, INA219, displays) |
| **SPI** | Hasta 80 MHz | Comunicación de alta velocidad cuando I2C no es suficiente |
| **UART / TTL** | Variable | Servos avanzados Dynamixel, GPS, módulos de comunicación |
| **PWM** | — | Servos estándar (señal de posición 50Hz) |
| **CAN Bus** | Hasta 1 Mbps | Comunicación robusta entre controladores (entornos con ruido) |
| **WiFi / BT** | — | Telemetría externa, control remoto, conexión con ROS2 |

---

#### 5.5 Fabricación: combinación de tecnologías

El robot humanoide se fabrica combinando tres tecnologías complementarias:

**Impresión 3D**  
Principal tecnología de fabricación para carcasas, soportes y piezas no estructurales. Permite iterar diseños rápidamente sin coste de utillaje.

- **PLA**: fácil de imprimir, buena rigidez, adecuado para prototipos y piezas sin carga térmica.
- **ABS**: mayor resistencia al impacto y temperatura; requiere cámara cerrada y puede post-procesarse con acetona para sellado.
- **PETG**: equilibrio entre PLA y ABS; buena resistencia química y algo de flexibilidad.
- **TPU**: material flexible para amortiguadores, suelas de pies y elementos de contacto.

**Mecanizado CNC**  
Para piezas metálicas que requieren tolerancias ajustadas: soportes de articulaciones, ejes, chapas de aluminio estructurales. Se utilizan archivos G-code generados desde el modelo CAD.

**Componentes comerciales**  
Rodamientos, tornillería, perfiles de aluminio extruido (tipo Bosch Rexroth o similar), conectores y cableado. Reducen el tiempo de fabricación y garantizan tolerancias de calidad industrial.

---

#### 5.6 Sistema de energía: el metabolismo artificial del robot

El sistema de energía es el equivalente al metabolismo biológico: gestiona la **obtención, almacenamiento, distribución y optimización** de la energía para todos los subsistemas.

**Almacenamiento:**

- **Batería LiPo 3S (11.1V nominal, 12.6V cargada)** de 5000 mAh y descarga 20C.
- Proporciona la capacidad de corriente necesaria para los picos de los servomotores sin caída de tensión.
- Autonomía estimada: 2-4 horas en uso moderado.

**Gestión y protección (BMS):**

- El **BMS** (*Battery Management System*) protege la batería contra sobredescarga, sobrecarga, cortocircuitos y desequilibrio entre celdas.
- Componente de seguridad crítico: sin BMS, una LiPo puede inflamarse si se descarga por debajo del umbral mínimo (~3.0V por celda).

**Distribución regulada:**

Los distintos subsistemas requieren voltajes diferentes, obtenidos mediante reguladores Buck (convertidores DC-DC):

| Subsistema | Voltaje | Corriente máxima |
|---|---|---|
| Raspberry Pi, sensores | 5V | 3A |
| Servomotores | 6V | 10A |
| STM32 / Arduino | 3.3V / 5V | 1A |
| ESP32 | 3.3V | 0.5A |

**Monitoreo:**

- El **INA219** mide en tiempo real el voltaje, corriente y potencia consumida por cada ramal de distribución.
- Permite detectar consumos anómalos, estimar la autonomía restante y gestionar el apagado ordenado del sistema.

---

#### 5.7 Seguridad: protocolos obligatorios

La seguridad en un sistema físico con actuadores de alto torque operando cerca de personas no es opcional. Se establecen dos niveles de protección:

**Seguridad hardware:**
- **Botón de parada de emergencia (E-stop)** físico y accesible, que corta la alimentación de los actuadores de forma inmediata.
- Fusibles en cada ramal de distribución de potencia.
- Conectores de desconexión rápida en la batería.

**Seguridad software:**
- Límites de rango de movimiento implementados en firmware: el robot no puede girar una articulación más allá de sus límites físicos.
- Sistema de logging continuo para análisis post-fallo.
- Watchdog timer: si el sistema de control principal deja de responder, el co-procesador detiene todos los actuadores.

**Checklist obligatorio pre-prueba:**
- Verificar voltaje y conexiones de la batería.
- Comprobar que el E-stop es accesible y funcional.
- Inspeccionar cableado: sin cables sueltos o pelados.
- Verificar estructura: sin grietas ni piezas flojas.
- Confirmar que los límites de movimiento están configurados.
- Asegurar que el área de pruebas está despejada.
- Nunca dejar el robot operando sin supervisión.

---

### 6. Metodología de investigación

| Fase | Descripción |
|---|---|
| **Fase 1 — Diseño (meses 3-4)** | Modelado CAD completo en SolidWorks o Fusion 360. Validación de interferencias, rangos de movimiento y análisis de elementos finitos (FEA) en piezas críticas. Diseño del esquema eléctrico completo y cálculo de consumo energético. |
| **Fase 2 — Fabricación mecánica (meses 5-6)** | Impresión 3D de carcasas y soportes con perfiles y orientaciones optimizados. Mecanizado CNC de piezas metálicas estructurales. Ensamblaje mecánico verificando alineación de articulaciones e instalación de rodamientos. |
| **Fase 3 — Montaje electrónico (mes 6)** | Soldadura de PCB personalizados si los hay. Montaje de microcontroladores, sensores y actuadores. Cableado siguiendo diagrama de distribución, con etiquetado y gestión de cables. |
| **Fase 4 — Integración y pruebas (mes 6)** | Pruebas incrementales: primero alimentación sin motores, luego un actuador a la vez, después sensores, y finalmente el sistema completo. Calibración de IMU, encoders y servos. Validación de protocolos de seguridad. |
| **Fase 5 — Validación con software** | Integración del hardware con ROS2 y los módulos de IA, SLAM y control. Pruebas de estrés y validación de las especificaciones técnicas objetivo (autonomía, velocidad de respuesta, carga útil). |

---

### 7. Variables de estudio

- **Variable independiente:** combinación de materiales estructurales (aluminio vs. PLA reforzado), tipo de actuador (servo PWM estándar vs. Dynamixel con retroalimentación) y capacidad de la batería.
- **Variable dependiente:** autonomía operativa, tiempo de respuesta del sistema de control, precisión de posicionamiento articular y peso total del robot.
- **Variable de control:** configuración de 25-30 DOF fija, mismo entorno de pruebas, temperatura ambiente estable y mismo conjunto de tareas de evaluación para todas las configuraciones.

---

## PARTE II — Plan de Formación Personal (PFP)

### 1. Justificación

Este módulo es el más transversal del proyecto en términos de disciplinas involucradas: exige conocimientos de mecánica, diseño CAD, electrónica analógica y digital, programación de microcontroladores, gestión de energía y fabricación. La formación debe construir estas competencias de forma progresiva, partiendo del diseño conceptual y avanzando hasta la integración y validación del sistema completo en hardware real.

---

### 2. Competencias a desarrollar

#### Bloque A — Diseño mecánico y CAD
- Fundamentos de mecánica de sólidos: fuerzas, momentos, resistencia de materiales.
- Modelado 3D paramétrico con **Fusion 360** o **SolidWorks**: ensamblajes, restricciones, planos de fabricación.
- Análisis de interferencias y simulación cinemática en CAD.
- Análisis de elementos finitos (FEA) básico para validación de piezas críticas.
- Diseño de articulaciones: selección de rodamientos, tolerancias y ajustes.

#### Bloque B — Electrónica y microcontroladores
- Electrónica básica: ley de Ohm, divisores de tensión, filtros RC, lectura de datasheets.
- Microcontroladores: programación de **Arduino** (C/C++) y **STM32** (HAL/LL); GPIO, timers, interrupciones.
- Protocolos de comunicación: implementación práctica de **I2C, SPI, UART, PWM** en microcontrolador.
- Control de servomotores: señales PWM, protocolo Dynamixel, librerías de control.
- Diseño de PCB con **KiCad**: esquemático, layout, generación de Gerbers.

#### Bloque C — Integración sensorial
- Lectura e interpretación de IMU (MPU6050 / BNO055): acelerómetro, giróscopo, magnetómetro.
- Fusión sensorial: filtro complementario, filtro de Kalman para estimación de orientación.
- Integración de sensores de fuerza (FSR), encoders y sensores de corriente (INA219).
- Drivers de sensores en ROS2: publicación de datos sensoriales como topics.

#### Bloque D — Gestión de energía
- Tecnología de baterías LiPo: parámetros clave (C-rating, balance, voltaje nominal/por celda).
- Seguridad con LiPo: carga correcta, almacenamiento, manipulación y protección BMS.
- Diseño de sistemas de distribución de potencia: reguladores Buck, cálculo de disipación.
- Monitoreo de energía: lectura de INA219, estimación de autonomía, alertas de batería baja.

#### Bloque E — Fabricación y materiales
- Impresión 3D FDM: parámetros clave (relleno, orientación de capas, soportes, temperaturas por material).
- Post-procesado de piezas impresas: lijado, sellado con acetona (ABS), pintura.
- Fundamentos de mecanizado CNC: lectura de G-code, tolerancias, herramientas de corte.
- Selección de materiales para robótica: criterios de rigidez, peso, fatiga y coste.

#### Bloque F — Integración del sistema y seguridad
- Arquitectura de sistemas embebidos distribuidos: comunicación entre Raspberry Pi, STM32 y ESP32.
- Firmware para control de robots: bucles de control en tiempo real, gestión de interrupciones.
- Protocolos de seguridad hardware: diseño de circuitos E-stop, fusibles, protección de inversión de polaridad.
- Pruebas y validación de hardware: metodología incremental, registro de fallos, análisis post-fallo.

---

### 3. Itinerario formativo

| Módulo | Contenido | Recursos sugeridos |
|---|---|---|
| **Módulo 1** — Diseño mecánico | CAD con Fusion 360, FEA básico, diseño de articulaciones | Autodesk Fusion 360 Learning Hub (gratuito); canal "NYC CNC" (YouTube) |
| **Módulo 2** — Electrónica básica | Circuitos, ley de Ohm, componentes pasivos, lectura de datasheets | "The Art of Electronics" (Horowitz & Hill); Falstad Circuit Simulator (online, gratuito) |
| **Módulo 3** — Microcontroladores | Arduino, STM32, protocolos I2C/SPI/UART/PWM | Documentación oficial Arduino; STM32 HAL Reference Manual; canal "Phil's Lab" (YouTube) |
| **Módulo 4** — Servos y actuadores | Control PWM y Dynamixel, calibración, integración con ROS2 | Robotis Dynamixel SDK docs; tutoriales ros2_control |
| **Módulo 5** — Gestión de energía | LiPo, BMS, reguladores Buck, INA219 | Datasheet INA219 (Texas Instruments); "LiPo Battery Guide" (oscarliang.com) |
| **Módulo 6** — Fabricación 3D | FDM, materiales, post-procesado, parámetros de impresión | Documentación Prusa/Bambu; canal "CNC Kitchen" (YouTube) |
| **Módulo 7** — Integración y seguridad | Sistema completo, E-stop, pruebas incrementales, ROS2 | "Hardware Hacker" (Grand); tutoriales ROS2 Hardware Interface |

---

### 4. Indicadores de logro

Al finalizar el plan de formación, se habrán alcanzado los siguientes hitos:

1. Modelo CAD completo del robot en Fusion 360 o SolidWorks, con ensamblaje validado (sin interferencias), planos de fabricación generados y análisis FEA en al menos tres piezas críticas.
2. Prototipo electrónico funcional con Raspberry Pi + STM32 comunicados por UART, controlando al menos 5 servomotores y leyendo datos de IMU en tiempo real.
3. Sistema de distribución de energía operativo: batería LiPo con BMS, reguladores a 5V y 6V verificados, monitoreo de corriente con INA219 funcionando en tiempo real.
4. Al menos el 80 % de las piezas impresas en 3D superan las pruebas de carga definidas sin deformación ni rotura.
5. Sistema completo integrado con ROS2: sensores publicando topics, servos respondiendo a comandos de posición con latencia inferior a 100 ms y E-stop hardware validado.
6. Documentación técnica completa: BOM (*Bill of Materials*), esquemas eléctricos, guías de ensamblaje y protocolo de seguridad pre-prueba.

---

### 5. Relación entre formación e investigación

| Objetivo de investigación | Competencia formativa asociada |
|---|---|
| Diseñar arquitectura mecánica y DOF | Bloque A — Diseño mecánico y CAD |
| Seleccionar y caracterizar actuadores | Bloque B — Electrónica + Bloque C (drivers de actuadores) |
| Definir arquitectura electrónica distribuida | Bloque B — Microcontroladores + Bloque F — Integración |
| Comparar tecnologías de fabricación | Bloque E — Fabricación y materiales |
| Diseñar sistema de gestión de energía | Bloque D — Gestión de energía |
| Establecer protocolos de seguridad | Bloque F — Integración y seguridad |

---

### 6. Especificaciones técnicas objetivo

| Parámetro | Valor objetivo |
|---|---|
| Altura | 150-180 cm |
| Peso total | 8-15 kg |
| DOF total | 25-30 |
| Autonomía operativa | 2-4 horas (uso moderado) |
| Velocidad de marcha | 0.5-1.5 km/h |
| Carga útil por brazo | 0.5-2 kg |
| Tiempo de respuesta | < 100 ms |
| Conectividad | WiFi 2.4/5 GHz + Bluetooth 5.0 |

---

### 7. Conexión con los módulos anteriores

Este módulo es la **base física** sobre la que operan todos los demás. Sin hardware, los algoritmos no tienen cuerpo en el que existir. La integración con los módulos anteriores es directa:

- **Módulo 1 — Visión:** la Raspberry Pi Camera y los sensores de profundidad son componentes hardware de este módulo. Su montaje, cableado y alimentación se definen aquí.
- **Módulo 2 — SLAM:** el LiDAR o cámara RGB-D, los encoders de las ruedas/articulaciones y la IMU son sensores físicos cuya integración electrónica se documenta en este módulo.
- **Módulo 3 — Planificación y Control:** los servomotores, sus drivers y los controladores PID de bajo nivel se implementan en el firmware del STM32, desarrollado en este módulo.
- **Módulo 4 — IA y ML:** el procesador principal (Raspberry Pi / Jetson Nano) que ejecuta los modelos de IA es el componente central de la arquitectura hardware de este módulo.

La arquitectura completa del robot humanoide, con los cinco módulos integrados:

```
HARDWARE FÍSICO (Módulo 5)
  Sensores:  Cámara + LiDAR + IMU + Encoders + FSR + Micrófono
  Cerebro:   Raspberry Pi 4 / Jetson Nano
  Control:   STM32 / Arduino Mega
  Comms:     ESP32 (WiFi / BT)
  Energía:   LiPo 3S → BMS → Reguladores Buck → Subsistemas
         ↓
[M1] Visión          → CNN → detección de objetos
[M2] SLAM            → localización + mapa semántico
[M4] IA / NLP        → comprensión de instrucciones + RL
         ↓
[M3] Planificación   → A* / Nav2 → trayectoria óptima
[M3] Control         → MPC + PID por articulación
         ↓
ACTUADORES (Módulo 5)
  Servomotores digitales (25-30 unidades)
  Motores DC brushless (movilidad, opcional)
```

---

*Documento generado en formato PIyPFP · Módulo 5 — Integración de Hardware, Mecatrónica y Sistemas de Energía*


**Nota de Seguridad**: Este robot tiene componentes móviles y eléctricos. Siempre seguir procedimientos de seguridad. En caso de duda, DETENER y consultar.

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

---

**Última actualización**: Febrero 2026