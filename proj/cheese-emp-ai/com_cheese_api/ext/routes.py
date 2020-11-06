import logging
from flask import Blueprint
from flask_restful import Api
from com_cheese_api.cmm.hom.resource.home import Home
from com_cheese_api.cop.rvw.model.review_dto import ReviewVo
from com_cheese_api.cop.chs.model.cheese_dto import CheeseVo
from com_cheese_api.cop.rvw.resource.review import Review, Reviews
from com_cheese_api.usr.resource.user import User, Users
from com_cheese_api.usr.resource.access import Access

# from com_cheese_api.resources.item import Item, Items
# from com_cheese_api.resources.user import User, Users, Auth, Access
# from com_cheese_api.resources.cabbage import Cheese

home = Blueprint('home', __name__, url_prefix='/api')
# user = Blueprint('user', __name__, url_prefix='/api/user')
# users = Blueprint('users', __name__, url_prefix='/api/users')
# auth = Blueprint('auth', __name__, url_prefix='/api/auth')
# access = Blueprint('access', __name__, url_prefix='/api/access')
cabbage = Blueprint('cheese', __name__, url_prefix='/api/cheese')

api = Api(home)

def initialize_routes(api):
    
    api.add_resource(Home, '/api')
    # api.add_resource(Item, '/api/item/<string:id>')
    # api.add_resource(Items,'/api/items')
    # api.add_resource(User, '/api/user/<string:id>')
    # api.add_resource(Users, '/api/users')
    # api.add_resource(Auth, '/api/auth')
    # api.add_resource(Access, '/api/access')
    api.add_resource(Cheese, '/api/cheese')


@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

# from com_cheese_api.home.api import Home
# from com_cheese_api.cheese.api import Cheese
# from com_cheese_api.recommend.api import Recommend
# from com_cheese_api.signin.api import SignIn
# from com_cheese_api.fnq.api import Fnq


# def initialize_routes(api):
#     api.add_resource(Home, '/api')
#     api.add_resource(Cheese, '/cheese')
#     api.add_resource(Recommend, '/recommend')
#     api.add_resource(SignIn, '/signin')
#     api.add_resource(Fnq, '/fnq')
