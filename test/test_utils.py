import pytest


def last_five_transactions(fixture):
    assert last_five_transactions(fixture) == [
        {"id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041"},
        {"id": 41428829,
         "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572"},
        {"id": 587085106,
         "state": "EXECUTED",
         "date": "2018-03-23T10:45:06.972075"},
        {"id": 142264268,
         "state": "EXECUTED",
         "date": "2019-04-04T23:20:05.206878"}
    ]


def test_json_file():
    load = test_transaction_json(load_json())
