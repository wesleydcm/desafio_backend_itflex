from dataclasses import asdict
from datetime import datetime, timezone
from http import HTTPStatus
import psycopg2
from app.exceptions.certificatesErrors import InvalidCertificateError
from app.models.certificates_model import Certificates
from app.models.groups_model import Groups
from flask import current_app, jsonify, request
from sqlalchemy.exc import (IntegrityError, InvalidRequestError,
                            ProgrammingError)


def list_certificates():
    return {"msg": "hello iTFLEX"}, HTTPStatus.OK


def create_certificate():
    try:
        data = request.json
        
        group_codes = data['groups']
        
        del data['groups']

        data = Certificates.insert_dates_new_certificates(data)

        new_certificate: Certificates = Certificates(**data)
        

        for code in group_codes:
            group: Groups = Groups.query.filter_by(code=code).first()

            if not group:
                new_group = Groups.verify_group(code)

                group: Groups = Groups(**new_group)
            
            new_certificate.groups.append(group)


        session = current_app.db.session
        session.add(new_certificate)
        session.commit()


        certificate = asdict(new_certificate)
        certificate['groups'] = group_codes


        return certificate, HTTPStatus.CREATED


    except KeyError as e:
        return {"msg": f'Need to have property {str(e)}'}, HTTPStatus.BAD_REQUEST
    
    except ValueError as e:
        return {"msg": str(e)}, HTTPStatus.BAD_REQUEST
    
    except InvalidCertificateError as error:
        return jsonify({'error': error.message}), HTTPStatus.NOT_FOUND
    
    except IntegrityError as e:
        print(e.orig)

        # Campo faltando
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'msg': str(e.orig).split('\n')[0]}, HTTPStatus.BAD_REQUEST

        # Campo unico já existe
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'msg': str(e.orig).split('\n')[1]}, HTTPStatus.CONFLICT


def update_certificate(id: int):

    certificate: Certificates = Certificates.query.get(id)

    if not certificate:
        return {"msg": "certificate not found!"}, HTTPStatus.NOT_FOUND


    try:
        data = request.json

        Certificates.query.filter_by(id=id).update(data)

        certificate: Certificates = Certificates.query.get(id)


        Certificates.query.filter_by(id=id).update(data)

        certificate: Certificates = Certificates.query.get(id)

        session = current_app.db.session
        session.commit()

        return jsonify(certificate), HTTPStatus.OK

    except ProgrammingError as e:
        if type(e.orig) == psycopg2.errors.SyntaxError:
            return jsonify({"msg": "Sintax error"}), HTTPStatus.NOT_FOUND

    # Campo não existe
    except TypeError as e:
        return jsonify({"msg": str(e)}), HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        print(e.orig)

        # Campo faltando
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'msg': str(e.orig).split('\n')[0]}, HTTPStatus.BAD_REQUEST

        # Campo unico já existe
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'msg': str(e.orig).split('\n')[1]}, HTTPStatus.CONFLICT
    
    except InvalidRequestError as e:
        return jsonify({"msg": str(e)}), HTTPStatus.BAD_REQUEST


def delete_certificate(id: int):
    certificate = Certificates.query.get(id)

    if not certificate:
        return jsonify({"msg": "certificate not found!"}), HTTPStatus.NOT_FOUND

    session = current_app.db.session
    session.delete(certificate)
    session.commit()

    return jsonify(''), HTTPStatus.NO_CONTENT
