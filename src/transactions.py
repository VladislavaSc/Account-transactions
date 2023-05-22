import datetime


class Transaction:

    def __init__(self, transaction):
        self.transaction = transaction

    def description(self):
        return self.transaction['description']

    def __repr__(self):
        return f'Class Transaction({self.transaction}'

    def from_account(self):
        if 'from' in self.transaction.key():
            return self.transaction['from']
        else:
            return ''

    def to_account(self):
        return self.transaction['to']

    def date(self):
        transaction_date = self.transaction['date']
        transaction_time = datetime.strptime(transaction_date, '%Y-%m-%dT%H:%M:%S.%f')
        return transaction_time.strftime('%d.%m.%Y')

    def hide_number(self, account):
        if account == '':
            return 'Depositing funds'
        else:
            account = account.split(' ')
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = ' '.join(account)
            if 'account' in account:
                return f'{account_name} **{account_number[16:20]}'
            else:
                return f'{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}'

        def amount(self):
            return f'{self.transaction["operationAmount"]["amount"]} {self.transaction["operationAmount"]["currency"]["name"]}'

