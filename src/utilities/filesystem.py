import os
from .constants import *
import json


def folder_Q(folder_path):
    return os.path.isdir(folder_path)

def file_Q(file_path):
    return os.path.exists(file_path)

def create_folder(folder_path):
    os.makedirs(folder_path)


def initialize_podcast_json():
    file_path = os.path.join(PROJ_PATH,"data","db","podcast_list.json")
    if not folder_Q(file_path):
        with open(file_path, "w") as write_file:
            json.dump(podcast_list, write_file) 
            # podcast_list is imported from constants

if __name__=="__main__":
    initialize_podcast_json()