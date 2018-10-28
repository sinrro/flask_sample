import os
import logging
from logging.config import dictConfig


class Config:
    SECRET_KEY = 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # MySQL config
    MYSQL_DATABASE = 'flask_test'
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_HOST = '127.0.0.1'

    # 子类实现该方法
    @staticmethod
    def init_app(app):
        dictConfig(loggingBaseConfig)
        # pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD,
                                                                   Config.MYSQL_HOST, Config.MYSQL_DATABASE)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD,
                                                                   Config.MYSQL_HOST, Config.MYSQL_DATABASE)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig,

    'default': DevelopmentConfig
}

loggingBaseConfig = {
    'version': 1,
    'formatters': {'default': dict(format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        # "console": {
        #     "class": "logging.StreamHandler",
        #     "level": "DEBUG",
        #     "formatter": "default",
        #     "stream": "ext://sys.stdout"
        # },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "default",
            "filename": "log/info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "default",
            "filename": "log/errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'info_file_handler', 'error_file_handler']
    }
}
