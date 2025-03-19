"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations), check if the transaction is successful based on the updated balance, and calculate loan details like the loan amount, interest, and term. 
"""


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

"""
This code is bad and does not follow best practices, making it harder to maintain, read, and scale:

1. Naming Conventions:
   - `pt()` is a vague function name (should be more descriptive like `process_transaction()`).
   - The variables `t` and `a` are unclear. `t` could be `transaction_types` and `a` could be `amount`.
   - `qd()` is not meaningful (should be `calculate_loan_details()` or something that explains its purpose).
   - Variables like `x`, `p`, `l` are not descriptive.

2. Function Responsibility:
   - The `pt()` function is doing too much: processing transactions and printing results. It violates the **Single Responsibility Principle**.

3. Formatting & Linting:
   - The code is hard to read due to unclear spacing, long lines, and lack of proper indentation in places.
   - It also lacks consistency in naming conventions.
"""
