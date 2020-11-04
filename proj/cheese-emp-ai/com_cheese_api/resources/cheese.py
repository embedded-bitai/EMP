from typing import List
from flask import request
from sqlalchemy import func
from sqlalchemy import and_, or_
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from sklearn.ensemble import RandomForestClassifier 


# from com_cheese_api.ext.db import db, openSession
# from com_cheese_api.ext.db import db
# from com_cheese_api.util import FileReader
from pathlib import Path
import pandas as pd
import numpy as np
import json
import os
import sys

# from selenium import webdriver
import csv, time

from sklearn.model_selection import train_test_split

# from wordcloud import WordCloud
# from collections import Counter


'''
 * @ Module Name : cheese.py 
 * @ Description : Recommendation for cheese product
 * @ since 2020.10.20
 * @ version 1.0
 * @ label : 'category'
 * @ 치즈 상품 추천 개발 김유정
 * @ special reference libraries
 *     finance_datareader, konlpy
 * @ 수정일         수정자                   수정내용
 *  -------    --------    ---------------------------
 *  2020.10.20    김유정          최초 생성
''' 

# 1. 데이터 추출 KDD의 목표는 csv로 만드는 것
# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================
class CheeseKdd(object):

    def cheese_Crawling(html):
        item_list = []
        item_dict = {}
        items = driver.find_elements_by_class_name('item')
        itemNum = 1
        for item in items:
            itemNum += 1
            title = item.find_element_by_class_name('name').text
            price = item.find_element_by_class_name('price').text
            info = item.find_element_by_class_name('desc').text
            src = item.find_element_by_css_selector('a.img>img').get_attribute('src')
            item_list.append([title, price, info, src])
            item_dict[str(itemNum)] = {'title':title, 'price':price, 'info':info, 'img':src}
        return item_list, item_dict
    def toCSV(cheese_list):
        file = open('cheese_kurly.csv', 'w', encoding='utf-8', newline='')
        csvfile = csv.writer(file)
        for row in cheese_list :
            csvfile.writerow(row)
        file.close()
        cheese_list = []
        cheese_dict = {}
        url = "https://www.kurly.com/shop/goods/goods_search.php?searched=Y&log=1&skey=all&hid_pr_text=&hid_link_url=&edit=Y&sword=%C4%A1%C1%EE&x=0&y=0"
        driver = webdriver.Chrome("./ChromeDriver/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.get(url)
        pages = driver.find_elements_by_class_name('layout-pagination-number')
        body = driver.find_element_by_css_selector('body')
        for page in pages:
            page.click()
            #print('-------------------------')
            #print('page', pagenum)
            #print('-------------------------')
            #pagenum += 1
            time.sleep(3)
            items = driver.find_elements_by_class_name('item')
            cheese_item = cheese_Crawling(items)
            cheese_list += cheese_item[0]
            cheese_dict = dict(cheese_dict, **cheese_item[1])
        # 리스트 출력
        for item in cheese_list :
            print(item)
        # 사전형 출력
        for item in cheese_dict :
            print(item, cheese_dict[item]['img'], cheese_dict[item]['title'], cheese_dict[item]['price'], cheese_dict[item]['info'])
        # CSV파일 생성
        toCSV(cheese_list)
        driver.quit()

    # 2. 전처리 (Df로 전환) -> processing에 결과는 DF
    # ==============================================================
    # =====================                  =======================
    # =====================    Preprocessing =======================
    # =====================                  =======================
    # ==============================================================

class CheeseDf():
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'\\data')
        self.odf = None

    # hook 하는 부분 : 순서를 정해줌
    def new_model(self):
        train = 'train.csv'
        test = 'test.csv'
        this = self.fileReader
        this.train = self.new_model(train) #payload
        this.test = self.new_model(test)   #payload
        
        # train = pd.read_csv("data/train.csv")
        # test = pd.read_csv("data/test.csv")

        # print("The train dat size : {}".format(train.shape))
        # print("The test data size : {}".format(test.shape))

        '''
        Original Model Generation
        '''
        self.odf = pd.DataFrame(
            {
                'cheese_id' : this.train.CheeseId,
                'ranking' : this.train.Ranking,
                'brand' : this.train.Brand,
                'name' : this.train.Name,
            }
        )

        this.id = this.test['CheeseId']
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocessing Test Variable : {this.test.columns}')    
        this = self.drop_feature(this, 'Country')
        this = self.drop_feature(this, 'Price')
        this = self.drop_feature(this, 'Content')
        this = self.drop_feature(this, 'Img')
        this = self.drop_feature(this, 'CheeseId')
        # print(f'Post-Drop Variable : {this.train.columns}')   

        this = self.ranking_ordinal(this)
        # print(f' Preprocessing Ranking Variable: {this.train.head()}')
        this = self.brand_norminal(this)
        # print(f' Preprocessing Brand Variable: {this.train.head()}')
        this = self.name_norminal(this)
        # print(f'Preprocessing Name Variable: {this.train.head()}')
        # this = self.matching_norminal(this)
        # print(f' Preprocessing Matching Variable: {this.train.head()}')
        this = self.texture_norminal(this)
        # print(f' Preprocessing Texture Variable: {this.train.head()}')
        this = self.types_norminal(this)
        # print(f'Preprocessing Types Variable: {this.train.head()}')
        this = self.category_norminal(this)
        #print(f' Preprocessing Category Variable" {this.train.head()}')

        # print(f'Preprocessing Train Result: {this.train.head()}')
        # print(f'Preprocessing Test Result: {this.test.head()}')
        # print(f'Train NA Check: {this.train.isnull().sum()}')
        # print(f'Test NA Check: {this.test.isnull().sum()}')    

        this.label = self.create_label(this) # payload
        this.train = self.create_train(this) # payload

        # print(f'Train Variable: {this.train.columns}')
        # print(f'Test Varibale: {this.test.columns}')
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)

        # print(this)
        df = pd.DataFrame(

            {
                # 'matching' : this.train.matching,
                'category' : this.train.Category,
                'price' : this. train.Price,
                'content' : this.train.Content,
                'img' : this.train.Img            
            }

        )

        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        return sumdf
