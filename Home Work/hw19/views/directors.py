from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json: str = request.json
        req_json['name'] = req_json['name'].lower().title()
        add_director = req_json['name']

        # проверяем есть ли уже такой режиссер
        is_director = director_service.get_all()
        directors_data = DirectorSchema(many=True).dump(is_director)
        directors_list = [] # создаем список всех жанров
        for director_data in directors_data:
            directors_list.append(director_data['name'])

        if add_director in directors_list:
            return  f'Отказано: директор "{add_director}" уже существует в базе данных', 405

        director = director_service.create(req_json)
        return f'Добавлен новый режиссер: "{add_director}"', 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, did):
        req_json = request.json
        req_json['name'] = req_json['name'].lower().title()
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        res = req_json['name']
        return f"Режиссер обновлен на {res} (пиши, не пиши - 204 код все равно ничего не вернет :-) )", 204

    def delete(self, did):
        director_service.delete(did)
        return "... режиссер ... удален ... (пиши, не пиши - 204 код все равно ничего не вернет :-) )", 204
