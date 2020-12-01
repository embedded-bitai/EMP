from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
import pandas as pd
import numpy as np
import os

import joblib
from com_cheese_api.cmm.utl.file import FileReader


class RecommendAi(object):
    def __init__(self):
        self.data = RecommendDfo().dump_to_csv('com_cheese_api', 'com_cheese_api/cop/rec/recommend/data/recommend_data.csv')
        # self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_knn_model.pkl")
        self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_model.h5")
        
    def recommend_cheese(self, user_id, file_path):
        query = """SELECT * FROM recommends WHERE user_id = 'user_id'"""
        survey = self.data(query)
        # cheese_data = FileReader.csv_load(file_path, 'utf-8-sig')
        return self.predict_data(self.model, survey)

    def predict_data(self, model, data):        
        recom_cheese = data['chooseFood_1', 'chooseFood_2']
        


if __name__ == '__main__':
    recommendAi = RecommendAi()
    # recommendAi.dump_to_csv('com_cheese_api', 'com_cheese_api/cop/rec/recommend/data/recommend_data.csv')


# from com_cheese_api.cop.rec.recommend.model.recommend_dfo import RecommendDfo
# import pandas as pd
# import numpy as np
# import os

# import joblib
# from com_cheese_api.cmm.utl.file import FileReader


# class RecommendAi(object):
#     def __init__(self):
#         self.data = RecommendDfo().dump_to_csv
#         # self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_knn_model.pkl")
#         self.cheese_model = joblib.load("com_cheese_api/cop/machine/cheese_model.h5")


#     def recommend_cheese(self, user_id, file_path):
#         query = """SELECT * FROM recommends WHERE user_id = 'user_id'"""
#         survey = self.data(query)
#         # cheese_data = FileReader.csv_load(file_path, 'utf-8-sig')
#         return self.predict_data(self.model, survey)

#     def predict_data(self, model, data):        
#         recom_cheese = data['chooseFood_1', 'chooseFood_2']
        


# if __name__ == '__main__':
#     recommendAi = RecommendAi()
#     # recommendAi.dump_to_csv('com_cheese_api', 'com_cheese_api/cop/rec/recommend/data/recommend_data.csv')