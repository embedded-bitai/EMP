import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader
from pathlib import Path
from com_cheese_api.ext.db import url, db, openSession, engine
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sqlalchemy.ext.declarative import declarative_base
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm


import os
import json


class UserDf:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.odf = None

    def new(self):
        user = 'users.csv'
        cheese = 'cheese_data.csv'
        this = self.fileReader
        this.user = self.new_model(user) # payload
        this.cheese = self.new_model(cheese)

        # print(this.user_origin)
        # print(this.cheese)

        print(this)

        category_count = UserDf.category_Count(this.user)
        item_count = UserDf.item_Count(this.user, category_count)
        this.user = UserDf.change_to_cheese(this.cheese, item_count)
        print(f'######## 치즈 상품 대체 체크 ##########')

        # this.user = self.new_model(user)
        
        print(this)

        this = UserDf.user_gender_norminal(this)
        this = UserDf.cheese_rank_oridinal(this)

        # print(min(this.user['user_age'])) # 고객 최소 나이 : 10
        # print(max(this.user['user_age'])) # 고객 최대 나이 : 80
        this = UserDf.user_age_norminal(this)
        print(f'######## age 전처리 체크 ##########')
        print(this.user.head(10))
        this = UserDf.cheese_code_ordinal(this)
        this = UserDf.buy_count_numeric(this)
        this = UserDf.cheese_category_nominal(this)
        this = UserDf.cheese_texture_nominal(this)

        print(f'Preprocessing User Dataset : {this.user}')

        print(f'######## train na 체크 ##########')
        print(f'{this.user.isnull().sum()}')
        print(f'######## test na 체크 ##########')
        print(f'{this.user.isnull().sum()}')
        print(f'######## data type 체크 ##########')
        print(this.user.dtypes)        


        user_split = UserDf.user_data_split(this.user)

        train = 'user_train.csv'
        test = 'user_test.csv'
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload
        print(f'Check Train Dataset : {this.train.head(5)}')
        print(f'Check Test Dataset : {this.test.head(5)}')
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocession Test Variable : {this.test.columns}')
        
        self.odf = pd.DataFrame(
            {
                'user_index': this.train.user_index,
                'user_id': this.train.user_id,
                'password': '1'
            }
        )

        print(self.odf)

        this.id = this.test['user_id'] # This becomes a question.
        
        # show_age_plot = UserDf.find_requency(this.user, 'user_index', 'user_age') 
        # 30대(1만5천) > 40대(1만4천) > 20대(3천5백) > 50대(3천1백) > 60대(523) > 10대=70대(80) >80대
        
        # print(show_age_plot)

        # show_wordcloud = self.make_wordcloud(this.user)
        # print(show_wordcloud)

        show_corr = UserDf.make_corr(this.train)

        # this = UserDf.drop_feature(this, 'user_index')
        this = UserDf.drop_feature(this, 'cheese_brand')
        this = UserDf.drop_feature(this, 'cheese_code')
        this = UserDf.drop_feature(this, 'cheese_name')
        this = UserDf.drop_feature(this, 'cheese_types')

        this = UserDf.drop_feature(this, 'cheese_rank')

        this.label = UserDf.create_label(this) # payload
        this.train = UserDf.create_train(this) # payload    

        df = pd.DataFrame(
            {
                'gender': this.train.gender,
                'age_group': this.train.age_group,
                'cheese_texture': this.train.cheese_texture_code,
                'buy_count': this.train.buy_count
            }
        )

        sumdf = pd.concat([self.odf, df], axis = 1)
        print('######## train 데이터 전처리 완료 체크 ##########')
        print(sumdf) # train 데이터만 추출했기 때문에 25811개
        sumdf.to_csv(os.path.join('com_cheese_api/resources/data', 'users_data.csv'), index=False, encoding='utf-8-sig')
        
        return sumdf




