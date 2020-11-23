from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto
from com_cheese_api.cop.rev.review.model.review_dfo import ReviewDfo
from com_cheese_api.ext.db import db, openSession

from sqlalchemy import func, and_, or_

# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB에 있는 데이터 가져오는 작업

Session = openSession()
session = Session()

class ReviewDao(ReviewDto):

    # No value for argument 'review_dfo' 
    # in classmethod callpylint(no-value-for-parameter)
    # @classmethod
    # def bulk(cls, review_dfo):
    #     dfo = review_dfo.create()
    #     print("리뷰 데이터 insert!!!")
    #     print(dfo.head())
    #     session.bulk_insert_mappings(cls, dfo.to_dict(orient="records"))
    #     session.commit()
    #     session.close()

    @staticmethod
    def bulk():
        print(f'========Reviews Data Insert!!!========')
        reviewDfo = ReviewDfo()
        
        df = reviewDfo.review_df_refine(reviewDfo.review_df())
        # df = reviewDfo.review_df()
        print(f'============ Review bulk()!!! ============')
        print(df.head())
        session.bulk_insert_mappings(ReviewDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @classmethod
    def count(cls):
        return session.query(func.count(cls.review_no)).one()

    @staticmethod
    def save(review):
        Session = openSession()
        session = Session()
        session.add(review)
        session.commit()

    @staticmethod
    def update(review):
        session.query(ReviewDto).filter(ReviewDto.review_no == review.review_no)\
            .update({ReviewDto.review_title: review.review_title,
                        ReviewDto.review_detail: review.review_detail})
        session.commit()
        session.close()
        print('[review_dao.py] -> Data Update Complete!')

    @classmethod
    def delete(cls, review_no):
        # cls.query(ReviewDto.review_no == review_no).delete()
        review = cls.query.get(review_no)
        db.session.delete(review)
        db.session.commit()


    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, review_no):
        return session.query(cls).filter(cls.review_no == review_no).one()
        # return cls.query.filter(ReviewDto.review_no == review_no).one()


class ReviewTF():
    ...
    
class ReviewAi():
    ...
