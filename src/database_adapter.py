import sqlite3

_DATABASE = "C:\\Users\\kleme\\Documents\\Database\\DeserveIt.db"

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
