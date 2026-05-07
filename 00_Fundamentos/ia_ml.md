# Fundamentos de inteligencia artificial y aprendizaje automático para robótica humanoide

## Resumen ejecutivo

La inteligencia artificial y el aprendizaje automático constituyen el cerebro cognitivo superior del robot humanoide, permitiéndole percibir, comprender, aprender y adaptarse a entornos complejos y dinámicos. Este documento presenta los fundamentos teóricos y prácticos necesarios para implement sistemas de IA en robótica a nivel doctoral, abarcando desde percepción visual hasta aprendizaje por refuerzo profundo.

## 1. Fundamentos de inteligencia artificial

### 1.1 Conceptos básicos de IA

**Definición**: La Inteligencia Artificial es la ciencia de hacer que las máquinas realicen tareas que requieren inteligencia cuando son realizadas por humanos.

**Categorías**:
1. **IA Débil (Estrecha)**: Especializada en tareas específicas (reconocimiento facial, juego de ajedrez)
2. **IA Fuerte (General)**: Inteligencia comparable a humanos en múltiples dominios (objetivo de investigación activa)

**Áreas relevantes para robótica humanoide**:
- Visión por computadora
- Procesamiento de lenguaje natural (NLP)
- Planificación y toma de decisiones
- Aprendizaje automático
- Razonamiento bajo incertidumbre

### 1.2 Representación del conocimiento

**Lógica proposicional y de primer orden**:
```python
# Ejemplo: Sistema experto simple para diagnóstico
class SistemaExpertoRobot:
    """Sistema basado en reglas para diagnóstico de estados"""
    
    def __init__(self):
        self.reglas = [
            {
                'condicion': lambda datos: datos['bateria'] < 20,
                'accion': 'regresar_base',
                'prioridad': 10
            },
            {
                'condicion': lambda datos: datos['temperatura'] > 60,
                'accion': 'detener_movimiento',
                'prioridad': 15
            },
            {
                'condicion': lambda datos: datos['obstaculo_distancia'] < 0.3,
                'accion': 'evitar_obstaculo',
                'prioridad': 8
            }
        ]
    
    def evaluar(self, datos_sensores):
        """Evalúa reglas y retorna acción de mayor prioridad"""
        acciones_activadas = []
        
        for regla in self.reglas:
            if regla['condicion'](datos_sensores):
                acciones_activadas.append((regla['accion'], regla['prioridad']))
        
        if acciones_activadas:
            # Ordenar por prioridad (mayor primero)
            acciones_activadas.sort(key=lambda x: x[1], reverse=True)
            return acciones_activadas[0][0]
        
        return 'continuar_normal'

# Uso
sistema = SistemaExpertoRobot()
datos = {'bateria': 15, 'temperatura': 45, 'obstaculo_distancia': 1.5}
accion = sistema.evaluar(datos)
print(f"Acción recomendada: {accion}")
```

### 1.3 Búsqueda y planificación

**Algoritmos de búsqueda fundamentales**:

