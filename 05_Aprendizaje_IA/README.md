# Aprendizaje automático y IA - robot humanoide

## Propósito

Implementar capacidades de inteligencia artificial en el robot humanoide, incluyendo reconocimiento de objetos, procesamiento de lenguaje natural, aprendizaje por refuerzo para control, y otras técnicas de ML/DL que permitan al robot percibir, aprender y mejorar sus capacidades.

## Área de conocimiento

Este módulo implementa el pilar 6: **Inteligencia Artificial y Aprendizaje Automático** (ver [recursos_conocimientos.md](../01_Proyecto/recursos_conocimientos.md)).


## PARTE I — Plan de Investigación (PI)

### 1. Antecedentes y contexto

Los tres módulos anteriores dotan al robot de percepción visual, orientación espacial y capacidad de movimiento. Sin embargo, un robot que solo ejecuta lo que se le programa explícitamente tiene un techo claro: no aprende, no se adapta y no mejora con la experiencia. Este módulo aborda el salto cualitativo que convierte un sistema robótico automatizado en un sistema verdaderamente **inteligente**.

La inteligencia artificial aplicada a la robótica humanoide no es una capa añadida sobre el sistema: es el **eje transversal** que conecta y potencia todos los módulos anteriores. Desde el reconocimiento de objetos hasta la comprensión del lenguaje natural, desde el aprendizaje de nuevas habilidades de movimiento hasta la detección de situaciones anómalas, la IA es la capacidad que permite al robot **percibir, razonar, aprender y mejorar**.

Este módulo investiga cómo implementar estas capacidades de forma integrada en el robot humanoide, siguiendo una progresión que va desde los tipos de IA más básicos hasta los paradigmas más avanzados de aprendizaje profundo y aprendizaje por refuerzo.

---

### 2. Planteamiento del problema

Los robots humanoides actuales son capaces de ejecutar tareas predefinidas con precisión, pero presentan limitaciones significativas cuando el entorno cambia, cuando aparecen situaciones no previstas o cuando es necesario interactuar de forma natural con personas. Resolver estas limitaciones requiere integrar múltiples capacidades de IA:

- **Percepción inteligente:** no solo detectar objetos, sino reconocerlos, clasificarlos y entender su relevancia para la tarea.
- **Comprensión del lenguaje:** recibir instrucciones en lenguaje natural y generar respuestas coherentes.
- **Aprendizaje continuo:** mejorar el comportamiento del robot a partir de la experiencia acumulada.
- **Adaptación al entorno:** generalizar lo aprendido a situaciones nuevas sin necesidad de reprogramación.

La pregunta de investigación central de este módulo es:

> ¿Cómo integrar de forma coordinada técnicas de aprendizaje supervisado, no supervisado y por refuerzo en un robot humanoide para dotarlo de capacidades de percepción inteligente, interacción en lenguaje natural y aprendizaje autónomo de habilidades motoras y cognitivas?

---

### 3. Objetivos de investigación

**Objetivo general:**  
Diseñar e implementar un sistema de inteligencia artificial integrado en el robot humanoide que cubra desde el reconocimiento de objetos y el procesamiento de lenguaje natural hasta el aprendizaje autónomo de habilidades de control y movimiento mediante técnicas de ML/DL y aprendizaje por refuerzo.

**Objetivos específicos:**

1. Analizar los distintos tipos de IA aplicables a robótica humanoide —IA reactiva, memoria limitada y teoría de la mente— y definir el nivel alcanzable en el contexto de este proyecto.

2. Investigar y seleccionar los paradigmas de aprendizaje automático más adecuados para cada subsistema del robot: supervisado para percepción, no supervisado para segmentación y detección de anomalías, y por refuerzo para control y navegación.

3. Estudiar las arquitecturas de redes neuronales profundas aplicadas al reconocimiento de objetos, procesamiento de imágenes y control motor, evaluando su viabilidad en hardware embebido.

4. Explorar los modelos de procesamiento de lenguaje natural (NLP/LLM) que permitan al robot recibir instrucciones verbales, mantener contexto conversacional y generar respuestas coherentes.

5. Implementar y validar algoritmos de aprendizaje por refuerzo —DQN, Policy Gradient, Actor-Critic— aplicados al control de locomoción y navegación autónoma del robot.

6. Diseñar una arquitectura de IA integrada que coordine los distintos módulos de aprendizaje y los conecte con los sistemas de visión, SLAM y control de los módulos anteriores.

