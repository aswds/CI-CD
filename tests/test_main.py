import pytest


@pytest.fixture(scope='module', params=['../file1.txt', '../file2.txt'])
def file_lines(request):
    file_name = request.param
    print(file_name)
    with open(file_name, 'r') as file:
        return file.readlines()


@pytest.fixture(scope='module')
def same_lines(file_lines):
    other_file_lines = file_lines[::-1]
    return set(file_lines).intersection(other_file_lines)


@pytest.fixture(scope='module')
def diff_lines(file_lines):
    other_file_lines = file_lines[::-1]
    return set(file_lines).symmetric_difference(other_file_lines)


@pytest.fixture(scope='module')
def same_file(same_lines):
    with open('../same.txt', 'w') as same_file:
        for line in same_lines:
            same_file.write(line)
    yield same_file


@pytest.fixture(scope='module')
def diff_file(diff_lines):
    with open('../diff.txt', 'w') as diff_file:
        for line in diff_lines:
            diff_file.write(line)
    yield diff_file


def test_same_file_contains_same_lines(same_file, same_lines):
    same_file_lines = set(same_file.readlines())
    assert same_file_lines == same_lines


def test_diff_file_contains_diff_lines(diff_file, diff_lines):
    diff_file_lines = set(diff_file.readlines())
    assert diff_file_lines == diff_lines
