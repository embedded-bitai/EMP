from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from bs4.element import NavigableString

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
        for i in range(0, 11):
            print(f'{i+1}')
            
        URL = 'https://www.kurly.com/shop/goods/goods_review_list.php?goodsno=40725&page={}'

        driver.get(URL)

        # 1.25초간 sleep
        sleep(1.25)

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

        for n in range(1, 18):
            # print("==1" + url)
            url = URL.format(n+1)
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
        
        review_list



        # csv 파일 다운로드하기
        import csv

        vid_csv_file = open("/home/bitai/WDOP/proj_my3/cheese_review_crawl_python/cheese2pic_real_part10.csv", "w", newline = "")
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
    import pandas as pd

    cheese_data_frame = pd.read_csv(
        '/home/bitai/Documents/EMP_Team/EMP_Main/Ai/cheese_flask_proj/data_set/cheese_review_for_analysis.csv',
        sep=','
    )


    cheese_data_frame
    cheese_data_frame.head(10)

    # 데이터 행과 열 확인
    cheese_data_frame.shape

    # 타입 확인
    cheese_data_frame.dtypes


    # '[' 제거
    split = df['review_views'].str.split("[")
    df['review_views'] = split.str.get(1)
    split

    # ']' 제거
    split = df['review_views'].str.split("]")
    df['review_views'] = split.str.get(0)
    split

    # "'" 제거
    split = df['review_views'].str.split("'")
    df['review_views'] = split.str.get(1)
    split

    # "\n" 제거
    split = df['review_detail'].str.split("\n")
    df['review_detail'] = split.str.get(1)
    split

    # 결측값 제거 필요


    # pandas로 가공한 데이터 csv 파일로 다시 저장하기
    # 
    # df.to_csv('cheese_review_panda.csv')
    return df

if __name__ == "__main__":
    print()


# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================
# DB로 데이터 전송하는 부분
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
        cls.query(ReviewDto.rev_id == rev_id).delete()
        session.commit()


class ReviewTF():
    ...
    
class ReviewAi():
    ...



# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================

# API로 만드는 부분
class ReviewApi():
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


# 리뷰 리스트 
class Reviews(Resource):
    def get(self):
        return {'reivews': list(map(lambda review: review.json(), ReviewDao.find_all()))}
