import pandas as pd
from com_cheese_api.cmm.utl.file import FileReader

import os
# ==============================================================
# ====================                     =====================
# ====================    Preprocessing    =====================
# ====================                     =====================
# ==============================================================


# 데이터 정제 과정
class ReviewDfo(object):

    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__))+'/data')
        self.odf = None
        # self.review_data_frame = None

    def review_df(self):
        review_data_frame = pd.read_csv(
            'com_cheese_api/cop/rev/review/data/cheese_review_for_analysis.csv',
            sep=','
        )
        
        return review_data_frame


    def review_df_refine(self, review_data_frame):

        print(f'[리뷰 데이터 행과 열 확인]\n{review_data_frame.shape}')
        print(f'[리뷰 데이터 타입 확인]\n{review_data_frame.dtypes}')

        df = pd.DataFrame(review_data_frame)

        # review_title 컬럼 정제
        # '[' 제거
        split = df['review_title'].str.split("[")
        df['review_title'] = split.str.get(1)
        split

        # ']' 제거
        split = df['review_title'].str.split("]")
        df['review_title'] = split.str.get(0)
        split

        # "'" 제거
        split = df['review_title'].str.split("'")
        df['review_title'] = split.str.get(1)
        split


        # review_views 컬럼 정제
        # '[' 제거
        split = df['review_views'].str.split("[")
        df['review_views'] = split.str.get(1)
        split

        # ']' 제거
        split = df['review_views'].str.split("]")
        df['review_views'] = split.str.get(0)
        split

        # "'" 제거
        split = df['review_views'].str.split("'")
        df['review_views'] = split.str.get(1)
        split


        # review_date 컬럼 정제
        # '[' 제거
        split = df['review_date'].str.split("[")
        df['review_date'] = split.str.get(1)
        split

        # ']' 제거
        split = df['review_date'].str.split("]")
        df['review_date'] = split.str.get(0)
        split

        # "'" 제거
        split = df['review_date'].str.split("'")
        df['review_date'] = split.str.get(1)
        split


        # review_detail 컬럼 정제
        # "\n" 제거(review_detail)
        split = df['review_detail'].str.split("\n")
        df['review_detail'] = split.str.get(1)
        split

        # bulk 진행 시 Unknown column 'nan' in 'field list' 오류 발생
        # 컬럼 속성값이 nan인 경우 발생, 결측값이 있는 행을 제거 후 
        # DB inset를 하면 된다.

        # 결측값 확인 및 제거
        print(f'\n========= 결측값 확인 !! =========')
        print(df.isnull().any())
        # 결측값이 있는 행 제거
        df.dropna(axis=0, how='any', inplace=True)

        # pandas로 가공한 데이터 csv 파일로 다시 저장하기
        # df.to_csv('cheese_review_panda1118_2.csv')
        print(f'\n========= 리뷰 df 출력 !! =========\n{df}')
        return df


# brand_name, product_name은 원래 '[퀘스크렘] 블루치즈 크림치즈' 이렇게 한 덩어리로 나옴
'''
	category	brand_name	product_name	review_title	review_detail	review_date	review_views
0	크림	퀘스크렘	블루치즈 크림치즈	['고르곤졸라피자를 좋아하신다면! ']	\n아웃백의 블루치즈드레싱을 엄청 좋아하고 고르곤졸라피자도 좋아합니다. 그래서 혹시...	['2020-10-27']	['4']
1	크림	퀘스크렘	블루치즈 크림치즈	['치즈맛 찐해요 ']	\n꼬소한 치즈 냄새가 확 나요\n	['2020-10-26']	['4']
2	크림	퀘스크렘	블루치즈 크림치즈	['좋아요 ']	\n많이 꼬릿꼬릿(?)하진 않아요~적당히 즐길수 있는 불루 치즈 맛입니다~~^^\n	['2020-10-25']	['7']
3	크림	퀘스크렘	블루치즈 크림치즈	['꿀이랑 너무 잘 어울림 ']	\n이것만 먹으면 꼬릿한데 꿀 넣으면 존맛탱\n	['2020-10-25']	['5']
4	크림	퀘스크렘	블루치즈 크림치즈	['맛있어요 ']	\n계속 재구매할것같아요\n	['2020-10-24']	['3']
...	...	...	...	...	...	...	...
995	브리	카스텔로	덴마크 브리 치즈	['샐러드용 ']	\n과일과 샐러드 해먹어도 좋아요~ 발사믹과 잘 어울립니다\n	['2020-10-25']	['1']
996	브리	카스텔로	덴마크 브리 치즈	['브리 ']	\n치즈 구워서 꿀이랑 견과류 짱맛\n	['2020-10-25']	['3']
997	브리	카스텔로	덴마크 브리 치즈	['첫구매 ']	\n와인안주로구매해밧어용\n	['2020-10-24']	['0']
998	브리	카스텔로	덴마크 브리 치즈	['브리치즈 ']	\n브리치즈 샌드위치 만드려고 샀어요 \n맛있었음 좋겠어요\n	['2020-10-24']	['1']
999	브리	카스텔로	덴마크 브리 치즈	['다들 추천하는 이유가 ']	\n짭쪼름하고 냄새 안나서 좋아요\n150도 예열 후 5분 땡 하면 너무 맛있게 구...	['2020-10-24']	['3']
1000 rows × 7 columns
'''