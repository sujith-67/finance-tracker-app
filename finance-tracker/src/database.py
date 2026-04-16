import sqlite3

DB_PATH = "data/finance.db"

def connect():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        amount REAL,
        category TEXT,
        tags TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_transaction(type_, amount, category, tags, date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (type, amount, category, tags, date) VALUES (?, ?, ?, ?, ?)",
        (type_, amount, category, tags, date)
    )

    conn.commit()
    conn.close()
    import sqlite3

DB_PATH = "data/finance.db"

def connect():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        amount REAL,
        category TEXT,
        tags TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_transaction(type_, amount, category, tags, date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (type, amount, category, tags, date) VALUES (?, ?, ?, ?, ?)",
        (type_, amount, category, tags, date)
    )

    conn.commit()
    conn.close()

def delete_transaction(txn_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id = ?", (txn_id,))
    
    conn.commit()
    conn.close()


def create_budget_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        month TEXT
    )
    """)

    conn.commit()
    conn.close()
def set_budget(category, amount, month):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO budgets (category, amount, month)
    VALUES (?, ?, ?)
    """, (category, amount, month))

    conn.commit()
    conn.close()


def get_budgets(month):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, amount FROM budgets WHERE month = ?
    """, (month,))

    data = cursor.fetchall()
    conn.close()

    return dict(data)    