import os
import argparse
from os.path import join, getsize


def find_duplicates(folder_path):
    known_files = dict()
    duplicate_path_position = 1
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_size = getsize(join(root, filename))
            uid = join(filename, str(file_size))
            if uid in known_files:
                known_files[uid][duplicate_path_position].append(root)
            else:
                duplicate_path = []
                known_files[uid] = [root, duplicate_path]
    return known_files


def pprint_duplicates(dupl_dict):
    duplicate_path = 1
    root_path = 0
    filename_pos = 0
    for item in filter(lambda x: dupl_dict[x][duplicate_path], dupl_dict):
        for path in dupl_dict[item][duplicate_path]:
            print('File "{}" located in "{}" and "{}"'.format(
                item.split('/')[filename_pos], dupl_dict[item][root_path], path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help="Input path to folder with duplicates:", type=str, required=True)

    args = parser.parse_args()
    pprint_duplicates(find_duplicates(args.path))
