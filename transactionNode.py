class TransactionNode:
    def __init__(self, Transaction_ID, Account_ID, Transaction_Type, Amount, Date_Time):
        self.Transaction_ID = Transaction_ID
        self.Account_ID = Account_ID
        self.Transaction_Type = Transaction_Type
        self.Amount = Amount
        self.Date_Time = Date_Time
        self.next = None

    def __repr__(self):
        return (f"Transaction({self.Transaction_ID}, {self.Transaction_Type}, "
                f"Amount: ${self.Amount}, Date: {self.Date_Time})")
