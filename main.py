from tracker import Expense, ExpenseTracker
from storage import Storage

tracker = ExpenseTracker()
tracker.add_expense(Expense(25.50, "Food", "2024-05-08", "Lunch"))

storage = Storage()
storage.save(tracker.get_all_expenses(), "expenses.json")

loaded = storage.load("expenses.json")
print(loaded)