---

### 4. Hipótesis de trabajo

La integración de un sistema de IA multicapa —que combine redes neuronales profundas para percepción, modelos de lenguaje para interacción y algoritmos Actor-Critic para control motor— permite al robot humanoide adaptarse a entornos y tareas no predefinidas, mejorando progresivamente su rendimiento sin necesidad de reprogramación explícita.

---

### 5. Marco conceptual

#### 5.1 Tipos de IA: niveles de capacidad cognitiva

No toda la IA es igual en cuanto a su nivel de sofisticación cognitiva. Para el robot humanoide se pueden identificar cuatro niveles progresivos:

| Nivel | Tipo de IA | Descripción | Estado en robótica actual |
|---|---|---|---|
| 1 | **IA reactiva** | Responde a estímulos sin memoria ni aprendizaje | Implementado y maduro |
| 2 | **Memoria limitada** | Usa experiencia reciente para mejorar decisiones | Implementado en la mayoría de sistemas avanzados |
| 3 | **Teoría de la mente** | Comprende emociones, intenciones y estados de otros | En investigación activa — objetivo de este proyecto |
| 4 | **Autoconciencia** | Conciencia propia y comprensión de sí mismo | Horizonte a largo plazo, no abordable actualmente |

> El objetivo realista de este proyecto es implementar un sistema de **memoria limitada** robusto y explorar los primeros pasos hacia la **teoría de la mente**, especialmente en lo que respecta a la comprensión de intenciones humanas en entornos de interacción.

---

#### 5.2 Aprendizaje automático: los tres paradigmas

##### 5.2.1 Aprendizaje supervisado

El robot aprende a partir de ejemplos etiquetados: se le muestra una entrada y la salida correcta esperada, y aprende a generalizar esa relación a nuevas entradas.

**Clasificación** — determinar a qué categoría pertenece una entrada:

- **SVM** (*Support Vector Machine*): eficaz para problemas de clasificación binaria con datos bien separables; útil para clasificación rápida de objetos simples.
- **Random Forest**: conjunto de árboles de decisión; robusto ante datos ruidosos y fácil de interpretar.
- **Redes neuronales**: la opción más potente para clasificación en imágenes y señales complejas.

**Regresión** — predecir un valor continuo:

- **Regresión lineal / polinomial**: modelos simples para relaciones directas entre variables.
- **Redes neuronales para regresión**: predicción de posiciones articulares, velocidades, fuerzas de contacto.

Aplicaciones en el robot humanoide: reconocimiento de objetos, clasificación de gestos, predicción de trayectorias.

---

##### 5.2.2 Aprendizaje no supervisado

El robot aprende estructura a partir de datos sin etiquetas, descubriendo patrones por sí mismo.

**Clustering** — agrupar datos similares sin categorías predefinidas:

- **K-means**: agrupa puntos en K grupos según distancia al centroide; útil para segmentación de nubes de puntos.
- **DBSCAN**: detecta grupos de forma arbitraria e identifica puntos atípicos; especialmente útil para segmentación de escenas 3D.
- **Clustering jerárquico**: construye una jerarquía de grupos; útil cuando no se conoce el número de categorías a priori.

**Reducción de dimensionalidad** — simplificar representaciones complejas:

- **PCA** (*Principal Component Analysis*): extrae las dimensiones de mayor varianza; reduce la carga computacional de datos sensoriales complejos.
- **t-SNE**: visualización de datos de alta dimensión en 2D/3D; útil para analizar representaciones internas de redes neuronales.

Aplicaciones en el robot humanoide: segmentación de escenas, detección de anomalías en comportamiento del robot, compresión de representaciones sensoriales.

---

##### 5.2.3 Aprendizaje por refuerzo

Es el paradigma más directamente ligado al control robótico autónomo. El robot aprende a través de la interacción con el entorno: ejecuta acciones, recibe recompensas o penalizaciones, y ajusta su política de comportamiento para maximizar la recompensa acumulada a largo plazo.

**Q-Learning**  
Algoritmo tabular que aprende el valor de cada par (estado, acción). Adecuado para espacios de estados discretos y pequeños. Base conceptual para entender los algoritmos más avanzados.

**Deep Q-Networks (DQN)**  
Extiende Q-Learning usando una red neuronal profunda para aproximar la función de valor Q en espacios de estados continuos y de alta dimensión. Permitió por primera vez aplicar RL a tareas con entrada visual directa.

