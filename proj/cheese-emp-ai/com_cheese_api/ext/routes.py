import logging
from re import search
from flask import Blueprint
from flask_restful import Api

from com_cheese_api.cmm.hom.home import Home
from com_cheese_api.usr.user.resource.user import User, Users
from com_cheese_api.usr.user.resource.login import Login
from com_cheese_api.usr.user.resource.signup import SignUp

from com_cheese_api.cop.itm.cheese.resource.cheese import Cheeses, Cheese, CheeseSearch
from com_cheese_api.cop.itm.cheese.model.cheese_dto import CheeseVo

from com_cheese_api.cop.ord.order.resource.order import Order, Orders
from com_cheese_api.cop.ord.order.resource.search import OrderSearch
from com_cheese_api.cop.ord.order.resource.best import GenderBest, AgeBest

from com_cheese_api.cop.rev.review.model.review_dto import ReviewVo
from com_cheese_api.cop.rev.review.resource.review import Review, Reviews

from com_cheese_api.cop.chat.chatbot.resource.chatbot import Chatbot
from com_cheese_api.cop.rec.recommend.resource.recommend import Recommend



home = Blueprint('home', __name__, url_prefix='/api')

# ================================= User =================================
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
login = Blueprint('login', __name__, url_prefix='api/login')
signup = Blueprint('signup', __name__, url_prefix='/api/signup')


# ================================= Cheese =================================
cheese = Blueprint('cheese', __name__, url_prefix='/api/cheese')
cheeses = Blueprint('cheeses', __name__, url_prefix='/api/cheeses')
cheese_search = Blueprint('cheese_search', __name__, url_prefix='/api/cheese/search')


# ================================= Order =================================
order = Blueprint('order', __name__, url_prefix='/api/order')
orders = Blueprint('orders', __name__, url_prefix='/api/orders')
order_search = Blueprint('order_search', __name__, url_prefix='/api/order/search')
gender_best = Blueprint('gender_best', __name__, url_prefix='/api/gender_best')
age_best = Blueprint('age_best', __name__, url_prefix='/api/age_best')


# ================================= Review =================================
review = Blueprint('review', __name__, url_prefix='/api/review')
# review_new = Blueprint('review_new', __name__, url_prefix='/api/review_new')
reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')


# ================================= Chatbot =================================
chatbot = Blueprint('chatbot', __name__, url_prefix='/api/chatbot/')


# ================================= Chatbot =================================
recommend = Blueprint('recommend', __name__, url_prefix='/api/recommend')




api = Api(home)

api = Api(user)
api = Api(users)
api = Api(login)
api = Api(signup)

# api = Api(cheese)
api = Api(cheeses)
api = Api(cheese_search)

api = Api(order)
api = Api(orders)
api = Api(order_search)
api = Api(gender_best)
api = Api(age_best)

api = Api(review)
# api = Api(review_new)
api = Api(reviews)


api = Api(chatbot)

api = Api(recommend)

####################################################################





def initialize_routes(api):    
    api.add_resource(Home, '/api')

    # ================================= User =================================
    api.add_resource(User, '/api/user', '/api/user/<user_id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Login, '/api/login')
    api.add_resource(SignUp, '/api/signup')

    # ================================= Cheese =================================
    api.add_resource(Cheese, '/api/cheese', '/api/cheese/<cheese_id>')
    api.add_resource(Cheeses, '/api/cheeses')
    api.add_resource(CheeseSearch, '/api/cheese/search', '/api/cheese/search/<category>')

    # ================================= Order =================================
    api.add_resource(Order, '/api/order', '/api/order/<user_id>')
    api.add_resource(OrderSearch, '/api/order/search/<order_no>')
    api.add_resource(Orders, '/api/orders')
    # api.add_resource(OrderBest, '/api/best')
    api.add_resource(GenderBest, '/api/gender_best')
    api.add_resource(AgeBest, '/api/age_best')

    # ================================= Review =================================
    api.add_resource(Review, '/api/review', '/api/review/<review_no>')
    # api.add_resource(ReviewNew, '/api/review_new/')
    api.add_resource(Reviews, '/api/reviews')


    # ================================= Chatbot =================================
    api.add_resource(Chatbot, '/api/chatbot')

    # ================================= Chatbot =================================
    api.add_resource(Recommend, '/api/recommend')


@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def login_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@user.errorhandler(500)
def auth_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@cheeses.errorhandler(500)
def cheese_api_error(e):
    logging.exception('An error occurred during cheeses request. %s' % str(e))
    return 'An internal error occurred.', 500

@order.errorhandler(500)
def order_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@cheeses.errorhandler(500)
def review_api_error(e):
    logging.exception('An error occurred during cheeses request. %s' % str(e))
    return 'An internal error occurred.', 500

@chatbot.errorhandler(500)
def review_api_error(e):
    logging.exception('An error occurred during cheeses request. %s' % str(e))
    return 'An internal error occurred.', 500

@recommend.errorhandler(500)
def review_api_error(e):
    logging.exception('An error occurred during cheeses request. %s' % str(e))
    return 'An internal error occurred.', 500
  
