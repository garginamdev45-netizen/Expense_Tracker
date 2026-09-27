import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import date

FONT = ("Times New Roman", 12)

DATA_FILE = "expenses.json"

categories = ["Food", "Transport", "Rent", "Shopping", "Entertainment", "Bills", "Other"]

expenses = []

def load_expenses():
    global expenses
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                expenses = json.load(f)
        except Exception:
            expenses = []
    else:
        expenses = []

def save_expenses():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    amount_text = amount_entry.get()
    note_text = note_entry.get()

    if not amount_text:
        messagebox.showwarning("Input Error", "Please enter an amount")
        return

    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showwarning("Wrong Amount Entered", "Please enter a valid numeric amount")
        return

    if amount <= 0:
        messagebox.showwarning("Input Error", "Amount must be greater than zero")
        return

    new_expense = {
        "date": str(date.today()),
        "category": category_var.get(),
        "amount": amount,
        "note": note_text
    }
    expenses.append(new_expense)
    save_expenses()

    refresh_list()
    update_total()

    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

def delete_expense():
    selected = expense_list.curselection()

    if not selected:
        messagebox.showwarning("Selection Error", "Please select an expense to delete")
        return

    index = selected[0]
    expenses.pop(index)
    save_expenses()

    refresh_list()
    update_total()

def refresh_list():
    expense_list.delete(0, tk.END)
    for expense in expenses:
        line = f"{expense['date']} | {expense['category']} | {expense['amount']:.2f} | {expense['note']}"
        expense_list.insert(tk.END, line)

def update_total():
    total = sum(expense["amount"] for expense in expenses)
    total_label.config(text=f"Total Spent: {total:.2f}")

root = tk.Tk()
root.title("Personal Finance & Expense Tracker")
root.geometry("700x800")

load_expenses()

tk.Label(root, text="Expense Tracker", font=("Times New Roman", 18, "bold")).pack(pady=10)

tk.Label(root, text="Amount:", font=FONT).pack()
amount_entry = tk.Entry(root, font=FONT)
amount_entry.pack(pady=5)

tk.Label(root, text="Category:", font=FONT).pack()
category_var = tk.StringVar(value=categories[0])
ttk.Combobox(root, textvariable=category_var, values=categories, font=FONT).pack(pady=5)

tk.Label(root, text="Note (optional):", font=FONT).pack()
note_entry = tk.Entry(root, font=FONT)
note_entry.pack(pady=5)

tk.Button(root, text="Add Expense", command=add_expense, bg="light blue", fg="black", font=FONT).pack(pady=15)

tk.Label(root, text="Recorded Expenses:", font=FONT).pack()
expense_list = tk.Listbox(root, width=55, height=15, font=FONT)
expense_list.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_expense, bg="salmon", fg="black", font=FONT).pack(pady=5)

total_label = tk.Label(root, text="Total Spent: 0.00", font=("Times New Roman", 14, "bold"))
total_label.pack(pady=10)

refresh_list()
update_total()

root.mainloop()