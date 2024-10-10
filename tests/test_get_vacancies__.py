import pytest
from src.api import HHAPI

def test_get_vacancies__():
    HHAPI.get_vacancies__(self, 'слесарь'):
    assert response.json()["items"]

    pass


# @pytest.fixture
# def example():
#     return HHAPI()
#
#
# def test_get_vacancies__(example):
#     for x in example.get_vacancies__(self, 'слесарь')