```python
import heapq
from collections import deque

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo
    
    def __lt__(self, otro):
        return self.costo < otro.costo

def a_star(estado_inicial, estado_objetivo, heuristica, acciones_func, costo_func):
    """
    Algoritmo A* para planificación de trayectorias
    
    Args:
        estado_inicial: Estado de partida
        estado_objetivo: Estado objetivo
        heuristica: Función h(estado) → costo estimado al objetivo
        acciones_func: Función que retorna acciones posibles desde un estado
        costo_func: Función que retorna costo de una acción
    
    Returns:
        camino: Lista de acciones desde inicial a objetivo
    """
    frontera = []
    heapq.heappush(frontera, (0, Nodo(estado_inicial)))
    explorados = set()
    
    while frontera:
        _, nodo_actual = heapq.heappop(frontera)
        
        if nodo_actual.estado == estado_objetivo:
            # Reconstruir camino
            camino = []
            while nodo_actual.padre is not None:
                camino.append(nodo_actual.accion)
                nodo_actual = nodo_actual.padre
            return camino[::-1]
        
        explorados.add(nodo_actual.estado)
        
        for accion in acciones_func(nodo_actual.estado):
            nuevo_estado = aplicar_accion(nodo_actual.estado, accion)
            
            if nuevo_estado not in explorados:
                g = nodo_actual.costo + costo_func(accion)
                h = heuristica(nuevo_estado, estado_objetivo)
                f = g + h
                
                nuevo_nodo = Nodo(nuevo_estado, nodo_actual, accion, g)
                heapq.heappush(frontera, (f, nuevo_nodo))
    
    return None  # No se encontró camino

# Ejemplo: Planificación en grid 2D
def heuristica_manhattan(estado, objetivo):
    return abs(estado[0] - objetivo[0]) + abs(estado[1] - objetivo[1])

def acciones_grid(estado):
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Arriba, Derecha, Abajo, Izquierda

def aplicar_accion(estado, accion):
    return (estado[0] + accion[0], estado[1] + accion[1])

# Buscar camino de (0,0) a (5,5)
camino = a_star(
    estado_inicial=(0, 0),
    estado_objetivo=(5, 5),
    heuristica=heuristica_manhattan,
    acciones_func=acciones_grid,
    costo_func=lambda a: 1
)
print(f"Camino encontrado: {camino}")
```

## 2. Aprendizaje automático (machine learning)

### 2.1 Aprendizaje supervisado

**Regresión Lineal**:
$$\hat{y} = w^Tx + b$$

**Función de costo (MSE)**:
$$J(w,b) = \frac{1}{2m}\sum_{i=1}^m(\hat{y}^{(i)} - y^{(i)})^2$$

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Ejemplo: Predecir consumo de batería basado en velocidad de marcha
# Datos de entrenamiento (velocidad[m/s], consumo[mA])
datos_entrenamiento = np.array([
    [0.0, 500], [0.2, 800], [0.4, 1200], [0.6, 1650],
    [0.8, 2100], [1.0, 2600], [1.2, 3150], [1.4, 3700]
])

X = datos_entrenamiento[:, 0].reshape(-1, 1)  # Velocidad
y = datos_entrenamiento[:, 1]  # Consumo

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

print(f"Ecuación: Consumo = {modelo.coef_[0]:.2f} × Velocidad + {modelo.intercept_:.2f}")

# Predecir para nueva velocidad
velocidad_nueva = 0.7
consumo_estimado = modelo.predict([[velocidad_nueva]])[0]
print(f"Consumo estimado a {velocidad_nueva} m/s: {consumo_estimado:.0f} mA")

# Visualizar
plt.scatter(X, y, label='Datos reales')
plt.plot(X, modelo.predict(X), 'r-', label='Modelo lineal')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Consumo (mA)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('regresion_consumo.png')
```

**Clasificación - Support Vector Machines (SVM)**:

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# Ejemplo: Clasificador de terreno basado en datos de IMU
class ClasificadorTerreno:
    """Clasifica tipo de terreno (plano, escaleras, rampa) desde IMU"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.modelo = SVC(kernel='rbf', C=1.0, gamma='scale')
        self.clases = ['plano', 'escaleras', 'rampa']
    
    def entrenar(self, X_train, y_train):
        """
        Entrena el clasificador
        
        Args:
            X_train: Features [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z]
            y_train: Labels [0: plano, 1: escaleras, 2: rampa]
        """
        # Normalizar features
        X_scaled = self.scaler.fit_transform(X_train)
        
        # Entrenar SVM
        self.modelo.fit(X_scaled, y_train)
        
        # Evaluar accuracy
        score = self.modelo.score(X_scaled, y_train)
        print(f"Accuracy en entrenamiento: {score*100:.2f}%")
    
    def predecir(self, accel, gyro):
        """
        Predice tipo de terreno
        
        Args:
            accel: [ax, ay, az] aceleración (m/s²)
            gyro: [gx, gy, gz] velocidad angular (rad/s)
        
        Returns:
            terreno: String con tipo de terreno
            confianza: Probabilidad de la predicción
        """
        features = np.concatenate([accel, gyro]).reshape(1, -1)
        features_scaled = self.scaler.transform(features)
        
        clase_predicha = self.modelo.predict(features_scaled)[0]
        
        # Distancia a hiperplano (proxy para confianza)
        decision = self.modelo.decision_function(features_scaled)[0]
        confianza = 1 / (1 + np.exp(-abs(decision)))  # Sigmoid
        
        return self.clases[clase_predicha], confianza

# Ejemplo de uso
clasificador = ClasificadorTerreno()

# Datos sintéticos (en práctica, recolectar de robot real)
X_train = np.random.randn(300, 6)  # 300 muestras, 6 features
y_train = np.random.randint(0, 3, 300)  # 3 clases

clasificador.entrenar(X_train, y_train)

# Predecir
accel_test = np.array([0.1, 0.05, 9.8])
gyro_test = np.array([0.02, -0.01, 0.0])
terreno, conf = clasificador.predecir(accel_test, gyro_test)
print(f"Terreno detectado: {terreno} (confianza: {conf*100:.1f}%)")
```

