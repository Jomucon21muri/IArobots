# Percepción y visión - sentidos del robot humanoide

## Propósito

Este módulo implementa la **percepción multimodal** del robot humanoide, simulando los sentidos humanos mediante sensores y algoritmos de procesamiento. El objetivo es crear un sistema perceptivo completo que permita al robot entender e interactuar con su entorno de manera similar a un humano.

El sistema integra **visión computacional avanzada** como el sentido primario, complementado con otros sistemas sensoriales para crear una percepción multimodal robusta.


## PARTE I — Plan de Investigación (PI)

### 1. Antecedentes y contexto

La robótica inteligente tiene sus orígenes conceptuales en los años 50, cuando surgieron las primeras ideas sobre sistemas capaces de sustituir al ser humano en tareas rutinarias. Desde entonces, el reto de la ingeniería ha sido trasladar las capacidades sensoriales y cognitivas humanas a sistemas digitales: la capacidad de ver, analizar el entorno y moverse en él.

Uno de los puntos fundamentales de este proceso es la **visión**, que en los humanos es inmediata e intuitiva. Cuando observamos un entorno, lo captamos de forma global pero a la vez somos capaces de **focalizar en un objeto concreto** sin perder de vista el contexto. Esta dualidad —percepción global + atención selectiva— es precisamente el reto que se plantea en esta investigación.

En la actualidad, los robots procesan el entorno completo de manera indiscriminada. La propuesta es avanzar hacia sistemas que, como hacemos los humanos, sean capaces de seguir la ruta hacia un objetivo concreto mientras mantienen conciencia del entorno que les rodea.



### 2. Planteamiento del problema

Los robots de servicio actuales utilizan cámaras como sensores de visión, que capturan imágenes del entorno. Sin embargo, **el sensor por sí solo no es suficiente**: lo que realmente trabaja es el modelo de inteligencia artificial integrado, que analiza cada imagen y determina qué hay en el entorno y cómo actuar en consecuencia.

El problema se puede formular así:

> ¿Cómo diseñar un sistema de visión e IA que permita a un robot de servicio focalizar en su objetivo sin perder de vista el entorno completo, optimizando el procesamiento y la capacidad de reacción?

Los factores clave que condicionan este problema son:

- El **tipo de cámara** utilizada (ángulo de captura, resolución, profundidad).
- El **modelo de IA** responsable de interpretar lo que capta la cámara.
- La **capacidad de procesamiento** del hardware embebido en el robot.
- La diferencia entre procesar el entorno completo y **focalizar en un objetivo concreto**.



### 3. Objetivos de investigación

**Objetivo general:**  
Diseñar e implementar un sistema de visión basado en inteligencia artificial que permita a un robot de servicio detectar y seguir un objetivo concreto de forma eficiente, sin perder la percepción global del entorno.

**Objetivos específicos:**

1. Analizar los tipos de cámaras y sensores de visión disponibles, evaluando su compatibilidad con modelos de IA en tiempo real y su adecuación para distintos ángulos de captura y condiciones de entorno.

2. Estudiar los modelos de detección de objetos más utilizados en robótica (YOLO, SSD, Vision Transformers) y seleccionar el más adecuado para el caso de uso planteado.

3. Explorar los modelos de **aprendizaje por refuerzo** (*Reinforcement Learning*) aplicados al movimiento y toma de decisiones espaciales del robot, como mecanismo para aprender a moverse eficientemente hacia el objetivo.

4. Diseñar un pipeline que combine detección global del entorno con un módulo de atención que priorice el objetivo del robot.

5. Determinar los requisitos de hardware necesarios para ejecutar estos modelos en tiempo real sobre un robot de servicio.



### 4. Hipótesis de trabajo

La combinación de un modelo ligero de detección de objetos con un módulo de atención basado en aprendizaje por refuerzo permite a un robot de servicio gestionar simultáneamente la navegación general y la focalización en su objetivo, reduciendo la carga computacional frente al procesamiento indiscriminado del entorno completo.



### 5. Marco conceptual

#### 5.1 El sensor de visión: la cámara como entrada

La cámara actúa como los ojos del robot. Existen diferentes tipos según el caso de uso:

| Tipo de cámara | Características | Uso en robótica |
|---|---|---|
| Monocular (RGB) | Una sola lente, imagen 2D | Detección de objetos básica |
| Estéreo | Dos lentes, percepción de profundidad | Navegación con obstáculos |
| RGB-D (profundidad) | Imagen + distancia por infrarrojo | Manipulación y localización 3D |
| Ojo de pez / gran angular | Amplio ángulo de captura | Vigilancia y mapeo |

