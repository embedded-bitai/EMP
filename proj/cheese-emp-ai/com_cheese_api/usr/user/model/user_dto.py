import numpy as np
import pandas as pd
# from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
# from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto

# from sqlalchemy import func
# from sqlalchemy.ext.declarative import declarative_base

import os
import json

class UserDto(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    # user_no: int = db.Column(db.Integer, primary_key= True, index = True)
    user_id: str = db.Column(db.String(20), primary_key=True, index=True)
    password: str = db.Column(db.String(5))
    name: str = db.Column(db.String(5))
    gender: str = db.Column(db.String(5))
    age: int = db.Column(db.Integer)
    phone: str = db.Column(db.String(20))
    email: str = db.Column(db.String(100))
    # cheese_texture: int = db.Column(db.Integer)
    # buy_count: int = db.Column(db.Integer)

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
    # articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

    # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')
    
    # 관계 설정
    #reviews = db.relationship('ReviewDto', back_populates='users')

    def __init__(self, user_id, password, name, gender, age, phone, email):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f'User(user_id={self.user_id}, password={self.password}, name={self.name}, \
                    gender = {self.gender}, age={self.age}, phone={self.phone}, email={self.email})'

    def __str__(self):
        return f'User(user_id={self.user_id}, password={self.password}, name={self.name}, \
                    gender = {self.gender}, age={self.age}, phone={self.phone}, email={self.email})'

    @property
    def json(self):
        return {
            # 'user_no' : self.user_no,
            'user_id' : self.user_id,
            'password': self.password,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'phone': self.phone,
            'email': self.email
        }

# Json 형태로 쓰기 위해 씀!
class UserVo():
    # user_no: int = 0
    user_id: str = ''
    password: str = ''
    name: str = ''
    gender: str = ''
    age: int = 0
    phone: str = ''
    email: str = ''


# db.init_app(app)
# with app.app_context():
#     db.create_all()