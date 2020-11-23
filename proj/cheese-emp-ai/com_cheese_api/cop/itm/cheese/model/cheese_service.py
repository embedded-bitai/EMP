# from com_cheese_api.ext.db import url, db, openSession, engine
# # from com_cheese_api.util.file import FileReader
# from com_cheese_api.cmm.utl.file import FileReader

# from flask import request
# from flask import Response, jsonify
# from flask_restful import Resource, reqparse

# from sqlalchemy import func
# from sqlalchemy import and_, or_

# from sklearn.ensemble import RandomForestClassifier # rforest
# from sklearn.tree import DecisionTreeClassifier # dtree
# from sklearn.naive_bayes import GaussianNB # nb
# from sklearn.neighbors import KNeighborsClassifier # knn
# from sklearn.svm import SVC # svm
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import KFold  # k value is understood as count
# from sklearn.model_selection import cross_val_score

# import pandas as pd
# import numpy as np
# import json
# import os
# import sys
# from typing import List
# from pathlib import Path


# # 코드 실행 후 생성되는 파일명
# # cheese_fin.csv, cheese_train.csv, cheese_test.csv

# class CheeseDfo(object):
#     def __init__(self):
#         self.fileReader = FileReader()
#         #self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
#         self.data = os.path.join('com_cheese_api/cop/itm/cheese/data')
#         self.odf = None

#     def new(self):
#         cheese = 'cheese_data.csv'
#         this = self.fileReader
#         this.cheese = self.new_model(cheese)
#         # print(f'===== 치즈 데이터 insert ===== this.cheese')
#         # print(this)

#         print(this.cheese.isnull().sum())

#         print(f'\n===================cheese_dfo.py 111\n')

#         this = CheeseDfo.ranking_ordinal(this)
#         this = CheeseDfo.cheese_texture_nominal(this)
#         this = CheeseDfo.types_nominal(this)
#         this = CheeseDfo.cheese_category_nominal(this)

#         print(f'===================cheese_dfo.py 222')

#         cheese_split = CheeseDfo.df_split(this.cheese)

#         # train, test 데이터#
#         train = 'cheese_train.csv'
#         test = 'cheese_test.csv'

#         this = self.fileReader
#         this.train = self.new_model(train) # payload
#         this.test = self.new_model(test) # payload

#         print(this)


#         self.odf = pd.DataFrame(
#             {
#                 'ranking' : this.train.ranking,
#                 'cheese_id' : this.train.cheese_id,
#                 'brand' : this.train.brand,
#                 'category' : this.train.category,
#                 'types': this.train.types
#             }
#         )


#         this.id = this.test['name']
#         # print(f'Preprocessing Train Variable : {this.train.columns}')
#         # print(f'Preprocessing Test Variable : {this.test.columns}')    
#         this = CheeseDfo.drop_feature(this, 'country')
#         this = CheeseDfo.drop_feature(this, 'price')
#         this = CheeseDfo.drop_feature(this, 'content')
#         this = CheeseDfo.drop_feature(this, 'cheese_id')
#         # print(f'Post-Drop Variable : {this.train.columns}')


#         # # print(f'Preprocessing Train Result: {this.train.head()}')
#         # # print(f'Preprocessing Test Result: {this.test.head()}')
#         # # print(f'Train NA Check: {this.train.isnull().sum()}')
#         # # print(f'Test NA Check: {this.test.isnull().sum()}')    

#         this.label = CheeseDfo.create_label(this) # payload
#         this.train = CheeseDfo.create_train(this) # payload

#         # # print(f'Train Variable: {this.train.columns}')
#         # # print(f'Test Varibale: {this.test.columns}')
#         # clf = RandomForestClassifier()
#         # clf.fit(this.train, this.label)
#         # prediction = clf.predict(this.test)

#         # print(this)


#         df = pd.DataFrame(
#             {
#                 'texture': this.train.texture,
#                 # 'matching' : this.train.matching,
#                 'img' : this.train.img
#             }
#         )

