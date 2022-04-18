from typing import Dict, Any
from marshmallow import ValidationError
from lib.dao import BaseDAO
from application.dao.models.models import Movie


class MoviesDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, uid: int):
        return self.session.query(Movie).filter(Movie.id == uid).first()

    def update(self, uid: int, data: Dict[str, Any]):
        result = self.session.query(Movie).filter(Movie.id == uid).update(data)
        if result != 1:
            self.session.rollback()  # не обязательно, но можно и с откатом в ручную.
            raise ValidationError(f'Movie with id {uid} not found.')

        self.session.commit()

    def create(self, data: Dict[str, Any]):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie, 201

    def delete(self, uid: int):
        result = self.session.query(Movie).filter(Movie.id == uid).delete()
        if result != 1:
            raise ValidationError(f'Movie with id {uid} not found.')
        self.session.commit()

    def get_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