### 2.2 Redes neuronales artificiales (ANN)

**Perceptrón multicapa (MLP)**:

```python
import torch
import torch.nn as nn
import torch.optim as optim

class RedNeuronalPostura(nn.Module):
    """
    Red neuronal para estimación de postura desde acelerómetro
    Input: [accel_x, accel_y, accel_z]
    Output: [roll, pitch, yaw] en radianes
    """
    
    def __init__(self, input_size=3, hidden_size=64, output_size=3):
        super(RedNeuronalPostura, self).__init__()
        
        self.red = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            nn.Linear(hidden_size, output_size),
            nn.Tanh()  # Salida entre -1 y 1
        )
    
    def forward(self, x):
        return self.red(x)

# Entrenar red
def entrenar_modelo(modelo, X_train, y_train, epochs=100, lr=0.001):
    """Entrena la red neuronal"""
    criterion = nn.MSELoss()
    optimizer = optim.Adam(modelo.parameters(), lr=lr)
    
    # Convertir a tensores
    X_tensor = torch.FloatTensor(X_train)
    y_tensor = torch.FloatTensor(y_train)
    
    for epoch in range(epochs):
        # Forward pass
        predicciones = modelo(X_tensor)
        loss = criterion(predicciones, y_tensor)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
    
    return modelo

# Ejemplo de uso
modelo = RedNeuronalPostura()

# Datos sintéticos (en práctica, recolectar de sensores reales)
X_train = np.random.randn(1000, 3)  # 1000 muestras de acelerómetro
y_train = np.random.uniform(-np.pi/2, np.pi/2, (1000, 3))  # Ángulos verdaderos

modelo_entrenado = entrenar_modelo(modelo, X_train, y_train, epochs=50)

# Inferencia
accel_nueva = torch.FloatTensor([[0.2, 0.1, 9.7]])
postura_estimada = modelo_entrenado(accel_nueva)
print(f"Postura estimada: roll={postura_estimada[0,0]:.3f}, pitch={postura_estimada[0,1]:.3f}, yaw={postura_estimada[0,2]:.3f}")
```

### 2.3 Redes neuronales convolucionales (CNN)

Para procesamiento de imágenes y visión por computadora.

```python
import torch.nn as nn
import torch.nn.functional as F

class CNNDetectorObjetos(nn.Module):
    """CNN simple para clasificación de objetos desde cámara del robot"""
    
    def __init__(self, num_clases=10):
        super(CNNDetectorObjetos, self).__init__()
        
        # Capas convolucionales
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)  # 3 canales RGB → 32 filtros
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        
        self.pool = nn.MaxPool2d(2, 2)  # Reduce tamaño por 2
        
        # Capas completamente conectadas
       self.fc1 = nn.Linear(128 * 8 * 8, 512)  # Depende de tamaño de imagen
        self.fc2 = nn.Linear(512, num_clases)
        
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        # Convoluciones + pooling
        x = self.pool(F.relu(self.conv1(x)))  # 64x64 → 32x32
        x = self.pool(F.relu(self.conv2(x)))  # 32x32 → 16x16
        x = self.pool(F.relu(self.conv3(x)))  # 16x16 → 8x8
        
        # Aplanar
        x = x.view(-1, 128 * 8 * 8)
        
        # Capas densas
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x

# Ejemplo de uso
modelo_cnn = CNNDetectorObjetos(num_clases=5)  # 5 objetos: pelota, caja, persona, silla, puerta

# Simular imagen de entrada (batch_size=1, channels=3, height=64, width=64)
imagen = torch.randn(1, 3, 64, 64)
salida = modelo_cnn(imagen)
clase_predicha = torch.argmax(salida).item()
print(f"Clase predicha: {clase_predicha}")
```

