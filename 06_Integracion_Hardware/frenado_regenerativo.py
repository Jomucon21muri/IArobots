'''
 Frenado regenerativo (para robots con movilidad con ruedas)
'''
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
