# service는 전처리하는 곳
# hook = 아래의 순서대로 하겠다.
# 'userid' : this.train.PassengerId = train에 있는 Pclass를 가져와서 userid로 바꾼다
# odf 랑 df 를 따로 만들어서 axis =1 로 양옆으로 둘을 붙일 수 있게(concat) 함
# staticmethod는  self가 없음 create_train같은 함수를 가져다 쓸 수 있게함

from typing import List
from flask import request
from sqlalchemy import func
from sqlalchemy import and_, or_
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier 
from com_cheese_api.ext.db import url, db, openSession, engine

# from com_cheese_api.ext.db import db, openSession
# from com_cheese_api.ext.db import db
from com_cheese_api.util.file import FileReader
from pathlib import Path
import pandas as pd
import numpy as np
import json
import os
import sys
sys.path

# from selenium import webdriver
import csv, time

from sklearn.model_selection import train_test_split



# 1. 데이터 추출 KDD의 목표는 csv로 만드는 것
# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================
# class CheeseKdd(object):

#     def __init__(self):
        
#     def cheese_Crawling(html):
#         item_list = []
#         item_dict = {}
#         items = driver.find_elements_by_class_name('item')
#         itemNum = 1
#         for item in items:
#             itemNum += 1
#             title = item.find_element_by_class_name('name').text
#             price = item.find_element_by_class_name('price').text
#             info = item.find_element_by_class_name('desc').text
#             src = item.find_element_by_css_selector('a.img>img').get_attribute('src')
#             item_list.append([title, price, info, src])
#             item_dict[str(itemNum)] = {'title':title, 'price':price, 'info':info, 'img':src}
#         return item_list, item_dict

#     def toCSV(cheese_list):
#         file = open('cheese_kurly.csv', 'w', encoding='utf-8', newline='')
#         csvfile = csv.writer(file)
#         for row in cheese_list :
#             csvfile.writerow(row)
#         file.close()
#         cheese_list = []
#         cheese_dict = {}
#         url = "https://www.kurly.com/shop/goods/goods_search.php?searched=Y&log=1&skey=all&hid_pr_text=&hid_link_url=&edit=Y&sword=%C4%A1%C1%EE&x=0&y=0"
#         driver = webdriver.Chrome("./ChromeDriver/")
#         driver.implicitly_wait(5)
#         driver.get(url)
#         pages = driver.find_elements_by_class_name('layout-pagination-number')
#         body = driver.find_element_by_css_selector('body')
#         for page in pages:
#             page.click()
#             #print('-------------------------')
#             #print('page', pagenum)
#             #print('-------------------------')
#             #pagenum += 1
#             time.sleep(3)
#             items = driver.find_elements_by_class_name('item')
#             cheese_item = cheese_Crawling(items)
#             cheese_list += cheese_item[0]
#             cheese_dict = dict(cheese_dict, **cheese_item[1])
#         # 리스트 출력
#         for item in cheese_list :
#             print(item)
#         # 사전형 출력
#         for item in cheese_dict :
#             print(item, cheese_dict[item]['img'], cheese_dict[item]['title'], cheese_dict[item]['price'], cheese_dict[item]['info'])
#         # CSV파일 생성
#         toCSV(cheese_list)
#         driver.quit()

    # 2. 전처리 (Df로 전환) -> processing에 결과는 DF
    # ==============================================================
    # =====================                  =======================
    # =====================    Preprocessing =======================
    # =====================                  =======================
    # ==============================================================

# from datetime import datetime
# from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy

# Session = openSession()
# session = Session()

# app = Flask(__name__)

# config = {
#     'user': 'bitai',
#     'password': '456123',
#     'host': '127.0.0.1',
#     'port': '3306',
#     'database': 'com_cheese_api'
# }

# charset = {'utf8':'utf8'}

# url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"



# app.config['SQLALCHEMY_DATABASE_URI'] = url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)



