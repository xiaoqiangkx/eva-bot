# encoding: utf-8

# count filetype in a directory, return dict of filetype and count
def count_filetype_in_dir(dir_path):
    import os
    import collections
    filetype_dict = collections.defaultdict(int)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            filetype = file.split('.')[-1]
            filetype_dict[filetype] += 1
    return filetype_dict


if __name__ == "__main__":
    from utils import consts
    import os
    dir_path = os.path.join(consts.ROOT_DIR, "datasets")
    filetype_dict = count_filetype_in_dir(dir_path)
    print(filetype_dict)
