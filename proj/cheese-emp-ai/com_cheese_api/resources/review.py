import pandas as pd
from com_cheese_api.util.file import FileReader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from com_cheese_api.ext.db import url, db, openSession, engine
from time import sleep
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import NavigableString

from sklearn.model_selection import train_test_split

import os
from pathlib import Path

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

Session = openSession()
session = Session()

app = Flask(__name__)

config = {
    'user': 'bitai',
    'password': '456123',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'com_cheese_api'
}

charset = {'utf8':'utf8'}

url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"



app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Duck typing 방식(엔티티 별로 분리시키고 모듈화한다. user, cheese, review)

# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================

# 데이터 크롤링 과정
class ReviewKdd():
    
    def __init__(self):
        self.name = ''

    def html_test(self):
        # 테스트
        self.name = '홍'

        html = """
        <div class="inner_view">
            <div class="name_purchase">
                [퀘스크렘] 블루치즈 크림치즈
            </div>
            <div class="review_photo"></div>
            진한 블루치즈 맛이네요    
        </div>
        """

        soup = BeautifulSoup(html, 'html.parser')
        target_tag = soup.select_one('.inner_view')
        print(target_tag.text)

    

    def crawling(self):
        print(self.name)
        # create a new chrome session
        options = Options()

        driver = webdriver.Chrome(options=options, executable_path="/home/bitai/Documents/EMP_Team/EMP_Main/Ai/cheese_flask_proj/chromedriver_linux64/chromedriver")
        driver.maximize_window()

        # 리뷰 페이지 주소
        # 55222 38186 32309 7388 5765 40724 52606 5869 47724 40725
        # URL = 'https://www.kurly.com/shop/goods/goods_review_list.php?goodsno=55222'
        # URL = 'https://www.kurly.com/shop/goods/goods_review_list.php?goodsno=55222&page={}'
        
        # 2 ~ 11 페이지의 내용을 크롤링 한다.(총 10 page)
        URL = 'https://www.kurly.com/shop/goods/goods_review_list.php?goodsno=55222&page={}'

        driver.get(URL)

        # 1.1초간 sleep
        sleep(1.1)

        # 리뷰 페이지 내용
        page = driver.page_source
        page
        

        # 웹사이트 2페이지 결과값
        soup = BeautifulSoup(page, 'html.parser')
        target_tag = soup.select('.inner_review')
        print(target_tag)


        # 제품명 확인
        product_name = soup.select('.name')
        product_name

        #리뷰 작성일 확인
        review_time = soup.select('.time')
        review_time

        # 리뷰 제목 확인
        review_title = soup.select('.fst')
        review_title

        # 조회수 확인
        review_views = soup.select('.review-hit-cnt')
        review_views


        # 2~17page 까지만 진행(range 1,18)
        # 17page(2~18p), 15page는 105개라 발생할 수 있는 더미 데이터까지 감안하면 애매해서 16page
        # -> 17page로 진행(생각보다 이상 데이터가 많다)
        review_list = []

        url_list = [55222, 38186, 32309, 7388, 5765, 40724, 52606, 5869, 47724, 40725]
        page_num = 0

        for url_element in url_list:

            # 2 ~ 11 페이지의 내용을 크롤링 한다.(총 10 page)
            # 2 ~ 3 페이지로 테스트 중 range(2, 4)
            for page_num in range(2, 4):
                URL = f'https://www.kurly.com/shop/goods/goods_review_list.php?goodsno={url_element}&page={page_num}'

                # for n in range(1, 18):
                # print("==1" + url)
                url = URL
                print("==2" + url)
                webpage = urlopen(url)
                
                driver.get(url)
                
                soup = BeautifulSoup(webpage, 'html.parser')
                
                review_details = []
                
                
                # 제품명, 제조사
                product_names = soup.select('.name')
                review_titles = soup.select('.fst')    
                review_times = soup.select('.time')
                review_viewss = soup.select('.review-hit-cnt')


                # 리뷰 상세
                target_tag = soup.select('.inner_review')    
                
                
                for tags in target_tag:
                    
                    webpage = urlopen(url)
                    driver.get(url)
                    soup = BeautifulSoup(webpage, 'html.parser')             
                    
                    cont = ''
                    for tag in tags:
                        if isinstance(tag, NavigableString) and tag != "\n":
                            cont = cont + tag

                    review_details.append(cont)
                    
                    time.sleep(random.uniform(1, 1.1))


                for i in range(0, len(review_titles)):

                    review_row = []

                    review_row.append(product_names[i].text.split('<div'))
                    review_row.append(review_titles[i].text.split('<div'))

                    # 리뷰 상세
                    review_row.append(review_details[i])

                    review_row.append(review_times[i].text.split('<td'))        
                    review_row.append(review_viewss[i].text.split('<span'))

                    review_list.append(review_row)

                    time.sleep(random.uniform(1, 1.1))
        
        print("크롤링 끝!!!")
        review_list



        # csv 파일 다운로드하기
        import csv

        vid_csv_file = open("/home/bitai/Documents/EMP_Team/EMP_Main/Ai/cheese_flask_proj/data_set/cheese2pic_real_part10.csv", "w", newline = "")
        vid_csv_writer = csv.writer(vid_csv_file)


        # 크롤링 데이터를 vs_row에 넣고 돌린다.
        # writerow 메소드로 vs_row를 csv 파일에 한줄씩 반복해서 넣는다.
        for vs_row in review_list:
            vid_csv_writer.writerow(vs_row)
            
        vid_csv_file.close()

