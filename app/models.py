# app/models.py
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'instance', 'demo.db')

def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT)')
    try:
        c.execute("INSERT INTO users (username, password) VALUES ('admin','admin123')")
    except Exception:
        pass
    conn.commit()
    conn.close()

def query_user_by_username(username):
    conn = get_conn()
    c = conn.cursor()
    # SQL injection pattern (intentional)
    q = f"SELECT username, password FROM users WHERE username='{username}';"
    c.execute(q)
    row = c.fetchone()
    conn.close()
    return row

def add_log(message):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO logs (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()