####################### 데이터 불러오기 & 생성 & featrue 제거 #######################

    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('cheese_category', axis=1) # Train is a dataset in which the answer is removed. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['cheese_category'] # Label is the answer.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this



    ####################### 원본 데이터를 치즈 구매 데이터 변환 #######################

    # 밑에 make_barplot()을 이용해서 시각화 가능.
    @staticmethod
    def find_requency(data, column1, column2):
        count_size = data[column1].groupby(data[column2]).count().reset_index(name='counts')
        count_size['rank'] = count_size['counts'].rank(ascending=False)
        show_barplot = UserDf.make_barplot(column2, 'counts', count_size)
        return count_size

    @staticmethod
    def category_Count(data) -> object:
        sub_size = data['buy_count'].groupby(data['sub1_category']).sum().reset_index(name='sub1_counts')
        sub_size['sub1_rank'] = sub_size['sub1_counts'].rank(ascending=False)
        # barplot = UserDf.make_barplot('sub1_category', 'sub1_counts', sub_size)
        return sub_size

    @staticmethod
    def item_Count(data, category_count):
        item_size = data['buy_count'].groupby([data['sub1_category'],data['sub2_category']]).sum().reset_index(name='sub2_counts')
        item_size['sub2_rank'] = item_size['sub2_counts'].rank(ascending=False, method="dense")

        category_item_rank = pd.merge(category_count, item_size, on = 'sub1_category', how = 'right')
        user_item_rank = pd.merge(data, category_item_rank, on = 'sub2_category', how = 'left')
        # print(user_item_rank)

        user_items_ranks = user_item_rank.drop(['sub1_category_y'], axis=1)
        users_item_data = user_items_ranks.rename(columns={'sub1_category_x': 'sub1_category'})
        # print(users_item_data)

        return users_item_data    


    @staticmethod
    def change_to_cheese(data, item_count):
        cheese_df = data.rename(columns={'ranking': 'sub2_rank'})
        user_cheese_merge = pd.merge(item_count, cheese_df, on = 'sub2_rank', how = 'left')
        user_data1 = user_cheese_merge.drop(['Unnamed: 0_x', 'item_code', 'item_name', 'item_add_name', 'category_x', 'sub1_category', 'sub2_category', 'item_brand', 'sub1_counts', 'sub1_rank', 'sub2_counts', 'buy_price'], axis=1)
        user_data2 = user_data1.drop(['country', 'matching', 'matching.1', 'content', 'img'], axis=1)
        user_data_fin = user_data2.rename(columns={'Unnamed: 0_y': 'cheese_code', 'brand': 'cheese_brand', 'name': 'cheese_name', 'price' : 'cheese_one_price', 'sub2_rank': 'cheese_rank', \
                                                        'category_y': 'cheese_category', 'texture': 'cheese_texture', 'types': 'cheese_types'})
        # print(list(users_cheese_merge))
        # print(user_data_fin)
        # user_data_fin.to_csv(os.path.join('com_cheese_api/resources/data', 'user_df.csv'), index=True, encoding='utf-8-sig')
        return user_data_fin
    # item_Change()

#     @staticmethod
#     def change_feature_name(data, origin_name, new_name):
#             data.rename(column={'origin_name': 'new_name'})
#         return data




    ####################### 데이터 정제 #######################
    
    @staticmethod
    def cheese_rank_oridinal(this) -> object:
        return this

    @staticmethod

    def user_gender_norminal(this) -> object:
        gender_mapping = {'M': 0, 'F': 1}
        this.user['gender'] = this.user['user_gender'].map(gender_mapping)
        this.user = this.user # overriding
        # this.user.to_csv(os.path.join('com_cheese_api/resources/data', 'check11.csv'), index=False, encoding='utf-8-sig')
        return this


    @staticmethod
    def user_age_norminal(this) -> object:
        user = this.user
        bins = [1, 29, 39, 49, 59, np.inf]
        labels = ['Youth', 'Adult30', 'Adult40', 'Adult50', 'Senior']
        user['age_group'] = pd.cut(user['user_age'], bins, right = True, labels = labels)
        age_mapping = {
                'Youth': 1,
                'Adult30': 2 ,
                'Adult40': 3 ,
                'Adult50': 4,
                'Senior': 5
        }
        user['age_group'] = user['age_group'].map(age_mapping)
        this.user = this.user # overriding
        print(this.user)
        # this.user.to_csv(os.path.join('com_cheese_api/resources/data', 'user_check.csv'), index=False, encoding='utf-8-sig')
        return this

    @staticmethod
    def cheese_code_ordinal(this) -> object:
        return this