# if __name__ == '__main__':
#     df = CheeseDf()
#     df.new_model()        

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{self.fname}')
        return pd.read_csv(Path(self.data, this.fname)) 

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Category', axis = 1)
        

    @staticmethod
    def drop_label(this) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this

    @staticmethod
    def ranking_ordinal(this) -> object:
        return this

    @staticmethod
    def texture_norminal(this) -> object:
        train = this.train
        test = this.test
        train['']
        return this

    @staticmethod
    def types_norminal(this) -> object:
        combine = [this.train, this.test]
        types_mapping = {'가공치즈':0, '자연치즈':1}
        for dataset in combine:
            dataset ['types'] = dataset['types'].map(type.mapping)
        this.train = this.train 
        this.test = this.test

        return this
    
    def word_cloud(self) :
        text = ""
        with open("./cheese_data.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                    text += line

        font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'

        wc = WordCloud(font_path=font_path, background_color="white", width=1000, height=700)
        wc.generate(text)
        wc.to_file("result.png")
        plt.imshow(wc)
        plt.show

        return wc
#  if __name__ == '__main__':
#     df = CheeseDf()
#     df.word_cloud()    
            
    def  cheese_brand_split(self):
        cheese_data = pd.read_csv('com_cheese_api/resources/data', encoding ='utf-8')
        name = cheese_data['name'].str.split(']')
        cheese_list['brand'] = name.str.get(0)
        cheese_data['name'] = name.str.get(1)
        split = cheese_data['brand'].str.split('[')
        cheese_data['brand'] = split.str.get(1)
        cheese_data.to_csv("cheese_list.csv")

    def df_split(self):
        feats = pd.read_csv("data/cheese_data.csv", index_col = 0)
        test_size = 0.2
        random_state = 42

        X_train, X_test = train_test_split(
            feats,
            test_size = test_size,
            random_state = random_state
        )

        print(f'Shape of X_train: {X_train.shape}')

        X_train.to_csv(os.path.join('data', 'cheese_train.csv'), index=False)
        X_test.to_csv(os.path.join('data', 'cheese_test.csv'), index=False)

# if __name__ == '__main__':
#     df = CheeseDf()
#     df.df_split() 


    def cheese_data(self, data):
        # cheese_data = pd.read_csv("data/cheese_data.csv", index_col = 0)   
        category_map = {
                '모짜렐라' : 0,
                '블루치즈' : 1,
                '리코타' : 2,
                '체다' : 3 ,
                '파르미지아노 레지아노' : 4,
                '고다' : 5,
                '까망베르' : 6,
                '브리' : 7,
                '만체고' : 8,
                '에멘탈' : 9,
                '부라타' : 10
        }
        cheese_data['category'] = cheese_data['category'].map(category_map)
        df_category = cheese_data['category']
        print(df_category)
        print(cheese_data)
        return df_category

        

if __name__ == '__main__' :
    df = CheeseDf()
    df.cheese_data() 

# 3. 모델링 (Dto)
# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class CheeseDto(db.Model):
    __tablename__='cheeses'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    cheeseid : int = db.Column(db.Integer, primary_key=True, index=True)
    name : str = db.Column(db.String(30))
    price : str = db.Column(db.String(30))
    types : str = db.Column(db.String(30))
    texture : str = db.Column(db.String(30))
    taste : str = db.Column(db.String(30))
    matching : str = db.Column(db.String(30))
    content : str = db. Column(db.String(30))

    #dairy = db.relationship('DiaryDto', lazy='dynamic')
    orders = db.relationship('OrderDto', back_populates='cheese', lazy='dynamic')
    prices = db.relationship('PriceDto', back_populates='cheese', lazy='dynamic')

    def __init__(self, cheeseid, name, price, types, texture, taste, matching, content) : 
        self.id = cheeseid
        self.name = name
        self.price = price
        self.types = types
        self.texture = texture
        self.taste = taste
        self.matching = matching
        self.content = content

    def __repr__(self):
        return f'cheese(cheeseid={self.cheeseid}, name={self.name}, price={self.price}, types={self.types}, texture={self.texture}, taste={self.taste}, matching={self.matching}, content={self.content})'

    @property
    def json(self):
        return {'cheeseid':self.cheeseid, 'name':self.name, 'price':self.price, 'types':self.types, 'texture':self.types, 'taste':self.types, 'matching':self.types, 'content':self.content}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   

# getter setter를 프론트 단에서 받아옴 
class cheeseDao(cheeseDto):
    
    @classmethod
    def find_all(cls):
        sql = cls.query.all()

    @classmethod
    def find_by_cheeseid(cls, cheeseid) :
        return cls.query.file_by(cheeseid == cheeseid).all()

    @classmethod
    def find_by_brand(cls, brand) :
        return cls.query.firter_by(brand == brand).all()         
    
    @classmethod
    def find_by_name(cls, name) :
        return cls.query.firter_by(name == name).all()              

    @classmethod
    def find_by_price(cls, price) :
        return cls.query.file_by(price == price).first()
    
    @classmethod
    def find_by_texture(cls, texture) :
        return cls.query.firter_by(texture == texture).first()  

    @classmethod
    def find_by_taste(cls, taste) :
        return cls.query.file_by(taste == taste).first()
    
    @classmethod
    def find_by_matching(cls, matching) :
        return cls.query.firter_by(matching == matching).first()             

    @classmethod
    def find_by_content(cls, content) :
        return cls.query.firter_by(content == content).first() 

# Json 형태로 쓰기 위해 씀!
class CheeseVo(db.Model):
    ...
# 텐서플로우가 걸리는 곳    
class CheeseTf(db.Model):
    ...
# 인공지능 판단해주는 곳
class CheeseAi(db.Model):
    ...

# # 4. 프론트에 데이터 보내주는 행위 (프론트에서 이 내용이 보임!!)
# # ==============================================================
# # =====================                  =======================
# # =====================    Resourcing    =======================
# # =====================                  =======================
# # ==============================================================

# # Resource 부분은 어떤걸 상속 받냐에 따라 달라짐
# class Cheese(Resource):
#     ...
