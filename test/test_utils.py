import pytest as pytest
from src.src_utils import last_five_transactions


@pytest.fixture
def src_utils_fixture():
    return [{"id": "1", "date": "01.01.2023", "state": "EXECUTED"},
            {},
            {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
            {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
            {"id": "4", "date": "01.05.2023", "state": "EXECUTED"}]

def test_last_five_transactions(src_utils_fixture):
    assert last_five_transactions(src_utils_fixture) == [{"id": "4", "date": "01.05.2023", "state": "EXECUTED"},
                                                         {"id": "3", "date": "01.02.2023", "state": "EXECUTED"},
                                                         {"id": "2", "date": "01.03.2023", "state": "EXECUTED"},
                                                         {"id": "1", "date": "01.01.2023", "state": "EXECUTED"}]