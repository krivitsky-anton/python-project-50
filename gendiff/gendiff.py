import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', dest='FORMAT', help='set format of output')
    # args = parser.parse_args()


if __name__ == '__main__':
    main()


def generate_diff(file1, file2):
    file1 = json.load(open(file1, 'r'))
    file2 = json.load(open(file2, 'r'))
    keys = set(file1.keys()).union(file2.keys())
    res = '{\n'
    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1[key] != file2[key]:
                res += f'- {key}: {file1[key]}\n'
                res += f'+ {key}: {file2[key]}\n'
            else:
                res += f'  {key}: {file1[key]}\n'
        elif key in file1:
            res += f'- {key}: {file1[key]}\n'
        else:
            res += f'+ {key}: {file2[key]}\n'
    res += '}'
    return res
