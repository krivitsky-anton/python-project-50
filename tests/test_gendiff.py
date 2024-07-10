import pytest


def test_generate_diff():
    pass


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
