import datetime

import pytest
from tracker import Expense, ExpenseTracker

def test_expense_creation():
    expense = Expense(70,"Food","2024-05-05","Lunch")
    assert expense.amount == 70
    assert expense.description == "Lunch"
    assert expense.date == "2024-05-05"
    assert expense.category == "Food"

def test_with_error_expense():
    with pytest.raises(ValueError, match="Amount must be positive"):
        Expense(-10,"Food","2024-05-05","Lunch")




def expense_empty_category():
    with pytest.raises(ValueError, match="Category must be specified"):
        expense = Expense(70,"Food","","")






def test_add_expense():
    tracker = ExpenseTracker()
    expense = Expense(25.50, "Food", "2024-05-08", "Lunch")
    tracker.add_expense(expense)
    assert len(tracker.get_all_expenses()) == 1
    assert tracker.get_all_expenses()[0] == expense

def test_add_invalid_type():
    tracker = ExpenseTracker()
    with pytest.raises(TypeError, match="Must be an Expense object"):
        tracker.add_expense("not an expense")

def test_get_total():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense(10, "Food", "2024-05-08", "A"))
    tracker.add_expense(Expense(20, "Food", "2024-05-08", "B"))
    assert tracker.get_total() == 30

def test_get_by_category():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense(10, "Food", "2024-05-08", "A"))
    tracker.add_expense(Expense(20, "Transport", "2024-05-08", "B"))
    food_expenses = tracker.get_by_category("Food")
    assert len(food_expenses) == 1
    assert food_expenses[0].amount == 10