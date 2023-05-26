from src.transactions import Transaction
from src_utils import download_transactions, last_five_transactions

transactions_list = download_transactions()

clean_list = last_five_transactions(transactions_list)

for item in clean_list:
    transactions = Transaction(item)
    print(f'''\n{transactions.date()} {transactions.description()}
{transactions.hide_number(transactions.from_account())} -> {transactions.hide_number(transactions.to_account())}
{transactions.amount()}''')