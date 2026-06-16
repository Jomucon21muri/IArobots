'''
En este módulo se simula un panel solar como fuente de energía auxiliar para el sistema.
'''
class SolarPanel:
    """Simula panel solar como fuente de energía auxiliar"""
    def __init__(self, area_m2=0.1, efficiency=0.15):
        self.area = area_m2
        self.efficiency = efficiency
        
    def get_power_output(self, solar_irradiance_w_m2, angle_deg=0):
        """
        Calcula potencia generada
        solar_irradiance: típicamente 400-1000 W/m² dependiendo de hora y clima
        """
        angle_factor = math.cos(math.radians(angle_deg))
        power_w = self.area * solar_irradiance_w_m2 * self.efficiency * angle_factor
        return max(0, power_w)
    
    def estimate_daily_generation(self, location_lat, season):
        """Estima generación diaria según ubicación"""
        # Simplificado: 5 horas de sol útil promedio
        avg_irradiance = 600  # W/m²
        useful_hours = 5
        daily_wh = self.get_power_output(avg_irradiance) * useful_hours
        return daily_wh