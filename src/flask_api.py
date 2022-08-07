from flask_restful import Api
from flask import Flask
from utilities.constants import *
from utilities.filesystem import *
from resources.podcasts import List_Episodes, List_Podcasts,Download_Episodes




app = Flask(__name__)
api = Api(app)

#Add url endpoints
api.add_resource(List_Episodes, '/list_episodes')
api.add_resource(List_Podcasts, '/list_podcasts')
api.add_resource(Download_Episodes, '/download_episodes')

if __name__ == '__main__':
    initialize_podcast_json()
    app.run(debug=False, host='0.0.0.0', port=5000)