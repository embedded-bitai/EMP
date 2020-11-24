import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from com_cheese_api.cmm.utl.file import FileReader

from com_cheese_api.ext.db import url, db, openSession, engine
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import seaborn as sns
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm

import os
import json

# 코드 실행시 생성되는 파일목록
# user_df.csv

# user_df 등 user csv 데이터의 컬럼명이 user_index -> user_no로 바뀜, 고쳐야 함

class OrderDfo:
    def __init__(self):
        self.fileReader = FileReader()
        # self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/m_data')
        self.data = os.path.join('com_cheese_api/cop/ord/order/data')
        self.odf = None
    
    def new(self):
        user = 'users.csv'
        cheese = pd.read_csv('com_cheese_api/cop/itm/cheese/data/cheese_data.csv')
        this = self.fileReader
        this.user = self.new_model(user) # payload

        print(this)

        category_count = OrderDfo.category_count(this.user)
        item_count = OrderDfo.item_count(this.user, category_count)
        this.user = OrderDfo.change_to_cheese(cheese, item_count)
        print(f'######## 치즈 상품 대체 체크 ##########')

        print(this)

        this = OrderDfo.user_gender_nominal(this)
        this = OrderDfo.cheese_rank_ordinal(this)

        # print(min(this.user['user_age'])) # 고객 최소 나이 : 10
        # print(max(this.user['user_age'])) # 고객 최대 나이 : 80
        # this = OrderDfo.user_age_nominal(this)
        print(f'######## age 전처리 체크 ##########')
        print(this.user.head(10))
        # this = OrderDfo.cheese_code_numeric(this)
        # this = OrderDfo.cheese_code_ordinal(this)
        this = OrderDfo.buy_count_numeric(this)
        # this = OrderDfo.cheese_category_nominal(this)
        # this = OrderDfo.cheese_texture_nominal(this)
        print(f'######## cheese, count 전처리 체크 ##########')
        print(this.user.head(10))

        this = OrderDfo.user_price_numeric(this)
        this = OrderDfo.total_buy_price(this)

        # print(f'Preprocessing User Dataset : {this.user}')

        print(f'######## train na 체크 ##########')
        print(f'{this.user.isnull().sum()}')
        print(f'######## test na 체크 ##########')
        print(f'{this.user.isnull().sum()}')
        print(f'######## data type 체크 ##########')
        print(this.user.dtypes)

        self.odf = pd.DataFrame(
            {
                # 'order_no': this.user.order_no, # duplicate 오류
                'user_id': this.user.user_id,
                'cheese_id': this.user.cheese_id,
                'buy_count': this.user.buy_count,
                'total_price': this.user.total_price
            }
        )

        self.odf.to_csv(os.path.join('com_cheese_api/cop/ord/order/data', 'user_order.csv'), index=False, encoding='utf-8-sig')
        print(f'######## 최종 user DF 결과 ##########')
        print(self.odf)
        return self.odf


    ################## 데이터 불러오기 & 생성 & featrue 제거 ###################

    # self, 메모리에 적재
    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))


    ####################### 원본 데이터를 치즈 구매 데이터 변환 #######################
    
    # 밑에 make_barplot()을 이용해서 시각화 가능. 
    @staticmethod
    def find_requency(data, column1, column2):
        count_size = data[column1].groupby(data[column2]).count().reset_index(name='counts')
        count_size['rank'] = count_size['counts'].rank(ascending=False)
        show_barplot = OrderDfo.make_barplot(column2, 'counts', count_size)
        return count_size

    @staticmethod
    def category_count(data) -> object:
        sub_size = data['buy_count'].groupby(data['sub1_category']).sum().reset_index(name='sub1_counts')
        sub_size['sub1_rank'] = sub_size['sub1_counts'].rank(ascending=False)
        # barplot = OrderDfo.make_barplot('sub1_category', 'sub1_counts', sub_size)
        return sub_size

    @staticmethod
    def item_count(data, category_count):
        item_size = data['buy_count'].groupby([data['sub1_category'],data['sub2_category']]).sum().reset_index(name='sub2_counts')
        item_size['sub2_rank'] = item_size['sub2_counts'].rank(ascending=False, method="dense")

        category_item_rank = pd.merge(category_count, item_size, on='sub1_category', how='right')
        user_item_rank = pd.merge(data, category_item_rank, on='sub2_category', how='left')
        # print(user_item_rank)

        user_items_ranks = user_item_rank.drop(['sub1_category_y'], axis=1)
        users_item_data = user_items_ranks.rename(columns={'sub1_category_x': 'sub1_category'})
        # print(users_item_data)

        return users_item_data

    @staticmethod
    def change_to_cheese(data, item_count):
        cheese_df = data.rename(columns={'ranking': 'sub2_rank'})
        user_cheese_merge = pd.merge(item_count, cheese_df, on='sub2_rank', how='left')
        user_data1 = user_cheese_merge.drop(['item_code', 'item_name', 'item_add_name', 'category_x',\
                                            'sub1_category', 'sub2_category', 'item_brand', 'sub1_counts', 'sub1_rank',\
                                            'sub2_counts', 'buy_price'], axis=1)
        user_data2 = user_data1.drop(['country', 'matching', 'content', 'img'], axis=1)
        user_data_fin = user_data2.rename(columns={'Unnamed: 0_x': 'order_no', 'Unnamed: 0_y': 'cheese_code',\
                                            'brand': 'cheese_brand', 'name': 'cheese_name', 'price': 'cheese_one_price',\
                                            'sub2_rank': 'cheese_rank', 'category_y': 'cheese_category', 'texture': 'cheese_texture', 'types': 'cheese_types'})
        # print(list(users_cheese_merge))
        # print(user_data_fin)
        # user_data_fin.to_csv(os.path.join('com_cheese_api/cop/ord/order/data', 'user_df.csv'), index=False, encoding='utf-8-sig')
        return user_data_fin


    
    ####################### 데이터 정제 #######################

    @staticmethod
    def cheese_rank_ordinal(this) -> object:
        return this

    @staticmethod
    def user_gender_nominal(this) -> object:
        gender_mapping = {'M': 0, 'F': 1}
        this.user['gender'] = this.user['user_gender'].map(gender_mapping)
        this.user = this.user # overriding
        # this.user.to_csv(os.path.join('data', 'check11.csv'), index=False, encoding='utf-8-sig')
        return this

    @staticmethod
    def cheese_code_numeric(this) -> object:
        this.user['cheese_id'] = this.user['cheese_id'].str.replace('p', '')
        return this

    @staticmethod
    def user_price_numeric(this) -> object:
        this.user['cheese_one_price'] = this.user['cheese_one_price'].str.replace(',', '')
        this.user['cheese_one_price'] = this.user['cheese_one_price'].str.replace('원', '')
        this.user = this.user.astype({'cheese_one_price': int})
        this.user = this.user
        return this

    @staticmethod
    def cheese_code_ordinal(this) -> object:
        return this

    @staticmethod
    def total_buy_price(this) -> object:
        this.user['total_price'] = this.user['cheese_one_price'] * this.user['buy_count']
        return this

    @staticmethod
    def buy_count_numeric(this) -> object:
        return this



