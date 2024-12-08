from flask import Flask
from app.extensions import init_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_extensions(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app