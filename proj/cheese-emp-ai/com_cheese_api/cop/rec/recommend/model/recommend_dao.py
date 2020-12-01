from com_cheese_api.cop.rec.recommend.model.recommend_dto import RecommendDto
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sqlalchemy import func
from sqlalchemy import and_, or_
from sqlalchemy.ext.declarative import declarative_base

import os
import json


Session = openSession()
session = Session()


class RecommendDao(RecommendDto):
    @staticmethod
    def save(recommend):
        session.add(recommend)
        session.commit()

    @classmethod
    def update(cls, recommend):
        session.query(cls).filter(cls.recommend_id == recommend['recommen_id'])\
                                .update({cls.chooseFood_1: recommend['chooseFood_1'],\
                                        cls.chooseFood_2: recommend['chooseFood_2'],\
                                        cls.user_id: recommend['user_id']})
        session.commit()
        session.close()

    @staticmethod
    def register(recommend):
        print("------ sign up ------")
        db.session.add(recommend)
        db.session.commit()

    @classmethod
    def delete(cls, recommend_id):
        data = cls.query.get(recommend_id)
        db.session.delete(data)
        db.session.commit()
        db.session.close()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.recommend_id)).one()

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, user_id):
        """
        주어진 아이디를 토대로 유저를 찾아서
        해당 정보를 리턴해준다.
        """
        return session.query(cls).filter(cls.user_id.like(f'{user_id}')).first()

        # return session.query(UserDto).filter(UserDto.user_id.like(f'{user_id}')).one()
