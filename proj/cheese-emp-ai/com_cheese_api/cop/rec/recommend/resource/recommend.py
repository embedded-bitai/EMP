from com_cheese_api.cop.rec.recommend.model.recommend_dto import RecommendDto
from com_cheese_api.cop.rec.recommend.model.recommend_dao import RecommendDao
from com_cheese_api.cop.rec.recommend.model.recommend_ai import RecommendAi
from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
from com_cheese_api.cop.itm.cheese.model.cheese_dao import CheeseDao
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

        return {'message': 'SUCCESS'}, 200   


    @staticmethod
    def get(user_id: str):
        userId = user_id
        try:
            query = """
                SELECT * FROM recommends WHERE user_id = %(userId)s
            """
            pred_code = RecommendAi().recommend_cheese(query, userId)
            pred_code_str = "".join(map(str, pred_code))
            recommend_cheese_code = 'p' + pred_code_str

            recommend_cheese_info = CheeseDao.find_by_cheese(recommend_cheese_code)
            if recommend_cheese_info:
                return jsonify([recommend_cheese_info.json])
        except Exception as e:
            print(e)
            return {'message': 'Recommend not found'}, 404
            
