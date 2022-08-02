import os


def folder_Q(folder_path):
    return os.path.isdir(folder_path)

def file_Q(file_path):
    return os.path.exists(file_path)

def create_folder(folder_path):
    os.makedirs(folder_path)