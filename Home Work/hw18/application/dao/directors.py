from typing import Dict, Any
from marshmallow import ValidationError
from lib.dao import BaseDAO
from application.dao.models.models import Director


class DirectorsDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, uid: int):
        return self.session.query(Director).filter(Director.id == uid).first()

    def update(self, uid: int, data: Dict[str, Any]):
        result = self.session.query(Director).filter(Director.id == uid).update(data)
        if result != 1:
            self.session.rollback()  # не обязательно, но можно и с откатом в ручную.
            raise ValidationError(f'Movie with id {uid} not found.')

        self.session.commit()

    def create(self, data: Dict[str, Any]):
        new_movie = Director(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie, 201

    def delete(self, uid: int):
        result = self.session.query(Director).filter(Director.id == uid).delete()
        if result != 1:
            raise ValidationError(f'Movie with id {uid} not found.')
        self.session.commit()
