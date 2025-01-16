import sqlite3
import os

DB_PATH = 'tasks.db'  # The path where the database will be stored

def create_connection():
    """Create and return a database connection."""
    connection = sqlite3.connect(DB_PATH)
    return connection

def create_table():
    """Create the tasks table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()

    # SQL statement to create the tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            deadline TEXT,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# In your database.py (or utils/database.py) file

def insert_task(label, deadline, note):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (label, deadline, note) VALUES (?, ?, ?)", (label, deadline, note))
    conn.commit()  # Make sure the transaction is committed
    conn.close()


def get_all_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")  # Adjust this query based on your table structure
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_in_db(task_id, label, deadline, note):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET label = ?, deadline = ?, note = ? WHERE id = ?",
        (label, deadline, note, task_id),
    )
    conn.commit()
    conn.close()

# Ensure the tasks table exists when the app starts
create_table()
