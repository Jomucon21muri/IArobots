# Dashboard de monitoreo energético

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class EnergyDashboard:
    def __init__(self):
        self.history = {
            'time': [],
            'charge': [],
            'consumption': [],
            'mode': []
        }
    
    def plot_energy_status(self):
        """Visualiza estado energético"""
        fig, axs = plt.subplots(3, 1, figsize=(10, 8))
        
        # Gráfico 1: Nivel de batería
        axs[0].plot(self.history['time'], self.history['charge'], 'b-')
        axs[0].set_ylabel('Carga (%)')
        axs[0].set_title('Estado de Batería')
        axs[0].axhline(y=20, color='r', linestyle='--', label='Umbral crítico')
        axs[0].legend()
        
        # Gráfico 2: Consumo instantáneo
        axs[1].plot(self.history['time'], self.history['consumption'], 'g-')
        axs[1].set_ylabel('Potencia (W)')
        axs[1].set_title('Consumo Instantáneo')
        
        # Gráfico 3: Modo de operación
        modes = {'PERFORMANCE': 3, 'BALANCED': 2, 'POWER_SAVE': 1, 'EMERGENCY': 0}
        mode_values = [modes[m] for m in self.history['mode']]
        axs[2].step(self.history['time'], mode_values, 'r-', where='post')
        axs[2].set_ylabel('Modo')
        axs[2].set_xlabel('Tiempo')
        axs[2].set_title('Modo de Operación')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self):
        """Genera reporte de eficiencia energética"""
        total_time = (self.history['time'][-1] - self.history['time'][0]).seconds / 3600  # horas
        avg_consumption = sum(self.history['consumption']) / len(self.history['consumption'])
        total_energy = avg_consumption * total_time  # Wh
        
        report = f"""
        REPORTE ENERGÉTICO
        ═══════════════════════════════
        Tiempo de operación: {total_time:.2f} horas
        Consumo promedio: {avg_consumption:.2f} W
        Energía total consumida: {total_energy:.2f} Wh
        Carga inicial: {self.history['charge'][0]:.1f}%
        Carga final: {self.history['charge'][-1]:.1f}%
        Eficiencia: {(self.history['charge'][0] - self.history['charge'][-1]) / total_energy * 55.5:.2f} %/Wh
        """
        return report
