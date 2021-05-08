from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    @staticmethod
    def get():
        return "Hello Mathematical API!"


api.add_resource(Hello, '/')
