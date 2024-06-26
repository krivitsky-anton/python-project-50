import json
import yaml


def generate_diff_json(file1, file2):
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


def generate_diff_yaml(file1, file2):
    with open(file1, 'r') as _file1:
        file1 = yaml.safe_load(_file1)
    with open(file2, 'r') as _file2:
        file2 = yaml.safe_load(_file2)
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
