import numpy as np
import pandas as pd
import random
import string
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

class UserDfo:
    def __init__(self):
        self.fileReader = FileReader()
        # self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/m_data')
        self.data = os.path.join('com_cheese_api/usr/user/data')
        self.odf = None

    def new(self):
        user = 'user_order.csv'
        this = self.fileReader
        this.user = self.new_model(user) # payload
        print(this)
        print(type(this.user))

        print(f'######## 중복값 제거 ##########')
        this = UserDfo.user_id_drop_duplicate(this, 'user_id')

        print(this)
        print(f'######## 중복값 제거 확인 ##########')

        print(f'######## user na 체크 ##########')
        print(f'{this.user.isnull().sum()}')

        this.user = this.user.dropna(axis = 0)

        print(this)

        this.user = pd.merge(this.user, UserDfo.make_name(), left_index=True, right_index=True, how='left')
        this.user = pd.merge(this.user, UserDfo.make_phone(), left_index=True, right_index=True, how='left')
        this.user = pd.merge(this.user, UserDfo.make_email(), left_index=True, right_index=True, how='left')
        # this.user.to_csv(os.path.join('com_cheese_api/usr/user/data', 'user_name2.csv'), index=False, encoding='utf-8-sig')

        print(f'######## test na 체크 ##########')
        print(f'{this.user.isnull().sum()}')
        print(f'######## data type 체크 ##########')
        print(this.user.dtypes)

        self.odf = pd.DataFrame(
            {
                'user_id': this.user.user_id,
                'password': '1',
                'gender': this.user.gender,
                'age': this.user.age,
                'name': this.user.name,
                'phone': this.user.phone,
                'email': this.user.email
            }
        )

        self.odf.to_csv(os.path.join('com_cheese_api/usr/user/data', 'user_data.csv'), index=False, encoding='utf-8-sig')
        print(f'######## 최종 user DF 결과 ##########')
        print(self.odf)
        return self.odf


    ################### 데이터 불러오기 & 생성 & featrue 제거 #######################

    # self, 메모리에 적재
    def new_model(self, payload):
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname))



    ####################### 데이터 정제 #######################

    @staticmethod
    def user_id_drop_duplicate(this, feature) -> object:
        this.user = this.user.drop_duplicates(feature)
        return this


    @staticmethod
    def make_name() -> object:
        last_name = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안",
                "송", "류", "전", "홍", "고", "문", "양", "손", "배", "조", "백", "허", "유", "남", "심", "노", "정", "하", "곽", "성", "차", "주",
                "우", "구", "신", "임", "나", "전", "민", "유", "진", "지", "엄", "채", "원", "천", "방", "공", "강", "현", "함", "변", "염", "양",
                "변", "여", "추", "노", "도", "소", "신", "석", "선", "설", "마", "길", "주", "연", "방", "위", "표", "명", "기", "반", "왕", "금",
                "옥", "육", "인", "맹", "제", "모", "장", "남", "탁", "국", "여", "진", "어", "은", "편", "구", "용"]

        first_name = ["가", "강", "건", "경", "고", "관", "광", "구", "규", "근", "기", "길", "나", "남", "노", "누", "다",
                "단", "달", "담", "대", "덕", "도", "동", "두", "라", "래", "로", "루", "리", "마", "만", "명", "무", "문", "미", "민", "바", "박",
                "백", "범", "별", "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", "설", "섭", "성", "세", "소", "솔", "수", "숙", "순",
                "숭", "슬", "승", "시", "신", "아", "안", "애", "엄", "여", "연", "영", "예", "오", "옥", "완", "요", "용", "우", "원", "월", "위",
                "유", "윤", "율", "으", "은", "의", "이", "익", "인", "일", "잎", "자", "잔", "장", "재", "전", "정", "제", "조", "종", "주", "준",
                "중", "지", "진", "찬", "창", "채", "천", "철", "초", "춘", "충", "치", "탐", "태", "택", "판", "하", "한", "해", "혁", "현", "형",
                "혜", "호", "홍", "화", "환", "회", "효", "훈", "휘", "희", "운", "모", "배", "부", "림", "봉", "혼", "황", "량", "린", "을", "비",
                "솜", "공", "면", "탁", "온", "디", "항", "후", "려", "균", "묵", "송", "욱", "휴", "언", "령", "섬", "들", "견", "추", "걸", "삼",
                "열", "웅", "분", "변", "양", "출", "타", "흥", "겸", "곤", "번", "식", "란", "더", "손", "술", "훔", "반", "빈", "실", "직", "흠",
                "흔", "악", "람", "뜸", "권", "복", "심", "헌", "엽", "학", "개", "롱", "평", "늘", "늬", "랑", "얀", "향", "울", "련"]

        num_list = []
        name_list = []

        for num in range(40000):
            name_no = num
            rand_name = random.choice(last_name) + random.choice(first_name) + random.choice(first_name)
            num_list.append(name_no)
            name_list.append(rand_name)
        name_df = pd.DataFrame({'name_no': num_list, 'name': name_list})
        name_df.to_csv(os.path.join('com_cheese_api/usr/user/data', 'random_name.csv'), index=False, encoding='utf-8-sig')
        return name_df


    @staticmethod
    def make_phone() -> object:
        phone_list = []
        for num in range(40000):
            rand_phone = '010' + '-' + str(1111) + '-' + str(1111)
            phone_list.append(rand_phone)
        phone_df = pd.DataFrame({'phone': phone_list})
        return phone_df


    @staticmethod
    def make_email() -> object:
        email_address = [
            "@naver.com", "@gmail.com"
        ]
        email_list = []
        for num in range(40000):
            rand_email_str = "".join([random.choice(string.ascii_letters) for _ in range(3)])
            rand_email_num = random.randrange(10, 1000, 2)
            rand_email = rand_email_str + str(rand_email_num) + random.choice(email_address)
            email_list.append(rand_email)
        email_df = pd.DataFrame({'email': email_list})
        return email_df

        

