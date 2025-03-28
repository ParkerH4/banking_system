import unittest
from LoanPriorityQueue import LoanPriorityQueue

class TestLoanPriorityQueue(unittest.TestCase):

    # Set up a priority queue with sample loans
    def setUp(self):
        self.loan_queue = LoanPriorityQueue()
        self.loan_queue.add_loan(201, "Mortgage", 95000, "2024-05-01")
        self.loan_queue.add_loan(202, "Car Loan", 18000, "2024-04-10")
        self.loan_queue.add_loan(203, "Student Loan", 25000, "2024-03-15")

    # Test adding a loan to the priority queue
    def test_add_loan(self):
        result = self.loan_queue.add_loan(204, "Business Loan", 30000, "2024-06-01")
        self.assertEqual(result, "Loan 204 added to priority queue.")

    # Test processing the loan with the earliest due date
    def test_process_next_loan(self):
        result = self.loan_queue.process_next_loan()
        self.assertIn("Processing Loan 203 (Student Loan)", result)
    
    # Test displaying loans in the correct priority order
    def test_display_loans(self):
        result = self.loan_queue.display_loans()
        self.assertIn("Loan 203 (Student Loan)", result)
        self.assertIn("Loan 201 (Mortgage)", result)

if __name__ == '__main__':
    unittest.main()