#         # print(self.odf)
#         # print(df)
#         # 변수 odf와 df의 데이터 프레임을 합침
#         sumdf = pd.concat([self.odf, df], axis=1)
#         print('=========cheese_dfo.py======111')
#         print(sumdf)
#         print('=========cheese_dfo.py======222')
#         print(sumdf.isnull().sum())
#         print(list(sumdf))
#         sumdf.to_csv(os.path.join('com_cheese_api/cop/itm/cheese/data', 'cheese_fin.csv'), index=False, encoding='utf-8-sig')
        
#         return sumdf



#     def new_model(self, payload) -> object:
#         this = self.fileReader
#         this.data = self.data
#         this.fname = payload
#         print(f'{self.data}')
#         print(f'{this.fname}')
#         return pd.read_csv(Path(self.data, this.fname)) 

#     @staticmethod
#     def create_train(this) -> object:
#         return this.train.drop('name', axis = 1)
        

#     @staticmethod
#     def create_label(this) -> object:
#         return this.train['name'] # Label is the answer.

#     @staticmethod
#     def drop_feature(this, feature) -> object:
#         this.train = this.train.drop([feature], axis = 1)
#         this.test = this.test.drop([feature], axis = 1)
#         return this

#     @staticmethod
#     def ranking_ordinal(this) -> object:
#         return this

#     @staticmethod
#     def cheese_texture_nominal(this) -> object:
#         this.cheese['texture'] = this.cheese['texture'].map({
#             '후레쉬치즈': 1,
#             '세미하드치즈': 2,
#             '세미하드': 2,
#             '하드치즈': 3,
#             '소프트치즈': 4,
#             '연성치즈': 5,
#             '경성치즈': 6
#         })
#         return this

#     @staticmethod
#     def types_nominal(this) -> object:
#         types_mapping = {'가공치즈':0, '자연치즈':1}
#         this.cheese ['types'] = this.cheese['types'].map(types_mapping)
#         this.cheese = this.cheese
#         return this

#     @staticmethod
#     def cheese_category_nominal(this) -> object:
#         category_map = {
#             '모짜렐라': 1,
#             '블루치즈': 2,
#             '리코타': 3,
#             '체다': 4,
#             '파르미지아노 레지아노': 5,
#             '고다': 6,
#             '까망베르': 7,
#             '브리': 8,
#             '만체고': 9,
#             '에멘탈': 10,
#             '부라타': 11
#         }
#         this.cheese['category'] = this.cheese['category'].map(category_map)
#         return this


#     @staticmethod
#     def df_split(data):
#         cheese_train, cheese_test = train_test_split(data, test_size = 0.3, random_state = 32)
#         cheese_train.to_csv(os.path.join('com_cheese_api/cop/itm/cheese/data', 'cheese_train.csv'), index=False)
#         cheese_test.to_csv(os.path.join('com_cheese_api/cop/itm/cheese/data', 'cheese_test.csv'), index=False)       
#         return cheese_train, cheese_test


# if __name__ == '__main__' :
#     df = CheeseDfo()
#     df.new() 



# '''
#     ranking cheese_id     brand     category  types  texture                                                img
# 0        33       p33       샴피뇽         2      1        4  https://img-cf.kurly.com/shop/data/goods/15954...
# 1        48       p48      푸글리제         3      1        1  https://img-cf.kurly.com/shop/data/goods/15319...
# 2        16       p16      zott         1      1        1  https://img-cf.kurly.com/shop/data/goods/15266...
# 3        57       p57    라 콘타디나         3      1        1  https://img-cf.kurly.com/shop/data/goods/15235...
# 4        47       p47       란다나         6      1        2  https://img-cf.kurly.com/shop/data/goods/15777...
# 5        32       p32       안젤로         2      1        2  https://img-cf.kurly.com/shop/data/goods/15107...
# 6        61       p61       사토리         4      1        2  https://img-cf.kurly.com/shop/data/goods/15311...
# 7        54       p54    퀘소로시난테         9      1        3  https://img-cf.kurly.com/shop/data/goods/15978...
# 8        49       p49      베르기어         6      1        2  https://img-cf.kurly.com/shop/data/goods/15281...
# 9        69       p69     그랑도르즈         7      1        4  https://img-cf.kurly.com/shop/data/goods/14775...
# 10       67       p67       사토리         4      1        3  https://img-cf.kurly.com/shop/data/goods/15639...
# [49 rows x 7 columns]
# '''