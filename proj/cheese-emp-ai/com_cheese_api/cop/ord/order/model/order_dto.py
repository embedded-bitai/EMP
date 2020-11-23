from com_cheese_api.ext.db import url, db, openSession, engine
from com_cheese_api.usr.user.model.user_dto import UserDto
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto

from sqlalchemy import func
from sqlalchemy import ForeignKey

import os
import json


class OrderDto(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    order_no: int = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    user_id: str = db.Column(db.String(20), db.ForeignKey(UserDto.user_id)) # FK
    cheese_id: str = db.Column(db.String(30), db.ForeignKey(CheeseDto.cheese_id)) # FK
    # gender: str = db.Column(db.String(5)), User Table
    # age: int = db.Column(db.Integer), User Table
    # cheese_name: str = db.Column(db.String(100))
    # cheese_texture: str = db.Column(db.String(100))
    # cheese_category: str = db.Column(db.String(50))
    buy_count: int = db.Column(db.Integer)
    total_price: int = db.Column(db.Integer)

    # 관계 설정
    # reviews = db.relationship('ReviewDto', back_populates='users', lazy='dynamic')

    def __init__(self, order_no, user_id, cheese_id, buy_count, total_price):
        self.order_no = order_no
        self.user_id = user_id
        self.cheese_id = cheese_id
        self.buy_count = buy_count
        self.total_price = total_price

    def __repr__(self):
        return f'User(order_no={self.order_no}, user_id={self.user_id}, \
                    cheese_id={self.cheese_id}, buy_count={self.buy_count}, total_price={self.total_price})'

    def __str__(self):
        return f'User(order_no={self.order_no}, user_id={self.user_id}, \
                    cheese_id={self.cheese_id}, buy_count={self.buy_count}, total_price={self.total_price})'

    # @property
    def json(self):
        return {
            'order_no': self.order_no, 
            'user_id': self.user_id,
            'cheese_id': self.cheese_id,
            'buy_count': self.buy_count,
            'total_price': self.total_price
            # 'count': self.count
            # 'rank': self.rank
        }

class OrderVo():
    order_no: int = 0
    user_id: str = ''
    cheese_id: str = ''
    buy_count: int = 0
    total_price: int = 0