**Policy Gradient**  
En lugar de aprender el valor de las acciones, aprende directamente la política: qué probabilidad asignar a cada acción en cada estado. Más adecuado para espacios de acción continuos, como el control articular de un robot.

**Actor-Critic**  
Combina las ventajas de Policy Gradient y Q-Learning: el **actor** aprende la política (qué hacer) y el **crítico** aprende a evaluar las acciones (qué tan buena es la decisión tomada). Es el paradigma más utilizado actualmente en control robótico avanzado. Variantes modernas: PPO (*Proximal Policy Optimization*), SAC (*Soft Actor-Critic*).

| Algoritmo | Espacio de estados | Espacio de acciones | Uso principal en robótica |
|---|---|---|---|
| Q-Learning | Discreto, pequeño | Discreto | Aprendizaje conceptual, entornos simples |
| DQN | Continuo (con red neuronal) | Discreto | Navegación con entrada visual |
| Policy Gradient | Continuo | Continuo | Control articular básico |
| Actor-Critic (PPO, SAC) | Continuo | Continuo | Locomoción, manipulación, control avanzado |

---

#### 5.3 Redes neuronales profundas aplicadas al robot

Las redes neuronales son el componente tecnológico central de la IA moderna en robótica. Según el tipo de dato y tarea, se utilizan arquitecturas distintas:

**CNN** (*Convolutional Neural Networks*)  
Diseñadas para procesamiento de imágenes. Extraen características visuales de forma jerárquica: bordes → formas → objetos. Son la base de los sistemas de reconocimiento de objetos como YOLO (Módulo 1).

**RNN / LSTM** (*Recurrent Neural Networks / Long Short-Term Memory*)  
Diseñadas para datos secuenciales. Mantienen memoria a lo largo del tiempo. Aplicaciones: comprensión de secuencias de movimiento, procesamiento de texto e instrucciones verbales.

**Transformer**  
Arquitectura dominante en procesamiento de lenguaje natural y, cada vez más, en visión y control robótico. Permite capturar dependencias a largo plazo mediante mecanismos de atención. Base de los modelos de lenguaje grandes (LLM).

**GNN** (*Graph Neural Networks*)  
Procesan datos estructurados como grafos. Útiles para representar relaciones entre objetos del entorno, partes del robot o secuencias de acciones.

---

#### 5.4 Procesamiento de lenguaje natural (NLP) para interacción humano-robot

Para que el robot pueda recibir instrucciones en lenguaje natural y responder de forma coherente, es necesario integrar un módulo de NLP. Las capacidades requeridas son:

- **Reconocimiento de voz** (*ASR — Automatic Speech Recognition*): convertir voz en texto. Herramientas: Whisper (OpenAI), Vosk.
- **Comprensión del lenguaje** (*NLU — Natural Language Understanding*): extraer la intención y las entidades de un texto. Ejemplo: "lleva el vaso a la mesa" → acción: llevar; objeto: vaso; destino: mesa.
- **Generación de respuestas** (*NLG — Natural Language Generation*): producir respuestas coherentes y contextuales. Herramientas: modelos LLM ligeros adaptados a ejecución en dispositivo.
- **Gestión del diálogo**: mantener el contexto de una conversación multi-turno para instrucciones encadenadas.

---

#### 5.5 Arquitectura de IA integrada

La arquitectura de IA del robot combina todos los paradigmas anteriores en una estructura coordinada:

```
Entrada sensorial (cámara, micrófono, encoders, LiDAR)
         ↓
[Percepción]    CNN → reconocimiento de objetos y escenas
[Lenguaje]      ASR + Transformer → comprensión de instrucciones
         ↓
[Razonamiento]  LLM ligero / árbol de comportamiento → planificación de tarea
         ↓
[Aprendizaje]   Actor-Critic (PPO/SAC) → política de control motor
         ↓
[Control]       Módulo 3 → planificación de trayectorias + PID
         ↓
Actuadores
```

---

### 6. Metodología de investigación

