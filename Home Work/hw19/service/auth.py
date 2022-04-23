from flask_restx import abort
from dao.auth import AuthDAO
from utils import get_hash_password, generate_tokens, decode_token


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def login(self, data: dict):
        user_data = self.dao.get_by_username(data['username'])
        if user_data.username is None:
            abort(401, message='... User NOT found ...')

        hashed_password = get_hash_password(data['password'])
        if user_data.password != hashed_password:
            abort(401, message='Invalid credentials (неверны учетные данные: пароль)')

        tokens: dict = generate_tokens(
            {
                'username': data['username'],
                'role': user_data.role,
            }
        )

        return tokens

    def get_new_tokens(self, refresh_token: str):
        decoded_token = decode_token(refresh_token, refresh_token=True)

        tokens = generate_tokens(
            data={
                'username': decoded_token['username'],
                'role': decoded_token['role']
            }
        )

        return tokens
