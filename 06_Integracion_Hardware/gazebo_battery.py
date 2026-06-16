''' 
Simulación de consumo en Gazebo
Plugin de Gazebo para simular descarga de batería
'''
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


