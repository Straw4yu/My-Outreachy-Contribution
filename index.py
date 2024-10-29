# Solution: Add Error Handling for Database Operations
# I can wrap the database operation in a try-except block to catch any exceptions that occur. If an error happens, we’ll return an error message to the client and avoid adding the task to the tasks list. Here’s how to do it:
# Updated Code with Error Handling
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, exc
import threading

app = Flask(_name_)
db_engine = create_engine('sqlite:///tasks.db')
tasks = []
tasks_lock = threading.Lock()

# Initialize database
def init_db():
    with db_engine.connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

@app.route('/tasks', methods=['POST'])
def create_task():
    task_name = request.form.get('name')
    
    if not task_name:
        return jsonify({"error": "Task name is required"}), 400

    try:
        with db_engine.connect() as conn:
            conn.execute("INSERT INTO tasks (name) VALUES (?)", (task_name,))
    except exc.SQLAlchemyError as e:
        # Log the error and return an error response
        print(f"Database error: {e}")
        return jsonify({"error": "Failed to create task due to a database error"}), 500

    # Use the lock to safely add to the tasks list
    with tasks_lock:
        tasks.append(task_name)
    
    return jsonify({"message": "Task created successfully!", "task_name": task_name}), 201

# Initialize database when the app starts
with app.app_context():
    init_db()

if _name_ == '_main_':
    app.run(debug=True)
# Summary of Fix
# 1.	Added a try-except block around the database operation to catch any SQLAlchemy errors.
# 2.	Logged the error with print(f"Database error: {e}") for debugging purposes.
# 3.	Returned a JSON error response with a 500 status code to inform the client of a database failure without exposing internal details.