'''
       order_no  user_id password gender  age  cheese_name cheese_texture cheese_category  buy_count  total_price
0             0  2391853        1      M   40       리코타 치즈          후레쉬치즈             리코타          1         4600
1             1  1799897        1      F   40       리코타 치즈          후레쉬치즈             리코타          1         4600
2             2  1614947        1      F   50         모짜렐라          후레쉬치즈            모짜렐라          1         5500
3             3  1614947        1      F   50         모짜렐라          후레쉬치즈            모짜렐라          1         5500
4             4  1614947        1      F   50         모짜렐라          후레쉬치즈            모짜렐라          5        24500
...         ...      ...      ...    ...  ...          ...            ...             ...        ...          ...
36868     36868  6159545        1      F   30      캄보졸라 치즈          소프트치즈            블루치즈          1         6400
36869     36869  1942828        1      M   40  덴마크 까망베르 치즈          소프트치즈            까망베르          1         4165        
36870     36870  1942828        1      M   40  덴마크 까망베르 치즈          소프트치즈            까망베르          1         4165        
36871     36871  6284056        1      M   30   락토스프리 모짜렐라          후레쉬치즈            모짜렐라          2        11400        
36872     36872  1306045        1      F   40       리코타 치즈          후레쉬치즈             리코타          1         4600

[36873 rows x 10 columns]
'''


# if __name__ == '__main__':
#     OrderDfo = OrderDfo()
#     OrderDfo.new()