from flask_restful import Resource, reqparse

class HomeAPI(Resource):
    def get(self):
        return {'message': 'Server Start'}