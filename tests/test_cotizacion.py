# test_cotizacion.py
from ..app.models.cotizacion import Cotizacion  # Importamos la clase que vamos a probar

class MockVentana:
    # Esta es una clase simulada para representar a las ventanas
    def __init__(self, costo):
        self.costo = costo

    def calcular_costo_total(self):
        return self.costo

class MockCliente:
    # Esta es una clase simulada para representar al cliente
    def __init__(self, cantidad_ventanas):
        self.cantidad_ventanas = cantidad_ventanas

def test_calcular_total_sin_descuento():
    # Creamos el cliente con menos de 100 ventanas (no aplica descuento)
    cliente = MockCliente(cantidad_ventanas=50)
    
    # Creamos algunas ventanas con diferentes costos
    ventanas = [MockVentana(costo=100), MockVentana(costo=200)]
    
    # Creamos la cotización
    cotizacion = Cotizacion(cliente, ventanas)
    
    # Verificamos que el total sea correcto (sin descuento)
    assert cotizacion.calcular_total() == 300

def test_calcular_total_con_descuento():
    # Creamos el cliente con más de 100 ventanas (aplica descuento)
    cliente = MockCliente(cantidad_ventanas=150)
    
    # Creamos algunas ventanas con diferentes costos
    ventanas = [MockVentana(costo=500), MockVentana(costo=500)]
    
    # Creamos la cotización
    cotizacion = Cotizacion(cliente, ventanas)
    
    # Verificamos que el total sea correcto (con descuento del 10%)
    assert cotizacion.calcular_total() == 900  # 1000 * 0.9
