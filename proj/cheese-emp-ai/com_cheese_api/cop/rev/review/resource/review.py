from flask.globals import request
from flask_restful import Resource, reqparse, fields, marshal_with
from com_cheese_api.cop.rev.review.model.review_dao import ReviewDao
from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto, ReviewVo

import json

'''
결과물 적어서 남겨놓기
'''

# 웹크롤링, 텍스트 마이닝 -> 데이터 마이닝

# 마일드 스톤(미국 도로보면 지역의 경계에 웰컴 어디어디 지역명 적어놓은것)
# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================


review_fields = {
    'review_no': fields.Integer,
    'review_title': fields.String,
    'review_detail': fields.String,
    'user_no': fields.Integer,
    'item_id': fields.Integer
}
# ==============================================================
# ====================                     =====================
# ====================        Review       =====================
# ====================                     =====================
# ==============================================================

parser = reqparse.RequestParser()

# API로 만드는 부분
class Review(Resource):

    # def __init__(self):
    #     self.parser = reqparse.RequestParser()
    
    @staticmethod
    def post():
        print(f'=========== Review POST()!!! ===========\n')
        body = request.get_json()
        review = ReviewDto(**body)
        ReviewDao.save(review)
        review_no = review.review_no

        return {'review_no': int(review_no)}, 200

        # try:
        #     ReviewDao.save(review)
        #     return {'code' : 0, 'message' : 'SUCCESS'}, 200
        # except:
        #     return {'message': 'An error occured inserting the review'}, 500

    @staticmethod
    def get(review_no: int):
        print(f'=========== Review GET()!!! ===========\n')
        review = ReviewDao.find_by_id(review_no)

        if review:
            return review.json()
        return {'message': 'Review not found'}, 404

    @staticmethod
    def put():
        print(f'=========== Review PUT()!!! ===========\n')
        parser.add_argument('review_no')
        parser.add_argument('review_title')
        parser.add_argument('review_detail')
        parser.add_argument('user_no')
        parser.add_argument('cheese_id')

        args = parser.parse_args()
        print(f'===== args 1 =====\n{args}')

        review = ReviewDto(args['review_no'],\
                            args['review_title'],\
                            args['review_detail'],\
                            args['user_no'],\
                            args['cheese_id'])
        print(f'===== args 2 =====\n{args}')

        try:
            print(f'===== {review} =====\n')
            ReviewDao.update(args)
            return {'code': 0, 'message': 'SUCCESS'}, 200

        except Exception as e:
            print(e)
            return {'message': 'Update Fail!!'}, 500
            

    @staticmethod
    def delete():
        print(f'=========== Review DELETE() !!! ===========\n')
        try:
            params = json.loads(request.get_data(), encoding='utf-8')

            # ???
            ReviewDao.delete(params['review_no'])
            print('\n=== deleted ===')
            return {'message': 'SUCCESS'}, 200

        except Exception as e:
            return {'message': 'NOT FOUND DATA'}, 404


# ==============================================================
# ====================                     =====================
# ====================       Reviews       =====================
# ====================                     =====================
# ==============================================================

# 리뷰 리스트 
class Reviews(Resource):

    # def __init__(self):
    #     self.parser = reqparse.RequestParser()

    @marshal_with(review_fields)
    def post(self):
        print(f'========== Reviews POST() HEAD ==========')

        review_count = ReviewDao.count()

        if review_count[0] == 0:
            ReviewDao.bulk()
        else:
            print("Reviews Data exists...")

    def get(self):
        return {'reivews': list(map(lambda review: review.json(), ReviewDao.find_all()))}


    # @staticmethod
    # def put(self, review, review_no):
    #     parser = self.parser
    #     parser.add_argument('review_no', type=int, required=False, help='This field cannot be left blank')
    #     # parser.add_argument('user_no', type=int, required=False, help='review user_no..')
    #     # parser.add_argument('item_id', type=int, required=False, help='review item_id..')
    #     parser.add_argument('review_title', type=str, required=False, help='review review_title..')
    #     parser.add_argument('review_detail', type=str, required=False, help='review review_detail..')
        
    #     args = parser.parse_args()
    #     review = ReviewVo()
    #     review.review_no = args['review_no']
    #     review.review_title = args['review_title']
    #     review.review_detail = args['review_detail']

    #     try:
    #         ReviewDao.update(review, review_no)
    #         return {'message': 'Review Updated Success!!'}, 200
    #     except:
    #         return {'message': 'Review Updated Fail!!'}, 500