from dao.model.user import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        ...

    def get_by_username(self, username):
        res = self.session.query(User).filter(User.username == username).first()
        return res
