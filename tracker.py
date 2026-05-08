class Expense:
    def __init__(self, amount, category, date, description):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not category:
            raise ValueError("Category must be specified")
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):

        return f"Expense({self.amount}, {self.category}, {self.date}, {self.description})"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []


    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            raise TypeError("Must be an Expense object")
        self.expenses.append(expense)

    def get_all_expenses(self):
        return self.expenses

    def get_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def get_by_category(self, category):
        result = []
        for expense in self.expenses:
            if expense.category == category:
                result.append(expense)
        return result