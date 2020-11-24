from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import NavigableString

# Duck typing 방식(엔티티 별로 분리시키고 모듈화한다. user, cheese, review)

# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================

# 데이터 크롤링 과정
class ReviewKdd(object):
    
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

        driver = webdriver.Chrome(options=options, executable_path="com_cheese_api/chromedriver_linux64/chromedriver")
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
        # print(target_tag)


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
        return review_list



    def save_csv(self, review_list):
        # csv 파일 다운로드하기
        import csv

        vid_csv_file = open('com_cheese_api/cop/rev/review/data/cheese2pic_real_part10.csv', 'w', newline = '')
        vid_csv_writer = csv.writer(vid_csv_file)


        # 크롤링 데이터를 vs_row에 넣고 돌린다.
        # writerow 메소드로 vs_row를 csv 파일에 한줄씩 반복해서 넣는다.
        for vs_row in review_list:
            vid_csv_writer.writerow(vs_row)
            
        vid_csv_file.close()

