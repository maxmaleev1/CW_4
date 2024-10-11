import pytest
from src.api import HHAPI


@pytest.fixture
def hh_api():
    return HHAPI()


def test_get_vacancies__(hh_api):
    data = hh_api.get_vacancies__("слесарь")
    assert len(data) != 0