import pandas as pd
import pymysql
from datetime import datetime



class RecommendDfo:
    def dump_to_csv(self, query, param):
        # DB Connection
        conn = pymysql.connect(host='localhost', port= 3306,
                user='root',
                password='',
                database='com_cheese_api')

        # Start Time
        start_tm = datetime.now()

        # Get a DataFrame
        # global query_result

        query_result = pd.read_sql_query(query, conn, params = {'userId': param})

        # Close connection
        end_tm = datetime.now()

        print('START TIME: ', str(start_tm))
        print('END TIME: ', str(end_tm))
        print('ELAP time: ', str(end_tm - start_tm))
        conn.close()
        
        print(type(query_result))
        print(query_result)

        food_value = query_result.values
        print(food_value)
        print(type(food_value))

        return query_result

query = """
    SELECT * FROM recommends
"""

if __name__ == '__main__':
    recommendDfo = RecommendDfo()
    recommendDfo.dump_to_csv(query)

