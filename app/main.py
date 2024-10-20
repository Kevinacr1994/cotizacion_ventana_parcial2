# main.py
from flask import Flask, render_template
from routes import main_routes  # Importa las rutas

app = Flask(__name__)

# Registra las rutas
app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run(debug=True)
