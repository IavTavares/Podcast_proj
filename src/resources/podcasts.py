#from utilities.constants import *
from flask import request, jsonify
from flask_restful import Resource
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from scraper import *
from utilities.filesystem import *

class List_Podcasts(Resource):
    """Manage the API.

    Parameters
    ----------
    Resource : flask_restful.Resource

    """
    
    def get(self):
        podcast_list={}
        success = True
        errors = []
        file_path = os.path.join(PROJ_PATH,"data","db","podcast_list.json")
        try:
            with open(file_path, "r") as file:
                podcast_list = json.load(file)
        except:
            success = False
            errors.append("Could not load json file with podcast_list")
        # podcast_list is imported from constants
        podcast_list_names = [podcast["name"] for podcast in podcast_list.values()]
        
        response = {'list_podcast' : podcast_list_names,
                    'success': success,
                    'errors': errors}
        print(response)
        return response

class List_Episodes(Resource):
    """Manage the API.

    Parameters
    ----------
    Resource : flask_restful.Resource

    """
    # def __init__(self, model_extr, model_sim = None,clean_out_model=None):
    #     self.model_extr = model_extr
    #     self.model_sim = model_sim
    #     self.clean_out_model = clean_out_model
    

    # curl --request POST --url http://127.0.0.1:5000/list_episodes --header 'Content-Type: application/json' --data '{"podcast_url": "https://www.radiofrance.fr/franceculture/podcasts/cultures-monde"}'
    def post(self):
        data = request.get_json() # --header 'Content-Type: application/json'
        podcast_name = data["podcast_name"]
        info = get_info_podcast(podcast_name)
        podcast_url = info["url"]
        list_episodes_url = episode_list(podcast_url)
        success = "True"
        errors = []
        if len(list_episodes_url)== 0:
            success = "False"
            errors.append("No episode was found.")
        else:
            list_episodes_names = [file_name(el) for el in list_episodes_url]

        response = {'list_episodes_url': list_episodes_url,
                    'list_episodes_names' : list_episodes_names,
                    'success': success,
                    'podcast_name': podcast_name, 'errors': errors}
        return response


# class DownloadForm(Form):

class Download_Episodes(Resource):
    """Manage the API.

    Parameters
    ----------
    Resource : flask_restful.Resource

    """
    # def __init__(self, model_extr, model_sim = None,clean_out_model=None):
    #     self.model_extr = model_extr
    #     self.model_sim = model_sim
    #     self.clean_out_model = clean_out_model
    

    # curl --request POST --url http://127.0.0.1:5000/download_episodes --header 'Content-Type: application/json' --data '{"episodes_url_list": ["example1", "example2"],"podcast_name": "podcast_name"}'
    def post(self):
        data = request.get_json() # --header 'Content-Type: application/json'
        episodes_url_list = data["episodes_url_list"]
        podcast_name = data["podcast_name"]
        info = get_info_podcast(podcast_name)
        folder_path = info["folder"]
        download_mp3(episodes_url_list,folder_path)
        list_episodes_names = [file_name(el) for el in episodes_url_list]
        success = "True"
        errors = []
        response = {'podcast_name': podcast_name,
                    'list_episodes_names' : list_episodes_names,
                    'success': success, 'errors': errors}
        return response

