import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "]\x82\xe5D6\xc6\xb2 \xb4\x0fb\x85\x94\xec\xf0I\xff\x13\xffs\xef~\xc8'"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False    