### 2.4 Aprendizaje por refuerzo (reinforcement learning)

**Concepto**: El agente aprende a tomar decisiones óptimas interactuando con el entorno y recibiendo recompensas.

**Componentes**:
- **Estado (s)**: Observación del entorno
- **Acción (a)**: Decisión del agente
- **Recompensa (r)**: Feedback del entorno
- **Política (π)**: Mapeo estado → acción
- **Función de valor (V, Q)**: Valor esperado de estar en un estado/tomar una acción

**Q-Learning (algoritmo básico)**:

$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

```python
import numpy as np

class QLearningAgent:
    """Agente Q-Learning para navegación en grid"""
    
    def __init__(self, n_estados, n_acciones, alpha=0.1, gamma=0.99, epsilon=0.1):
        """
        Args:
            n_estados: Número de estados posibles
            n_acciones: Número de acciones posibles
            alpha: Tasa de aprendizaje
            gamma: Factor de descuento
            epsilon: Probabilidad de exploración
        """
        self.Q = np.zeros((n_estados, n_acciones))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_acciones = n_acciones
    
    def elegir_accion(self, estado):
        """Política epsilon-greedy"""
        if np.random.random() < self.epsilon:
            # Exploración: acción aleatoria
            return np.random.randint(self.n_acciones)
        else:
            # Explotación: mejor acción según Q
            return np.argmax(self.Q[estado])
    
    def actualizar(self, estado, accion, recompensa, siguiente_estado):
        """Actualiza tabla Q"""
        mejor_siguiente = np.max(self.Q[siguiente_estado])
        td_target = recompensa + self.gamma * mejor_siguiente
        td_error = td_target - self.Q[estado, accion]
        self.Q[estado, accion] += self.alpha * td_error
    
    def entrenar(self, entorno, episodios=1000):
        """Entrena el agente en el entorno"""
        recompensas_episodio = []
        
        for episodio in range(episodios):
            estado = entorno.reset()
            recompensa_total = 0
            terminado = False
            
            while not terminado:
                accion = self.elegir_accion(estado)
                siguiente_estado, recompensa, terminado = entorno.step(accion)
                
                self.actualizar(estado, accion, recompensa, siguiente_estado)
                
                estado = siguiente_estado
                recompensa_total += recompensa
            
            recompensas_episodio.append(recompensa_total)
            
            if (episodio + 1) % 100 == 0:
                promedio_100 = np.mean(recompensas_episodio[-100:])
                print(f"Episodio {episodio+1}: Recompensa promedio = {promedio_100:.2f}")
        
        return recompensas_episodio

# Entorno simple de grid 5x5
class EntornoGrid:
    """Entorno de grid 5x5 con objetivo"""
    
    def __init__(self, tamaño=5):
        self.tamaño = tamaño
        self.objetivo = (4, 4)  # Esquina inferior derecha
        self.reset()
    
    def reset(self):
        self.posicion = (0, 0)  # Inicio en esquina superior izquierda
        return self._estado()
    
    def _estado(self):
        """Convierte (x,y) a índice de estado"""
        return self.posicion[0] * self.tamaño + self.posicion[1]
    
    def step(self, accion):
        """
        Ejecuta acción: 0=arriba, 1=derecha, 2=abajo, 3=izquierda
        
        Returns:
            nuevo_estado, recompensa, terminado
        """
        x, y = self.posicion
        
        # Aplicar acción
        if accion == 0 and x > 0: x -= 1  # Arriba
        elif accion == 1 and y < self.tamaño - 1: y += 1  # Derecha
        elif accion == 2 and x < self.tamaño - 1: x += 1  # Abajo
        elif accion == 3 and y > 0: y -= 1  # Izquierda
        
        self.posicion = (x, y)
        
        # Calcular recompensa
        if self.posicion == self.objetivo:
            recompensa = 100
            terminado = True
        else:
            recompensa = -1  # Penalización por paso
            terminado = False
        
        return self._estado(), recompensa, terminado

# Entrenar agente
entorno = EntornoGrid(tamaño=5)
agente = QLearningAgent(n_estados=25, n_acciones=4, epsilon=0.2)
recompensas = agente.entrenar(entorno, episodios=500)

# Visualizar política aprendida
print("\nPolítica aprendida (mejor acción en cada estado):")
for i in range(5):
    fila = []
    for j in range(5):
        estado = i * 5 + j
        accion = np.argmax(agente.Q[estado])
        simbolos = ['↑', '→', '↓', '←']
        fila.append(simbolos[accion])
    print(' '.join(fila))
```

