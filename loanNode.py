class LoanNode:
    def __init__(self, Loan_ID, Loan_Type, Original_Amount, Interest_Rate, Remaining_Balance, Start_Date, End_Date, Status):
        self.Loan_ID = Loan_ID
        self.Loan_Type = Loan_Type
        self.Original_Amount = Original_Amount
        self.Interest_Rate = Interest_Rate
        self.Remaining_Balance = Remaining_Balance
        self.Start_Date = Start_Date
        self.End_Date = End_Date
        self.Status = Status
        self.next = None

    def __repr__(self):
        return (f"Loan({self.Loan_ID}, {self.Loan_Type}, "
                f"Balance: ${self.Remaining_Balance}, "
                f"Status: {self.Status})")
