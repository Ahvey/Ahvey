from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize routes
    with app.app_context():
        from . import routes

    return app

app = create_app()