import sqlite3
from datetime import datetime
from collections import defaultdict
print(r"""

 ██████████                                                            
░░███░░░░░█                                                            
 ░███  █ ░  █████ █████ ████████   ██████  ████████    █████   ██████  
 ░██████   ░░███ ░░███ ░░███░░███ ███░░███░░███░░███  ███░░   ███░░███ 
 ░███░░█    ░░░█████░   ░███ ░███░███████  ░███ ░███ ░░█████ ░███████  
 ░███ ░   █  ███░░░███  ░███ ░███░███░░░   ░███ ░███  ░░░░███░███░░░   
 ██████████ █████ █████ ░███████ ░░██████  ████ █████ ██████ ░░██████  
░░░░░░░░░░ ░░░░░ ░░░░░  ░███░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░░   ░░░░░░   
                        ░███                                           
                        █████                                          
                       ░░░░░                                           
 ███████████                              █████                        
░█░░░███░░░█                             ░░███                         
░   ░███  ░  ████████   ██████    ██████  ░███ █████  ██████  ████████ 
    ░███    ░░███░░███ ░░░░░███  ███░░███ ░███░░███  ███░░███░░███░░███
    ░███     ░███ ░░░   ███████ ░███ ░░░  ░██████░  ░███████  ░███ ░░░ 
    ░███     ░███      ███░░███ ░███  ███ ░███░░███ ░███░░░   ░███     
    █████    █████    ░░████████░░██████  ████ █████░░██████  █████    
   ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
   
""")


DB_NAME = "expenses.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()


CATEGORIES = ["Food", "Transport", "Rent", "Utilities", "Entertainment", "Health", "Shopping", "Other"]


def add_expense():
    print("\nCategories:", ", ".join(CATEGORIES))
    category = input("Category: ").strip().title()
    if category not in CATEGORIES:
        print("Not in list — saving as 'Other' subcategory note.")
        category = "Other"

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Description (optional): ").strip()
    date_input = input("Date (YYYY-MM-DD, blank = today): ").strip()
    date = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Expense not saved.")
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )
    conn.commit()
    conn.close()
    print(f"Added: {category} - {amount} on {date}")


def view_all():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, date, category, amount, description FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No expenses recorded yet.")
        return

    print(f"\n{'ID':<4}{'Date':<12}{'Category':<15}{'Amount':<10}Description")
    print("-" * 60)
    for r in rows:
        print(f"{r[0]:<4}{r[1]:<12}{r[2]:<15}{r[3]:<10.2f}{r[4] or ''}")


def category_summary():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No data available.")
        return

    total = sum(r[1] for r in rows)
    print("\nSpending by Category")
    print("-" * 35)
    for cat, amt in rows:
        pct = (amt / total) * 100
        bar = "#" * int(pct / 2)
        print(f"{cat:<15}{amt:>10.2f} ({pct:5.1f}%) {bar}")
    print("-" * 35)
    print(f"{'Total':<15}{total:>10.2f}")


def monthly_report():
    month = input("Enter month (YYYY-MM): ").strip()
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid format. Use YYYY-MM.")
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT category, amount, date, description FROM expenses WHERE date LIKE ?",
        (f"{month}%",)
    )
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print(f"No expenses found for {month}.")
        return

    by_cat = defaultdict(float)
    total = 0
    for cat, amt, date, desc in rows:
        by_cat[cat] += amt
        total += amt

    print(f"\nMonthly Report: {month}")
    print("=" * 35)
    for cat, amt in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"{cat:<15}{amt:>10.2f}")
    print("-" * 35)
    print(f"{'Total':<15}{total:>10.2f}")
    print(f"{'Transactions':<15}{len(rows):>10}")
    print(f"{'Daily Avg':<15}{total/len(set(r[2] for r in rows)):>10.2f}")


def delete_expense():
    view_all()
    try:
        exp_id = int(input("\nEnter ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?", (exp_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    print("Deleted." if deleted else "ID not found.")


def main():
    init_db()
    menu = """
=== Expense Tracker ===
1. Add Expense
2. View All Expenses
3. Category Summary
4. Monthly Report
5. Delete Expense
6. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()