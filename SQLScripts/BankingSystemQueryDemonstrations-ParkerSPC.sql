-- Query Demonstration

-- Show all tables and explain how they are related to one another (keys, triggers, etc.)
SHOW TABLES;

-- Show table structures
DESC Customer;
DESC Account;
DESC Loan;
DESC Transaction;

-- Show relationships (foreign keys)
SELECT 
    TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'BankingSystem' AND REFERENCED_TABLE_NAME IS NOT NULL;




-- Basic Retrieval Query (Get all customers)
SELECT * FROM Customer;


-- A retrieval query with ordered results (sorting transactions by amount)
SELECT * FROM Transaction ORDER BY Amount DESC;


-- A nested retrieval query (all customers who have taken a loan)
SELECT * FROM Customer 
WHERE Customer_ID IN (SELECT Customer_ID FROM Loan);

-- A retrieval query using joined tables (transactions with account type and customer name)
SELECT T.Transaction_ID, T.Transaction_Type, T.Amount, A.Account_Type, C.FName, C.LName
FROM Transaction T
JOIN Account A ON T.Account_ID = A.Account_ID
JOIN Customer C ON A.Customer_ID = C.Customer_ID;


-- An update operation with any necessary triggers (Changing Parker's loan to paid)
UPDATE Loan
SET Status = 'Paid'
WHERE Customer_ID = 1 AND Loan_Type = 'Auto';

-- Checking Parker's loans now
SELECT * FROM Loan WHERE Customer_ID = 1;

-- A deletion operation with any necessary triggers (inserting new banking customer, then deleting to show it works, maybe a customer switches banks after a while as example)
INSERT INTO Customer (FName, LName, Email, Phone, Address, Date_Of_Birth) 
VALUES ('Test', 'User', 'testuser@example.com', '555-555-5555', '999 Test Ave, Toronto, ON', '1995-07-01');

SELECT * FROM Customer WHERE Email = 'testuser@example.com';

DELETE FROM Customer WHERE Email = 'testuser@example.com';

SELECT * FROM Customer WHERE Email = 'testuser@example.com';



