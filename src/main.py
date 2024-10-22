from flask import Flask, render_template, redirect, url_for, request
import database_adapter;
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/")
def home():
    tasks = database_adapter.get_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/perform-action', methods=['POST'])
def perform_action():
    id = request.form.get("id")
    time = request.form.get("reduce_minutes")


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
    database_adapter.update_time(id,result_time_str)
    return redirect(url_for('home'))  # Redirect back to the main page