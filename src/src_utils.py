import datetime
import os
import json

path_to_file = os.path.abspath('../data/')
path_to_transaction = os.path.join(path_to_file, 'operations.json')

def download_transactions():

    with open(path_to_transaction, 'r', encoding='utf8') as file:
        transactions_list = json.load(file)

        return transactions_list

