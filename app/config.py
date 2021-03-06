import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost/linkbucket'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