> El ángulo de captura y la resolución determinan cuánta información recibe el modelo, pero también cuánto tiene que procesar. Un ángulo demasiado amplio puede saturar el sistema; uno demasiado estrecho puede hacer que el robot pierda el contexto del entorno.

#### 5.2 El modelo de IA: lo que realmente interpreta el entorno

El sensor solo captura: el **modelo de IA es quien entiende** lo que hay en la imagen. Aquí entran en juego dos tipos de modelos fundamentales:

**Modelos de detección de objetos**  
Permiten identificar y localizar objetos dentro de una imagen. Los más utilizados en robótica en tiempo real son:

- **YOLO** (*You Only Look Once*): muy rápido, adecuado para procesamiento en tiempo real.
- **SSD** (*Single Shot Detector*): equilibrio entre velocidad y precisión.
- **Vision Transformers (ViT)**: mayor precisión, aunque requieren más recursos computacionales.

**Aprendizaje por refuerzo (Reinforcement Learning)**  
Es el mecanismo mediante el cual el robot aprende a tomar decisiones: qué camino seguir, cómo esquivar obstáculos, cómo llegar a su objetivo. Funciona mediante un sistema de recompensas: el robot "aprende" que ciertas acciones le acercan a su meta y otras lo alejan.

> El aprendizaje por refuerzo juega un papel fundamental en la robótica de servicio porque no es suficiente detectar objetos: el robot tiene que saber qué hacer con esa información, y hacerlo bien en entornos dinámicos.

#### 5.3 El reto de la atención dual

Los humanos observamos el entorno de forma global pero focalizamos en un objeto concreto. Los robots actuales procesan todo el entorno sin distinción, lo que supone una carga computacional elevada y ralentiza la toma de decisiones.

El reto de investigación consiste en implementar un mecanismo de **atención selectiva** que permita al robot:

- Mantener una percepción general del entorno (para evitar colisiones, detectar cambios).
- Focalizar el procesamiento intensivo sobre el objetivo concreto (para seguirlo, interactuar con él o alcanzarlo).



### 6. Metodología de investigación

| Fase | Descripción |
|---|---|
| **Fase 1 — Revisión del estado del arte** | Análisis de publicaciones sobre visión robótica, modelos de detección y RL aplicado a navegación. Fuentes: IEEE, arxiv.org (cs.RO, cs.CV). |
| **Fase 2 — Selección tecnológica** | Comparativa de cámaras y modelos de IA según criterios: latencia, precisión, consumo computacional y compatibilidad con hardware embebido. |
| **Fase 3 — Diseño del sistema** | Diseño del pipeline: visión → detección → atención selectiva → decisión → actuación. Esquema de integración con ROS2. |
| **Fase 4 — Implementación y pruebas** | Entrenamiento en simulador (Gazebo, Isaac Sim) y validación en hardware real. Métricas: precisión de detección, latencia, tasa de éxito en navegación. |



### 7. Variables de estudio

- **Variable independiente:** tipo de cámara y modelo de IA seleccionado.
- **Variable dependiente:** precisión de detección, latencia de procesamiento y eficacia del módulo de atención selectiva.
- **Variable de control:** entorno físico estandarizado, iluminación constante y distancia inicial al objetivo definida.



## PARTE II 

### 1. Justificación

Para llevar a cabo esta investigación con rigor técnico es necesario desarrollar competencias específicas que, partiendo de los fundamentos de la visión artificial, lleguen hasta la integración en hardware robótico real. El plan contempla una formación progresiva y aplicada, directamente vinculada a los objetivos del plan de investigación.



### 2. Competencias a desarrollar

#### Bloque A — Visión artificial y sensores
- Fundamentos de procesamiento de imágenes con **OpenCV**.
- Calibración de cámaras y corrección de distorsiones.
- Tipos de cámaras y selección según caso de uso (ángulo, profundidad, resolución).
- Introducción a la visión estéreo y cámaras RGB-D.

#### Bloque B — Inteligencia artificial aplicada a detección
- Redes neuronales convolucionales (CNN) para visión por computador.
- Implementación y ajuste de modelos **YOLO** para detección en tiempo real.
- *Transfer learning*: adaptar modelos preentrenados a nuevos entornos.
- Evaluación de modelos: métricas mAP, precisión, recall.

#### Bloque C — Aprendizaje por refuerzo para robótica
- Fundamentos de **Reinforcement Learning**: agente, entorno, recompensa, política.
- Algoritmos principales: PPO, DQN, SAC.
- Entrenamiento en simuladores robóticos: Gazebo, NVIDIA Isaac Gym.
- Diseño de funciones de recompensa para tareas de navegación y focalización.

