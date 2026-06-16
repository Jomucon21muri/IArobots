'''
 Regulación energética (homeostasis)
 Qué se simula
 Balance energético dinámico según las tareas realizadas
 Asignación inteligente de recursos
 Modos de ahorro de energía

 Estrategias de optimización
 Modos de operación:
'''
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
