from tracker import Expense, ExpenseTracker
from storage import Storage

tracker = ExpenseTracker()
storage = Storage()

# Load existing data if available
try:
    loaded = storage.load("expenses.json")
    for expense in loaded:
        tracker.add_expense(expense)
        storage.save(tracker.get_all_expenses(), "expenses.json")
except FileNotFoundError:
    pass  # no existing file, start fresh

while True:
    print("\n1. Add expense")
    print("2. View all")
    print("3. View total")
    print("4. Filter by category")
    print("5. Save and exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")

            expense = Expense(amount, category, date, description)
            tracker.add_expense(expense)
            print("Added!")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")

    elif choice == "2":
        expenses = tracker.get_all_expenses()
        if not expenses:
            print("No expenses yet.")
        else:
            for expense in expenses:
                print(expense)

    elif choice == "3":
        print(f"Total: {tracker.get_total()}")

    elif choice == "4":
        category = input("Category: ")
        filtered = tracker.get_by_category(category)
        if not filtered:
            print(f"No expenses in category: {category}")
        else:
            for expense in filtered:
                print(expense)

    elif choice == "5":
        storage.save(tracker.get_all_expenses(), "expenses.json")
        print("Saved!")
        break

    else:
        print("Invalid choice")