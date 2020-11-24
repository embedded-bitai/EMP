import logging
from flask import Blueprint
from flask_restful import Api

from flask_restful import Resource

class Home(Resource):

    @staticmethod
    def get():
        return {'message': 'Server Start'}