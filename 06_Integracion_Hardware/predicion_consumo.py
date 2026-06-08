# Predicción de consumo con IA

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