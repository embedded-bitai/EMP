from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
import pandas as pd
import numpy as np
import os

import joblib
from com_cheese_api.cmm.utl.file import FileReader


class RecommendAi(object):
    def __init__(self):
        self.data = None
        self.cheese_model = joblib.load("com_cheese_api/cop/modeling/cheese_knn_model.pkl")
        
    @staticmethod
    def read_survey(query, param):
        survey_result = RecommendDfo().dump_to_csv(query, param)
        return survey_result
    

    def preprocessing_data(self, query, param):
        survey_result = RecommendAi.read_survey(query, param) 

        features = ['user_id',  '간식', '감자', '견과류', '과일', '그라탕',
       '김가루', '꿀', '딥소스', '라자냐', '리소토', '마르게리타 피자', '막걸리', '맥앤치즈', '맥주',
       '멤브리요', '무화과', '바질', '발사믹 식초', '발사믹식초', '배', '베이컨', '볶음밥', '비스킷', '빵',
       '사케', '사퀘테리', '샌드위치', '샐러드', '샐러리', '샤퀴테리', '소금', '스테이크', '스프', '스프레드',
       '올리브오일', '올리브유', '와인', '위스키', '잼', '채소', '치즈케이크', '카나페', '카프레제',
       '카프레제 샐러드', '크래커', '크로스티니', '키쉬', '타르트', '타파스', '테이블치즈', '토마토', '토스트',
       '파스타', '팬케이크', '퐁듀', '피자', '핑거 푸드', '핑거푸드', '화이트와인']
        survey_df = pd.DataFrame(survey_result, columns=features)

        food_value = survey_result.values

        select_food = []
        for food_item in food_value:
            select_food.append(food_item[1:])


        for select_food in food_value:
            for column_item in survey_df.columns:
                if column_item in select_food:
                    survey_df[column_item] = 1
                else:
                    survey_df.fillna(0, inplace=True)


        if (survey_df['피자'] == 1).any:
            survey_df['마르게리타 피자'] = 1
        if (survey_df['베이컨'] == 1).any:
            survey_df['샤퀴테리'] = 1
        if (survey_df['맥앤치즈'] == 1).any:
            survey_df['테이블치즈'] = 1
        if (survey_df['볶음밥'] == 1).any:
            survey_df['김가루'] = 1
        if (survey_df['과일'] == 1).any:
            survey_df['배'] = 1
            survey_df['토마토'] = 1
            survey_df['무화과'] = 1
        if (survey_df['빵'] == 1).any:
            survey_df['토스트'] = 1
            survey_df['샌드위치'] = 1 
            survey_df['팬케이크'] = 1 
            survey_df['간식'] = 1
        if (survey_df['샐러드'] == 1).any:
            survey_df['샐러리'] = 1
            survey_df['채소'] = 1
        if (survey_df['카프레제'] == 1).any:
            survey_df['카프레제 샐러드'] = 1
        if (survey_df['핑거푸드'] == 1).any:
            survey_df['타파스'] = 1
            survey_df['핑거 푸드'] = 1
            survey_df['크로스티니'] = 1 
            survey_df['카나페'] = 1 
            survey_df['크래커'] = 1
            survey_df['비스킷'] = 1
        if (survey_df['타르트'] == 1).any:
            survey_df['키쉬'] = 1
        if (survey_df['견과류'] == 1).any:
            survey_df['감자'] = 1
            survey_df['멤브리요'] = 1
        if (survey_df['딥소스'] == 1).any:
            survey_df['스프레드'] = 1
        if (survey_df['발사믹식초'] == 1).any:
            survey_df['발사믹 식초'] = 1
            survey_df['소금'] = 1
        if (survey_df['올리브유'] == 1).any:
            survey_df['올리브오일'] = 1

        self.data = survey_df

        survey_list = []
        for list_item in np.array(self.data):
            survey_list.append(list_item[1:])
        return survey_list

    def recommend_cheese(self, query, param):
        survey_list = self.preprocessing_data(query, param)
        recommend_pred = self.cheese_model.predict(np.array(survey_list).tolist()).tolist()
        return recommend_pred

        


if __name__ == '__main__':
    recommendAi = RecommendAi()
    recommendAi.recommend_cheese(query, param)
