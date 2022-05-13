from project.dao.models.user import User
from project.utils import get_hash_password
from sqlalchemy.orm.scoping import scoped_session


class AuthDAO:
    def __init__(self, session: scoped_session):
        self.session = session

    def create(self, user_data: dict):
        user_data['password'] = get_hash_password(user_data['password'])
        return self.create(user_data)

    def get_by_username(self, username):
        res = self.session.query(User).filter(User.username == username).first()
        return res

