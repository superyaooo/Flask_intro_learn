import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "(it's a secret)"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False    
