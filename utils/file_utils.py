# encoding: utf-8
"""
file utilities
"""
import os
import collections
from utils import consts


# count filetype in a directory, return dict of filetype and count
def count_filetype_in_dir(dir_path: str) -> dict:
    """count filetype in a directory, return dict of filetype and count
    """
    filetype_dict = collections.defaultdict(int)
    for _, _, files in os.walk(dir_path):
        for file in files:
            filetype = file.split('.')[-1]
            filetype_dict[filetype] += 1
    return filetype_dict


# aggregate all files in a directory, return a dict of filetype and list of files
def aggregate_files_in_dir(dir_path: str) -> dict:
    """
        aggregate all files in a directory, return a dict of filetype and list of files
    """
    filetype_dict = collections.defaultdict(list)
    for root, _, files in os.walk(dir_path):
        for file in files:
            filetype = file.split('.')[-1]
            filetype_dict[filetype].append(os.path.join(root, file))
    return filetype_dict


if __name__ == "__main__":
    data_dir = os.path.join(consts.ROOT_DIR, "datasets")
    output = count_filetype_in_dir(data_dir)
    print(output)