#### Bloque D — Integración en sistemas robóticos
- **ROS2**: arquitectura de nodos, topics, servicios y comunicación entre módulos.
- Despliegue de modelos de IA en hardware embebido: NVIDIA Jetson, Raspberry Pi.
- Optimización de modelos para inferencia eficiente: **TensorRT**, ONNX.
- Integración del pipeline completo: cámara → modelo → decisión → actuación.



### 3. Itinerario formativo

| Módulo | Contenido | Recursos sugeridos |
|---|---|---|
| **Módulo 1** — Visión artificial | OpenCV, tipos de cámaras, calibración | Documentación oficial OpenCV, curso "Computer Vision" (Coursera - deeplearning.ai) |
| **Módulo 2** — Detección con IA | YOLO, transfer learning, evaluación de modelos | Ultralytics YOLO docs, fast.ai, Hugging Face Hub |
| **Módulo 3** — Aprendizaje por refuerzo | RL aplicado a navegación, simuladores | Gymnasium (OpenAI), Stable Baselines3, NVIDIA Isaac Gym |
| **Módulo 4** — Robótica integrada | ROS2, hardware embebido, optimización | ROS2 Humble docs, NVIDIA Jetson tutorials, TensorRT guide |



### 4. Indicadores de logro

Al finalizar el plan de formación, se habrán alcanzado los siguientes hitos:

1. Implementación funcional de un detector de objetos en tiempo real sobre vídeo en directo (latencia < 30 ms).
2. Agente de RL entrenado en simulador capaz de navegar hacia un objetivo con tasa de éxito superior al 80 %.
3. Integración del pipeline completo (cámara + modelo + ROS2) en hardware embebido con funcionamiento estable.
4. Documentación técnica del sistema desarrollado, incluyendo descripción del pipeline, resultados y conclusiones.


### 5. Relación entre formación e investigación

| Objetivo de investigación | Competencia formativa asociada |
|---|---|
| Analizar tipos de cámaras | Bloque A — Visión artificial y sensores |
| Seleccionar modelo de detección | Bloque B — IA aplicada a detección |
| Implementar módulo de atención (RL) | Bloque C — Aprendizaje por refuerzo |
| Diseñar pipeline de integración | Bloque D — Sistemas robóticos |
| Validar en hardware real | Bloque D — Hardware embebido y optimización |


*Documento generado en formato PIyPFP · Robótica Inteligente e Inteligencia Artificial*


---

## Visión general: los 7 sentidos robóticos

El robot humanoide integra los siguientes sistemas sensoriales:

