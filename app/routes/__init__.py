from flask import Flask

from .api_blueprint import bp

def init_app(app: Flask):
    app.register_blueprint(bp)
