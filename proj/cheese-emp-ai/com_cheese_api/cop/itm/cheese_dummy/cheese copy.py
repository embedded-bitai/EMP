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

'''
결과물 적어서 남겨놓기
'''

# 웹크롤링, 텍스트 마이닝 -> 데이터 마이닝

# service는 전처리하는 곳
# hook = 아래의 순서대로 하겠다.
# 'userid' : this.train.PassengerId = train에 있는 Pclass를 가져와서 userid로 바꾼다
# odf 랑 df 를 따로 만들어서 axis =1 로 양옆으로 둘을 붙일 수 있게(concat) 함
# staticmethod는  self가 없음 create_train같은 함수를 가져다 쓸 수 있게함


# 마일드 스톤(미국 도로보면 지역의 경계에 웰컴 어디어디 지역명 적어놓은것)
# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================

class CheeseKdd(db.Model)):
    ...



# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================

class CheeseDf(object):
    ...

class CheeseWordCloud():
    cheese_list = pd.read_csv('cheese_data.csv', encoding='utf-8')
    cheese_list
    text = ""
    with open('./cheese_data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            text += line
    
    font_path = ''

    wc = WordCloud(font_path=font_path, background_color="white", width=1000, height=700)
    wc.generate(text)
    wc.to_file("result.png")
    plt.imshow(wc)
    plt.show



# ==============================================================
# ====================                     =====================
# ====================       Modeling      =====================
# ====================                     =====================
# ==============================================================

class CheeseDto(db.Model):
    ...

class CheeseVo(object):
    ...

class CheeseDao(CheeseDto):
    ...

class CheeseTF(object):
    ...

class CheeseAi(object):
    ...

# ==============================================================
# ====================                     =====================
# ====================      Resourcing     =====================
# ====================                     =====================
# ==============================================================

# Api가 될 녀석
# 외부에 공표될 부분
class Cheese(Resource):
    ...

