import os
import argparse
from os.path import join, getsize


def are_files_duplicates(folder_path):
    known_files = dict()
    size_position = 0
    duplicate_position = 2
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_size = getsize(join(root, filename))
            if filename in known_files and file_size == known_files[filename][size_position]:
                known_files[filename][duplicate_position].append(root)
            else:
                duplicate_path = []
                known_files[filename] = [file_size, root, duplicate_path]
    return known_files


def pprint_duplicates(data):
    duplicate_position = 2
    root_position = 1
    if data:
        for key in data:
            if key:
                for path in data[key][duplicate_position]:
                    print('File "{}" located in "{}" and "{}"'.format(
                        key, data[key][root_position], path))
    else:
        print('In this folder are no duplicates!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help="Input path to folder with duplicates:", type=str, required=True)

    args = parser.parse_args()
    pprint_duplicates(are_files_duplicates(args.path))
