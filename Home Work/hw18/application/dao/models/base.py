from application.database import db


class BaseModal(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
