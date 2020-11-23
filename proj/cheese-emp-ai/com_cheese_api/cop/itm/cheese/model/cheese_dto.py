from com_cheese_api.ext.db import url, db, openSession, engine
# from com_cheese_api.util.file import FileReader
# from com_cheese_api.cmm.utl.file import FileReader

# from flask import Response, jsonify
# from flask_restful import Resource, reqparse

import json
# from typing import List
# from pathlib import Path


class CheeseDto(db.Model):
    __tablename__='cheeses'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    # cname -> name으로 바꿈
    # cname으로 하면 DB에 NULL 값이 들어감
    
    cheese_id : str = db.Column(db.String(30), primary_key=True, index=True)
    name : str = db.Column(db.String(30), primary_key=True)
    ranking : int = db.Column(db.Integer)
    category: str = db.Column(db.String(30))
    brand : str = db.Column(db.String(30))
    content : str = db.Column(db.String(100))
    texture : str = db.Column(db.String(30))
    types : str = db.Column(db.String(30))
    price : int = db.Column(db.Integer)
    img : str = db.Column(db.String(255))

    # diary = db.relationship('DiaryDto', lazy='dynamic')
    # orders = db.relationship('OrderDto', back_populates='cheese', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='cheese', lazy='dynamic')

    def __init__(self, cheese_id, ranking, category, brand, name, content, texture, types, price, img): 
        self.cheese_id = cheese_id
        self.ranking = ranking
        self.category = category
        self.brand = brand
        self.name = name
        self.content = content
        self.texture = texture
        self.types = types
        self.price = price
        self.img = img

    def __repr__(self):
        return f'cheese(cheese_id={self.cheese_id}, ranking={self.ranking}, category={self.category}, \
                    brand={self.brand}, name={self.name}, content={self.content}, texture={self.texture}, \
                        types={self.types}, price={self.price}, img={self.img})'

    def __str__(self):
        return f'cheese(cheese_id={self.cheese_id}, ranking={self.ranking}, category={self.category}, \
                    brand={self.brand}, name={self.name}, content={self.content}, texture={self.texture}, \
                        types={self.types}, price={self.price}, img={self.img})'

    @property
    def json(self):
        return {
            'cheese_id':self.cheese_id, 
            'ranking':self.ranking, 
            'category':self.category,
            'brand':self.brand,
            'name':self.name,
            'content':self.content,
            'texture':self.texture,
            'types':self.types,
            'price':self.price,
            'img':self.img
        }

class CheeseVo(object):
    cheese_id : ''
    ranking : 0
    category: ''
    brand: ''
    name: ''
    content: ''
    texture : ''
    types: ''
    price: 0
    img : ''