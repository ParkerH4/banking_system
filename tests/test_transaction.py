import unittest
from transactionLinkedList import TransactionLinkedList

class TestTransactionLinkedList(unittest.TestCase):

    # Set up a transaction list with sample transactions
    def setUp(self):
        self.transaction_list = TransactionLinkedList()
        self.transaction_list.add_transaction(301, 101, "Deposit", 1000, "2024-03-10 14:30")
        self.transaction_list.add_transaction(302, 101, "Withdrawal", 500, "2024-03-12 09:15")

    # Test adding a transaction
    def test_add_transaction(self):
        result = self.transaction_list.add_transaction(303, 102, "Transfer", 200, "2024-03-13 11:00")
        self.assertEqual(result, "Transaction 303 recorded successfully.")

    # Test removing a transaction
    def test_remove_transaction(self):
        result = self.transaction_list.remove_transaction(301)
        self.assertEqual(result, "Transaction 301 removed.")
        self.assertEqual(self.transaction_list.find_transaction(301), "Transaction 301 not found.")

    # Test finding a transaction
    def test_find_transaction(self):
        transaction = self.transaction_list.find_transaction(302)
        self.assertEqual(transaction.Transaction_Type, "Withdrawal")

if __name__ == '__main__':
    unittest.main()
