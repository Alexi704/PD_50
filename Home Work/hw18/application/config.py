import os


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "test.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

