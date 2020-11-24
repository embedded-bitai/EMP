import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pandas as pd
import numpy as np
# sklearn algorithm : classification, regression, clustring, reduction
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold # k값은 count 의 의미로 이해
from sklearn.model_selection import cross_val_score


# dtree, rforest, nb, knn, svm,


"""
context: /Users/bitai/emp_ai
fname:
PassengerId 고객ID,
Survived 생존여부, --> 머신러닝 모델이 맞춰야 할 답
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

from dataclasses import dataclass

@dataclass
class FileReader:

    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

class TitanicModel:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = './data'

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        return pd.read_csv(os.path.join(this.data, this.fname)) # p.139  df = tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # train 은 답이 제거된 데이터셋이다. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # label은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1) # p.149 에 보면 훈련, 테스트 세트로 나눈다
        return this


    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        combine = [this.train, this.test] # train과 test 가 묶입니다. 
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train # overriding
        this.test = this.test
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
         # age 를 평균으로 넣기도 애매하고, 다수결로 넣기도 너무 근거가 없다...
         # 특히 age 는 생존률 판단에서 가중치(weight)가 상당하므로 디테일한 접근이 필요합니다.
         # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있어서 
         # -0.5 라는 중간값으로 처리했습니다.
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이 파트는 범위를 뜻합니다.
         # -1 이상 0 미만....60이상 기타 ...
         # [] 에 있으니 이것은 변수명이겠군요..라고 판단하셨으면 잘 이해한 겁니다.
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        # [] 은 변수명으로 선언되었음
        train['AgeGroup'] = pd.cut(train['Age'], bins, lables=labels)
        test['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown',
            1: 'Baby',
            2: 'Child',
            3: 'Teenager',
            4: 'Student',
            5: 'Young Adult',
            6: 'Adult',
            7: 'Senior'
        } # 이렇게 []에서 {}으로 처리하면 labels를 값으로 처리하겠네요.
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]

        age_mapping = {
            'Unknown': 0,
            'Baby': 1,
            'Child': 2,
            'Teenager': 3,
            'Student': 4,
            'Young Adult': 5,
            'Adult': 6,
            'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this

    @staticmethod
    def sibsp_numeric(this) -> object:
        return this

    @staticmethod
    def parch_numeric(this) -> object:
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        return this


    @staticmethod
    def fareBand_nominal(this) -> object: # 요금이 다양하니 클러스터링을 하기 위한 준비
        this.train = this.train.fillna({'FareBand': 1}) # FareBand 는 없는 변수인데 추가함
        this.test = this.test.fillna({'FareBand': 1})
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'}) # S가 가장 많아서 빈곳에 채움
        this.test = this.test.fillna({'Embarked': 'S'}) # 교과서 144
        # 많은 머신러닝 라이브러리는 클래스 레이블이 *정수* 로 인코딩 되었다고 기대함
        # 교과서 146 문자 blue = 0, green = 1, red = 2 로 치환 -> mapping 합니다.
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3}) # ordinal 아닙니다.
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0) # Unknown
        this.train = this.train
        this.test = this.test
        return this


    # Learning Algorithm 중에서 dtree, rforest, nb, knn, svm 이것을 대표로 사용하겠습니다.

    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10, shuffle=True, random_state=0)


    def accuracy_by_dtree(self, this):
        dtree = DecisionTreeClassifier()
        score = cross_val_score(dtree, this.train, this.label, cv=TitanicModel.create_k_fold(),\
            n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_rforest(self, this):
        rforest = RandomForestClassifier()
        score = cross_val_score(rforest, this.train, this.label, cv=TitanicModel.create_k_fold(),\
            n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_nb(self, this):
        nb = GaussianNB()
        score = cross_val_score(nb, this.train, this.label, cv=TitanicModel.create_k_fold(),\
            n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_knn(self, this):
        knn = KNeighborsClassifier()
        score = cross_val_score(knn, this.train, this.label, cv=TitanicModel.create_k_fold(),\
            n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_svm(self, this):
        svm = SVC()
        score = cross_val_score(svm, this.train, this.label, cv=TitanicModel.create_k_fold(),\
            n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)


class TitanicService:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = './data'
        self.model = TitanicModel()

    def modeling(self, train, test):
        model = self.model
        this = self.preprocessing(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        print(f'>> Train 변수 : {this.train.columns}')
        print(f'>> Test 변수 : {this.test.columns}')
        return this

    def preprocessing(self, train, test):
        model = self.model
        this = self.fileReader
        this.train = model.new_model(train) # payload
        this.test = model.new_model(test) # payload
        this.id = this.test['PassengerId'] # machine 에게는 이것이 question 이 됩니다.
        print(f'정제 전 Train 변수 : {this.train.columns}')
        print(f'정제 전 Test 변수 : {this.test.columns}')

        this = model.drop_feature(this, 'Cabin')
        this = model.drop_feature(this, 'Ticket')
        print(f'드롭 후 변수 : {this.train.columns}')

        this = model.embarked_nominal(this)
        print(f'승선한 항구 정제결과: {this.train.head()}')

        this = model.title_nominal(this)
        print(f'타이틀 정제결과: {this.train.head()}')
        # name 변수에서 title 을 추출했으니 name 은 필요가 없어졌고, str 이니 
        # 후에 ML-lib 가 이를 인식하는 과정에서 에러를 발생시킬것이다.
        this = model.drop_feature(this, 'Name')
        this = model.drop_feature(this, 'PassengerId')
        this = model.age_ordinal(this)
        print(f'나이 정제결과: {this.train.head()}')

        this = model.drop_feature(this, 'SibSp')
        this = model.sex_nominal(this)
        print(f'성별 정제결과: {this.train.head()}')
        
        this = model.fareBand_nominal(this)
        print(f'요금 정제결과: {this.train.head()}')

        this = model.drop_feature(this, 'Fare')
        print(f'########### TRAIN 정제결과 ###########')
        print(f'{this.train.head()}')

        print(f'########### TEST 정제결과 ###########')
        print(f'{this.test.head()}')

        print(f'########### train na 체크 ###########')
        print(f'{this.train.isnull().sum()}')

        print(f'########### test na 체크 ###########')
        print(f'{this.test.isnull().sum()}')
        return this


    def learning(self, train, test):
        model = self.model
        this = self.modeling(train, test)
        print('&&&&&&&&&&&&&&&&& Learning 결과 &&&&&&&&&&&&&&&&&')
        print(f'결정트리 검증결과: {model.accuracy_by_dtree(this)}')
        print(f'랜덤포레스트 검증결과: {model.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과: {model.accuracy_by_nb(this)}')
        print(f'KNN 검증결과: {model.accuracy_by_knn(this)}')
        print(f'SVM 검증결과: {model.accuracy_by_svm(this)}')

    def submit(self, train, test): # machine 이 된다. 이 단계는 캐글에게 내 머신을 보내서 평가받게 하는 것 입니다. 마치 수능장에 자식보낸 부모님 마음 ...
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame(
            {'PassengerId' : this.id, 'Survived' : prediction}
        ).to_csv(os.path.join('./data', 'submission.csv'), index=False)
        
if __name__ == '__main__':
    service = TitanicService()
    service.submit('train.csv', 'test.csv')