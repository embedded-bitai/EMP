import pandas as pd
df = pd.read_csv('cheese_data.csv', encoding = 'utf-8')
#cheese_data = df.drop(cheese_data.columns[[0]], axis='columns')
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
cheese_data['category']