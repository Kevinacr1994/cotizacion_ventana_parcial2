class Cliente:
    def __init__(self, nombre, empresa, cantidad_ventanas):
        """
        Inicializa la clase Cliente con el nombre del cliente, la empresa y la cantidad de ventanas solicitadas.
        """
        self.nombre = nombre
        self.empresa = empresa
        self.cantidad_ventanas = cantidad_ventanas

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Cliente, útil para debugging o mostrar información básica.
        """
        return f"Cliente: {self.nombre}, Empresa: {self.empresa}, Ventanas: {self.cantidad_ventanas}"

    def get_info(self):
        """
        Retorna un diccionario con la información del cliente.
        Este método es útil para generar reportes o pasar datos entre funciones.
        """
        return {
            'nombre': self.nombre,
            'empresa': self.empresa,
            'cantidad_ventanas': self.cantidad_ventanas
        }
