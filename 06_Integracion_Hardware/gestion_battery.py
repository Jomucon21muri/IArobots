''' Software de gestión
Battery Management System (BMS) personalizado
'''
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