| Fase | Descripción |
|---|---|
| **Fase 1 — Revisión del estado del arte** | Análisis de arquitecturas de IA para robótica humanoide, modelos de RL para control motor y sistemas NLP para interacción humano-robot. Fuentes: NeurIPS, ICML, ICRA, arxiv. |
| **Fase 2 — Selección de modelos** | Evaluación y selección de modelos de reconocimiento de objetos, NLP y RL según restricciones de hardware (latencia, memoria, consumo). |
| **Fase 3 — Implementación por subsistemas** | Desarrollo independiente de cada módulo de IA: reconocimiento de objetos, NLP, RL para control. Validación unitaria de cada componente. |
| **Fase 4 — Entrenamiento y evaluación** | Entrenamiento de modelos en simulador (Isaac Gym) y en datos reales. Evaluación con métricas específicas por módulo. |
| **Fase 5 — Integración y validación** | Conexión de todos los módulos de IA con los sistemas de visión, SLAM y control. Validación del sistema completo en escenarios de interacción real. |

---

### 7. Variables de estudio

- **Variable independiente:** algoritmo de RL seleccionado (DQN vs. PPO vs. SAC) y arquitectura de red neuronal utilizada.
- **Variable dependiente:** tasa de éxito en la tarea, recompensa acumulada, precisión de reconocimiento de objetos y comprensión de instrucciones en lenguaje natural.
- **Variable de control:** conjunto de tareas de evaluación estandarizado, mismo entorno de simulación y misma cantidad de pasos de entrenamiento para comparaciones entre algoritmos.

---

## PARTE II — Plan de Formación Personal (PFP)

### 1. Justificación

Este módulo representa la mayor amplitud conceptual del proyecto: cubre desde los fundamentos del aprendizaje automático hasta arquitecturas avanzadas de deep learning, RL y NLP. La formación está organizada para construir conocimiento de forma progresiva, partiendo de los conceptos matemáticos necesarios y avanzando hacia la implementación práctica de cada paradigma, con especial atención a su aplicación directa en el robot humanoide.

---

### 2. Competencias a desarrollar

#### Bloque A — Fundamentos matemáticos de ML
- Álgebra lineal aplicada: vectores, matrices, productos escalares, descomposición SVD.
- Probabilidad y estadística: distribuciones, esperanza, varianza, regla de Bayes.
- Cálculo para optimización: gradiente, regla de la cadena, descenso de gradiente y variantes (SGD, Adam, RMSProp).
- Teoría de la información: entropía, entropía cruzada, divergencia KL.

#### Bloque B — Aprendizaje supervisado y no supervisado
- Implementación de clasificadores: SVM, Random Forest, redes neuronales simples con scikit-learn.
- Métricas de evaluación: precisión, recall, F1, AUC-ROC, matriz de confusión.
- Algoritmos de clustering: K-means, DBSCAN, evaluación con índice de silueta.
- Reducción de dimensionalidad: PCA, t-SNE, UMAP; interpretación y visualización.

#### Bloque C — Redes neuronales profundas (Deep Learning)
- Fundamentos de redes neuronales: perceptrón, retropropagación, funciones de activación.
- **CNN**: arquitecturas clásicas (ResNet, EfficientNet), implementación en PyTorch, *transfer learning*.
- **RNN / LSTM**: modelado de secuencias, aplicaciones en series temporales de sensores.
- **Transformers**: mecanismo de atención, arquitectura encoder-decoder, Vision Transformer (ViT).
- Herramientas: PyTorch, TensorFlow Lite para despliegue embebido, Hugging Face para modelos preentrenados.

#### Bloque D — Aprendizaje por refuerzo para robótica
- Fundamentos de RL: MDP, función de valor, política, ecuación de Bellman.
- Algoritmos tabulares: Q-Learning, SARSA.
- Deep RL: **DQN**, redes de experiencia de repetición, redes objetivo.
- Policy Gradient: REINFORCE, ventaja, **PPO** (*Proximal Policy Optimization*).
- Actor-Critic avanzado: **SAC** (*Soft Actor-Critic*), TD3; aplicaciones a control continuo.
- Entrenamiento en simuladores: **Isaac Gym**, Gymnasium, MuJoCo.

#### Bloque E — Procesamiento de lenguaje natural (NLP)
- Fundamentos de NLP: tokenización, embeddings (Word2Vec, GloVe, BERT).
- Modelos de lenguaje: arquitectura Transformer, modelos preentrenados (BERT, GPT, LLaMA).
- Reconocimiento de voz: **Whisper** (OpenAI), integración en tiempo real.
- NLU aplicado al robot: extracción de intención y entidades, frameworks Rasa, spaCy.
- Integración de LLM ligeros en hardware embebido: cuantización, GGUF, llama.cpp.

