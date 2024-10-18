from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from datetime import datetime, timedelta

_DATABASE = "C:\\Users\\kleme\\Documents\\Database\\DeserveIt.db"
app = Flask(__name__)


@app.route("/")
def home():
    conn = sqlite3.connect(_DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM whish_list')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)
#    return render_template("index.html")


@app.route('/perform-action', methods=['POST'])
def perform_action():
    print("Woho")
    id = request.form.get("id")

    initial_time_str = request.form.get("current_time")
    hours, minutes, seconds = map(int, initial_time_str.split(':'))
    initial_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    time_to_subtract = timedelta(minutes=10)
    new_time = initial_time - time_to_subtract
    total_seconds = int(new_time.total_seconds())
    new_hours, remainder = divmod(total_seconds, 3600)
    new_minutes, new_seconds = divmod(remainder, 60)
    result_time_str = f"{new_hours:02}:{new_minutes:02}:{new_seconds:02}"
    print("New time after subtracting 10 minutes:", result_time_str)
    conn = sqlite3.connect(_DATABASE)
    c = conn.cursor()
    c.execute('UPDATE whish_list SET time = ? WHERE id = ? ', (result_time_str, id));
    conn.commit()
    conn.close()
    # Fetch the current time from the database
    # cursor.execute('SELECT id, event_time FROM events')
    # events = cursor.fetchall()

    # for event in events:
    #     event_id, event_time = event
    #     # Parse the event_time string to a datetime object
    #     event_time_dt = datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S')

    #     # Decrement by 10 minutes
    #     new_event_time = event_time_dt - timedelta(minutes=10)

    #     # Update the database with the new time
    #     cursor.execute('''
    #         UPDATE events SET event_time = ? WHERE id = ?
    #     ''', (new_event_time.strftime('%Y-%m-%d %H:%M:%S'), event_id))

    # conn.commit()
    # conn.close()
    return redirect(url_for('home'))  # Redirect back to the main page