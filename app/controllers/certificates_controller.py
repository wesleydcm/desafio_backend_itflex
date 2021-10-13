from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from http import HTTPStatus

import psycopg2
from app.exceptions.groupsErrors import InvalidGroupError
from app.models.certificates_model import Certificates
from app.models.groups_model import Groups
from app.models.queries_categories_model import QueriesCertificates
from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError, InvalidRequestError


def list_certificates():
    order_by = 'order_by'

    query_params = request.args

    if not query_params:
        return QueriesCertificates.all_certificates()

    if order_by in query_params and len(query_params) == 1:
        order_by = query_params[order_by]
        return QueriesCertificates.certificates_order_by(order_by)


    return {'msg': "certificate not found..."}, HTTPStatus.NOT_FOUND


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
    

    except InvalidGroupError as error:
        return jsonify({'error': error.message}), HTTPStatus.NOT_FOUND

    
    except IntegrityError as e:
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

        data["updated_at"] = datetime.now(timezone.utc)

        if "expiration" in data and data['expiration'] > 1:
            data["expirated_at"] = (certificate.created_at + timedelta(days=data['expiration']))


        if "groups" in data:
            group_codes = data['groups']

            del data['groups']

            certificate.groups.clear()

            for code in group_codes:
                group: Groups = Groups.query.filter_by(code=code).first()

                if not group:
                    new_group = Groups.verify_group(code)

                    group: Groups = Groups(**new_group)

                certificate.groups.append(group)


        Certificates.query.filter_by(id=id).update(data)

        certificate: Certificates = Certificates.query.get(id)

        session = current_app.db.session
        session.commit()

        return jsonify(certificate), HTTPStatus.OK
        

    except InvalidGroupError as error:
        return jsonify({'error': error.message}), HTTPStatus.NOT_FOUND

    # Campo não existe
    except TypeError as e:
        return jsonify({"msg": str(e)}), HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        # Campo unico já existe
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'msg': str(e.orig).split('\n')[1]}, HTTPStatus.CONFLICT
    
    except InvalidRequestError as e:
        return jsonify({"msg": str(e)}), HTTPStatus.BAD_REQUEST



def certificates_filter_by_username(username: str):

    query = Certificates.query\
        .filter(Certificates\
        .username == username)\
        .all()

    if not query:
        return {'msg': f"there are no certificates for username: {username}"}, HTTPStatus.NOT_FOUND

    return jsonify(query), HTTPStatus.OK



def certificates_filter_by_name(name: str):

    query = Certificates.query\
        .filter(Certificates\
        .name == name)\
        .all()

    if not query:
        return {'msg': f"there are no certificates for name: {name}"}, HTTPStatus.NOT_FOUND

    return jsonify(query), HTTPStatus.OK



def delete_certificate(id: int):
    certificate = Certificates.query.get(id)

    if not certificate:
        return jsonify({"msg": "certificate not found!"}), HTTPStatus.NOT_FOUND

    session = current_app.db.session
    session.delete(certificate)
    session.commit()

    return jsonify(''), HTTPStatus.NO_CONTENT
