from app.config import Config
from flask import Flask
from .extensions import db, migrate, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # <- Obligatoire
    login_manager.init_app(app)
    login_manager.login_view = "login"
    # from .routes import main
    # app.register_blueprint(main)

    # importation de toutes les tables
    from .models import User, Client, Contrat, Paiement


    return app