#### Bloque F — Integración de IA en ROS2 y hardware
- Despliegue de modelos de DL en hardware embebido: TensorRT, ONNX Runtime, optimización de inferencia.
- Integración de módulos de IA como nodos ROS2: publicación/suscripción de inferencias.
- Pipelines de datos para entrenamiento continuo: recolección, etiquetado, reentrenamiento.
- Evaluación y monitorización del sistema de IA en producción.

---

### 3. Itinerario formativo

| Módulo | Contenido | Recursos sugeridos |
|---|---|---|
| **Módulo 1** — Fundamentos matemáticos | Álgebra lineal, probabilidad, cálculo para ML | "Mathematics for Machine Learning" (Deisenroth) — acceso libre; 3Blue1Brown (YouTube) |
| **Módulo 2** — ML clásico | Supervisado, no supervisado, métricas | Coursera "Machine Learning" (Andrew Ng); scikit-learn docs |
| **Módulo 3** — Deep Learning | CNN, RNN, Transformers, PyTorch | fast.ai (curso práctico); "Deep Learning" (Goodfellow) — acceso libre |
| **Módulo 4** — Aprendizaje por refuerzo | Q-Learning, DQN, PPO, SAC, Isaac Gym | "Spinning Up in Deep RL" (OpenAI); Hugging Face Deep RL Course |
| **Módulo 5** — NLP y modelos de lenguaje | Transformers, Whisper, NLU, LLM embebido | Hugging Face NLP Course; llama.cpp docs; documentación Whisper |
| **Módulo 6** — Integración en ROS2 | TensorRT, nodos de IA en ROS2, monitorización | NVIDIA Isaac ROS docs; ros2 tutorials |

---

### 4. Indicadores de logro

Al finalizar el plan de formación, se habrán alcanzado los siguientes hitos:

1. Implementación de un clasificador de objetos basado en CNN con precisión superior al 90 % en el conjunto de prueba del entorno de trabajo del robot.
2. Agente Actor-Critic (PPO o SAC) entrenado en Isaac Gym capaz de ejecutar una tarea de locomoción o manipulación con tasa de éxito superior al 85 %.
3. Módulo NLP funcional que interprete instrucciones verbales en lenguaje natural y las traduzca en acciones ejecutables por el robot, con tasa de comprensión correcta superior al 80 % en el conjunto de prueba.
4. Integración de los módulos de IA (percepción + NLP + RL) como nodos ROS2 funcionando de forma coordinada en el sistema completo.
5. Documentación técnica del sistema de IA: arquitecturas empleadas, proceso de entrenamiento, métricas de evaluación y análisis de limitaciones.

---

### 5. Relación entre formación e investigación

| Objetivo de investigación | Competencia formativa asociada |
|---|---|
| Analizar tipos de IA y nivel alcanzable | Bloque A — Fundamentos + contexto conceptual |
| Seleccionar paradigmas ML por subsistema | Bloque B — ML supervisado y no supervisado |
| Estudiar arquitecturas de redes neuronales | Bloque C — Deep Learning |
| Explorar NLP para interacción humano-robot | Bloque E — NLP y modelos de lenguaje |
| Implementar RL para locomoción y navegación | Bloque D — Aprendizaje por refuerzo |
| Diseñar arquitectura de IA integrada | Bloque F — Integración en ROS2 y hardware |

---

### 6. Conexión con los módulos anteriores

Este módulo es el **eje transversal** del proyecto: no sustituye a los módulos anteriores sino que los potencia con capacidad de aprendizaje y adaptación.

- **Módulo 1 — Visión:** las CNN del Bloque C son la base de los modelos de detección de objetos. El RL del Bloque D permite mejorar la política de atención selectiva.
- **Módulo 2 — SLAM:** los algoritmos de clustering (Bloque B) se aplican a la segmentación de nubes de puntos. Los mapas semánticos se construyen integrando la percepción CNN con el mapa espacial.
- **Módulo 3 — Planificación y Control:** los algoritmos Actor-Critic (Bloque D) reemplazan o complementan los planificadores clásicos, aprendiendo políticas de movimiento directamente desde datos de experiencia.

La arquitectura completa del robot, con los cuatro módulos integrados:

