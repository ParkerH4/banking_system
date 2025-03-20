from transactionNode import TransactionNode

class TransactionLinkedList:
    def __init__(self):
        self.head = None

    # Adds a transaction to the beginnig of the linked list
    def add_transaction(self, Transaction_ID, Account_ID, Transaction_Type, Amount, Date_Time):
        new_transaction = TransactionNode(Transaction_ID, Account_ID, Transaction_Type, Amount, Date_Time)
        new_transaction.next = self.head
        self.head = new_transaction
        return f"Transaction {Transaction_ID} recorded successfully."

    # Removes a transaction from the linked list
    def remove_transaction(self, Transaction_ID):
        current = self.head
        prev = None

        while current and current.Transaction_ID != Transaction_ID:
            prev = current
            current = current.next

        if not current:
            return f"Transaction {Transaction_ID} not found."

        if prev:
            prev.next = current.next
        else:
            self.head = current.next

        return f"Transaction {Transaction_ID} removed."

    # Finds a specific transaction
    def find_transaction(self, Transaction_ID):
        current = self.head
        while current:
            if current.Transaction_ID == Transaction_ID:
                return current
            current = current.next
        return f"Transaction {Transaction_ID} not found."

    # Displays all transactions in the linked lsit
    def display_transactions(self):
        current = self.head
        if not current:
            return "No transactions available."
        
        transactions = []
        while current:
            transactions.append(f" Time: {current.Date_Time} | Account:  {current.Transaction_Type} | Action: {current.Account_ID} | Amount: ${current.Amount:.2f}")
            current = current.next

        return "\n".join(transactions)