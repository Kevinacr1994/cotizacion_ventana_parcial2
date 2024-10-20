from .cliente import Cliente
from .ventana import Ventana

class Cotizacion:
    def __init__(self, cliente, ventanas):
        if not isinstance(cliente, Cliente):
            raise ValueError("El cliente debe ser una instancia de la clase Cliente.")
        if not all(isinstance(ventana, Ventana) for ventana in ventanas):
            raise ValueError("Todas las ventanas deben ser instancias de la clase Ventana.")

        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_total(self):
        """Calcula el costo total de la cotización, aplicando descuentos si corresponde."""
        total = sum(ventana.calcular_costo_total() for ventana in self.ventanas)

        # Aplicar descuento si el cliente solicita más de 100 ventanas
        if self.cliente.cantidad_ventanas > 100:
            total *= 0.9  # 10% de descuento

        return total

    def resumen_cotizacion(self):
        """Devuelve un resumen de la cotización."""
        total = self.calcular_total()
        return {
            'cliente': self.cliente.get_info(),
            'cantidad_ventanas': len(self.ventanas),
            'total': total
        }
