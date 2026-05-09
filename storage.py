import json
from tracker import  ExpenseTracker
import json
from tracker import Expense

class Storage:
    def save(self, expenses, filename):
        # Convert each Expense to dict, then save list
        data = [expense.to_dict() for expense in expenses]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        # Convert each dict back to Expense object
        return [Expense(**item) for item in data]