import constants
from flask import request
from flask_restful import Resource
import json

from scraper import *
from utilities.filesystem import *


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
    

    # curl --request POST --url http://127.0.0.1:5000/list_episodes --data '{"podcast_url": "example.com"}'

    def post(self):
        data = request.get_json()
        podcast_url = data["podcast_url"]
        list_episodes_url = episode_list(podcast_url)
        success = "True"
        errors = []
        if len(list_episodes_url)== 0:
            success = "False"
            errors.append("No episode was found.")
        else:
            list_episodes_names = [file_name(el) for el in list_episodes_url]

        response = {'list_episodes_url': list_episodes_url,
                    'list_episodes_names' : list_episodes_url,
                    'success': success,
                    'podcast_url': podcast_url, 'errors': errors}
        return response