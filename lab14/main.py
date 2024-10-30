import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('myfirstdb.db')
cursor = conn.cursor()

# Создание таблицы accounts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number TEXT NOT NULL,
        balance TEXT NOT NULL
    )
''')

# Вставка данных в таблицу accounts
cursor.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", ("1234567890", "1000.00"))
cursor.execute("INSERT INTO accounts (account_number, balance) VALUES (?, ?)", ("0987654321", "500.00"))
conn.commit()

# Создание таблицы clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT NOT NULL
    )
''')

# Вставка данных в таблицу clients
cursor.execute("INSERT INTO clients (name, contact) VALUES (?, ?)", ("Иванов Иван", "ivanov@example.com"))
cursor.execute("INSERT INTO clients (name, contact) VALUES (?, ?)", ("Петров Петр", "petrov@example.com"))
conn.commit()

# Создание таблицы transactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        amount TEXT NOT NULL,
        operation_type TEXT NOT NULL,
        FOREIGN KEY (account_id) REFERENCES accounts(account_id)
    )
''')

# Вставка данных в таблицу transactions
cursor.execute("INSERT INTO transactions (account_id, date, amount, operation_type) VALUES (?, ?, ?, ?)", (1, "2021-01-01", "100.00", "приход"))
cursor.execute("INSERT INTO transactions (account_id, date, amount, operation_type) VALUES (?, ?, ?, ?)", (2, "2021-01-01", "50.00", "приход"))
cursor.execute("INSERT INTO transactions (account_id, date, amount, operation_type) VALUES (?, ?, ?, ?)", (1, "2021-01-02", "200.00", "расход"))
conn.commit()

# Закрытие соединения
conn.close()
