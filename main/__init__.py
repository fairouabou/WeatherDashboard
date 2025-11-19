from flask import Blueprint

main_bp = Blueprint(
    "main",
    __name__,
    template_folder="templates"
)

# IMPORTANT: import routes AFTER creating the blueprint
from . import routes
