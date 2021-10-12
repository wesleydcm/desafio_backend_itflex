from flask import Flask
from app.configs import env_configs, database, migrate
from app import routes


def create_app() -> Flask:
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    routes.init_app(app)

    return app
