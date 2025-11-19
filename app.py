"""
Entry point for running the Weather Dashboard application.
Uses the application factory pattern (create_app) for clean architecture.
"""

from flask import Flask
from main.routes import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
