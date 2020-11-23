# ORM 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from flask_marshmallow import Marshmallow

db = SQLAlchemy()


config = {
    'user': 'bitai',
    'password': '456123',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'com_cheese_api',
    'auth_plugin': 'mysql_native_password'
}

charset = {'utf8':'utf8'}

url = f"mysql+mysqlconnector://{ config['user'] }:{ config['password'] }@{ config['host'] }:{ config['port'] }/{ config['database'] }?charset=utf8"
Base = declarative_base()
engine = create_engine(url)


def openSession():
    return sessionmaker(bind = engine)

# openSession()