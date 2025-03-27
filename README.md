
# 💰 Banking System

A command-line based banking system that simulates real-world banking operations such as deposits, withdrawals, transfers, and loan payments. Built using **Python** and **MySQL**, the project integrates concepts from **Data Structures** and **Database Systems**.


## Features

- View accounts and balances
- Deposit, withdraw, and transfer funds
- View transaction history (linked list)
- View and pay off loans (prioritized with min-heap)
- Login with Customer ID
- Close account

## Project Integration

- **Linked List**: Used to store and display transaction history
- **Min Heap**: Used to prioritize loan payments by due date


## Technologies Used

- **Python** – Backend logic and Menu
- **MySQL** – Database


## Setup Instructions 
(Install Python)

1. Run the provided sql script in MySQL to create and populate the database.
2. Open the project folder in VS Code.
3. (Optional) Create a virtual environment:
   - `CTRL + SHIFT + P` → “Python: Create Environment” → Select `.venv`
4. Install required package:
   ```bash
   pip install mysql-connector-python
   ```
5. In `database.py`, update the password to your MySQL root password.
6. Test DB connection:
   ```bash
   python database.py
   ```
7. Run the application:
   ```bash
   python main.py
   ```

---

## File Overview

-  main.py - Main menu and app entry point                
- bankingfunctions.py - Core banking operations
- database.py - DB connection logic
- LoanPriorityQueue.py - Min-heap for loan prioritization 
- transactionLinkedList.py - Linked list for transactions