| Sentido | Hardware | Software | Subcarpeta |
|---------|----------|----------|------------|
| **Visión** | Cámaras RGB + RGB-D | OpenCV, YOLO, ORB-SLAM | [`vision/`](#visión) |
| **Audición** | Micrófonos array | FFT, MFCC, Whisper, NLP | `sensores/audio/` |
| **Olfato** | Sensores de gas (MQ) | Clasificación ML | `sensores/chemical/` |
| **Gusto** | Biosensores químicos | Análisis de composición | `sensores/chemical/` |
| **Tacto** | Sensores hápticos/FSR | RNN, LSTM | `sensores/tactile/` |
| **Propiocepción** | IMU, encoders | Filtros Kalman, PID | `sensores/imu/` |
| **Equilibrio** | IMU, giroscopio | Control dinámico | Ver [04_Planificacion_Control](../04_Planificacion_Control/) |

---

## Estructura del directorio

```
02_Percepcion_Vision/
├── README.md (este archivo)
│
├── vision/                         # Sistema visual completo
│   ├── detection/                 # Detección de objetos (YOLO, Faster R-CNN)
│   ├── segmentation/              # Segmentación semántica/instancia
│   ├── face_recognition/          # Reconocimiento facial
│   ├── pose_estimation/           # Estimación de pose humana
│   ├── slam/                      # SLAM Visual (ORB-SLAM3)
│   ├── depth/                     # Percepción de profundidad (RGB-D, estéreo)
│   ├── tracking/                  # Seguimiento de objetos (DeepSORT)
│   ├── gestures/                  # Reconocimiento de gestos
│   ├── ocr/                       # Reconocimiento de texto
│   └── models/                    # Modelos entrenados
│
├── sensores/                       # Drivers y procesamiento de sensores
│   ├── cameras/                   # Cámaras RGB y RGB-D
│   ├── audio/                     # Micrófonos y arrays
│   ├── chemical/                  # Sensores de gas y químicos
│   ├── tactile/                   # Sensores de fuerza y presión
│   ├── imu/                       # IMU, giroscopios, acelerómetros
│   └── temperature/               # Sensores de temperatura
│
├── fusion/                         # Fusión sensorial multimodal
│   ├── ekf/                       # Extended Kalman Filter
│   ├── ukf/                       # Unscented Kalman Filter
│   ├── complementary/             # Filtros complementarios
│   └── multimodal/                # Fusión de múltiples modalidades
│
├── preprocessing/                  # Preprocesamiento de señales
│   ├── calibration/               # Calibración de sensores
│   ├── filtering/                 # Filtrado de ruido
│   ├── normalization/             # Normalización de datos
│   └── feature_extraction/        # Extracción de características
│
└── notebooks/                      # Notebooks de demostración
    ├── vision_detection.ipynb
    ├── face_recognition.ipynb
    ├── audio_processing.ipynb
    ├── sensor_fusion.ipynb
    └── multimodal_perception.ipynb
```

---

## Visión

### Capacidades del sistema visual

| Capacidad | Descripción | Tecnología Principal |
|-----------|-------------|---------------------|
| **Detección de objetos** | Identificar y localizar objetos | YOLO v8, Faster R-CNN |
| **Segmentación** | Separar objetos por píxeles | Mask R-CNN, U-Net |
| **Reconocimiento facial** | Identificar y verificar personas | FaceNet, ArcFace |
| **Estimación de pose** | Detectar posiciones de personas | OpenPose, MediaPipe |
| **SLAM Visual** | Mapeo y localización simultáneos | ORB-SLAM3, RTAB-Map |
| **Percepción 3D** | Reconstrucción tridimensional | Estéreo, RGB-D |
| **Seguimiento** | Rastrear objetos en movimiento | SORT, DeepSORT |
| **Gestos** | Interpretar gestos humanos | MediaPipe, CNN |

### Hardware recomendado
- **Cámaras RGB**: Raspberry Pi Camera V2, Logitech C920
- **Cámaras de profundidad**: Intel RealSense D435i, Kinect v2
- **Estéreo**: Dual Pi Camera setup
- **Resolución**: Mínimo 720p @ 30fps

### Ejemplo: detección de objetos con YOLO

```python
from ultralytics import YOLO
import cv2

# Cargar modelo YOLO
model = YOLO('yolov8n.pt')

# Detectar objetos en tiempo real
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        results = model(frame, conf=0.5)
        annotated_frame = results[0].plot()
        cv2.imshow('Detección', annotated_frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## Audición

### Hardware
- **Micrófonos**: Array de 4-6 micrófonos para localización de fuentes
- **Interfaz**: USB (Blue Yeti) o I2S (MEMS)

### Software
```python
import librosa
import numpy as np
from transformers import pipeline

# Reconocimiento de voz con Whisper
recognizer = pipeline("automatic-speech-recognition", model="openai/whisper-base")
result = recognizer("audio.wav")
print(result['text'])
```

---

## Tacto

### Hardware
- **FSR (Force Sensitive Resistors)**: Sensores de presión
- **Sensores capacitivos**: Detección de contacto
- **Encoders**: Retroalimentación de posición

### Aplicaciones
- Agarre adaptativo de objetos
- Detección de colisiones
- Interacción segura con humanos

---

## Propiocepción y Equilibrio

### Hardware
- **IMU**: MPU6050, BNO055 (acelerómetro + giroscopio + magnetómetro)
- **Encoders**: En articulaciones para conocer ángulos

### Algoritmos
- **Filtro de Kalman**: Fusión de acelerómetro y giroscopio
- **Filtro Complementario**: Alternativa más ligera
- **PID**: Control de postura

---

## Conexiones con otros módulos

- **[03_Localizacion_Mapeo](../03_Localizacion_Mapeo/)**: Usa datos de visión y sensores para SLAM
- **[04_Planificacion_Control](../04_Planificacion_Control/)**: Recibe datos sensoriales para control
- **[05_Aprendizaje_IA](../05_Aprendizaje_IA/)**: Entrena modelos de reconocimiento visual
- **[00_Fundamentos](../00_Fundamentos/)**: Teoría de procesamiento de señales y visión

---

## Recursos

### Datasets de visión
- **COCO**: Common Objects in Context
- **ImageNet**: Clasificación de imágenes
- **KITTI**: Conducción autónoma y SLAM
- **LFW**: Labeled Faces in the Wild

### Librerías principales
```python
import cv2                      # OpenCV
from ultralytics import YOLO    # YOLO v8
import torch
from torchvision import models
import pyrealsense2 as rs       # Intel RealSense
import librosa                  # Audio processing
import mediapipe as mp          # Pose/hand tracking
```

---

## Próximos pasos

1. Implementar sistema de detección de objetos en tiempo real
2. Calibrar cámaras estéreo para percepción de profundidad
3. Integrar reconocimiento facial con base de datos
4. Desarrollar fusión sensorial multimodal
5. Optimizar para ejecución en hardware embebido (Jetson Nano/Xavier)
