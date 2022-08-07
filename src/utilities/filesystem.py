import os
if __name__!="__main__":
    from .constants import *
else:
    from constants import *

import json


def folder_Q(folder_path):
    return os.path.isdir(folder_path)

def file_Q(file_path):
    return os.path.exists(file_path)

def create_folder(folder_path):
    os.makedirs(folder_path)

def get_info_podcast(name:str)-> dict:
    file_path = os.path.join(PROJ_PATH,"data","db","podcast_list.json")
    with open(file_path, "r") as file:
            db_json = json.load(file)
    for show,info in db_json.items():
        if info["name"] == name:
            return info
        else:
            {"folder":None,"url":None,"name":None}


def initialize_podcast_json():
    file_path = os.path.join(PROJ_PATH,"data","db","podcast_list.json")
    if not folder_Q(file_path):
        with open(file_path, "w") as write_file:
            json.dump(podcast_list, write_file) 
            # podcast_list is imported from constants

if __name__=="__main__":
    initialize_podcast_json()
    name = "Concordance des Temps"
    get_info_podcast(name) == {'folder': '/home/ivo/Programmin..._des_temps', 'url': 'https://www.radiofra...-des-temps', 'name': 'Concordance des Temps'}