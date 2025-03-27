import mysql.connector
from database import connect_to_db
from transactionLinkedList import TransactionLinkedList
from LoanPriorityQueue import LoanPriorityQueue

db_connection = connect_to_db()

# HOMEPAGE
def show_homepage():
    print("\n--- Home Page ---")
    print("1. View Accounts")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Funds")
    print("5. View Transaction History")
    print("6. View Loans")
    print("7. Loan Payment")
    print("8. Close Account")
    print("9. Exit System\n")

# DISPLAY THE CUSTOMERS ACCOUNTS
def view_accounts(connection, customer_id):
    try:
        cursor = connection.cursor()
        
        # SQL Query
        cursor.execute("SELECT Account_Type, Balance FROM Account WHERE Customer_ID = %s;", (customer_id,))
        
        # Get all results from DB
        accounts = cursor.fetchall()
        
        if accounts:
            print("\n--- Your Accounts ---")
            for account in accounts:
                print(f"Account Type: {account[0]}, Balance: ${account[1]:.2f}")
        else:
            print("No accounts found for this customer.\n")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()

# DEPOSIT MONEY FUNCTION
def deposit_money(connection, customer_id):
    account_type = input("Enter the account to deposit into (Chequing/Savings/TFSA/RRSP): ")
    amount = float(input("Enter the amount to deposit: $"))
    
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Account
        SET Balance = Balance + %s
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (amount, customer_id, account_type))
    
    connection.commit()
    print(f"${amount:.2f} has been deposited into your {account_type} account.\n")
    
    # Add transaction in the Transaction table
    cursor.execute("""
        INSERT INTO Transaction (Account_ID, Transaction_Type, Amount)
        SELECT Account_ID, 'Deposit', %s
        FROM Account
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (amount, customer_id, account_type))
    
    connection.commit()
    print(f"Transaction recorded: Deposit of ${amount:.2f} into your {account_type} account.\n")
    
    cursor.close()

# WITHDRAW MONEY FUNCTION
def withdraw_money(connection, customer_id):
    account_type = input("Enter the account to withdraw from (Chequing/Savings/TFSA/RRSP): ")
    amount = float(input("Enter the amount to withdraw: $"))
    
    cursor = connection.cursor()
    cursor.execute("""
        SELECT Balance FROM Account WHERE Customer_ID = %s AND Account_Type = %s;
    """, (customer_id, account_type))
    
    account = cursor.fetchone()
    if account and account[0] >= amount:
        cursor.execute("""
            UPDATE Account
            SET Balance = Balance - %s
            WHERE Customer_ID = %s AND Account_Type = %s;
        """, (amount, customer_id, account_type))
        connection.commit()
        print(f"${amount:.2f} has been withdrawn from your {account_type} account.\n")
        
        # Add in the Transaction table
        cursor.execute("""
            INSERT INTO Transaction (Account_ID, Transaction_Type, Amount)
            SELECT Account_ID, 'Withdrawal', -%s
            FROM Account
            WHERE Customer_ID = %s AND Account_Type = %s;
        """, (amount, customer_id, account_type))
        
        connection.commit()
        print(f"Transaction recorded: Withdrawal of ${amount:.2f} from your {account_type} account.\n")
    else:
        print("Insufficient funds.\n")
    
    cursor.close()

# TRANSFER FUNDS FUNCTION
def transfer_funds(connection, customer_id):
    
    from_account_type = input("Enter the account type to transfer from (Chequing/Savings/TFSA/RRSP): ")
    to_account_type = input("Enter the account type to transfer to (Chequing/Savings/TFSA/RRSP): ")
    amount = float(input("Enter the amount to transfer: $"))
    
    cursor = connection.cursor()
    
    
    cursor.execute("""
        SELECT Account_ID, Balance FROM Account
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (customer_id, from_account_type))
    from_account = cursor.fetchone()
    
    if not from_account:
        print(f"Error: No {from_account_type} account found.")
        cursor.close()
        return
    
    from_account_id, from_balance = from_account
    
    if from_balance < amount:
        print("Insufficient funds.\n")
        cursor.close()
        return
    
    
    cursor.execute("""
        SELECT Account_ID FROM Account
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (customer_id, to_account_type))
    to_account = cursor.fetchone()
    
    if not to_account:
        print(f"Error: No {to_account_type} account found.")
        cursor.close()
        return
    
    to_account_id = to_account[0]
    
    # Update account balances
    cursor.execute("UPDATE Account SET Balance = Balance - %s WHERE Account_ID = %s", (amount, from_account_id))
    cursor.execute("UPDATE Account SET Balance = Balance + %s WHERE Account_ID = %s", (amount, to_account_id))
    connection.commit()
    
    # Add to transaction table
    cursor.execute("""
        INSERT INTO Transaction (Account_ID, Transaction_Type, Amount)
        VALUES (%s, 'Transfer', %s)
    """, (from_account_id, -amount))  
    
    cursor.execute("""
        INSERT INTO Transaction (Account_ID, Transaction_Type, Amount)
        VALUES (%s, 'Transfer', %s)
    """, (to_account_id, amount))  
    
    connection.commit()
    
    print(f"Transferred ${amount:.2f} from your {from_account_type} account to your {to_account_type} account.\n")
    
    cursor.close()

# VIEW TRANSACTION HISTORY FUNCTION

# Initialize linked list at the start
transaction_history = TransactionLinkedList()

def view_transaction_history(connection, customer_id):
    cursor = connection.cursor()

    global transaction_list
    transaction_list = TransactionLinkedList()  # Reset the linked list

    cursor.execute("""
        SELECT T.Transaction_ID, T.Transaction_Type, A.Account_Type, T.Amount, T.Transaction_Date
        FROM Transaction T
        JOIN Account A ON T.Account_ID = A.Account_ID
        WHERE A.Customer_ID = %s
        ORDER BY T.Transaction_Date DESC;
    """, (customer_id,))
    
    transactions = cursor.fetchall()

    # Linked List
    if transactions:
        print("\n--- Transaction History ---")
        for transaction in transactions:
            transaction_list.add_transaction(
                transaction[0],  # Transaction_ID
                transaction[1],  # Transaction_Type
                transaction[2],  # Account_Type
                transaction[3],  # Amount
                transaction[4]   # Transaction_Date
            )
        print(transaction_list.display_transactions())  # Display linked list
    else:
        print("No transaction history found.\n")

    cursor.close()


# Initialize the priority queue at the start
loan_queue = LoanPriorityQueue()


# VIEW LOANS
def view_loans(connection, customer_id):
    global loan_queue  # setup global queue
    loan_queue = LoanPriorityQueue()  # Reset queue before adding new loans

    cursor = connection.cursor()
    cursor.execute("""
        SELECT Loan_ID, Loan_Type, Remaining_Balance, End_Date
        FROM Loan WHERE Customer_ID = %s AND Status = 'Active'
        ORDER BY End_Date ASC;
    """, (customer_id,))

    loans = cursor.fetchall()
    
    if not loans:
        print("No active loans found.\n")
        return

    # Min Heap 
    print("\n--- Active Loans (Prioritized by Due Date) ---")
    for loan in loans:
        # Insert loans into priority queue (earliest due date gets highest priority)
        loan_queue.add_loan(loan[0], loan[1], loan[2], loan[3])

    print(loan_queue.display_loans())  # Display loans from the heap

    cursor.close()


# LOAN PAYMENTS
def loan_payment(connection, customer_id):
    global loan_queue  # setup global queue
    cursor = connection.cursor()

    # Check if the customer has any active loans
    cursor.execute("""
        SELECT COUNT(*) FROM Loan WHERE Customer_ID = %s AND Status = 'Active';
    """, (customer_id,))
    
    active_loans = cursor.fetchone()[0]
    
    if active_loans == 0:
        print("\nYou have no active loans to pay.")
        cursor.close()
        return  

    # Use heap to find the most urgent loan to pay (soonest due date)
    print("\n--- Priority Loan Payment ---")
    print("The system recommends paying the following loan first:\n")
    print(loan_queue.process_next_loan())  # Pops the highest priority loan

    loan_id = input("Enter Loan ID to make a payment: ")
    amount = float(input("Enter payment amount: "))

    # Subtract payment from the remaining balance
    cursor.execute("""
        UPDATE Loan
        SET Remaining_Balance = Remaining_Balance - %s
        WHERE Loan_ID = %s AND Customer_ID = %s AND Status = 'Active';
    """, (amount, loan_id, customer_id))

    connection.commit()

    # Check if the loan is fully paid
    cursor.execute("SELECT Remaining_Balance FROM Loan WHERE Loan_ID = %s", (loan_id,))
    remaining_balance = cursor.fetchone()[0]

    if remaining_balance <= 0:
        cursor.execute("""
            UPDATE Loan
            SET Status = 'Paid'
            WHERE Loan_ID = %s;
        """, (loan_id,))
        print("\nLoan fully paid off!")

    connection.commit()

    # Add new loan payments to the transaction history
    cursor.execute("""
        INSERT INTO Transaction (Account_ID, Loan_ID, Transaction_Type, Amount, Transaction_Date)
        SELECT A.Account_ID, L.Loan_ID, 'Loan Payment', %s, NOW()
        FROM Account A
        JOIN Loan L ON A.Customer_ID = L.Customer_ID
        WHERE L.Loan_ID = %s AND L.Customer_ID = %s
        LIMIT 1;
    """, (amount, loan_id, customer_id))
    
    connection.commit()
    
    cursor.close()
    
    print("Loan payment processed successfully!\n")

    # REBUILD the loan queue so it doesn't keep outdated loans
    view_loans(connection, customer_id)

    # Close Acccount
def close_account(connection, customer_id):
    account_type = input("Enter the account to close (Chequing/Savings/TFSA/RRSP): ")

    cursor = connection.cursor()

    # Check if account exists
    cursor.execute("""
        SELECT * FROM Account 
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (customer_id, account_type))

    account = cursor.fetchone()

    if not account:
        print("No such account found.\n")
        cursor.close()
        return

    # Delete account
    cursor.execute("""
        DELETE FROM Account 
        WHERE Customer_ID = %s AND Account_Type = %s;
    """, (customer_id, account_type))

    connection.commit()
    cursor.close()

    print(f"{account_type} account closed successfully.\n")


# EXIT PROGRAM
def exit_program(connection, first_name, last_name):
    if connection.is_connected():
        connection.close()  
        print("Database connection closed.")
    print(f"Thank you for banking with us, {first_name} {last_name}. Have a great rest of your day!")
    exit()  