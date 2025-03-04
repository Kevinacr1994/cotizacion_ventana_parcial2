from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa las rutas y registra el blueprint
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
