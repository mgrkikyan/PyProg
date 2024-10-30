import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import sqlite3

expenses = []

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    expense TEXT,
    amount REAL
)
''')

conn.commit()

def add_expense():
    expense = entry_expense.get()
    amount = entry_amount.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expenses.append((date, expense, amount))
    
    entry_expense.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    cursor.execute("INSERT INTO expenses (date, expense, amount) VALUES (?, ?, ?)", (date, expense, amount))
    conn.commit()

    update_expenses_list()

def update_expenses_list():
    listbox_expenses.delete(0, tk.END)
    for date, expense, amount in expenses:
        listbox_expenses.insert(tk.END, f"{date}: {expense} - {amount} руб.")

def clear_expenses():
    expenses.clear()
    listbox_expenses.delete(0, tk.END)

def show_summary():
    total = sum(float(amount) for _, _, amount in expenses)
    messagebox.showinfo("Сводка расходов", f"Общая сумма расходов: {total} руб.")

root = tk.Tk()
root.title("Финансовый трекер расходов")

label_expense = ttk.Label(root, text="Расход:")
label_expense.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_expense = ttk.Entry(root)
entry_expense.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

label_amount = ttk.Label(root, text="Сумма:")
label_amount.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_amount = ttk.Entry(root)
entry_amount.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

button_add = ttk.Button(root, text="Добавить", command=add_expense)
button_add.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

button_summary = ttk.Button(root, text="Сводка", command=show_summary)
button_summary.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

button_clear = ttk.Button(root, text="Очистить", command=clear_expenses)
button_clear.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)

listbox_expenses = tk.Listbox(root)
listbox_expenses.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

root.mainloop()

