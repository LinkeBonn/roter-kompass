from flask import Blueprint
from .action_routes import action_bp
from .opinion_routes import opinion_bp

def register_routes(app):
    app.register_blueprint(action_bp, url_prefix="/api/action")
    app.register_blueprint(opinion_bp, url_prefix="/api/opinion")
