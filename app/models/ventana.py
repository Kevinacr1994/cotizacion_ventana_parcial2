class Ventana:
    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado):
        self.estilo = estilo  # 'O', 'XO', 'OXXO', etc.
        self.ancho = ancho  # Ancho total de la ventana
        self.alto = alto    # Alto total de la ventana
        self.acabado = acabado  # Pulido, Lacado Brillante, etc.
        self.tipo_vidrio = tipo_vidrio  # Transparente, Bronce, Azul
        self.esmerilado = esmerilado  # Si el vidrio es esmerilado o no

    def calcular_costo_aluminio(self):
        # Costos por metro lineal
        precios_acabado = {
            "Pulido": 50700,
            "Lacado Brillante": 54200,
            "Lacado Mate": 53600,
            "Anodizado": 57300
        }
        
        # Tamaño de las naves
        numero_naves = len(self.estilo)
        ancho_nave = self.ancho / numero_naves
        
        # Longitud de aluminio (marco) por nave
        perimetro_nave = (2 * (ancho_nave + self.alto)) - (4 * 1)  # Restar el grosor de las esquinas (1 cm en cada lado)

        # Costo de aluminio por nave
        costo_aluminio_nave = perimetro_nave * precios_acabado[self.acabado] / 100  # Dividido entre 100 para pasar a metros
        return costo_aluminio_nave * numero_naves

    def calcular_costo_vidrio(self):
        # Costos por cm2 de vidrio
        precios_vidrio = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }

        # Calcular área de cada nave
        numero_naves = len(self.estilo)
        ancho_nave = self.ancho / numero_naves
        area_vidrio_nave = (ancho_nave - 1.5) * (self.alto - 1.5)  # Descontar el borde para insertar el vidrio

        # Costo de vidrio
        costo_vidrio_nave = area_vidrio_nave * precios_vidrio.get(self.tipo_vidrio, 0)  # Usar get para evitar KeyError
        
        # Si es esmerilado, sumar el costo adicional
        if self.esmerilado:
            costo_vidrio_nave += area_vidrio_nave * 5.20
        
        return costo_vidrio_nave * numero_naves

    def calcular_costo_total(self):
        # Calcular el costo total sumando el costo del aluminio y del vidrio
        costo_total = self.calcular_costo_aluminio() + self.calcular_costo_vidrio()
        return costo_total
