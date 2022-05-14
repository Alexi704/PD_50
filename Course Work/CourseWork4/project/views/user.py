from flask import request
from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import UsersService
from project.setup_db import db

user_ns = Namespace("user")


@user_ns.route("/<int:user_id>")
class UserView(Resource):
    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def get(self, user_id: int):
        """Get user by id"""
        try:
            return UsersService(db.session).get_item_by_id(user_id)
        except ItemNotFound:
            abort(404, message="User not found")

    @user_ns.response(200, "OK")
    @user_ns.response(404, "User not found")
    def patch(self, user_id: int):
        """ изменяем информацию о пользователе через его id """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = user_id
        UsersService(db.session).update(request.json)
        return "", 204