# from com_cheese_api.cop.chs.model.cheese_dto import CheeseDto
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto, CheeseVo
from com_cheese_api.cop.itm.cheese.model.cheese_dfo import CheeseDfo
from com_cheese_api.ext.db import url, db, openSession, engine
# from com_cheese_api.cmm.utl.file import FileReader

from sqlalchemy import func, and_, or_

# from flask import request, Response, jsonify
# from flask_restful import Resource, reqparse

# import pandas as pd
# import numpy as np
import json
import os
import sys
from typing import List
from pathlib import Path


Session = openSession()
session = Session()

class CheeseDao(CheeseDto):

    # @classmethod
    # def bulk(cls, cheese_dfo):
    #     # cheeseDfo = CheeseDfo()
    #     # df = CheeseDfo.new()
    #     dfo = cheese_dfo.create()
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        print("========cheese DAO 1========")
        cheeseDfo = CheeseDfo()
        df = cheeseDfo.cheese_df()
        print("========cheese DAO 2========")
        print(df.head())
        session.bulk_insert_mappings(CheeseDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.cheese_id)).one()

    @staticmethod
    def save(cheese):
        Session = openSession()
        session = Session()
        session.add(cheese)
        session.commit()


    @classmethod
    def find_all(cls):
        #cheese = session.query(CheeseVo).all()
        return cls.query.all()

    @classmethod
    def find_by_cheese(cls, cheese_id):
        # rst = cls.query.filter(cls.cheese_id == cheese_id).one()
        # print(f'find_by_cheese {rst}')
        return session.query(cls).filter(cls.cheese_id == cheese_id).one()
        # return session.query(func.filter(cls.cheese_id == cheese_id)).one()

    # @classmethod
    # def find_by_category(cls, category):
    #     # return session.query(cls).filter(cls.category == category).all()
    #     return session.query(cls).filter(cls.category.like(category)).all()

    @classmethod
    def find_by_category(cls, category):
        # return session.query(cls).filter(cls.category == category).all()
        print("================find_by_category()================")
        return session.query(cls).filter(cls.category.like(f'%{category}%')).all()

    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name == name).all()

    # @classmethod
    # def update(cls, cheese):
    #     session.query(cls).filter(cls.cheese_id == cheese['cheese_id'])\
    #         .update({cls.ranking:cheese['ranking'],\
    #             cls.category:cheese['category'],\
    #             cls.brand:cheese['brand'],\
    #             cls.name:cheese['name'],\
    #             cls.content:cheese['content'],\
    #             cls.texture:cheese['texture'],\
    #             cls.types:cheese['types'],\
    #             cls.price:cheese['price'],\
    #             cls.img:cheese['img']})
                
    #     session.add(cheese)
    #     session.commit()
    #     session.close()
    #     print('[cheese_dao.py] -> Data Update Complete!!!')

    @staticmethod
    def update(cheese):
        session.query(CheeseDto).filter(CheeseDto.cheese_id == cheese['cheese_id'])\
            .update({CheeseDto.ranking:cheese['ranking'],\
                CheeseDto.category:cheese['category'],\
                CheeseDto.brand:cheese['brand'],\
                CheeseDto.name:cheese['name'],\
                CheeseDto.content:cheese['content'],\
                CheeseDto.texture:cheese['texture'],\
                CheeseDto.types:cheese['types'],\
                CheeseDto.price:cheese['price'],\
                CheeseDto.img:cheese['img']})

        # session.add(cheese)
        session.commit()
        session.close()
        print('[cheese_dao.py] -> Data Update Complete!!!')


    @classmethod
    def delete(cls, cheese_id):
        cheese = cls.query.get(cheese_id)
        db.session.delete(cheese)
        db.session.commit()


# if __name__ == '__main__':
#     CheeseDao.bulk()