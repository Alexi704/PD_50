class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


