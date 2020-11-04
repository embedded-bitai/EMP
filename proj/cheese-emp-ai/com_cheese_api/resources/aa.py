import pandas as pd

class aaa:
    def __init__(self):
    def hook(self):
        cheese_data = pd.read_csv("data/cheese_data.csv", index_col = 0)
        a = self.cheese_data(cheese_data)

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
        data['category'] = data['category'].map(category_map)
        df_category = data['category']
        print(df_category)
        print(cheese_data)
        return df_category

if __name__ == '__main__':
    aaa.hook()