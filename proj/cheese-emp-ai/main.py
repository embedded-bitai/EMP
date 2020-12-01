from flask import Flask
from flask_restful import Api
from com_cheese_api.ext.db import url, db, openSession
from com_cheese_api.ext.routes import initialize_routes

from com_cheese_api.usr.user.model.user_dfo import UserDfo
from com_cheese_api.usr.user.model.user_dao import UserDao
# from com_cheese_api.usr.user.model.user_dto import UserDto

from com_cheese_api.cop.ord.order.model.order_dfo import OrderDfo
from com_cheese_api.cop.ord.order.model.order_dao import OrderDao
# from com_cheese_api.cop.ord.order.model.order_dto import OrderDto

from com_cheese_api.cop.itm.cheese.model.cheese_dfo import CheeseDfo
from com_cheese_api.cop.itm.cheese.model.cheese_dao import CheeseDao
# from com_cheese_api.cop.itm.cheese.model.cheese_dto import cheeseDto

# from com_cheese_api.cop.rev.review.model.review_dto import ReviewDto
from com_cheese_api.cop.rev.review.model.review_dao import ReviewDao

from flask_cors import CORS,cross_origin

Session = openSession()
session = Session()


app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})
CORS(app, resources={r'/api/*': {"origins": "http://localhost:3000"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)



# if __name__ == '__main__':

with app.app_context():

    db.create_all()
# User > Cheese > Order > Review
# ================================= User =================================
    user_count = UserDao.count()
    print(f'USER TABLE CNT : {user_count[0]:10}')

    print(f'===== Users Total Count is {user_count} =====')
    if user_count[0] == 0:
        UserDao.bulk()
    else:
        print("Users Data exists...")

    # user_all = UserDao.find_all()
    print(f'insert 테스트!!')
    # print(f'===== Users Total Count is {user_all} =====')
    # UserDao.bulk()
    # user_all.bulk()

# ================================= Cheese =================================
    cheese_count = CheeseDao.count()

    # cheese_find_one = CheeseDao.find_by_cheese(cheese_id)
    # print(f'===== Cheese find one {cheese_find_one} =====')

    # cheese_all = CheeseDao.find_all()
    # print(f'========Cheese all {cheese_all} ==========')

    print(f'==========Cheeses Data Insert!!!==========')
    print(f'===== Cheeses Total Count is {cheese_count} =====')
    if cheese_count[0] == 0:
        CheeseDao.bulk()
    else:
        print("Cheeses Data exists...")


# ================================= Order =================================
    print(f'==========Orders Data Insert!!!==========')
    order_count = OrderDao.count()

    if order_count[0] == 0:
        OrderDao.bulk()
    else:
        print("Orders Data exists...")

# ================================= Review =================================
    print(f'==========Reviews Data Insert!!!==========')
    review_count = ReviewDao.count()

    if review_count[0] == 0:
        ReviewDao.bulk()
    else:
        print("Reviews Data exists...")


initialize_routes(api)

print("========== main.py END ==========")