#######################더미변수로?! 여쭤보기~~###############################
    # @staticmethod
    # def cheese_brand_nominal(this) -> object:
    #     train = this.train
    #     test = this.test

    #     train[]

    @staticmethod
    def buy_count_numeric(this) -> object:
        return this

    @staticmethod
    def cheese_category_nominal(this) -> object:
        this.user['cheese_category_code'] = this.user['cheese_category'].map({
            '모짜렐라': 1,
            '블루치즈': 2,
            '리코타': 3,
            '체다': 4,
            '파르미지아노 레지아노': 5,
            '고다': 6,
            '까망베르': 7,
            '브리': 8,
            '만체고': 9,
            '에멘탈': 10,
            '부라타': 11
        })
        return this

    @staticmethod
    def cheese_texture_nominal(this) -> object:
        this.user['cheese_texture_code'] = this.user['cheese_texture'].map({
            '후레쉬치즈': 1,
            '세미하드치즈': 2,
            '세미하드': 2,
            '하드치즈': 3,
            '소프트치즈': 4,
            '연성치즈': 5,
            '경성치즈': 6
        })

        return this


    # @staticmethod
    # def cheese_one_price_numeric(this) -> object:


    ####################### train, test 데이터 셋 나누기 #######################

    @staticmethod
    def user_data_split (data):
        user_train, user_test = train_test_split(data, test_size=0.3, random_state = 32)
        user_train.to_csv(os.path.join('com_cheese_api/resources/data', 'user_train.csv'), index=False)
        user_test.to_csv(os.path.join('com_cheese_api/resources/data', 'user_test.csv'), index=False)
        return user_train, user_test



    ####################### 데이터 탐색 & 시각화 #######################

    # find_requency()에서 시각화로 사용.
    @staticmethod
    def make_barplot(x_name, y_name, data_name):
        # font_path = 'C:\\Windows\\Fonts\\NanumGothic.ttf'
        # font_name1 = fm.FontProperties(fname = font_path).get_name()
        # plt.rc('font', family = font_name1)
        plt.xticks(rotation = 45)
        sns.barplot(x = x_name, y = y_name, data = data_name)
        plt.show()



    @staticmethod
    def make_wordcloud(data):
        user_df = data.loc[:,['cheese_name']]
        user_lists = np.array(user_df['cheese_name'].tolist())
                
        with open('com_cheese_api/resources/data/stopword.txt', 'r') as file:
            lines = file.readlines()
            stop_str = ''.join(lines)
            stopword = stop_str.replace('\n', ' ')
        stopwords = stopword.split(' ')

        sentences_tag = []
        
        okt = Okt()

        #형태소 분석하여 리스트에 넣기
        for sentence in user_lists:
            morph = okt.pos(sentence)
            sentences_tag.append(morph)
            #print(morph)
            #print('-' * 30)
        
        #print(sentences_tag)
        #print('\n' * 3)
        
        noun_adj_list = []
        #명사와 형용사만 구분하여 이스트에 넣기
        for sentence1 in sentences_tag:
            for word, tag in sentence1:
                if word not in stopwords:
                    if tag in ['Noun']:
                        if len(word) >= 2:
                            noun_adj_list.append(word)
                        
        
        word_count_list = []
        #형태소별 count
        counts = Counter(noun_adj_list)
        tags = counts.most_common(100)
        word_count_list.append(tags)
        word_list = sum(word_count_list, [])
        print(word_list)
        print(type(word_list))
    
        # wordCloud 생성
        # 한글 깨지는 문제 해결하기 위해 font_path 지정
        wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf', background_color='white', width=800, height=600)
        #print(dict(tags))
        cloud = wc.generate_from_frequencies(dict(tags))
        plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(cloud)
        return plt.show()


    @staticmethod
    def make_corr(data):
        make_corr = data.corr()
        sns.clustermap(make_corr, annot = True, cmap = 'RdYlBu_r', linewidths=.5, cbar_kws={"shrink": .5}, vmin = -1, vmax = 1)
        plt.show()

'''
       user_id password  gender  age_group  cheese_texture  buy_count
0      1751881        1       1          2               1          2
1      1835210        1       1          2               1          2
2      5824726        1       1          4               1          1
3      1752218        1       0          3               1          3
4      2034072        1       1          3               1          1
...        ...      ...     ...        ...             ...        ...
25806  1718175        1       1          1               1          1
25807  2155344        1       1          3               4          1
25808  5939075        1       1          2               2          3
25809  4959284        1       1          2               1          1
25810  1747758        1       1          4               2          1

[25811 rows x 6 columns]
'''


if __name__ == '__main__':
    userDf = UserDf()
    userDf.new()



# 2. 모델링 (Dto)
# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class UserDto(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    user_index: int = db.Column(db.Integer, primary_key= True, index = True)
    user_id: str = db.Column(db.String(20))
    password: str = db.Column(db.String(1))
    gender: int = db.Column(db.Integer)
    age_group: int = db.Column(db.Integer)
    cheese_texture: int = db.Column(db.Integer)
    buy_count: int = db.Column(db.Integer)

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
    # articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

    def __init__(self, user_index, user_id, password, gender, age_group, cheese_texture, buy_count):
        self.user_index = user_index
        self.user_id = user_id
        self.password = password
        self.gender = gender
        self.age_group = age_group
        self.cheese_texture = cheese_texture
        self.buy_count = buy_count

    def __repr__(self):
        return f'User(user_index={self.user_index}, user_id={self.user_id}, password={self.password}, \
                    gender = {self.gender}, age_group={self.age_group}, \
                    cheese_texture={self.cheese_texture}, buy_count={self.buy_count})'

    def __str__(self):
        return f'User(user_index={self.user_index}, user_id={self.user_id}, password={self.password}, \
                    gender = {self.gender}, age_group={self.age_group}, \
                    cheese_texture={self.cheese_texture}, buy_count={self.buy_count})'

    def json(self):
        return {
            'user_index' : self.user_index,
            'userId' : self.user_id,
            'password': self.password,
            'gender': self.gender,
            'age_group': self.age_group,
            'cheese_texture': self.cheese_texture,
            'buy_count': self.buy_count
        }

# Json 형태로 쓰기 위해 씀!
class UserVo():
    user_index: int = 0
    user_id: str = ''
    password: str = ''
    gender: int = 0
    age_group: int = 0
    cheese_texture: int = 0
    buy_count: int = 0

# 텐서플로우가 걸리는 곳
# class UserTf():
#     ...

# 인공지능 판단해주는 곳
# class UserAi():
#     ...


Session = openSession()
session = Session()
    

# class UserDao(UserDto):
#     @classmethod
#     def bulk(cls, UserDf):
#         userDf = UserDf()
#         df = UserDf.new()
#         print(df.head())
#         session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
#         session.commit()
#         session.close()

# if __name__ == '__main__':
#     UserDao.bulk()