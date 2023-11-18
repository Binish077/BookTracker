import sqlite3
from flask import Flask, render_template

# from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)

@app.route('/')
def hello():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM books').fetchall()
    conn.row_factory = sqlite3.Row
    return render_template('index.html')