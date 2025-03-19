from loanNode import LoanNode

# Linked List to manage multiple loans for a customer 
class LoanLinkedList:

    def __init__(self):
        self.head = None 

    # Adds loan to linked list
    def add_loan(self, Loan_ID, Loan_Type, Original_Amount, Interest_Rate, Remaining_Balance, Start_Date, End_Date, Status):
        new_loan = LoanNode(Loan_ID, Loan_Type, Original_Amount, Interest_Rate, Remaining_Balance, Start_Date, End_Date, Status)
        if not self.head:
            self.head = new_loan
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_loan
        return f"Loan {Loan_ID} added successfully."

    # Removes loan from linked list
    def remove_loan(self, Loan_ID):
        current = self.head
        prev = None

        while current and current.Loan_ID != Loan_ID:
            prev = current
            current = current.next

        if not current:
            return f"Loan {Loan_ID} not found."

        if prev:
            prev.next = current.next
        else:
            self.head = current.next

        return f"Loan {Loan_ID} removed."

    # Finds loan in linked list
    def find_loan(self, Loan_ID):
        current = self.head
        while current:
            if current.Loan_ID == Loan_ID:
                return current
            current = current.next
        return f"Loan {Loan_ID} not found."
    
    # DIsplays all loans in linked list
    def display_loans(self):
        current = self.head
        loans = []
        while current:
            loans.append(str(current))
            current = current.next
        return " -> ".join(loans) if loans else "No loans available."
