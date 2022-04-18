from sqlalchemy.orm import relationship
from application.dao.models.base import BaseModal
from application.database import db


class Genre(BaseModal):
    __tablename__ = 'genres'
    name = db.Column(db.String)


class Director(BaseModal):
    __tablename__ = 'directors'
    name = db.Column(db.String)


class Movie(BaseModal):
    __tablename__ = 'movies'

    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

    director = relationship('Director')
    genre = relationship('Genre')

