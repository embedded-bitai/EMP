
from flask_restful import Resource, reqparse
from com_cheese_api.ext.db import db, openSession
from com_cheese_api.resources.user import UserDto
from com_cheese_api.resources.item import ItemDto

class ReviewDto(db.Model):
    __tableName__="reviews"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    rev_id: int = db.Column(db.Integer, primary_key=True, index=True)
    review_title: str = db.Column(db.String(100))
    review_detail: str = db.Column(db.String(500))

    user_id = db.Column(db.String(10), db.ForeignKey(UserDto.user_id))
    user = db.relationship('UserDto', back_populates='reviews')
    item_id = db.Column(db.Integer, db.ForeignKey(ItemDto.item_id))
    item = db.relationship('ItemDto', back_populates='reviews')

    def __init__(self, title, review_detail, user_id, item_id):
        self.review_title = title
        self.review_detail = review_detail
        self.user_id = user_id
        self.item_id = item_id

    def __repr__(self):
        return f'rev_id={self.rev_id}, user_id={self.user_id}, item_id={self.item_id},\
            review_title={self.review_title}, review_detail={self.review_detail}'

    def json(self):
        return {
            'rev_id': self.rev_id,
            'user_id': self.user_id,
            'item_id': self.item_id,
            'review_title': self.review_title,
            'review_detail': self.review_detail
        }

class ReviewVo():
    rev_id: int = 0
    user_id: str = ''
    item_id: int = 0
    review_title: str = ''
    review_detail: str = ''

class ReviewDao(ReviewDto):

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query,filter(ReviewDto.rev_id == id).one()

    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        session.add(review)
        session.commit()

    @staticmethod
    def update(review, review_id):
        Session = openSession()
        session = Session()
        session.query(ReviewDto).filter(ReviewDto.rev_id == review.review_id)\
            .update({ReviewDto.review_title: review.review_title,
                        ReviewDto.review_detail: review.review_detail})
        session.commit()

    @classmethod
    def delete(cls, rev_id):
        Session = openSession()
        session = Session()
        session = Session()
        cls.query(ReviewDto.rev_id == rev_id).delete()
        session.commit()



class Review(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        parser = self.parser
        parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        article = ReviewDto(args['review_title'], args['review_detail'],\
                            args['user_id'], args['item_id'])
        try:
            ReviewDao.save(review)
            return {'code' : 0, 'message' : 'SUCCESS'}, 200
        except:
            return {'message': 'An error occured inserting the review'}, 500
    @staticmethod
    def get(id):
        review = ReviewDao.find_by_id(id)
        if review:
            return review.json()
        return {'message': 'Review not found'}, 404
    @staticmethod
    def put(self, review, review_id):
        parser = self.parser
        parser.add_argument('rev_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        review = ReviewVo()
        review.review_title = args['review_title']
        review.review_detail = args['review_detail']
        review.rev_id = args['rev_id']
        try:
            ReviewDao.update(review, review_id)
            return {'message': 'Review was Updated Successfully'}, 200
        except:
            return {'message': 'An Error Occured Updating the Review'}, 500


class Reviews(Resource):
    def get(self):
        return {'reivews': list(map(lambda review: review.json(), ReviewDao.find_all()))}
# # ==============================================================
# # ====================                     =====================
# # ====================         KDD         =====================
# # ====================                     =====================
# # ==============================================================
# class UserKdd(db.Model):
#     ...

# # ==============================================================
# # =====================                  =======================
# # =====================    Preprocessing =======================
# # =====================                  =======================
# # ==============================================================

# class UserDf():
#     ...

# # ==============================================================
# # =======================                =======================
# # =======================    Modeling    =======================
# # =======================                =======================
# # ==============================================================

# class UserDto(db.Model):
#     ...

# class UserVo(db.Model):
#     ...

# class UserTf(db.Model):
#     ...

# class UserAi(db.Model):
#     ...

# # ==============================================================
# # =====================                  =======================
# # =====================    Resourcing    =======================
# # =====================                  =======================
# # ==============================================================


# class User(db.Model):
#     ...