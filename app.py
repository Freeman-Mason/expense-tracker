from flask import Flask, jsonify, request
from tracker import Expense, ExpenseTracker
from storage import Storage

app = Flask(__name__)
tracker = ExpenseTracker()
storage = Storage()

@app.route("/")
def home():
    return "Expense Tracker API is running!"

if __name__ == "__main__":
    app.run(debug=True)