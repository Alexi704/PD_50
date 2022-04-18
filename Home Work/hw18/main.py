from flask import Flask
from application.config import Config
from application.database import db
from flask_restx import Api

from application.views.directors import directors_ns
from application.views.genres import genres_ns
from application.views.movies import movies_ns


def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    return app


def configure_app(app: Flask):
    db.init_app(app)
    # db.drop_all()
    db.create_all()
    api = Api(app, prefix='/api', doc='/docs')
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app_ = creat_app()
    configure_app(app_)
    app_.run()
