#from com_cheese_api.usr.model.user_dto import UserDto
#from com_cheese_api.usr.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto
from com_cheese_api.usr.user.model.user_dao import UserDao

#from com_cheese_api.util.file import FileReader
from com_cheese_api.cmm.utl.file import FileReader

import numpy as np
import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json
import os


'''
json = json.loads() => dict
dict = json.dumps() => json
'''

'''
서버와 정보를 주고 받는다.
'''

parser = reqparse.RequestParser()

class User(Resource):

    @staticmethod
    def post():
        print('====== user post 요청 받음 ======')
        print(f'[User Signup Resource Enter]')

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
        user = UserDto(**body)
        UserDao.save(user)
        user_id = user.user_id

        return {'mesasge': 'SUCCESS', 'user_id': str(user_id)}, 200

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
            user = UserDao.find_by_id(user_id)

            if user:
                # return jsonify([user.json]), 200
                # GET http://localhost:8080/api/user/1000190
                return user.json
                # return json.dumps(user.json()), 200
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404

    @staticmethod
    def put():
        """
        서버에서 해당 ID 의 새로운 유저 정보를 받아온다.
        정보를 토대로 해당 ID 유저의 정보를 바꿔서
        정보를 서버에 보내준다.
        parameter: 유저 아이디를 받아온다.
        return: 새로운 유저 데이터를 리턴 한다.
        """
        print(f'[User Put Resource Enter]')        
        parser.add_argument('user_id', type=str, required=True, help='This is user_id field')
        parser.add_argument('password', type=str, required=True, help='This is password field')
        parser.add_argument('name', type=str, required=True, help='This is name field')
        parser.add_argument('gender', type=str, required=True, help='This is gender field')
        parser.add_argument('age', type=str, required=True, help='This is age field')
        parser.add_argument('phone')
        parser.add_argument('email')

        print("argument added")

        args = parser.parse_args()
        print(f'User {args["user_id"]} updated')
        print(f'User {args["password"]} updated')

        user = UserDto(args['user_id'],\
                         args['password'],\
                         args['name'],\
                         args['gender'],\
                         args['age'],\
                         args['phone'],\
                         args['email'])

        print("User created")
        UserDao.update(args)
        # data = user.json()
        
        return args, 200

    @staticmethod
    def delete(user_id: str):
        """
        유저 아이디를 받아와 해당 유저를 삭제한다.
        Parameter: 유저 아이디
        DEL http://localhost:8080/api/user/1000190
        """
        # UserDao.delete(id)
        # print(f'User {id} Deleted')
        print(f'[ User Delete Resource Enter ]')
        args = parser.parse_args()
        UserDao.delete(user_id)
        # print(f'User {args["user_id"]} deleted')
        return {'code': 0, 'message': 'DELETE SUCCESS'}, 200

class Users(Resource):

    @staticmethod
    def post():
        print(f'[ User Bulk Resource Enter ]')

        user_count = UserDao.count()

        if user_count[0] == 0:
            UserDao.bulk()
        else:
            print("Users Data exists...")
        
    @staticmethod
    def get():
        print(f'[ User List Resource Enter ]')
        data = UserDao.find_all()
        return jsonify([item.json for item in data])
        # return json.dumps(data), 200