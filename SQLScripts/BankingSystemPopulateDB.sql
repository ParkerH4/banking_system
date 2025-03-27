-- Step 1: Create Database
CREATE DATABASE BankingSystem;
USE BankingSystem;

-- Step 2: Create Tables

-- Customer Table
CREATE TABLE Customer (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    FName VARCHAR(50) NOT NULL,
    LName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Address VARCHAR(255),
    Date_Of_Birth DATE
);

-- Account Table
CREATE TABLE Account (
    Account_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Account_Type ENUM('Chequing', 'Savings', 'TFSA', 'RRSP') NOT NULL,
    Balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    Date_Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE
);

-- Loan Table
CREATE TABLE Loan (
    Loan_ID INT AUTO_INCREMENT PRIMARY KEY,
    Loan_Type ENUM('Personal', 'Mortgage', 'Auto', 'Student') NOT NULL,
    Customer_ID INT NOT NULL,
    Loan_Amount DECIMAL(15,2) NOT NULL,
    Interest_Rate DECIMAL(5,2) NOT NULL,
    Remaining_Balance DECIMAL(15,2) NOT NULL,
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL,
    Status ENUM('Active', 'Paid', 'Default') NOT NULL,
    Loan_Term INT NOT NULL, -- Term in months
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE
);

-- Transaction Table
CREATE TABLE Transaction (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    Account_ID INT NOT NULL,
    Loan_ID INT NULL, -- Can be NULL if not related to a loan
    Transaction_Type ENUM('Deposit', 'Withdrawal', 'Transfer', 'Loan Payment') NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
    Transaction_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- contains transaction_time so removed it
    FOREIGN KEY (Account_ID) REFERENCES Account(Account_ID) ON DELETE CASCADE,
    FOREIGN KEY (Loan_ID) REFERENCES Loan(Loan_ID) ON DELETE SET NULL
);

-- Step 3: Insert Sample Data

-- Insert Customers
INSERT INTO Customer (FName, LName, Email, Phone, Address, Date_Of_Birth) VALUES
('Parker', 'Hewitt', 'parkerhewitt@example.com', '4035551234', '123 University Dr, Calgary, AB', '2000-06-15'),
('Ryan', 'Thibault', 'ryanthibault@example.com', '5875555678', '456 Maple St, Edmonton, AB', '1999-03-22'),
('Amy', 'Sidhu', 'amysidhu@example.com', '7805557890', '789 Birch Rd, Vancouver, BC', '2001-09-10');

-- Insert Accounts
INSERT INTO Account (Customer_ID, Account_Type, Balance, Date_Created) VALUES
(1, 'Chequing', 3200.00, '2023-05-10'),  -- Parker's chequing account
(1, 'Savings', 12000.00, '2022-11-20'),  -- Parker's savings account
(2, 'Chequing', 800.00, '2023-01-15'),   -- Ryan's chequing account
(2, 'TFSA', 18000.00, '2021-09-05'),     -- Ryan's TFSA
(3, 'Chequing', 400.00, '2024-02-01'),   -- Amy's chequing account
(3, 'RRSP', 25000.00, '2019-07-18');     -- Amy's RRSP

-- Insert Loans 
INSERT INTO Loan (Loan_Type, Customer_ID, Loan_Amount, Interest_Rate, Remaining_Balance, Start_Date, End_Date, Status, Loan_Term) VALUES
-- Parker's Loans
('Auto', 1, 20000.00, 4.5, 15000.00, '2022-08-01', '2027-08-01', 'Active', 60),  
('Personal', 1, 5000.00, 6.0, 1000.00, '2023-03-01', '2025-03-01', 'Active', 24),  
('Mortgage', 1, 300000.00, 2.9, 250000.00, '2021-06-15', '2046-06-15', 'Active', 300), 

-- Ryan's Loans
('Student', 2, 35000.00, 3.8, 28000.00, '2021-09-01', '2031-09-01', 'Active', 120),  
('Auto', 2, 25000.00, 5.2, 5000.00, '2022-11-15', '2027-11-15', 'Active', 60),  
('Personal', 2, 8000.00, 7.5, 0.00, '2020-05-01', '2023-05-01', 'Active', 36), 

-- Amy's Loans
('Mortgage', 3, 300000.00, 2.9, 290000.00, '2023-04-15', '2048-04-15', 'Active', 300),  
('Personal', 3, 15000.00, 6.2, 5000.00, '2021-02-01', '2026-02-01', 'Active', 60);


-- Insert Transactions
INSERT INTO Transaction (Account_ID, Loan_ID, Transaction_Type, Amount, Transaction_Date) VALUES
(1, NULL, 'Deposit', 1500.00, '2024-03-01'),  -- Parker deposits to chequing
(1, NULL, 'Withdrawal', 300.00, '2024-03-02'),  -- Parker withdraws from chequing
(2, NULL, 'Transfer', 2000.00, '2024-03-05'),  -- Parker transfers from savings to chequing
(3, NULL, 'Deposit', 1000.00, '2024-03-07'),  -- Ryan deposits to chequing
(4, NULL, 'Withdrawal', 500.00, '2024-03-08'),  -- Ryan withdraws from TFSA
(5, NULL, 'Deposit', 750.00, '2024-03-10'),  -- Amy deposits to chequing
(6, 3, 'Loan Payment', 2500.00, '2024-03-12'),  -- Amy makes a mortgage payment
(1, 1, 'Loan Payment', 400.00, '2024-03-15'),  -- Parker pays part of car loan
(3, 2, 'Loan Payment', 300.00, '2024-03-18');  -- Ryan pays part of student loan

