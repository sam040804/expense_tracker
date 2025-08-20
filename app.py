from flask import Flask, render_template, request, redirect, url_for
import json, os, datetime

app = Flask(__name__)
DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f)

@app.route('/')
def index():
    expenses = load_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    expenses = load_expenses()
    expense = {
        "title": request.form['title'],
        "amount": float(request.form['amount']),
        "category": request.form['category'],
        "date": request.form['date'] if request.form['date'] else str(datetime.date.today())
    }
    expenses.append(expense)
    save_expenses(expenses)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
