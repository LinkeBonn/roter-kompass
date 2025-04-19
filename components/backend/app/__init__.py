from flask import Flask
from .extensions import db, migrate, ma
from .config import Config
from .routes import register_routes
from app import models
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    register_routes(app)

    return app
