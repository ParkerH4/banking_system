from accountNode import AccountNode

# Linked List to manage multiple accounts for a customer 
class AccountLinkedList:
    
    def __init__(self):
        self.head = None

    # Adds account to linked list
    def add_account(self, Account_ID, Account_Type, Balance, Date_Created):
        new_account = AccountNode(Account_ID, Account_Type, Balance, Date_Created)
        if not self.head:
            self.head = new_account
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_account
        return f"Account {Account_ID} created successfully."

    # Removes account from linked list
    def remove_account(self, Account_ID):
        current = self.head
        prev = None

        while current and current.Account_ID != Account_ID:
            prev = current
            current = current.next

        if not current:
            return f"Account {Account_ID} not found."

        if prev:
            prev.next = current.next
        else:
            self.head = current.next

        return f"Account {Account_ID} removed."

    # Finds account in linked list
    def find_account(self, Account_ID):
        current = self.head
        while current:
            if current.Account_ID == Account_ID:
                return current
            current = current.next
        return f"Account {Account_ID} not found."

    # Displays all accounts in linked list
    def display_accounts(self):
        current = self.head
        accounts = []
        while current:
            accounts.append(str(current))
            current = current.next
        return " -> ".join(accounts) if accounts else "No accounts available."
