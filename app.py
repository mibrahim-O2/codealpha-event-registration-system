# app.py
# Event Registration System
# Developer: Muhammad Ibrahim
# LinkedIn: https://www.linkedin.com/in/muhammad-ibrahim-o2
# Year: 2026

import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'eventhub_secret_2026'

DATABASE = 'events.db'


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM events')
    event_count = cursor.fetchone()[0]
    conn.close()
    return render_template('index.html', event_count=event_count)


@app.route('/events')
def events():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events ORDER BY date ASC')
    all_events = cursor.fetchall()
    conn.close()
    return render_template('events.html', events=all_events)


@app.route('/events/<int:event_id>')
def event_detail(event_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    event = cursor.fetchone()
    conn.close()
    if event is None:
        return render_template('404.html'), 404
    return render_template('event_detail.html', event=event)


@app.route('/events/<int:event_id>/register', methods=['POST'])
def register(event_id):
    student_name = request.form.get('student_name', '').strip()
    email        = request.form.get('email', '').strip()

    if not student_name or not email:
        flash('Please fill in all fields.', 'danger')
        return redirect(url_for('event_detail', event_id=event_id))

    if '@' not in email:
        flash('Please enter a valid email address.', 'danger')
        return redirect(url_for('event_detail', event_id=event_id))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT id FROM registrations WHERE event_id = ? AND email = ?',
        (event_id, email)
    )
    existing = cursor.fetchone()

    if existing:
        flash('This email is already registered for this event.', 'warning')
        conn.close()
        return redirect(url_for('event_detail', event_id=event_id))

    cursor.execute(
        'INSERT INTO registrations (event_id, student_name, email) VALUES (?, ?, ?)',
        (event_id, student_name, email)
    )
    conn.commit()
    conn.close()

    flash(f'Registration successful! Welcome, {student_name}.', 'success')
    return redirect(url_for('event_detail', event_id=event_id))


@app.route('/events/<int:event_id>/registrations')
def view_registrations(event_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    event = cursor.fetchone()

    if event is None:
        conn.close()
        return render_template('404.html'), 404

    cursor.execute(
        'SELECT * FROM registrations WHERE event_id = ? ORDER BY id ASC',
        (event_id,)
    )
    registrations = cursor.fetchall()
    conn.close()

    return render_template('registrations.html', event=event, registrations=registrations)


@app.route('/cancel/<int:registration_id>', methods=['POST'])
def cancel_registration(registration_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT event_id FROM registrations WHERE id = ?',
        (registration_id,)
    )
    registration = cursor.fetchone()

    if registration is None:
        conn.close()
        flash('Registration not found.', 'danger')
        return redirect(url_for('events'))

    event_id = registration['event_id']

    cursor.execute('DELETE FROM registrations WHERE id = ?', (registration_id,))
    conn.commit()
    conn.close()

    flash('Registration has been cancelled successfully.', 'info')
    return redirect(url_for('view_registrations', event_id=event_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)