**Deep Q-Network (DQN)** - Combina Q-Learning con redes neuronales profundas:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random

class DQN(nn.Module):
    """Red neuronal para aproximar Q(s,a)"""
    
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.red = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )
    
    def forward(self, x):
        return self.red(x)

class AgenteDQN:
    """Agente con Deep Q-Network y Experience Replay"""
    
    def __init__(self, input_dim, n_acciones, lr=0.001, gamma=0.99):
        self.q_network = DQN(input_dim, n_acciones)
        self.target_network = DQN(input_dim, n_acciones)
        self.target_network.load_state_dict(self.q_network.state_dict())
        
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.criterion = nn.MSELoss()
        
        self.gamma = gamma
        self.n_acciones = n_acciones
        
        # Experience replay buffer
        self.memoria = deque(maxlen=10000)
        self.batch_size = 64
    
    def elegir_accion(self, estado, epsilon=0.1):
        """Epsilon-greedy con red neuronal"""
        if random.random() < epsilon:
            return random.randint(0, self.n_acciones - 1)
        
        with torch.no_grad():
            estado_tensor = torch.FloatTensor(estado).unsqueeze(0)
            q_values = self.q_network(estado_tensor)
            return torch.argmax(q_values).item()
    
    def almacenar_experiencia(self, estado, accion, recompensa, siguiente_estado, terminado):
        """Guarda experiencia en memoria replay"""
        self.memoria.append((estado, accion, recompensa, siguiente_estado, terminado))
    
    def entrenar_paso(self):
        """Entrena con un mini-batch de experiencias"""
        if len(self.memoria) < self.batch_size:
            return
        
        # Samplear mini-batch
        batch = random.sample(self.memoria, self.batch_size)
        
        estados = torch.FloatTensor([e[0] for e in batch])
        acciones = torch.LongTensor([e[1] for e in batch])
        recompensas = torch.FloatTensor([e[2] for e in batch])
        siguientes_estados = torch.FloatTensor([e[3] for e in batch])
        terminados = torch.FloatTensor([e[4] for e in batch])
        
        # Q-values actuales
        q_values = self.q_network(estados).gather(1, acciones.unsqueeze(1))
        
        # Q-values objetivo (usando target network)
        with torch.no_grad():
            next_q_values = self.target_network(siguientes_estados).max(1)[0]
            target_q_values = recompensas + (1 - terminados) * self.gamma * next_q_values
        
        # Calcular pérdida y actualizar
        loss = self.criterion(q_values.squeeze(), target_q_values)
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
    
    def actualizar_target_network(self):
        """Copia pesos de Q-network a target network"""
        self.target_network.load_state_dict(self.q_network.state_dict())

