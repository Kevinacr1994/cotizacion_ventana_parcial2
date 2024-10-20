# Sistema de Cotización de Ventanas para la Compañía PQR

## Descripción

Este proyecto consiste en el desarrollo de un sistema de cotización de ventanas para la empresa PQR, con el fin de automatizar su proceso manual. El sistema permite calcular el costo total de las ventanas basándose en el estilo de la ventana, tipo de vidrio, acabado de aluminio y otros componentes adicionales.

## Características
- Cálculo de costos para diferentes estilos de ventanas (O, XO, OXXO, OXO).
- Tipos de vidrios y acabados de aluminio.
- Inclusión de componentes adicionales como esquinas y chapas.
- Aplicación de descuentos para pedidos superiores a 100 ventanas.
- Generación de cotización detallada.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

1. **Python 3.6 o superior**: Asegúrate de tener Python instalado en tu sistema.
2. **Entorno Virtual**: Se recomienda crear un entorno virtual para manejar las dependencias del proyecto.
3. **Dependencias**: Este proyecto utiliza algunas bibliotecas que deben ser instaladas.

## Instrucciones para Ejecutar el Proyecto

Sigue los pasos a continuación para ejecutar el sistema de cotización de ventanas:

### 1.  Crea y Activa un Entorno Virtual

Crea un entorno virtual para manejar las dependencias del proyecto:


# En Windows
python -m venv .venv
.\.venv\Scripts\activate

# En macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

## Instalar las Dependencias
Instale las dependencias necesarias utilizando pip:

pip install -r requirements.txt

## Ejecutar la aplicacion 
Para ejecutar la aplicación, utilice el siguiente comando:

python run.py

Esto iniciará el servidor de desarrollo y podrás acceder al sistema en tu navegador http://127.0.0.1:5000