from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from application.services.schemas.movie import MovieSchema
from application.container import movies_dao, movies_service

movies_ns = Namespace('movies')
movie_schema = MovieSchema()


@movies_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid):
        return movies_service.get_one(uid)

    def put(self, uid):
        try:
            return movies_service.update(uid, request.json), 204
        except ValidationError as ex:
            return {'errors': ex.normalized_messages()}, 400

    def delete(self, uid):
        return movies_service.delete(uid), 202


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        args = request.args
        if 'director_id' in args:
            return movies_service.get_by_director_id(args['director_id'])
        if 'genre_id' in args:
            return movies_service.get_by_genre_id(args['genre_id'])
        return movies_service.qet_all()

    def post(self):
        return movies_service.create(request.json), 201
