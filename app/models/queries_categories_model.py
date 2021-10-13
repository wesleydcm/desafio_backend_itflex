from http import HTTPStatus

from flask import current_app, jsonify, request

from .certificates_model import Certificates


class QueriesCertificates():

    @staticmethod
    def all_certificates():
        query = Certificates.query.all()

        return jsonify(query),HTTPStatus.OK


    @staticmethod
    def certificates_order_by(order_by):

        if order_by == "username":
            query = Certificates.query.order_by(Certificates.username).all()

            if not query:
                return {'msg': "certificate not found..."}, 404


        if order_by == "name":
            query = Certificates.query.order_by(Certificates.name).all()

            if not query:
                return {'msg': "certificate not found..."}, 404


        return jsonify(query), HTTPStatus.OK


