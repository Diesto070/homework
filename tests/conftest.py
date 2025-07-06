import pytest

@pytest.fixture
def my_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]