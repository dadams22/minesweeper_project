from os import listdir
from os.path import isfile, join


def get_all_files(directory_path: str):
    return [join(directory_path, f) for f in listdir(directory_path) if isfile(join(directory_path, f))]