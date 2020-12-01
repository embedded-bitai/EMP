from com_cheese_api.cop.rec.recommend.model.recommend_dto import RecommendDto
from com_cheese_api.cop.rec.recommend.model.recommend_dao import RecommendDao

from com_cheese_api.cmm.utl.file import FileReader

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json


parser = reqparse.RequestParser() 

class Recommend(Resource):

    @staticmethod
    def post():
        args = parser.parse_args()
        print('type(args): ', type(args))
        print('args: ', args)

        body = request.get_json()
        print('type(body): ', type(body))
        print('body: ', body)
        if len(body) == 0:
            return 'No parameter'
        
        body_str = ''
        for key in body.keys():
            body_str += 'key: {}, value: {}<br>'.format(key, body[key])

        # create 구현
        recommend = RecommendDto(**body)
        RecommendDao.save(recommend)
        # recommend_id = recommend.recommend_id

        # return {'message': 'SUCCESS', 'recommend_id': str(recommend_id)}, 200
        return {'message': 'SUCCESS'}, 200   

    @staticmethod
    def get(user_id: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객체
        """
        print('===========user_id=============')
        print(user_id)
        try:
            print(f'User ID is {user_id}')
            recommend = RecommendDao.find_by_id(user_id)
            
            if recommend:
                return jsonify([recommend.json])
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404


    # @staticmethod
    # def put(user_id: str):
    #     """
    #     서버에서 해당 ID 의 새로운 유저 정보를 받아온다.
    #     정보를 토대로 해당 ID 유저의 정보를 바꿔서
    #     정보를 서버에 보내준다.
    #     parameter: 유저 아이디를 받아온다
    #     return: 새로운 유저 데이터를 리턴 한다
    #     """
    #     print(f'[User Put Resource Enter]')        
    #     parser = reqparse.RequestParser() 
    #     parser.add_argument('user_id', type=str, required=True, help='This is user_id field')
    #     parser.add_argument('password', type=str, required=True, help='This is password field')
    #     parser.add_argument('name', type=str, required=True, help='This is name field')
    #     parser.add_argument('gender', type=str, required=True, help='This is gender field')
    #     parser.add_argument('age', type=str, required=True, help='This is age field')
    #     parser.add_argument('phone')
    #     parser.add_argument('email')

    #     print("argument added")

    #     args = parser.parse_args()
    #     print(f'User {args["user_id"]} updated')
    #     print(f'User {args["password"]} updated')

    #     user = UserDto(args['user_id'],\
    #                      args['password'],\
    #                      args['name'],\
    #                      args['gender'],\
    #                      args['age'],\
    #                      args['phone'],\
    #                      args['email'])

    #     print("User created")
    #     UserDao.update(args)
    #     # data = user.json()
        
    #     return args, 200

    # @staticmethod
    # def delete(user_id: str):
    #     """
    #     유저 아이디를 받아와 해당 유저를 삭제한다.
    #     Parameter: 유저 아이디
    #     """
    #     # UserDao.delete(id)
    #     # print(f'User {id} Deleted')
    #     print(f'[ User Delete Resource Enter ]')
    #     args = parser.parse_args()
    #     print(args)
    #     UserDao.delete(user_id)
    #     # print(f'User {args["user_id"]} deleted')
    #     return {'code': 0, 'message': 'DELETE SUCCESS'}, 200
