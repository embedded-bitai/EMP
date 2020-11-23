from flask.globals import request
from flask_restful import Resource, reqparse
from com_cheese_api.usr.user.model.user_dao import UserDao
from com_cheese_api.usr.user.model.user_dto import UserDto

class SignUp(Resource):
    # self, user_id, password, name, gender, age, phone, email
    @staticmethod
    def post():
        """
        유저 정보를 받아와 새로운 유저를 생성해 준다.
        """
        print("-------- signup.py --------\n")
        body = request.get_json()
        print('type(body): ', type(body))
        print('body:' , body)

        user = UserDto(**body)
        print(f'[ user Dto ] {user}')

        print('아이디: ', user.user_id)
        print('비밀번호: ', user.password)
        print('이름: ', user.name)
        print('성별: ', user.gender)
        print('나이: ', user.age)
        print('핸드폰 번호: ', user.phone)
        print('이메일: ', user.email)
        
        try:
            UserDao.register(user)
            return "worked.."
        except Exception as e:
            return e