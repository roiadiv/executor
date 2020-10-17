from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Task(Resource):

    def get(self, search):
        return {"search": search}


api.add_resource(Task, '/search/<string:search>')

app.run()
