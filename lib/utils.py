import os
import re

def get_sub_folder_path(directory):
    entries = os.listdir(directory)

    # Filter out only the folders (directories)
    folders = {}
    for entry in entries:
        if os.path.isdir(os.path.join(directory, entry)):
            folders[entry] = os.path.join(directory, entry)

    return folders

def is_valid_regex(regex_string):
    try:
        re.compile(regex_string)
        return None
    except re.error as e:
        return e