# Ejemplo de uso con entorno personalizado
# (Requiere definir entorno que retorne estados como vectores numéricos)
```

## 3. Aplicaciones específicas en robótica humanoide

### 3.1 Reconocimiento de voz

```python
import speech_recognition as sr

class ReconocedorVoz:
    """Sistema de reconocimiento de voz para comandos del robot"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microfono = sr.Microphone()
        
        # Calibrar para ruido ambiente
        with self.microfono as source:
            print("Calibrando para ruido ambiente...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
    
    def escuchar_comando(self, timeout=5):
        """
        Escucha y reconoce comando de voz
        
        Args:
            timeout: Tiempo máximo de espera (s)
        
        Returns:
            texto: Comando reconocido o None
        """
        with self.microfono as source:
            print("Escuchando...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                texto = self.recognizer.recognize_google(audio, language='es-ES')
                print(f"Reconocido: '{texto}'")
                return texto.lower()
            except sr.WaitTimeoutError:
                print("Timeout: No se detectó voz")
                return None
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
                return None
            except sr.RequestError as e:
                print(f"Error del servicio: {e}")
                return None
    
    def interpretar_comando(self, texto):
        """Mapea texto a acción del robot"""
        comandos = {
            'adelante': 'caminar_adelante',
            'atrás': 'caminar_atras',
            'detente': 'detener',
            'saluda': 'saludar',
            'siéntate': 'sentarse',
            'levántate': 'levantarse'
        }
        
        for palabra_clave, accion in comandos.items():
            if palabra_clave in texto:
                return accion
        
        return 'comando_desconocido'

# Uso
reconocedor = ReconocedorVoz()
comando = reconocedor.escuchar_comando()
if comando:
    accion = reconocedor.interpretar_comando(comando)
    print(f"Acción a ejecutar: {accion}")
```

### 3.2 Detección y reconocimiento facial

```python
import cv2
import face_recognition

class ReconocedorRostros:
    """Sistema de reconocimiento facial para interacción personalizada"""
    
    def __init__(self):
        self.rostros_conocidos = {}  # nombre -> encoding
        self.tolerancia = 0.6  # Umbral de similitud
    
    def registrar_persona(self, nombre, imagen_path):
        """Registra una persona nueva en la base de datos"""
        imagen = face_recognition.load_image_file(imagen_path)
        encodings = face_recognition.face_encodings(imagen)
        
        if len(encodings) > 0:
            self.rostros_conocidos[nombre] = encodings[0]
            print(f"Registrado: {nombre}")
        else:
            print(f"No se detectó rostro en {imagen_path}")
    
    def reconocer_desde_camara(self):
        """Detecta y reconoce rostros en tiempo real desde cámara"""
        captura = cv2.VideoCapture(0)
        
        while True:
            ret, frame = captura.read()
            if not ret:
                break
            
            # Reducir tamaño para mayor velocidad
            frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
            
            # Detectar rostros
            ubicaciones = face_recognition.face_locations(rgb_small)
            encodings = face_recognition.face_encodings(rgb_small, ubicaciones)
            
            # Identificar cada rostro
            for (top, right, bottom, left), encoding in zip(ubicaciones, encodings):
                # Escalar ubicación de vuelta a tamaño original
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                
                # Comparar con rostros conocidos
                nombre = "Desconocido"
                distancias = face_recognition.face_distance(
                    list(self.rostros_conocidos.values()), encoding
                )
                
                if len(distancias) > 0:
                    mejor_match = min(range(len(distancias)), key=lambda i: distancias[i])
                    if distancias[mejor_match] < self.tolerancia:
                        nombre = list(self.rostros_conocidos.keys())[mejor_match]
                
                # Dibujar rectángulo y nombre
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, nombre, (left, top - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            
            cv2.imshow('Reconocimiento Facial', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        captura.release()
        cv2.destroyAllWindows()

# Uso
reconocedor = ReconocedorRostros()
reconocedor.registrar_persona("Juan", "juan.jpg")
reconocedor.registrar_persona("María", "maria.jpg")
reconocedor.reconocer_desde_camara()
```

## 4. Consideraciones éticas en IA para robótica

### 4.1 Sesgos y equidad

**Problema**: Algoritmos de IA pueden perpetuar sesgos presentes en datos de entrenamiento.

**Mitigación**:
- Auditar datasets por representatividad
- Evaluarvmétricas de equidad (disparate impact, demographic parity)
- Técnicas de debiasing (re-weighting, adversarial debiasing)

### 4.2 Transparencia y explicabilidad

**Técnicas de IA Explicable (XAI)**:

```python
import shap

def explicar_prediccion_modelo(modelo, instancia, datos_fondo):
    """
    Explica predicción usando SHAP (SHapley Additive exPlanations)
    
    Args:
        modelo: Modelo entrenado
        instancia: Muestra a explicar
        datos_fondo: Dataset de referencia
    """
    explainer = shap.Explainer(modelo, datos_fondo)
    shap_values = explainer(instancia)
    
    # Visualizar contribución de cada feature
    shap.plots.waterfall(shap_values[0])
    
    return shap_values
```

### 4.3 Privacidad de datos

**Principios**:
- Minimización de datos
- Anonimización
- Consentimiento informado
- Derecho al olvido

## 5. Optimización para deployment en edge

### 5.1 Cuantización de modelos

```python
import torch

def cuantizar_modelo(modelo, ejemplo_entrada):
    """
    Cuantiza modelo de FP32 a INT8 para inferencia rápida
    
    Args:
        modelo: Modelo PyTorch
        ejemplo_entrada: Input de ejemplo para tracing
    
    Returns:
        modelo_cuantizado
    """
    modelo.eval()
    
    # Cuantización dinámica (pesos INT8, activaciones FP32)
    modelo_cuantizado = torch.quantization.quantize_dynamic(
        modelo,
        {torch.nn.Linear},  # Capas a cuantizar
        dtype=torch.qint8
    )
    
    # Comparar tamaños
    tamaño_original = sum(p.numel() * p.element_size() for p in modelo.parameters())
    tamaño_cuantizado = sum(p.numel() * p.element_size() for p in modelo_cuantizado.parameters())
    
    print(f"Tamaño original: {tamaño_original / 1024:.2f} KB")
    print(f"Tamaño cuantizado: {tamaño_cuantizado / 1024:.2f} KB")
    print(f"Reducción: {(1 - tamaño_cuantizado/tamaño_original)*100:.1f}%")
    
    return modelo_cuantizado
```

### 5.2 Pruning (poda de redes)

```python
import torch.nn.utils.prune as prune

def podar_modelo(modelo, cantidad=0.3):
    """
    Poda pesos con menor magnitud
    
    Args:
        modelo: Modelo PyTorch
        cantidad: Fracción de pesos a eliminar (0.0-1.0)
    """
    for name, module in modelo.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.l1_unstructured(module, name='weight', amount=cantidad)
    
    print(f"Modelo podado: {cantidad*100:.0f}% de pesos eliminados")
```

## Referencias

- **Libros**:
  - "Deep Learning" - Goodfellow, Bengio, Courville
  - "Reinforcement Learning: An Introduction" - Sutton & Barto
  - "Pattern Recognition and Machine Learning" - Christopher Bishop

- **Cursos**:
  - CS229 (Machine Learning) - Stanford
  - CS231n (Computer Vision) - Stanford
  - CS294 (Deep Reinforcement Learning) - Berkeley

- **Frameworks**:
  - PyTorch / TensorFlow
  - OpenCV
  - Scikit-learn
  - ROS

---

## Conclusión

La inteligencia artificial y el aprendizaje automático son componentes esenciales para dotar a robots humanoides de capacidades avanzadas de percepción, comprensión, adaptación y toma de decisiones autónomas. La combinación de técnicas clásicas de ML con deep learning y aprendizaje por refuerzo permite crear sistemas robóticos verdaderamente inteligentes que pueden operar en entornos complejos y dinámicos del mundo real.

**Próximo módulo**: [Comunicaciones e interfaces](../07_Comunicaciones/) para integración de sistemas distribuidos.
