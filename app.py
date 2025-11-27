"""
Entry point for running the Weather Dashboard application.
Uses the application factory pattern (create_app) for clean architecture.
"""

from flask import Flask, request
from main.routes import main_bp
import time
from main.routes import main_bp

from utils.metrics import (
    record_request,
    record_error,
    record_request_latency,
    generate_metrics
)

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    @app.before_request
    def before_request():
        request.start_time = time.time()
        record_request()

    @app.after_request
    def after_request(response):
        record_request_latency(request.start_time)
        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        record_error()
        return {"error": str(e)}, 500
    
    @app.route("/metrics")
    def metrics():
        return generate_metrics(), 200, {"Content-Type": "text/plain"}
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
