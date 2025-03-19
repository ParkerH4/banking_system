from bankingfunctions import show_homepage
from bankingfunctions import view_accounts
from bankingfunctions import deposit_money
from bankingfunctions import withdraw_money
from bankingfunctions import transfer_funds
from bankingfunctions import view_transaction_history
from bankingfunctions import exit_program
from database import connect_to_db

def verify_customer(connection, customer_id):
    cursor = connection.cursor()
    cursor.execute("SELECT FName, LName FROM Customer WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()

    if customer:  # If the customer exists, return their first and last name
        return customer  
    else:
        return None  

def main():
    # Connect to DB
    db_connection = connect_to_db()

    if db_connection is None:
        print("Could not connect to the database")
        return

    print("Welcome to your Personal Banking System!\n")
    
    # Customer Login for security purposes
    while True:
        customer_id = input("Please enter your unique Customer ID to log in: ")
        print() 
        # Verify the customer ID and get the customer's name
        customer_info = verify_customer(db_connection, customer_id)
        
        if customer_info:
            first_name, last_name = customer_info
            print("LOGIN SUCCESSFUL\n")
            print()
            print(f"Welcome, {first_name} {last_name}!\n")
            break  # Go to the main menu when the customer is verified
        else:
            print("Invalid Customer ID. Please try again.\n")

    # Main menu
    while True:
        # Homepage 
        show_homepage()
        print("\nPlease select an option from the menu below:\n")
        # User input
        choice = input("Please Enter an option from the menu (1-7): ")

        if choice == '1':
            view_accounts(db_connection, customer_id)
        elif choice == '2':
            deposit_money(db_connection, customer_id)
        elif choice == '3':
            withdraw_money(db_connection, customer_id)
        elif choice == '4':
            transfer_funds(db_connection, customer_id)
        elif choice == '5':
            view_transaction_history(db_connection, customer_id)
        elif choice == '6':
            loan_payment(db_connection, customer_id)
        elif choice == '7':
            exit_program(db_connection, first_name, last_name)
        else:
            print("Invalid option. Please try again.\n")



if __name__ == "__main__":
    main()
