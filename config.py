import os


def get_env_variable(name):
    try:
        return os.getenv(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


# import .env variables for DB connection
# TODO: Unify these ENV variables by pulling from different dot files
def get_env_db_url(env_setting):
    if env_setting == "development":
        return os.getenv('SQLALCHEMY_DATABASE_URI')
    elif env_setting == "testing":
        return os.getenv('TEST_SQLALCHEMY_DATABASE_URI')
    elif env_setting == "production":
        return os.getenv('PROD_SQLALCHEMY_DATABASE_URI')


# DB URLS for each Environment
DEV_DB_URL = get_env_db_url("development")
TESTING_DB_URL = get_env_db_url("testing")
PROD_DB_URL = get_env_db_url("production")


class Config(object):
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL
    DEBUG = False
    TESTING = False
