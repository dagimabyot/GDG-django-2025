import json
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def get_account_type(self):
        pass


class SavingsAccount(Account):
    def get_account_type(self):
        return "This is a Savings Account."


class CurrentAccount(Account):
    def get_account_type(self):
        return "This is a Current Account."


json_data = '''
[
  {"account_type": "savings"},
  {"account_type": "current"}
]
'''

data = json.loads(json_data)

accounts = []

for item in data:
    if item["account_type"] == "savings":
        accounts.append(SavingsAccount())

    elif item["account_type"] == "current":
        accounts.append(CurrentAccount())


for acc in accounts:
    print(acc.get_account_type())
