from gendiff.gendiff import generate_diff
from tests.fixtures import fixtures


def test_two_json():
    result = generate_diff('tests/files/file1.json', 'tests/files/file2.json')
    true_result = fixtures.result_file1_file2
    assert result == true_result

