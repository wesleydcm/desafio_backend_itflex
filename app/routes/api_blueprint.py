from flask import Blueprint

from . import certificate_blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(certificate_blueprint.bp_certificates)
