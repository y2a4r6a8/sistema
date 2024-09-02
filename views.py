from flask import render_template, request, redirect, url_for
from app import app
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('site.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('event_list.html', events=events)

@app.route('/create_event', methods=('GET', 'POST'))
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        conn = get_db_connection()
        conn.execute('INSERT INTO events (title) VALUES (?)', (title,))
        conn.commit()
        conn.close()
        return redirect(url_for('events'))
    return render_template('create_event.html')

# Adicione rotas semelhantes para participants, locations e roles
