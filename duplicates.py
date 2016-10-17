import os
import argparse


def are_files_duplicates(folder_path):
    duplicates = dict()
    for directory in os.walk(folder_path):
        for filename in directory[2]:
            size = os.path.getsize(directory[0] + '/' + filename)
            if filename in duplicates.keys() and size == duplicates[filename][1]:
                print (
                    filename, 'IN',  directory[0], 'AND', duplicates[filename][0])
            else:
                duplicates[filename] = [directory[0], size]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help="Input path to folder this duplicates:", type=str, required=True)

    args = parser.parse_args()
    are_files_duplicates(args.path)
