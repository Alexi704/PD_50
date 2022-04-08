from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource
from application.models import db
from application import models, schema

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')
directors_ns: Namespace = api.namespace('directors')
genres_ns: Namespace = api.namespace('genres')

movie_schema = schema.Movie()
movies_schema = schema.Movie(many=True)

director_schema = schema.Director()
directors_schema = schema.Director(many=True)

genre_schema = schema.Genre()
genres_schema = schema.Genre(many=True)


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    """ Ищем фильм по его id """
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()
        if movie is None:
            return {404: 'такого фильма нет в базе'}, 404
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        """ Обновляем какое-либо из полей """
        updated_rows = db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        if updated_rows != 1:
            return {400: 'обновление невозможно, т.к. такого фильма нет в базе'}, 400
        db.session.commit()
        return {204: 'обновление прошло успешно'}, 204

    def delete(self, movie_id):
        """ Удаляем фильм """
        delete_row = db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()
        if delete_row != 1:
            return {400: 'удаление невозможно, т.к. не найден фильм'}, 400

        db.session.commit()
        return {200: 'фильм успешно удален'}, 200


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """ Загружаем всю базу для просмотра """
        movies_query = db.session.query(models.Movie)

        args = request.args

        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(models.Movie.director_id == director_id)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(models.Movie.genre_id == genre_id)

        movies = movies_query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        """ Добавляем фильм в базу данных """
        movie = movie_schema.load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()

        return {201: 'фильм успешно ДОБАВЛЕН!!!'}, 201


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id):
        """ Загружаем фильм по его id """
        director = db.session.query(models.Director).filter(models.Director.id == director_id).first()
        if director is None:
            return {404: 'таких режиссеров не найдено'}, 404
        return director_schema.dump(director), 200


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(models.Director).all()
        return directors_schema.dump(directors), 200


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id).first()
        if genre is None:
            return {404: 'таких жанров не найдено'}, 404
        return genre_schema.dump(genre), 200


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(models.Genre).all()
        return genres_schema.dump(genres), 200
