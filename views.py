from flask import render_template, request, redirect, url_for
from app import app
from models import get_db_connection

# Rota para listar eventos
@app.route('/')
def index():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('index.html', events=events)

# Rota para listar eventos
@app.route('/events')
def events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('event_list.html', events=events)

# Rota para criar um novo evento
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

# Rota para listar participantes
@app.route('/participants')
def participants():
    conn = get_db_connection()
    participants = conn.execute('SELECT * FROM participants').fetchall()
    conn.close()
    return render_template('participant_list.html', participants=participants)

# Rota para criar um novo participante
@app.route('/create_participant', methods=('GET', 'POST'))
def create_participant():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        conn.execute('INSERT INTO participants (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('participants'))
    return render_template('create_participant.html')

# Rota para listar localizações
@app.route('/locations')
def locations():
    conn = get_db_connection()
    locations = conn.execute('SELECT * FROM locations').fetchall()
    conn.close()
    return render_template('location_list.html', locations=locations)

# Rota para criar uma nova localização
@app.route('/create_location', methods=('GET', 'POST'))
def create_location():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        conn = get_db_connection()
        conn.execute('INSERT INTO locations (name, address) VALUES (?, ?)', (name, address))
        conn.commit()
        conn.close()
        return redirect(url_for('locations'))
    return render_template('create_location.html')

# Rota para listar papéis
@app.route('/roles')
def roles():
    conn = get_db_connection()
    roles = conn.execute('SELECT * FROM roles').fetchall()
    conn.close()
    return render_template('role_list.html', roles=roles)

# Rota para criar um novo papel
@app.route('/create_role', methods=('GET', 'POST'))
def create_role():
    if request.method == 'POST':
        role_name = request.form['role_name']
        conn = get_db_connection()
        conn.execute('INSERT INTO roles (role_name) VALUES (?)', (role_name,))
        conn.commit()
        conn.close()
        return redirect(url_for('roles'))
    return render_template('create_role.html')
