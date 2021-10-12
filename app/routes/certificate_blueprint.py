from flask import Blueprint
from app.controllers.certificates_controller import list_certificates, create_certificate, delete_certificate, update_certificate

bp_certificates = Blueprint('certificates', __name__, url_prefix="/certificates")


bp_certificates.get('')(list_certificates)
bp_certificates.post('')(create_certificate)
bp_certificates.patch('/<int:id>')(update_certificate)
bp_certificates.delete('/<int:id>')(delete_certificate)
