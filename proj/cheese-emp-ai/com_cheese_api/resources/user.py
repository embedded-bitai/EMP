import numpy as np
import pandas as pd
from com_cheese_api.util.file import FileReader

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

import os


# ==============================================================
# ====================                     =====================
# ====================         KDD         =====================
# ====================                     =====================
# ==============================================================
class UserKdd(db.Model):
    ...

# ==============================================================
# =====================                  =======================
# =====================    Preprocessing =======================
# =====================                  =======================
# ==============================================================

#def read_stopword():
#    with open('com_cheese_api/user/data/stopword.txt', 'r') as file:
#        lines = file.readlines()
#        stop_str = ''.join(lines)
#        stopword = stop_str.replace('\n', ' ')
#    stopwords = stopword.split(' ')
#    return stopwords

class UserDf:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.okt = Okt()
        self.odf = None

    def make_wordcloud(self):
        
        _data = pd.read_csv("com_cheese_api/resources/data/users.csv")
        _df = _data.loc[:,['cheese_name']]
        _lists = np.array(_df['cheese_name'].tolist())
                
        with open('com_cheese_api/user/data/stopword.txt', 'r') as file:
            lines = file.readlines()
            stop_str = ''.join(lines)
            stopword = stop_str.replace('\n', ' ')
        stopwords = stopword.split(' ')

        sentences_tag = []
        
        #형태소 분석하여 리스트에 넣기
        for sentence in _lists:
            morph = self.okt.pos(sentence)
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

    #make_wordcloud()

def change_list() :
        top_ = (['비타민', '김치', '삼다수', '풀무원', '생수', '제주', '홍삼', '유산균', '캡슐', '훈제', '증정', '사과', '쇼핑', '큐브', '락토핏', '고려', '은단', '야채', '밸런스', '라이트', '홍진경', '선물', '간편', '플러스', '스테이크', '도시락', '롯데', '곤약', '멀티', '콜라겐', '라이프','견과', '두유', '오메가', '네슬레', '아셉틱', '퓨어', '소시지', '청양고추', '칼슘', '젤리', '시래기', '솥밥', '표고버섯', '프리미엄', '건강', '포도', '우먼', '스틱', '종근당', '포장', '석류', '주스', '하루', '실속', '불고기', '만두', '백화점', '키즈', '자연', '볶음', '모음', '미니', '낱봉', '호두', '라이스', '마그네슘', '혼합', '루테', '영양', '볶음밥', '리지', '워터', '버섯', '샘물', '유기농', '아몬드', '계란', '간장','수제', '안국', '미네랄', '포맨', '노니', '정환', '에너지', '코어', '매콤', '실버', '굿데이', '견과류', '안심', '프로','밀크', '꼬치','테일러','식이섬유', '땅콩','가야','베이스'])
        #print(type(top_))
        #print(top_)

        _data = pd.read_csv("com_cheese_api/resources/data/users.csv")
        _df = _data.loc[:,['cheese_name']]
        _lists = np.array(_df['cheese_name'].tolist())
        #print(type(_lists))

        cheese_data = pd.read_csv("com_cheese_api/resources/data/cheese_data.csv")
        cheese_df = cheese_data.loc[:,['name']]
        cheese_lists = np.array(cheese_df['name']).tolist()
        #print(cheese_lists)

        for _list in _lists:
            for _num in range(len(_lists)):
                if _list in top_:
                    change_value_dict = {_list[_num]: cheese_lists[_num]}
                    change__data = _data.replace({'cheese_name': change_value_dict})
                    print(change__data)
                else:
                    break

def change_category() :
    
    _data = pd.read_csv("com_cheese_api/resources/data/users.csv")
    _df = _data.loc[:,['sub1_category']]
    _lists = np.array(_df['sub1_category'].tolist())
    #print(type(_lists))

    rank_category = _data['sub1_category'].value_counts()
    categories = np.array(rank_category.index).tolist()

    cheese_data = pd.read_csv("com_cheese_api/resources/data/cheese_data.csv")
    cheese_df = cheese_data.loc[:,['name']]
    cheese_lists = np.array(cheese_df['name']).tolist()
    #print(cheese_lists)

    match_value = {'영양제' : '모짜렐라', '생수' : '리코타', '닭고기류' : '블루치즈' , '냉동간편식' : '체다',\
                    '홍삼/인삼가공식품' : '파르미지아노 레지아노', '견과류' : '파르미지아노 레지아노', \
                        '포장반찬' : '고다', '건강진액' : '에멘탈', '건강보조식품' : '까망베르', '국산과일' : '부라타',\
                            '두유' : '만체고', '기능성음료' : '부라타', '축산선물세트' : '까망베르' }

    for _list in range(len(_lists)):
        _df = _data.replace({'sub1_category': match_value})
    print(_df)

def data_split ():
    users = pd.read_csv("com_cheese_api/resources/data/users.csv")
    user_train, user_test = train_test_split(users, test_size=0.3, random_state = 32)
    user_train.to_csv(os.path.join('com_cheese_api/resources/data', 'user_train.csv'), index=False)
    user_test.to_csv(os.path.join('com_cheese_api/resources/data', 'user_test.csv'), index=False)

def new(self):
    train = 'user_train.csv'
    test = 'user_test.csv'
    this = self.fileReader
    this.train = self.new_model(train) # payload
    this.test = self.new_model(test) # payload

    '''
    Original Model Generation
    '''

    self.odf = pd.Data

def corrs():
    return 


@staticmethod
def drop_feature(this, feature) -> object:
    this.train = this.train.drop([feature], axis = 1)
    this.test = this.test.drop([feature], axis = 1)
    return this

@staticmethod
def category_ordinal(this) -> object:
    category_title_mapping = {
        0 : '모짜렐라',
        1 : '리코타',
        2 : '블루치즈',
        3 : '체다',
        4 : '파르미지아노 레지아노',
        5 : '고다',
        6 : '에멘탈',
        7 : '까망베르',
        8 : '부라타',
        9 : '만체고'
    }

    for x in range(len(_df['sub1_category'])):
        if _df['sub1_category'][x] == '모짜렐라':
            _df['sub1_category'][x] == category_title_mapping[_df['Title'][x]]

    category_mapping = {
        0 : '모짜렐라',
        1 : '리코타',
        2 : '블루치즈',
        3 : '체다',
        4 : '파르미지아노 레지아노',
        5 : '고다',
        6 : '에멘탈',
        7 : '까망베르',
        8 : '부라타',
        9 : '만체고'
    }

    _df['sub1_category'] = _df['sub1_category'].map(category_mapping)

    return this
# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class UserDto(db.Model):
    ...

class UserVo(db.Model):
    ...

class UserTf(db.Model):
    ...

class UserAi(db.Model):
    ...

# ==============================================================
# =====================                  =======================
# =====================    Resourcing    =======================
# =====================                  =======================
# ==============================================================


class User(db.Model):
    ...