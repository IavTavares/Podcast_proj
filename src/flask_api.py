from flask_restful import Api
from flask import Flask
from constants import *
from resources.list_episodes import List_Episodes



app = Flask(__name__)
api = Api(app)

#Add url endpoints
api.add_resource(List_Episodes, '/list_episodes')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)