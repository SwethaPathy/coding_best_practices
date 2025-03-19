"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations), check if the transaction is successful based on the updated balance, and calculate loan details like the loan amount, interest, and term.
"""

import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

TRANSACTION_LIMIT = 1000  # Constant: UPPER_CASE


class TransactionProcessor:

    def __init__(self):
        self.balance = 0
        logging.info("TransactionProcessor initialized with balance = 0")

    def process_transaction(self, transaction_types, amount):
        """
        Process a list of transaction types ('credit', 'debit') and update balance accordingly.
        Follows the Single Responsibility Principle: only processes transactions.
        """
        logging.info(
            f"Processing transactions: {transaction_types} with amount: {amount}"
        )
        for transaction_type in transaction_types:
            if transaction_type == "credit":
                self.balance += amount
                logging.info(
                    f"Credit transaction: New balance = {self.balance}")
            elif transaction_type == "debit":
                self.balance -= amount
                logging.info(
                    f"Debit transaction: New balance = {self.balance}")

        return self.balance

    def is_transaction_successful(self):
        """
        Check if the balance after transactions exceeds the transaction limit.
        """
        if self.balance > TRANSACTION_LIMIT:
            logging.info(
                f"Transaction successful: balance {self.balance} exceeds {TRANSACTION_LIMIT}"
            )
            return True
        else:
            logging.warning(
                f"Transaction failed: balance {self.balance} is below the limit {TRANSACTION_LIMIT}"
            )
            return False


def calculate_loan_details(principal, loan_interest_rate, loan_term):
    """
    Calculate loan details based on principal, interest rate, and term.
    This follows the Single Responsibility Principle: only calculates loan details.
    """
    loan_amount = principal + (principal * loan_interest_rate * loan_term)
    logging.info(
        f"Calculated loan amount: {loan_amount} for principal: {principal}, interest rate: {loan_interest_rate}, term: {loan_term}"
    )
    return loan_amount, loan_interest_rate, loan_term


# Run good code example
if __name__ == "__main__":
    # Create a transaction processor instance
    processor = TransactionProcessor()

    # Sample transactions: 2 credits (500 each) and 1 debit (300)
    transaction_types = ["credit", "credit", "debit"]
    amount = 500

    # Process the transactions
    final_balance = processor.process_transaction(transaction_types, amount)
    logging.info(f"Final Balance: {final_balance}")

    # Check if transaction was successful (balance > 1000)
    transaction_success = processor.is_transaction_successful()
    logging.info(f"Transaction Successful: {transaction_success}")

    # Calculate loan details
    principal = 100000
    loan_interest_rate = 0.05  # 5% interest rate
    loan_term = 10  # 10 years
    loan_details = calculate_loan_details(principal, loan_interest_rate,
                                          loan_term)
    logging.info(
        f"Loan Details: Principal = {loan_details[0]}, Interest Rate = {loan_details[1]}, Term = {loan_details[2]} years"
    )

"""
Why This Is Better:

1. Naming Conventions:
   - Function Names: `process_transaction()` is descriptive and clear, telling you exactly what it does. `calculate_loan_details()` is self-explanatory.
   - Variable Names: `transaction_types` and `amount` are clear, explaining what they represent. `balance` describes what is being updated in `process_transaction()`.
   - Class Name: `TransactionProcessor` follows PascalCase and is more descriptive than just a generic name.
   - Constants: `TRANSACTION_LIMIT` uses UPPER_CASE for constants, which is the best practice.

2. Single Responsibility Principle:
   - The `process_transaction()` method only handles the transaction processing, while `is_transaction_successful()` checks if the balance exceeds the limit. Both functions have clear, single responsibilities.
   - The `calculate_loan_details()` function is focused only on calculating loan details, not mixing it with other concerns.

3. Code Formatting & Linting:
   - Indentation is consistent, making the code easy to read.
   - Proper spacing around operators and inside function definitions.
   - Shorter lines of code, improving readability. No line is overly long (staying within the 80-character limit is recommended).
   - Proper docstrings explain what each function does, improving clarity for other developers.

4. Maintainability and Scalability:
   - By following these practices, the code is now more modular, readable, and maintainable.
   - It’s easier to scale as additional transaction types or other logic can be added in a structured manner.
"""
