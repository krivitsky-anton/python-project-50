import argparse

from gendiff.parser import generate_diff_json, generate_diff_yaml


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', dest='FORMAT', help='set format of output')
    args = parser.parse_args()
    if str(args.first_file)[-4:] == 'json':
        generate_diff_json(args.first_file, args.second_file)
    else:
        generate_diff_yaml(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
