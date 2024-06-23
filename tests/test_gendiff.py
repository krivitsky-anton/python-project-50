from gendiff.gendiff import generate_diff
from tests.fixtures import fixtures

FILE_PATH = 'tests/files/'


def test_f1_f2():
    result = generate_diff(f'{FILE_PATH}file1.json', f'{FILE_PATH}file2.json')
    true_result = fixtures.result_f1_f2
    assert result == true_result


def test_f1_f3():
    result = generate_diff(f'{FILE_PATH}file1.json', f'{FILE_PATH}file3.json')
    true_result = fixtures.result_f1_f3
    assert result == true_result


def test_f3_f2():
    result = generate_diff(f'{FILE_PATH}file3.json', f'{FILE_PATH}file2.json')
    true_result = fixtures.result_f3_f2
    assert result == true_result
