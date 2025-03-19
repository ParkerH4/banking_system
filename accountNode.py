class AccountNode:
    def __init__(self, Account_ID, Account_Type, Balance, Date_Created):
        self.Account_ID = Account_ID
        self.Account_Type = Account_Type
        self.Balance = Balance
        self.Date_Created = Date_Created
        self.next = None

    def __repr__(self):
        return f"Account({self.Account_ID}, {self.Account_Type}, Balance: ${self.Balance})"