```
Sensores (cámara + LiDAR + micrófono + encoders)
         ↓
[M1] Visión → CNN → detección y clasificación de objetos
[M2] SLAM  → localización + mapa semántico del entorno
[M4] NLP   → ASR + Transformer → comprensión de instrucciones
         ↓
[M4] Razonamiento → LLM / árbol de comportamiento → tarea a ejecutar
[M4] RL    → Actor-Critic → política de control aprendida
         ↓
[M3] Planificación de trayectorias (A* / Nav2)
[M3] Control (MPC + PID por articulación)
         ↓
Actuadores (motores, servos)
```

---

## Estructura del directorio

```
05_Aprendizaje_IA/
├── README.md (este archivo)
├── supervised/
│   ├── clasificacion/       # Clasificación de objetos, gestos
│   ├── deteccion/           # Detección de objetos (YOLO, SSD)
│   ├── segmentacion/        # Segmentación semántica
│   └── regresion/           # Predicción continua (pose estimation)
├── rl/
│   ├── entornos/            # Entornos de simulación (Gym, PyBullet)
│   ├── agentes/             # Implementaciones de agentes (PPO, SAC)
│   ├── politicas/           # Políticas entrenadas
│   └── experimentos/        # Logs, resultados de entrenamiento
├── nlp/
│   ├── speech_recognition/  # Reconocimiento de voz
│   ├── text_to_speech/      # Síntesis de voz
│   ├── nlu/                 # Natural Language Understanding
│   └── conversation/        # Manejo de diálogos
├── imitation/
│   ├── demonstrations/      # Datos de demostración humana
│   ├── behavioral_cloning/  # Clonación de comportamiento
│   └── inverse_rl/          # Reinforcement Learning inverso
├── vision/
│   ├── face_recognition/    # Reconocimiento facial
│   ├── pose_estimation/     # Estimación de pose humana
│   ├── gesture_recognition/ # Reconocimiento de gestos
│   └── tracking/            # Seguimiento de objetos
├── models/
│   ├── pretrained/          # Modelos pre-entrenados
│   ├── finetuned/           # Modelos fine-tuneados
│   └── custom/              # Modelos personalizados
├── datasets/
│   ├── coleccion/           # Scripts de recolección de datos
│   ├── procesamiento/       # Limpieza y augmentation
│   └── splits/              # Train/val/test splits
└── deployment/
    ├── optimization/        # Cuantización, pruning
    ├── inference/           # Código de inferencia
    └── edge/                # Optimización para edge (Jetson)
```

## Aplicaciones de IA en el robot humanoide

### 1. Percepción visual

**Reconocimiento de Objetos**:
- Identificar objetos del entorno
- Modelos: YOLO, EfficientDet
- Uso: Navegación, manipulación

**Reconocimiento Facial**:
- Identificar personas conocidas
- Modelos: FaceNet, ArcFace
- Uso: Interacción personalizada

**Estimación de Pose**:
- Detectar postura de humanos
- Modelos: OpenPose, MediaPipe
- Uso: Imitación de movimientos, interacción

**Ejemplo: Detección de objetos con YOLO**:
```python
import cv2
import torch

# Cargar modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image):
    """
    Detecta objetos en imagen usando YOLOv5
    
    Args:
        image: Imagen BGR de OpenCV
    
    Returns:
        results: Detecciones con bbox, clase, confianza
    """
    # Inferencia
    results = model(image)
    
    # Obtener detecciones
    detections = results.pandas().xyxy[0]
    
    return detections

# Uso con cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    detections = detect_objects(frame)
    
    # Dibujar resultados
    for _, det in detections.iterrows():
        x1, y1, x2, y2 = int(det['xmin']), int(det['ymin']), int(det['xmax']), int(det['ymax'])
        label = f"{det['name']} {det['confidence']:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow('Object Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### 2. Procesamiento de lenguaje natural

**Reconocimiento de Voz**:
```python
import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self, language='es-ES'):
        self.recognizer = sr.Recognizer()
        self.language = language
    
    def listen(self, timeout=5):
        """
        Escucha y transcribe comando de voz
        
        Returns:
            str: Texto transcrito o None si falla
        """
        with sr.Microphone() as source:
            print("Escuchando...")
            
            # Ajustar ruido ambiente
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                text = self.recognizer.recognize_google(audio, language=self.language)
                print(f"Reconocido: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Timeout")
                return None
            except sr.UnknownValueError:
                print("No se pudo entender")
                return None
            except sr.RequestError as e:
                print(f"Error del servicio: {e}")
                return None

