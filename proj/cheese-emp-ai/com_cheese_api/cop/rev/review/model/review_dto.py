from flask_restful import Resource, reqparse, fields, marshal_with
# from com_cheese_api.usr.user import UserDto
from com_cheese_api.ext.db import db, openSession
from com_cheese_api.usr.user.model.user_dto import UserDto
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseDto

# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB로 접속하는 부분

# review_num,
# category,
# brand_name,
# product_name,
# review_title,
# review_detail,
# review_date,
# review_views

class ReviewDto(db.Model):
    __tablename__="reviews"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    review_no: int = db.Column(db.Integer, primary_key=True, index=True) # PK
    review_title: str = db.Column(db.String(100))
    review_detail: str = db.Column(db.String(500))
    # user_no = db.Column(db.Integer, db.ForeignKey(UserDto.user_no)) # FK(user_no)
    user_id = db.Column(db.String(20), db.ForeignKey(UserDto.user_id)) # FK(user_id)
    cheese_id = db.Column(db.String(30), db.ForeignKey(CheeseDto.cheese_id)) # FK(cheese_id)
    

    # time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # time_created = Column(DateTime(timezone=True), server_default=func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # 관계 설정
    # user = db.relationship('UserDto', back_populates='reviews')
    # cheese = db.relationship('CheeseDto', back_populates='reviews')

    def __init__(self, review_no, review_title, review_detail, user_id, cheese_id):
        self.review_no = review_no
        self.review_title = review_title
        self.review_detail = review_detail
        self.user_id = user_id
        # self.user_no = user_no
        self.cheese_id = cheese_id

    def __repr__(self):
        return f'review_no={self.review_no}, user_id={self.user_id}, cheese_id={self.cheese_id},\
            review_title={self.review_title}, review_detail={self.review_detail}'

    def json(self):
        return {
            'review_no': self.review_no,
            'review_title': self.review_title,
            'review_detail': self.review_detail,
            'user_id': self.user_id,
            # 'user_no': self.user_no,
            'cheese_id': self.cheese_id
        }


class ReviewVo():
    review_no: int = 0
    review_title: str = ''
    review_detail: str = ''
    user_id: str = ''
    cheese_id: int = 0
    # user_no: int = 0
    # name: str = ''
