from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from application.services.schemas.genre import GenreSchema
from application.container import genres_service

genres_ns = Namespace('genres')
genre_schema = GenreSchema()


@genres_ns.route('/<int:uid>')
class GenreView(Resource):

    def get(self, uid):
        return genres_service.get_one(uid)

    def put(self, uid):
        try:
            return genres_service.update(uid, request.json), 204
        except ValidationError as ex:
            return {'errors': ex.normalized_messages()}, 400

    def delete(self, uid):
        return genres_service.delete(uid), 202


@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        return genres_service.qet_all()

    def post(self):
        return genres_service.create(request.json), 201
