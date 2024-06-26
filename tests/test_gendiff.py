from gendiff.parser import generate_diff_json, generate_diff_yaml
from tests.fixtures import fixtures

FILE_PATH = 'tests/files/'


def test_json_f1_f2():
    result = generate_diff_json(f'{FILE_PATH}file1.json', f'{FILE_PATH}file2.json')
    true_result = fixtures.result_f1_f2
    assert result == true_result


def test_json_f1_f3():
    result = generate_diff_json(f'{FILE_PATH}file1.json', f'{FILE_PATH}file3.json')
    true_result = fixtures.result_f1_f3
    assert result == true_result


def test_json_f3_f2():
    result = generate_diff_json(f'{FILE_PATH}file3.json', f'{FILE_PATH}file2.json')
    true_result = fixtures.result_f3_f2
    assert result == true_result


def test_yaml_f3_f2():
    result = generate_diff_yaml(f'{FILE_PATH}file3.yml', f'{FILE_PATH}file2.yaml')
    true_result = fixtures.result_f3_f2
    assert result == true_result


def test_yaml_f1_f2():
    result = generate_diff_yaml(f'{FILE_PATH}file1.yml', f'{FILE_PATH}file2.yaml')
    true_result = fixtures.result_f1_f2
    assert result == true_result


def test_yaml_f1_f3():
    result = generate_diff_yaml(f'{FILE_PATH}file1.yml', f'{FILE_PATH}file3.yml')
    true_result = fixtures.result_f1_f3
    assert result == true_result
