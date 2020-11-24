from flask_restful import Resource, reqparse

class CheeseAPI(Resource):
    def get(self):
        return {'message': 'Cheese Api Start !!'}