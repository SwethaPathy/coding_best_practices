"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations), check if the transaction is successful based on the updated balance, and calculate loan details like the loan amount, interest, and term. We also need to ensure the code is readable, maintainable, and follows industry-standard coding best practices.
"""
TRANSACTION_LIMIT = 1000  # Constant: UPPER_CASE

class TransactionProcessor:
    def __init__(self):
        self.balance = 0

    def process_transaction(self, transaction_types, amount):
        """
        Process a list of transaction types ('credit', 'debit') and update balance accordingly.
        Follows the Single Responsibility Principle: only processes transactions.
        """
        for transaction_type in transaction_types:
            if transaction_type == "credit":
                self.balance += amount
            elif transaction_type == "debit":
                self.balance -= amount

        return self.balance

    def is_transaction_successful(self):
        """
        Check if the balance after transactions exceeds the transaction limit.
        """
        return self.balance > TRANSACTION_LIMIT


def calculate_loan_details(principal, loan_interest_rate, loan_term):
    """
    Calculate loan details based on principal, interest rate, and term.
    This follows the Single Responsibility Principle: only calculates loan details.
    """
    loan_amount = principal + (principal * loan_interest_rate * loan_term)
    return loan_amount, loan_interest_rate, loan_term