'''
       user_no  user_id password gender  age name          phone             email
0            0  2391853        1      M   40  길비충  010-8596-4444  kxx252@gmail.com
1            1  1799897        1      F   40  노루술  010-5460-2136  mGX646@gmail.com
2            2  1614947        1      F   50  황환아  010-2588-4300  QdK116@naver.com
6            6  6523993        1      F   50  권새혼  010-6112-1808   TVM90@gmail.com
9            9   389215        1      F   50  여문하  010-8024-3524  TGa288@naver.com
...        ...      ...      ...    ...  ...  ...            ...               ...
36866    36866     7361        1      F   40  손엄지  010-6324-2968  oqb402@gmail.com
36868    36868  6159545        1      F   30  성흠채  010-4452-7120  LHU452@gmail.com
36869    36869  1942828        1      M   40  옥여선  010-2640-8088  GmY658@naver.com
36871    36871  6284056        1      M   30  모요길  010-9656-8424  JNS754@naver.com
36872    36872  1306045        1      F   40  김홍기  010-8248-7668   ZZK20@naver.com
[22270 rows x 8 columns]
'''

'''
       user_no  user_id password gender  age name          phone             email
0            0  2391853        1      M   40  국제이  010-1111-1111  NBI948@gmail.com
1            1  1799897        1      F   40  기더헌  010-1111-1111  voR668@naver.com
2            2  1614947        1      F   50  손용치  010-1111-1111  MxE606@naver.com
6            6  6523993        1      F   50  조종영  010-1111-1111  bkF708@naver.com
9            9   389215        1      F   50  육휘상  010-1111-1111  keR876@gmail.com
...        ...      ...      ...    ...  ...  ...            ...               ...
36866    36866     7361        1      F   40  추으천  010-1111-1111  qfw212@gmail.com
36868    36868  6159545        1      F   30  장선예  010-1111-1111  TQj288@gmail.com
36869    36869  1942828        1      M   40  채시실  010-1111-1111  bgG686@naver.com
36871    36871  6284056        1      M   30  편혼부  010-1111-1111  jPt386@naver.com
36872    36872  1306045        1      F   40  장전오  010-1111-1111   gVd70@naver.com

[22270 rows x 8 columns]
'''


# if __name__ == '__main__':
#     UserDfo = UserDfo()
#     UserDfo.new()