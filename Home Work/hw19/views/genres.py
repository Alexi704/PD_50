from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        req_json['name'] = req_json['name'].lower().title()
        add_genre = req_json['name']

        # проверяем есть ли уже данный жанр
        is_genre = genre_service.get_all()
        genres_data = GenreSchema(many=True).dump(is_genre)
        genre_list = [] # создаем список всех жанров
        for genre_data in genres_data:
            genre_list.append(genre_data['name'])

        if add_genre in genre_list:
            return  f'Отказано: жанр "{add_genre}" уже существует в базе данных', 405

        genre = genre_service.create(req_json)
        return f'Добавлен новый жанр: "{add_genre}"', 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, gid):
        req_json = request.json
        req_json['name'] = req_json['name'].lower().title()
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        res = req_json['name']
        return f"Жанр обновлен на {res} (пиши, не пиши - 204 код все равно ничего не вернет :-) )", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "Жанр удален... (пиши, не пиши - 204 код все равно ничего не вернет :-) )", 204
