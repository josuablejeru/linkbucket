import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('./.env')
load_dotenv(dotenv_path=env_path, verbose=True)


MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')

SERVER_IP = os.environ.get('SERVER')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{SERVER_IP}/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