if __name__ == "__main__":
    rw = ReviewKdd()
    rw.crawling()

# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

# 데이터 정제 과정
class ReviewDf():
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.user = None
        self.odf = None

    def new(self):
        review = 'cheese_review_panda_2.csv'
        this = self.fileReader
        this.review = self.new_model(review)
        
        # this = ReviewDf.split_str_1(this.review, 'review_views', "[")
        # this = ReviewDf.split_str_0(this.review, 'review_views', "]")
        # this = ReviewDf.split_str_1(this.review, 'review_views', "'")
        # this = ReviewDf.split_str_1(this.review, 'review_detail', "\n")

        this = ReviewDf.cheese_category_norminal(this)

        this = ReviewDf.brand_merge_code(this)
        this = ReviewDf.change_column_name(this)
        print(this.review)


        review_split = ReviewDf.df_split(this.review)

    cheese_data_frame = pd.read_csv(
        '/home/bitai/Documents/EMP_Team/EMP_Main/Ai/cheese_flask_proj/data_set/cheese2pic_real_part10.csv',
        sep=','
    )


        train = 'review_train.csv'
        test = 'review_test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload


        print(this.train)



        self.odf = pd.DataFrame(
            {
                'review_no' : this.train.review_no
            }
        )

        this = ReviewDf.drop_feature(this, 'review_date')

        # this.label = ReviewDf.create_label(this) # payload
        # this.train = ReviewDf.create_train(this) # payload

        df = pd.DataFrame(

            {
                'category': this.train.category,
                'brand' : this.train.brand_code,
                'cheese_name': this.train.product_name,
                'review_title': this.train.review_title,
                'review_detail': this.train.review_detail,
                'review_views': this.train.review_views
                
            }

        )

        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        print(sumdf)
        print(sumdf.isnull().sum())
        print(list(sumdf))
        sumdf.to_csv(os.path.join('data', 'review_fin.csv'), index=False, encoding='utf-8-sig')
        return sumdf


    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))

    # @staticmethod
    # def create_train(this) -> object:
    #     return this.train.drop('name', axis = 1)
        

    # @staticmethod
    # def create_label(this) -> object:
    #     return this.train['name'] # Label is the answer.


    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this

    @staticmethod
    def split_str_0(this, column, part):
        split = this[column].str.split(part)
        this[column] = split.str.get(0)
        return split

    @staticmethod
    def split_str_1(this, column, part):
        split = this[column].str.split(part)
        this[column] = split.str.get(1)
        return split

    @staticmethod
    def change_column_name(this):
        this.review = this.review.rename(columns={"Unnamed: 0": "review_no"})
        return this

    @staticmethod
    def cheese_category_norminal(this) -> object:
        category_map = {
            '크림': 0,
            '모짜렐라': 1,
            '고르곤졸라': 2,
            '리코타': 3,
            '체다': 4,
            '파마산': 5,
            '고다': 6,
            '까망베르': 7,
            '브리': 8,
            '만체고': 9,
            '에멘탈': 10,
            '부라타': 11
        }
        this.review['category'] = this.review['category'].map(category_map)
        return this


    @staticmethod
    def brand_merge_code(this) -> object:
        brand_code = pd.read_csv("data/cheese_brand_code.csv")
        this.review = pd.merge(this.review, brand_code, left_on = 'brand_name', right_on='brand', how = 'left')
        return this

    # 결측값 제거 필요

    @staticmethod
    def df_split(data):
        review_train, review_test = train_test_split(data, test_size = 0.3, random_state = 32)
        review_train.to_csv(os.path.join('data', 'review_train.csv'), index=False)
        review_test.to_csv(os.path.join('data', 'review_test.csv'), index=False)       
        return review_train, review_test


#     # pandas로 가공한 데이터 csv 파일로 다시 저장하기
#     # 
#     # df.to_csv('cheese_review_panda.csv')
#     return df

if __name__ == "__main__":
    reviewDf = ReviewDf()
    reviewDf.new()


# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB로 데이터 전송하는 부분
class ReviewDto(db.Model):

    __tableName__="reviews"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    review_no: int = db.Column(db.Integer, primary_key=True, index=True)
    category: int = db.Column(db.Integer)
    brand: str = db.Column(db.String(255))
    cheese_name: str = db.Column(db.String(255))
    review_title: str = db.Column(db.String(100))
    review_detail: str = db.Column(db.String(500))
    review_views: int = db.Column(db.Integer)

#     user_id = db.Column(db.String(10), db.ForeignKey(ReviewDto.user_id))
#     user = db.relationship('ReviewDto', back_populates='reviews')
#     item_id = db.Column(db.Integer, db.ForeignKey(ItemDto.item_id))
#     item = db.relationship('ItemDto', back_populates='reviews')

    def __init__(self,  review_no, category, brand, cheese_name, review_title, review_detail, review_views):
        self.review_no = review_no,
        self.category = category,
        self.brand = brand,
        self.cheese_name = cheese_name,
        self.review_title = title,
        self.review_detail = review_detail,
        self.review_views = review_views


    def __repr__(self):
        return f'review_no={self.review_no}, category={self.category}, brand={self.brand},\
            cheese_name={self.cheese_name}, review_title={self.review_title}, review_detail={self.review_detail}, \
                review_views={self.review_views}'

    def json(self):
        return {
            'review_no': self.review_no,
            'category': self.category,
            'brand': self.brand,
            'cheese_name': self.cheese_name,
            'review_title': self.review_title,
            'review_detail': self.review_detail,
            'review_views': self.review_views
        }


class ReviewVo():
    review_no: int = 0
    category: str = 0
    brand: int = ''
    cheese_name: str = ''
    review_title: str = ''
    review_detail: str = ''
    review_views: int = 0


db.init_app(app)
with app.app_context():
    db.create_all()

class ReviewDao(ReviewDto):
    @staticmethod
    def bulk():
        reviewDf = ReviewDf()
        df = reviewDf.new()
        print(df.head())
        session.bulk_insert_mappings(ReviewDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

if __name__ == '__main__':
    ReviewDao.bulk()


#     @classmethod
#     def find_all(cls):
#         return cls.query.all()

#     @classmethod
#     def find_by_name(cls, name):
#         return cls.query.filer_by(name == name).all()

#     @classmethod
#     def find_by_id(cls, id):
#         return cls.query,filter(ReviewDto.rev_id == id).one()

#     @staticmethod
#     def save(review):
#         Session = openSession()
#         session = Session()
#         session.add(review)
#         session.commit()

#     @staticmethod
#     def update(review, review_id):
#         Session = openSession()
#         session = Session()
#         session.query(ReviewDto).filter(ReviewDto.rev_id == review.review_id)\
#             .update({ReviewDto.review_title: review.review_title,
#                         ReviewDto.review_detail: review.review_detail})
#         session.commit()

#     @classmethod
#     def delete(cls, rev_id):
#         Session = openSession()
#         session = Session()
#         cls.query(ReviewDto.rev_id == rev_id).delete()
#         session.commit()


# class ReviewTF():
#     ...
    
# class ReviewAi():
#     ...

# if __name__ == '__main__':
#     ReviewDao.bulk()


# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================

# # API로 만드는 부분
# class ReviewApi():
#     def __init__(self):
#         self.parser = reqparse.RequestParser()

#     def post(self):
#         parser = self.parser
#         parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
#         parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
#         parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
#         parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
#         args = parser.parse_args()
#         article = ReviewDto(args['review_title'], args['review_detail'],\
#                             args['user_id'], args['item_id'])
#         try:
#             ReviewDao.save(review)
#             return {'code' : 0, 'message' : 'SUCCESS'}, 200
#         except:
#             return {'message': 'An error occured inserting the review'}, 500

#     @staticmethod
#     def get(id):
#         review = ReviewDao.find_by_id(id)
#         if review:
#             return review.json()
#         return {'message': 'Review not found'}, 404

#     @staticmethod
#     def put(self, review, review_id):
#         parser = self.parser
#         parser.add_argument('rev_id', type=int, required=False, help='This field cannot be left blank')
#         parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
#         parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
#         parser.add_argument('review_title', type=str, required=False, help='This field cannot be left blank')
#         parser.add_argument('review_detail', type=str, required=False, help='This field cannot be left blank')
#         args = parser.parse_args()
#         review = ReviewVo()
#         review.review_title = args['review_title']
#         review.review_detail = args['review_detail']
#         review.rev_id = args['rev_id']
#         try:
#             ReviewDao.update(review, review_id)
#             return {'message': 'Review was Updated Successfully'}, 200
#         except:
#             return {'message': 'An Error Occured Updating the Review'}, 500


# # 리뷰 리스트 
# class Reviews(Resource):
#     def get(self):
#         return {'reivews': list(map(lambda review: review.json(), ReviewDao.find_all()))}
