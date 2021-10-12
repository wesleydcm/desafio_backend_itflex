from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.groups_model import Groups
    from app.models.certificates_model import Certificates
    from app.models.certificates_groups_table import certificates_groups

    Migrate(app, app.db)