class CheeseDf():
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.odf = None

    def new(self):
        this = self.fileReader
        cheese = 'cheese_data.csv'    
        this.cheese = self.new_model(cheese)
        print(this.cheese)
        # print(this)

        print(this.cheese.isnull().sum())

        this = CheeseDf.ranking_ordinal(this)
        this = CheeseDf.cheese_texture_norminal(this)
        this = CheeseDf.types_norminal(this)
        this = CheeseDf.cheese_category_norminal(this)

        cheese_split = CheeseDf.df_split(this.cheese)

        # train, test 데이터#
        train = 'cheese_train.csv'
        test = 'cheese_test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload

        print(this)


        self.odf = pd.DataFrame(
            {
                'ranking' : this.train.ranking,
                'cheese_id' : this.train.cheese_id,
                'brand' : this.train.brand,
                'category' : this.train.category,
                'types': this.train.types
            }
        )


        this.id = this.test['name']
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocessing Test Variable : {this.test.columns}')    
        this = CheeseDf.drop_feature(this, 'country')
        this = CheeseDf.drop_feature(this, 'price')
        this = CheeseDf.drop_feature(this, 'content')
        this = CheeseDf.drop_feature(this, 'cheese_id')
        # print(f'Post-Drop Variable : {this.train.columns}')   



        # # print(f'Preprocessing Train Result: {this.train.head()}')
        # # print(f'Preprocessing Test Result: {this.test.head()}')
        # # print(f'Train NA Check: {this.train.isnull().sum()}')
        # # print(f'Test NA Check: {this.test.isnull().sum()}')    

        this.label = CheeseDf.create_label(this) # payload
        this.train = CheeseDf.create_train(this) # payload

        # # print(f'Train Variable: {this.train.columns}')
        # # print(f'Test Varibale: {this.test.columns}')
        # clf = RandomForestClassifier()
        # clf.fit(this.train, this.label)
        # prediction = clf.predict(this.test)

        # print(this)


        df = pd.DataFrame(

            {
                'texture': this.train.texture,
                # 'matching' : this.train.matching,
                'img' : this.train.img            
            }

        )

        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        print(sumdf)
        print(sumdf.isnull().sum())
        print(list(sumdf))
        sumdf.to_csv(os.path.join('com_cheese_api/resources/data', 'cheese_fin.csv'), index=False, encoding='utf-8-sig')
        return sumdf



    def new_model(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname)) 

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('name', axis = 1)
        

    @staticmethod
    def create_label(this) -> object:
        return this.train['name'] # Label is the answer.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this

    @staticmethod
    def ranking_ordinal(this) -> object:
        return this

    @staticmethod
    def cheese_texture_norminal(this) -> object:
        this.cheese['texture'] = this.cheese['texture'].map({
            '후레쉬치즈': 1,
            '세미하드치즈': 2,
            '세미하드': 2,
            '하드치즈': 3,
            '소프트치즈': 4,
            '연성치즈': 5,
            '경성치즈': 6
        })
        return this

    @staticmethod
    def types_norminal(this) -> object:
        types_mapping = {'가공치즈':0, '자연치즈':1}
        this.cheese ['types'] = this.cheese['types'].map(types_mapping)
        this.cheese = this.cheese
        return this

    @staticmethod
    def cheese_category_norminal(this) -> object:
        category_map = {
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
        }
        this.cheese['category'] = this.cheese['category'].map(category_map)
        return this


    @staticmethod
    def df_split(data):
        cheese_train, cheese_test = train_test_split(data, test_size = 0.3, random_state = 32)
        cheese_train.to_csv(os.path.join('com_cheese_api/resources/data', 'cheese_train.csv'), index=False)
        cheese_test.to_csv(os.path.join('com_cheese_api/resources/data', 'cheese_test.csv'), index=False)       
        return cheese_train, cheese_test

# if __name__ == '__main__' :
#     df = CheeseDf()
#     df.new() 



'''
    ranking cheese_id     brand     category  types  texture                                                img
0        33       p33       샴피뇽         2      1        4  https://img-cf.kurly.com/shop/data/goods/15954...
1        48       p48      푸글리제         3      1        1  https://img-cf.kurly.com/shop/data/goods/15319...
2        16       p16      zott         1      1        1  https://img-cf.kurly.com/shop/data/goods/15266...
3        57       p57    라 콘타디나         3      1        1  https://img-cf.kurly.com/shop/data/goods/15235...
4        47       p47       란다나         6      1        2  https://img-cf.kurly.com/shop/data/goods/15777...
5        32       p32       안젤로         2      1        2  https://img-cf.kurly.com/shop/data/goods/15107...
6        61       p61       사토리         4      1        2  https://img-cf.kurly.com/shop/data/goods/15311...
7        54       p54    퀘소로시난테         9      1        3  https://img-cf.kurly.com/shop/data/goods/15978...
8        49       p49      베르기어         6      1        2  https://img-cf.kurly.com/shop/data/goods/15281...
9        69       p69     그랑도르즈         7      1        4  https://img-cf.kurly.com/shop/data/goods/14775...
10       67       p67       사토리         4      1        3  https://img-cf.kurly.com/shop/data/goods/15639...
[49 rows x 7 columns]
'''




# # 3. 모델링 (Dto)
# # ==============================================================
# # =======================                =======================
# # =======================    Modeling    =======================
# # =======================                =======================
# # ==============================================================

class CheeseDto(db.Model):
    __tablename__='cheeses'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    cheese_id : int = db.Column(db.Integer, primary_key=True, index=True)
    ranking : int = db.Column(db.Integer)
    category: int = db.Column(db.Integer)
    types : int = db.Column(db.Integer)
    brand : str = db.Column(db.String(30))
    texture : str = db.Column(db.String(30))
    img : str = db.Column(db.String(255))


    #dairy = db.relationship('DiaryDto', lazy='dynamic')
    orders = db.relationship('OrderDto', back_populates='cheese', lazy='dynamic')
    prices = db.relationship('PriceDto', back_populates='cheese', lazy='dynamic')

    def __init__(self, cheeseid, name, price, types, texture, taste, matching, content) : 
        self.cheese_id = cheese_id
        self.ranking = ranking
        self.category = category
        self.types = types
        self.brand = brand
        self.texture = texture
        self.img = img

    def __repr__(self):
        return f'cheese(cheese_id={self.cheese_id}, ranking={self.ranking}, category={self.category}, \
                    types={self.types}, texture={self.texture}, brand={self.brand}, img={self.img})'

    @property
    def json(self):
        return {'cheese_id':self.cheese_id, 'ranking':self.ranking, 'category':self.category, 'types':self.types, 'texture':self.types, \
                    'brand':self.brand, 'img':self.img}

class CheeseVo():
    cheese_id : 0
    ranking : 0
    category: 0
    types : 0
    brand : ''
    texture : ''
    img : ''


Session = openSession()
session = Session()
    

# class CheeseDao(CheeseDto):
#     @classmethod
#     def bulk(cls, CheeseDf):
#         cheeseDf = CheeseDf()
#         df = CheeseDf.new()
#         print(df.head())
#         session.bulk_insert_mappings(CheeseDto, df.to_dict(orient="records"))
#         session.commit()
#         session.close()

# if __name__ == '__main__':
#     CheeseDao.bulk()