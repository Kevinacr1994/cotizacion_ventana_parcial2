from ..app.models.ventana import Ventana
import pytest

def test_calcular_costo_aluminio():
    ventana = Ventana(estilo="XO", ancho=200, alto=150, acabado="Pulido", tipo_vidrio="Transparente", esmerilado=False)
    costo_aluminio = ventana.calcular_costo_aluminio()
    assert costo_aluminio == pytest.approx(147402.0, 0.1)

def test_calcular_costo_vidrio():
    ventana = Ventana(estilo="XO", ancho=200, alto=150, acabado="Pulido", tipo_vidrio="Transparente", esmerilado=False)
    costo_vidrio = ventana.calcular_costo_vidrio()
    assert costo_vidrio == pytest.approx(23193.375, 0.1)

def test_calcular_costo_total():
    ventana = Ventana(estilo="XO", ancho=200, alto=150, acabado="Pulido", tipo_vidrio="Transparente", esmerilado=False)
    costo_total = ventana.calcular_costo_total()
    assert costo_total == pytest.approx(170595.375, 0.1)
