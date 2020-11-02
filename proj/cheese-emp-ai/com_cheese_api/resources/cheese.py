from com_emp_api.ext.db import db, openSession
from com_emp_api.cheese.service import cheeseService
import pandas as pd
import json
from com_emp_api.ext.db import db
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from wordcloud import WordCloud
import pandas as pd
from collections import Counter




# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================
class CheeseKdd(db.Model):
    ...

# ==============================================================
# =====================                  =======================
# =====================    Preprocessing =======================
# =====================                  =======================
# ==============================================================

class CheeseWordCloud():
    cheese_list = pd.read_csv('cheese_data.csv', encoding ='utf-8')
    cheese_list     
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

class CheeseSplit():
    cheese_data = pd.read_csv('cheese_data.csv', encoding ='utf-8')
        name = cheese_data['name'].str.split(']')
        cheese_list['brand'] = name.str.get(0)
        cheese_data['name'] = name.str.get(1)
        split = cheese_data['brand'].str.split('[')
        cheese_data['brand'] = split.str.get(1)
            cheese_data.to_csv("cheese_list.csv")

# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class cheeseDto(db.Model):
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

class CheeseVo(db.Model):
    ...
class CheeseTf(db.Model):
    ...

class CheeseAi(db.Model):
    ...

# ==============================================================
# =====================                  =======================
# =====================    Resourcing    =======================
# =====================                  =======================
# ==============================================================

# Resource 부분은 어떤걸 상속 받냐에 따라 달라짐
class Cheese(Resource):
    ...

 # # ==============================================================
# # ====================                     =====================
# # ====================         KDD         =====================
# # ====================                     =====================
# # ==============================================================
# class UserKdd(db.Model):
#     ...

# # ==============================================================
# # =====================                  =======================
# # =====================    Preprocessing =======================
# # =====================                  =======================
# # ==============================================================

# class UserDf():
#     ...

# # ==============================================================
# # =======================                =======================
# # =======================    Modeling    =======================
# # =======================                =======================
# # ==============================================================

# class UserDto(db.Model):
#     ...

# class UserVo(db.Model):
#     ...

# class UserTf(db.Model):
#     ...

# class UserAi(db.Model):
#     ...

# # ==============================================================
# # =====================                  =======================
# # =====================    Resourcing    =======================
# # =====================                  =======================
# # ==============================================================


# class User(db.Model):
#     ...   