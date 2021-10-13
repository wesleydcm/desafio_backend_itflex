from app.controllers.certificates_controller import (
    certificates_filter_by_name, certificates_filter_by_username,
    create_certificate, delete_certificate, list_certificates,
    update_certificate)
from flask import Blueprint

bp_certificates = Blueprint('certificates', __name__, url_prefix="/certificates")


bp_certificates.get('')(list_certificates)
bp_certificates.post('')(create_certificate)
bp_certificates.patch('/<int:id>')(update_certificate)
bp_certificates.delete('/<int:id>')(delete_certificate)

bp_certificates.get('/of_the_username/<string:username>')(certificates_filter_by_username)
bp_certificates.get('/of_the_name/<string:name>')(certificates_filter_by_name)
