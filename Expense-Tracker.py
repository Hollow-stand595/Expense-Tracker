import sqlite3
from datetime import datetime

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    note TEXT,
    date TEXT
)
""")
conn.commit()


def insert_sample_data():
    cursor.execute("SELECT COUNT(*) FROM expenses")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_data = [
            (100, "Food", "Lunch", "2026-03-30 12:30:00"),
            (250, "Travel", "Bus ticket", "2026-03-30 09:00:00"),
            (500, "Shopping", "Clothes", "2026-03-29 18:45:00"),
            (50, "Food", "Snacks", "2026-03-29 16:00:00"),
            (1200, "Bills", "Electricity bill", "2026-03-28 20:00:00"),
            (300, "Entertainment", "Movie", "2026-03-27 21:30:00")
        ]

        cursor.executemany(
            "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
            sample_data
        )
        conn.commit()
        print("✅ Sample data inserted!")


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    cursor.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, date)
    )
    conn.commit()
    print("✅ Expense added!")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses found.")
        return

    for row in rows:
        print(f"{row[0]}. ₹{row[1]} | {row[2]} | {row[3]} | {row[4]}")


def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"💰 Total Expense: ₹{total if total else 0}")


def category_expense():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")


def main():
    insert_sample_data()  

    while True:
        print("\n==== Expense Tracker (DB) ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_expense()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()