from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from application.services.schemas.director import DirectorSchema
from application.container import directors_service

directors_ns = Namespace('directors')
director_schema = DirectorSchema()


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    def get(self, uid):
        return directors_service.get_one(uid)

    def put(self, uid):
        try:
            return directors_service.update(uid, request.json), 204
        except ValidationError as ex:
            return {'errors': ex.normalized_messages()}, 400

    def delete(self, uid):
        return directors_service.delete(uid), 202


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        return directors_service.qet_all()

    def post(self):
        return directors_service.create(request.json), 201

