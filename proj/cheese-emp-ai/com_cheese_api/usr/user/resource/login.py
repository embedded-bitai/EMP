from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao 
from com_cheese_api.usr.user.model.user_dto import UserVo
import json
from flask import jsonify


class Login(Resource):

    @staticmethod
    def post():        
        print('====== login.py POST(), 로그인 처리 ======')
        print('====== access post 요청 받음 ======')
        parser = reqparse.RequestParser()
        print(f'parser ===> {parser}')

        parser.add_argument('user_id', type=str, required=True, help='user_id field')
        parser.add_argument('password', type=str, required=True, help='password field')
        args = parser.parse_args()
        print(f'args ===> {args}')

        print(f'*********>')

        user = UserVo()
        print(f'user: {user}')

        print(f'[ ID ] {args.user_id} \n [ Password ] {args.password}')
        user.user_id = args.user_id
        user.password = args.password

        user = UserVo()
        user.user_id = args.user_id
        user.password = args.password

        print('ID: ', user.user_id)
        print('Password: ', user.password)

        data = UserDao.login(user)
        print(f'Login Result : {data}\n')

        # return print(f'로그인 성공!!! {data[0]}\n'), 200
        return data[0], 200


    # def get(self):
    #     return {'message': 'Login API Start !!'}