"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations),
check if the transaction is successful based on the updated balance, and calculate loan details
like the loan amount, interest, and term.
"""

import logging

# Setting up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

TRANSACTION_LIMIT = (
    1000  # ✅ Use of constants in UPPER_CASE for clarity and maintainability
)


class TransactionProcessor:
    """
    Class responsible for processing transactions and maintaining balance.
    ✅ Follows Object-Oriented Programming (OOP) principles.
    ✅ Encapsulation: Balance is managed within the class.
    """

    def __init__(self):
        self.balance = 0
        logging.info("TransactionProcessor initialized with balance = 0")

    def process_transaction(self, transaction_types, amount):
        """
        Process a list of transaction types ('credit', 'debit') and update balance accordingly.
        ✅ Meaningful function name: Clearly indicates purpose.
        ✅ Follows the Single Responsibility Principle: Only processes transactions.
        ✅ Logs important actions instead of using print().
        """
        logging.info(
            f"Processing transactions: {transaction_types} with amount: {amount}"
        )

        for transaction_type in transaction_types:
            if transaction_type == "credit":
                self.balance += amount
                logging.info(f"Credit transaction: New balance = {self.balance}")
            elif transaction_type == "debit":
                self.balance -= amount
                logging.info(f"Debit transaction: New balance = {self.balance}")
            else:
                logging.warning(f"Invalid transaction type: {transaction_type}")

        return self.balance

    def is_transaction_successful(self):
        """
        Check if the balance after transactions exceeds the transaction limit.
        ✅ Separates concerns by providing a dedicated function for success validation.
        ✅ Uses logging for proper event tracking instead of print().
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
    ✅ Meaningful function name that describes its purpose.
    ✅ Uses parameters to make the function reusable.
    ✅ Follows the Single Responsibility Principle: Only calculates loan details.
    """
    loan_amount = principal + (principal * loan_interest_rate * loan_term)
    logging.info(
        f"Calculated loan amount: {loan_amount} for principal: {principal}, interest rate: {loan_interest_rate}, term: {loan_term}"
    )
    return loan_amount, loan_interest_rate, loan_term


# Run good code example
if __name__ == "__main__":
    # ✅ Uses if __name__ == "__main__": to ensure code runs only when executed directly.

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
    loan_interest_rate = 0.05  # ✅ Uses meaningful variable names
    loan_term = 10  # 10 years
    loan_details = calculate_loan_details(principal, loan_interest_rate, loan_term)
    logging.info(
        f"Loan Details: Principal = {loan_details[0]}, Interest Rate = {loan_details[1]}, Term = {loan_details[2]} years"
    )
