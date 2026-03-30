💰 Expense Tracker (Python + SQLite)

A simple and efficient **Command Line Expense Tracker** built using **Python** and **SQLite database**.
This project helps users manage their daily expenses, track spending, and analyze expenses by category.

🚀 Features

* ➕ Add new expenses
* 📄 View all expenses
* 💰 Calculate total expenses
* 📊 Category-wise expense summary
* 💾 Data stored permanently using SQLite database
* ⚡ Auto-insert sample data (first run only)

🛠️ Technologies Used

 **Python 3**
 **SQLite3 (Database)**
 **Datetime module**

📁 Project Structure
expense-tracker/
│── main.py          # Main Python file
│── expenses.db      # SQLite database (auto-created)
│── README.md        # Project documentation

▶️ How to Run the Project

Step 1: Install Python

Make sure Python is installed:
python --version

Step 2: Run the Program
python main.py`

📌 Menu Options

When you run the program, you will see:
==== Expense Tracker (DB) ====
1. Add Expense
2. View Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

🧪 Sample Data

On the **first run**, the database is automatically filled with sample data like:

₹100  | Food          | Lunch
₹250  | Travel        | Bus ticket
₹500  | Shopping      | Clothes
₹1200 | Bills         | Electricity bill
₹300  | Entertainment | Movie

📊 Example Output
View Expenses

1. ₹100 | Food | Lunch | 2026-03-30 12:30:00
2. ₹250 | Travel | Bus ticket | 2026-03-30 09:00:00
Total Expense

💰 Total Expense: ₹2400

Category-wise Expense
Food: ₹150
Travel: ₹250
Shopping: ₹500
Bills: ₹1200
Entertainment: ₹300

🧠 Concepts Used

* Python Functions
* Loops and Conditionals
* SQLite Database Operations (CRUD)
* SQL Queries:

  * INSERT
  * SELECT
  * SUM
  * GROUP BY

