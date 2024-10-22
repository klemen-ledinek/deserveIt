import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

_DATABASE = os.getenv('DATABASE_PATH')

def get_tasks():
    conn = sqlite3.connect(_DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM whish_list')
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_time(id, new_time):
    conn = sqlite3.connect(_DATABASE)
    c = conn.cursor()
    c.execute('UPDATE whish_list SET time = ? WHERE id = ? ', (new_time, id));
    conn.commit()
    conn.close()
