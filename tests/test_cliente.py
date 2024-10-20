# tests/test_cliente.py
from ..app.models.cliente import Cliente

def test_cliente_inicializacion():
    cliente = Cliente(nombre="José", empresa="Argos", cantidad_ventanas=50)
    
    # Verificar que los atributos se inicializan correctamente
    assert cliente.nombre == "José"
    assert cliente.empresa == "Argos"
    assert cliente.cantidad_ventanas == 50

def test_cliente_modificacion_atributos():
    cliente = Cliente(nombre="María", empresa="Ventanas SA", cantidad_ventanas=100)
    
    # Modificar los atributos
    cliente.nombre = "Ana"
    cliente.empresa = "Ventanas otra"
    cliente.cantidad_ventanas = 200
    
    # Verificar que los atributos se actualizan correctamente
    assert cliente.nombre == "Ana"
    assert cliente.empresa == "Ventanas otra"
    assert cliente.cantidad_ventanas == 200
