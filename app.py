from flask import Flask
from flask_restful import Api

from resources import Fibonacci

app = Flask(__name__)
api = Api(app, prefix='/api')

api.add_resource(Fibonacci, '/fibonacci')
