from flask_restful import Resource, reqparse
from flask import request, jsonify
# from com_cheese_api.cop.itm.cheese.model.cheese_ai import CheeseAi
from com_cheese_api.cop.chat.chatbot.model.chatbot_dao import ChatbotDao
from com_cheese_api.cop.chat.chatbot.model.chatbot_dto import ChatbotDto

import json



parser = reqparse.RequestParser() 

class Chatbot(Resource):
    # @staticmethod
    # def post():
    #     print("들어옴")
    #     ai = CheeseAi()
    #     args = request.get_json()
    #     print(args)
    #     args = [args[i]['value'] for i in args.keys()]
    #     print(args)
    #     name = ai.train_actors(args)
    #     print(name)
    #     return name

    # @staticmethod
    # def load_model():
    #     print('=== load_model ===')


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
        chatbot = ChatbotDto(**body)
        ChatbotDao.save(chatbot)
        chatbot_id = chatbot.chatbot_id

        return {'message': 'SUCCESS', 'chatbot_id': str(chatbot_id)}, 200

    # @staticmethod
    # def get(user_id: str):
    #     """
    #     유저 아이디를 받아와 해당 유저 객채를 리턴한다
    #     Parameter: User ID 를 받아온다
    #     return: 해당 아이디 유저 객체
    #     """
    #     print('===========user_id=============')
    #     print(user_id)
    #     try:
    #         print(f'User ID is {user_id}')
    #         chatbot = ChatbotDao.find_by_id(user_id)
            
    #         if chatbot:
    #             return jsonify([chatbot.json])
    #     except Exception as e:
    #         print(e)
    #         return {'message': 'User not found'}, 404

        