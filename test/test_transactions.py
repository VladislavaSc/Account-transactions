import pytest
from src.transactions import Transaction


@pytest.fixture
def fixture_transaction_1():
    test_operation_1 = Transaction({"date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "rub.",
        "code": "RUB"
      }
    },
    "description": "Opening a deposit",
    "to": "Account 90817634362091276762"
  })
    return test_operation_1


@pytest.fixture
def test__repr__(fixture_transaction_1):
    assert fixture_transaction_1.__repr__() == ''Class Transaction({"date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "rub.",
        "code": "RUB"
      }
    },
    "description": "Opening a deposit",
    "to": "Account 90817634362091276762"
  })''

def test_date(fixture_transaction_1):
    assert fixture_transaction_1.date() == '21.06.2019'

def test_amount(fixture_transaction_1):
    assert fixture_transaction_1.amount() == '25762.92'

def test_description(fixture_transaction_1):
    assert fixture_transaction_1.description() == 'Opening a deposit'

def test_to_account(fixture_transaction_1):
    assert fixture_transaction_1.to_account() == 'Account 90817634362091276762'
