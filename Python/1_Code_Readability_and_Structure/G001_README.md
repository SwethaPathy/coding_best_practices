# Financial Transactions: Bad vs Good Code

## Problem Statement
In a financial application, we need to:
- Process transactions (credit and debit operations).
- Check if a transaction is successful based on the updated balance.
- Calculate loan details like loan amount, interest, and term.

## Bad Code
```python
# Bad Code: Poor practices in naming, structure, and error handling
def pt(t, a):
    x = 0
    for i in t:
        if i == "credit":
            x += a
        elif i == "debit":
            x -= a
    if x > 1000:
        print("Transaction completed")
    else:
        print("Transaction failed")
    return x

def qd(t):
    p = 100000
    l = 1000
    return p, l, 3000

# Run bad code example
transaction_types = ["credit", "debit", "credit"]
amount = 500

result = pt(transaction_types, amount)
print(f"Final Balance: {result}")

loan_details = qd(transaction_types)
print(f"Loan Details: {loan_details}")
```

### Issues in Bad Code
- ❌ **Unclear function and variable names** (e.g., `pt`, `qd`, `x`, `t`).
- ❌ **No error handling** for invalid transactions.
- ❌ **No logging**—only prints output.
- ❌ **Hardcoded values** instead of constants.
- ❌ **No class structure**, making it harder to manage transactions.

---

## Good Code
```python
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TRANSACTION_LIMIT = 1000  # Constant in UPPER_CASE

class TransactionProcessor:
    def __init__(self):
        self.balance = 0
        logging.info("TransactionProcessor initialized with balance = 0")

    def process_transaction(self, transaction_types, amount):
        """Process transactions and update balance."""
        logging.info(f"Processing transactions: {transaction_types} with amount: {amount}")
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
        """Check if the balance after transactions exceeds the limit."""
        if self.balance > TRANSACTION_LIMIT:
            logging.info(f"Transaction successful: balance {self.balance} exceeds {TRANSACTION_LIMIT}")
            return True
        logging.warning(f"Transaction failed: balance {self.balance} is below the limit {TRANSACTION_LIMIT}")
        return False

def calculate_loan_details(principal, loan_interest_rate, loan_term):
    """Calculate loan details based on given parameters."""
    loan_amount = principal + (principal * loan_interest_rate * loan_term)
    logging.info(f"Calculated loan amount: {loan_amount} for principal: {principal}, interest rate: {loan_interest_rate}, term: {loan_term}")
    return loan_amount, loan_interest_rate, loan_term

if __name__ == "__main__":
    processor = TransactionProcessor()
    transaction_types = ["credit", "credit", "debit"]
    amount = 500
    
    final_balance = processor.process_transaction(transaction_types, amount)
    logging.info(f"Final Balance: {final_balance}")
    transaction_success = processor.is_transaction_successful()
    logging.info(f"Transaction Successful: {transaction_success}")
    
    principal = 100000
    loan_interest_rate = 0.05
    loan_term = 10
    loan_details = calculate_loan_details(principal, loan_interest_rate, loan_term)
    logging.info(f"Loan Details: Principal = {loan_details[0]}, Interest Rate = {loan_details[1]}, Term = {loan_details[2]} years")
```

### Improvements in Good Code
- ✅ **Clear function and variable names** (e.g., `process_transaction`, `calculate_loan_details`).
- ✅ **Error handling** (logs warnings for invalid transactions).
- ✅ **Uses logging** instead of print statements.
- ✅ **Uses a class-based approach** for better structure and encapsulation.
- ✅ **Uses constants** for better maintainability.
- ✅ **Follows the Single Responsibility Principle** (each function does one thing).

---

## Key Differences
| Feature                 | Bad Code 🚨 | Good Code ✅ |
|-------------------------|------------|-------------|
| **Naming Conventions**  | Poor, uses short, unclear names (`pt`, `qd`) | Uses descriptive names (`process_transaction`, `calculate_loan_details`) |
| **Code Structure**      | No classes, procedural style | Uses OOP principles, encapsulated in a class |
| **Error Handling**      | None, no checks for invalid data | Logs warnings for invalid transactions |
| **Logging**             | Uses `print()` statements | Uses Python's `logging` module for structured logging |
| **Constants**           | Hardcoded values | Uses constants (`TRANSACTION_LIMIT`) for better maintainability |
| **Function Design**     | Functions do multiple things | Functions follow **Single Responsibility Principle** |

---

## Conclusion
- **Bad Code** lacks structure, readability, and maintainability.
- **Good Code** follows best practices: **clear naming, structured logging, modular functions, error handling, and OOP principles**.
- Following these best practices improves **scalability, debugging, and future maintenance** of the application. 🚀
