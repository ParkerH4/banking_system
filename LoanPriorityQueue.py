import heapq

class LoanPriorityQueue:

    def __init__(self):
        self.heap = []  # Min-heap for loan repayments

    # Adds loan to the priority queue
    def add_loan(self, loan_id, loan_type, remaining_balance, due_date):
        heapq.heappush(self.heap, (due_date, loan_id, loan_type, remaining_balance))
        return f"Loan {loan_id} added to priority queue."

    # Removes and returns the loan with the earliest due date
    def process_next_loan(self):
        if not self.heap:
            return "No loans to process."
        due_date, loan_id, loan_type, remaining_balance = heapq.heappop(self.heap)
        return f"Processing Loan {loan_id} ({loan_type}), Remaining Balance: ${remaining_balance}, Due Date: {due_date}"

    # Displays all loans in the queue sorted by due date
    def display_loans(self):
        if not self.heap:
            return "No loans in queue."
        sorted_loans = sorted(self.heap)
        return "\n".join([f"Loan {loan[1]} ({loan[2]}), Due Date: {loan[0]}, Balance: ${loan[3]}" for loan in sorted_loans])
