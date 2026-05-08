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
