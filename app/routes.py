from flask import Blueprint, render_template, request, send_file
from .models.cliente import Cliente
from .models.ventana import Ventana
from .models.cotizacion import Cotizacion
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('cotizacion.html')

@main_routes.route('/cotizar', methods=['POST'])
def cotizar():
    nombre_cliente = request.form['nombre_cliente']
    empresa_cliente = request.form['empresa_cliente']
    cantidad_ventanas = int(request.form['cantidad_ventanas'])
    cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)

    ventanas = []
    for i in range(1, cantidad_ventanas + 1):
        estilo = request.form[f'tipo_ventana_{i}']
        dimensiones = request.form[f'dimensiones_ventana_{i}'].split('x')
        ancho = float(dimensiones[0].strip())
        alto = float(dimensiones[1].strip())
        acabado = request.form[f'acabado_ventana_{i}']
        tipo_vidrio = request.form[f'tipo_vidrio_{i}']
        esmerilado = request.form.get(f'esmerilado_{i}', 'N') == 'S'

        ventana = Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado)
        ventanas.append(ventana)
    
    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()  # Asegúrate de que este método esté implementado en tu clase Cotizacion
    
    return render_template('resultado.html', total=total, cliente=cliente, ventanas=ventanas)

@main_routes.route('/descargar_factura')
def generar_factura():
    # Obtener la información del cliente y las ventanas desde la sesión o un método de tu elección
    cliente_info = {'nombre': "kevin yule", 'empresa': "argos"}  # Ejemplo estático, debería ser dinámico
    ventanas = [
        Ventana("O", 100, 200, "Lacado Brillante", "Templado", False),  # Ejemplo estático, debería ser dinámico
        Ventana("XO", 150, 300, "Lacado Mate", "Estándar", True)  # Ejemplo estático, debería ser dinámico
    ]  
    total = sum(ventana.calcular_costo_total() for ventana in ventanas)  # Calcular el total dinámicamente

    # Crear PDF en memoria
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Título de la factura
    c.setFont("Helvetica", 16)
    c.drawString(100, height - 50, "Factura de Cotización")
    
    # Información del cliente
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Cliente: {cliente_info['nombre']}")
    c.drawString(100, height - 120, f"Empresa: {cliente_info['empresa']}")
    c.drawString(100, height - 140, f"Cantidad de Ventanas: {len(ventanas)}")

    # Detalles de las ventanas
    c.drawString(100, height - 180, "Detalles de las Ventanas:")
    
    y_position = height - 200
    for index, ventana in enumerate(ventanas):
        precio = ventana.calcular_costo_total()  # Llama al método para calcular el precio
        c.drawString(100, y_position, f"Ventana {index + 1}: {ventana.estilo}, {ventana.ancho} x {ventana.alto} cm, "
                                       f"Acabado: {ventana.acabado}, Vidrio: {ventana.tipo_vidrio}, "
                                       f"Esmerilado: {'Sí' if ventana.esmerilado else 'No'}, Precio: ${precio:.2f}")
        y_position -= 20

    # Total
    c.drawString(100, y_position - 20, f"Total de la Cotización: ${total:.2f}")

    c.save()
    buffer.seek(0)  # Mover el puntero al inicio del buffer

    # Enviar el PDF como archivo
    return send_file(buffer, as_attachment=True, download_name='factura.pdf', mimetype='application/pdf')
