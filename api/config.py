class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "9609f734-00c8-48fa-9425-8c865778410e"
    PROPAGATE_EXCEPTIONS = True
    #     JWT
    JWT_SECRET_KEY = "bedf0efd-67d4-45fc-becf-fc7bb727ab07"


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/PseudoElephant"


class TestingConfig(Config):
    TESTING = True
