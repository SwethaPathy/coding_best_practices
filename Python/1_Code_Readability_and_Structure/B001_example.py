"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations),
    check if the transaction is successful based on the updated balance, and calculate loan details
    like the loan amount, interest, and term.
"""

# Bad Code Example


def pt(t, a):  # ❌ Poor function name: Not descriptive, should be 'process_transaction'
    x = 0  # ❌ Poor variable name: 'x' is unclear, should be 'balance'

    for i in t:  # ❌ Inefficient loop: No validation for transaction type
        if i == "credit":
            x += a
        elif i == "debit":
            x -= a

    if x > 1000:  # ❌ Hardcoded threshold value: Should use a constant
        print("Transaction completed")  # ❌ Using print instead of logging
    else:
        print("Transaction failed")  # ❌ No detailed failure reason

    return x


def qd(t):  # ❌ Poor function name: 'qd' is unclear, should be 'calculate_loan_details'
    p = 100000  # ❌ Hardcoded principal amount, should be configurable
    l = 1000  # ❌ Poor variable naming: 'l' is unclear, should be 'interest_rate'
    return p, l, 3000  # ❌ Magic numbers: 3000 should have a meaningful name


# Run bad code example
transaction_types = ["credit", "debit", "credit"]
amount = 500

result = pt(transaction_types, amount)
print(f"Final Balance: {result}")  # ❌ Using print instead of logging

loan_details = qd(transaction_types)
print(f"Loan Details: {loan_details}")  # ❌ Function parameter 't' is unused
