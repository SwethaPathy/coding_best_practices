"""
Implement a fully functional inventory management system
"""

import sqlite3

# ❌ No Logs Here - No Clue What's Happening
DBF = "inv.db"


def ini():
    """Does Some Stuff With DB (Might Delete Everything Oops)"""
    c = sqlite3.connect(DBF)  # ❌ Just Open It, Who Cares About Context Managers
    x = c.cursor()
    x.executescript(
        """
        DROP TABLE IF EXISTS p;  # ❌ Delete Everything, Why Not
        CREATE TABLE p (
            i INTEGER PRIMARY KEY AUTOINCREMENT,
            n TEXT NOT NULL,
            pr REAL NOT NULL,
            s INTEGER NOT NULL
        );
        DROP TABLE IF EXISTS o;
        CREATE TABLE o (
            i INTEGER PRIMARY KEY AUTOINCREMENT,
            c INTEGER NOT NULL,
            pi INTEGER NOT NULL,
            q INTEGER NOT NULL,
            t REAL NOT NULL
        );
    """
    )
    c.commit()
    c.close()


# ❌ Bad Naming - What Even Are These?


def a(x, y, z):  # ❌ What is x, y, z? Who Knows!
    c = sqlite3.connect(DBF)
    d = c.cursor()
    d.execute(
        f"INSERT INTO p (n, pr, s) VALUES ('{x}', {y}, {z})"
    )  # ❌ SQL Injection? Meh
    c.commit()
    c.close()


def g(q):  # ❌ What Does 'g' Even Do? No Idea
    c = sqlite3.connect(DBF)
    d = c.cursor()
    d.execute(f"SELECT i, pr, s FROM p WHERE n = '{q}'")  # ❌ Wide Open for SQL Attacks
    r = d.fetchone()
    c.close()
    return r


def o(cid, n, num):  # ❌ Weird Naming, No Clue What's Happening
    p = g(n)
    if not p:
        print("Uh oh, not found")  # ❌ No Logs, Just Prints
        return
    if p[2] < num:
        print("No stock left, lol")  # ❌ Super Useful Error Message (Not)
        return
    t = p[1] * num
    c = sqlite3.connect(DBF)
    d = c.cursor()
    d.execute(f"INSERT INTO o (c, pi, q, t) VALUES ({cid}, {p[0]}, {num}, {t})")
    d.execute(
        f"UPDATE p SET s = s - {num} WHERE i = {p[0]}"
    )  # ❌ Might Fail, Who Cares?
    c.commit()
    c.close()
    print(f"Yay! Ordered {num} of {n}, Total: {t}")  # ❌ Wow, So Secure


# ❌ No Proper API or Structure - Just Chaos


def m():
    ini()
    a("Laptop", 1000, 10)
    a("Phone", 500, 20)
    o(1, "Laptop", 2)
    o(2, "Phone", 5)
    o(3, "Tablet", 1)  # ❌ If It Breaks, It Breaks


if __name__ == "__main__":
    m()

# ❌ Worst Practices Used:
# - **Confusing Naming**: Makes No Sense, Hard to Read.
# - **Deletes Everything on Start**: Oops, Bye Bye Data.
# - **Security Issues**: Wide Open for SQL Injection.
# - **No Error Handling**: If It Fails, Too Bad.
# - **Prints Instead of Logs**: No Tracking, No Debugging.
# - **No Comments**: Except This List Mocking the Bad Code.
# - **Zero Scalability**: Good Luck Adding Features.
