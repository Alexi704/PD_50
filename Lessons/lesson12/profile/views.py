from flask import Blueprint

profile_blueprint = Blueprint('profile_blueprint', __name__, url_prefix='/profile')


@profile_blueprint.route('/<int:user_id>')
def profile_page(user_id):
    return f"Я страничка пользователя {user_id}"
