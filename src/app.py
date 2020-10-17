from flask import Flask, request
from flask_restful import Resource, Api
from scripts.WikipediaRobot import WikipediaRobot

app = Flask(__name__)
api = Api(app)


class Task(Resource):

    def get(self, search):
        wikipediaRobot = WikipediaRobot(search)
        return wikipediaRobot.getData()


api.add_resource(Task, '/search/<string:search>')

app.run(debug=True)
