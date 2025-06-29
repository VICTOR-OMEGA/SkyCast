from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")

    # Optional: Load config from file
    app.config.from_pyfile("config.py", silent=True)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app

