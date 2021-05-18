from flask import Flask, jsonify
from flask_restful import Resource, Api

from data.utils import *

app = Flask(__name__)
api = Api(app)


class GlobalCases(Resource):
    def get(self):
        data = complete_world_df().to_json()
        return data  # jsonify(data)


api.add_resource(GlobalCases, '/')

if __name__ == '__main__':
    app.run(debug=False)