# Uso
vr = VoiceRecognizer()
command = vr.listen()

if command:
    # Procesar comando
    if "adelante" in command.lower():
        robot.move_forward()
    elif "atrás" in command.lower():
        robot.move_backward()
```

**Síntesis de Voz (TTS)**:
```python
import pyttsx3

class VoiceSynthesizer:
    def __init__(self, rate=150, volume=0.9):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Configurar voz en español si está disponible
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'spanish' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
    
    def speak(self, text):
        """
        Sintetiza y reproduce texto
        
        Args:
            text (str): Texto a hablar
        """
        print(f"Diciendo: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def speak_async(self, text):
        """Habla sin bloquear"""
        self.engine.say(text)
        self.engine.startLoop(False)
        self.engine.iterate()
        self.engine.endLoop()

# Uso
tts = VoiceSynthesizer()
tts.speak("Hola, soy un robot humanoide")
tts.speak("¿En qué puedo ayudarte?")
```

### 3. Aprendizaje por refuerzo

**Control de Locomoción**:
Entrenar al robot a caminar de forma estable usando RL.

```python
import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Crear entorno personalizado
class HumanoidWalkEnv(gym.Env):
    """
    Entorno de marcha para robot humanoide
    """
    def __init__(self):
        super(HumanoidWalkEnv, self).__init__()
        
        # Espacio de observación: posiciones articulares, velocidades, IMU
        self.observation_space = gym.spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(40,),  # Ejemplo
            dtype=np.float32
        )
        
        # Espacio de acción: torques/ángulos de articulaciones
        self.action_space = gym.spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(12,),  # 12 articulaciones principales
            dtype=np.float32
        )
        
        self.robot = None  # Conexión con simulador o robot real
    
    def reset(self):
        # Resetear robot a posición inicial
        state = self.robot.reset()
        return state
    
    def step(self, action):
        # Aplicar acción
        self.robot.apply_action(action)
        
        # Obtener nuevo estado
        state = self.robot.get_state()
        
        # Calcular recompensa
        reward = self._calculate_reward(state, action)
        
        # Verificar si terminó
        done = self._check_done(state)
        
        info = {}
        
        return state, reward, done, info
    
    def _calculate_reward(self, state, action):
        """
        Función de recompensa:
        - Avanzar hacia adelante: +
        - Mantener equilibrio: +
        - Consumo energético: -
        - Caída: - -
        """
        forward_velocity = state['velocity_x']
        height = state['torso_height']
        energy = np.sum(np.abs(action))
        
        reward = 0.0
        reward += forward_velocity * 10  # Incentivar avance
        reward += max(0, height - 0.8) * 5  # Mantener altura
        reward -= energy * 0.01  # Penalizar gasto energético
        
        if height < 0.5:  # Caída
            reward -= 100
        
        return reward
    
    def _check_done(self, state):
        """Terminar si se cae o alcanza objetivo"""
        if state['torso_height'] < 0.5:
            return True
        if state['position_x'] > 10.0:  # Meta
            return True
        return False

# Entrenamiento
env = make_vec_env(HumanoidWalkEnv, n_envs=4)

# Crear agente PPO
model = PPO(
    'MlpPolicy',
    env,
    verbose=1,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    tensorboard_log="./logs/"
)

# Entrenar
model.learn(total_timesteps=1_000_000)

# Guardar modelo
model.save("humanoid_walk_ppo")

# Evaluar
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
```

### 4. Aprendizaje por imitación

**Clonación de Comportamiento**:
Aprender acciones a partir de demostraciones humanas (ej: gestos, manipulación).

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

class DemonstrationDataset(Dataset):
    """Dataset de demostraciones humanas"""
    def __init__(self, demonstrations):
        self.states = []
        self.actions = []
        
        for demo in demonstrations:
            self.states.extend(demo['states'])
            self.actions.extend(demo['actions'])
        
        self.states = torch.FloatTensor(self.states)
        self.actions = torch.FloatTensor(self.actions)
    
    def __len__(self):
        return len(self.states)
    
    def __getitem__(self, idx):
        return self.states[idx], self.actions[idx]

class BehavioralCloningNet(nn.Module):
    """Red para clonar comportamiento"""
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Tanh()  # Acciones [-1, 1]
        )
    
    def forward(self, state):
        return self.net(state)

# Cargar demostraciones
demonstrations = load_demonstrations('demos/wave_gesture.pkl')

# Crear dataset
dataset = DemonstrationDataset(demonstrations)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Crear modelo
model = BehavioralCloningNet(state_dim=40, action_dim=12)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Entrenar
for epoch in range(100):
    total_loss = 0
    for states, actions in dataloader:
        optimizer.zero_grad()
        
        pred_actions = model(states)
        loss = criterion(pred_actions, actions)
        
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch}: Loss = {avg_loss:.4f}")

# Guardar modelo
torch.save(model.state_dict(), 'models/wave_gesture_bc.pth')
```

