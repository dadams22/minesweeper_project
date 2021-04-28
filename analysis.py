from os import listdir
from os.path import isfile, join


def get_all_files(directory_path: str):
    files = []
    for file in listdir(directory_path):
        full_filepath = join(directory_path, file)
        if isfile(full_filepath):
            files.append(full_filepath)
    return files