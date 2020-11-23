from com_cheese_api.cop.ord.order.model.order_dto import OrderDto
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json


# 사용 보류 클래스, order_dto.py의 json()과 연관해 오류 발생(+ search.py)
class GenderBest(Resource):
    @staticmethod
    def get():
        print("best.py, GenderBest GET()")
        # print(f'성별: {gender}')
        # print(f'나이: {age}')
        # print(f'치즈 카테고리: {cheese_category}')
        # print(f'치즈 이름: {cheese_name}')
        best = OrderDao.find_cheese_by_gender_count()

        print(f'Gender Best List : {best}')
        print(type(best))

        print(f'Gender Best json : {jsonify(best)}')
        # itemList = []
        # for item in best:
        #         print(f'for문 결과: ', item)
        #         itemList.append(item)
        # print(f'Best List : {itemList}')
        # print(type(itemList))
                
        
        # return jsonify([item.json for item in best])
        return jsonify(best)

class AgeBest(Resource):
    @staticmethod
    def get():
        print("best.py, AgeBest GET()")
        # print(f'성별: {gender}')
        # print(f'나이: {age}')
        # print(f'치즈 카테고리: {cheese_category}')
        # print(f'치즈 이름: {cheese_name}')
        best = OrderDao.find_cheese_by_age_count()

        print(f'Age Best List : {best}')
        print(type(best))

        print(f'Age Best json : {jsonify(best)}')
        # itemList = []
        # for item in best:
        #         print(f'for문 결과: ', item)
        #         itemList.append(item)
        # print(f'Best List : {itemList}')
        # print(type(itemList))
                
        
        # return jsonify([item.json for item in best])
        return jsonify(best)


# class OrderBest(Resource):
#     @staticmethod
#     def get():
#         print("best.py, OrderBest GET()")
#         # print(f'성별: {gender}')
#         # print(f'나이: {age}')
#         # print(f'치즈 카테고리: {cheese_category}')
#         # print(f'치즈 이름: {cheese_name}')
#         best = OrderDao.find_cheese_by_gender_count()

#         print(f'Best List : {best}')
#         print(type(best))

#         print(f'Best json : {jsonify(best)}')
#         # itemList = []
#         # for item in best:
#         #         print(f'for문 결과: ', item)
#         #         itemList.append(item)
#         # print(f'Best List : {itemList}')
#         # print(type(itemList))
                
        
#         # return jsonify([item.json for item in best])
#         return jsonify(best)