## Optimización para edge deployment

**Cuantización de Modelos**:
Reducir tamaño y acelerar inferencia en Raspberry Pi / Jetson Nano.

```python
import torch
import torch.quantization

# Modelo entrenado
model = YourModel()
model.load_state_dict(torch.load('model.pth'))
model.eval()

# Cuantización dinámica (fácil, sin calibración)
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},  # Capas a cuantizar
    dtype=torch.qint8
)

# Guardar modelo cuantizado
torch.save(quantized_model.state_dict(), 'model_quantized.pth')

# Comparar tamaño
import os
original_size = os.path.getsize('model.pth') / 1024 / 1024
quantized_size = os.path.getsize('model_quantized.pth') / 1024 / 1024

print(f"Original: {original_size:.2f} MB")
print(f"Quantized: {quantized_size:.2f} MB")
print(f"Reducción: {(1 - quantized_size/original_size)*100:.1f}%")

# Inferencia
with torch.no_grad():
    output = quantized_model(input_tensor)
```

**TensorRT (para Nvidia Jetson)**:
```python
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit

# Convertir modelo PyTorch a ONNX
torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
)

# Convertir ONNX a TensorRT (optimizado para Jetson)
# Usar herramienta trtexec o Python API
```

## Métricas y evaluación

**Clasificación**:
- Accuracy, Precision, Recall, F1-Score
- Matriz de confusión

**Detección**:
- mAP (mean Average Precision)
- IoU (Intersection over Union)
- FPS (frames per second)

**RL**:
- Recompensa acumulada por episodio
- Tasa de éxito
- Número de pasos por episodio

**Ejemplo de evaluación**:
```python
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification(model, test_loader, class_names):
    """
    Evalúa modelo de clasificación
    """
    model.eval()
    
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    # Métricas
    accuracy = accuracy_score(all_labels, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(
        all_labels, all_preds, average='weighted'
    )
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    
    # Matriz de confusión
    cm = confusion_matrix(all_labels, all_preds)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    plt.show()

# Uso
evaluate_classification(model, test_loader, ['person', 'cup', 'book', ...])
```

## Datasets recomendados

**Visión**:
- **COCO**: Detección de objetos (80 clases)
- **ImageNet**: Clasificación (1000 clases)
- **MPII**: Estimación de pose humana
- **VoxCeleb**: Reconocimiento facial

**Manipulación**:
- **RoboNet**: Datos de robots manipuladores
- **MIME**: Interacción móvil de manipulación

**Lenguaje**:
- **Common Voice**: Voz en múltiples idiomas
- **LibriSpeech**: Speech recognition en inglés

**Custom**:
Recolectar datos propios del robot en operación.

## Herramientas y frameworks

**Deep Learning**:
- PyTorch, TensorFlow/Keras
- Hugging Face Transformers
- ONNX (interoperabilidad)

**RL**:
- Stable-Baselines3
- RLlib (Ray)
- OpenAI Gym

**Visión**:
- OpenCV
- Detectron2 (Facebook)
- MMDetection

**NLP**:
- spaCy, NLTK
- SpeechRecognition
- pyttsx3, gTTS

## Próximos pasos

1. **Configurar entorno** de desarrollo (Python, PyTorch)
2. **Recolectar datos** iniciales (imágenes desde cámara)
3. **Entrenar modelo simple** (clasificación de objetos)
4. **Desplegar en robot** y probar inferencia
5. **Iterar**: Mejorar datos, modelo, optimización

## Referencias

- "Deep Learning" - Goodfellow, Bengio, Courville
- "Reinforcement Learning: An Introduction" - Sutton & Barto
- Coursera: Deep Learning Specialization
- Fast.ai: Practical Deep Learning
- Papers With Code: State-of-the-art en AI

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