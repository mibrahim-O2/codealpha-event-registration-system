# database.py
# Creates the SQLite database and tables.
# Run once before starting the app: python database.py
# Developer: Muhammad Ibrahim
# LinkedIn: https://www.linkedin.com/in/muhammad-ibrahim-o2
# Year: 2026

import sqlite3

conn = sqlite3.connect('events.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        title       TEXT    NOT NULL,
        description TEXT    NOT NULL,
        date        TEXT    NOT NULL,
        venue       TEXT    NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS registrations (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id     INTEGER NOT NULL,
        student_name TEXT    NOT NULL,
        email        TEXT    NOT NULL,
        FOREIGN KEY (event_id) REFERENCES events(id)
    )
''')

cursor.execute('SELECT COUNT(*) FROM events')
count = cursor.fetchone()[0]

if count == 0:
    sample_events = [
        (
            'AI & Machine Learning Workshop',
            'A hands-on workshop covering the fundamentals of AI, machine learning, '
            'and neural networks. Suitable for CS students and tech enthusiasts.',
            '2026-08-10',
            'FAST NUCES, Karachi'
        ),
        (
            'Web Development Bootcamp',
            'A full-day bootcamp covering HTML, CSS, JavaScript, and Flask. '
            'Build your first web application from scratch.',
            '2026-08-20',
            'NED University, Karachi'
        ),
        (
            'Cybersecurity Awareness Seminar',
            'Learn about ethical hacking, penetration testing, and how to protect '
            'systems from modern cyber threats.',
            '2026-09-05',
            'IBA Main Campus, Karachi'
        ),
        (
            'Open Source Contribution Day',
            'Collaborate with fellow developers to contribute to open-source projects '
            'on GitHub. Beginners are welcome.',
            '2026-09-15',
            'DHA Suffa University, Karachi'
        ),
    ]
    cursor.executemany(
        'INSERT INTO events (title, description, date, venue) VALUES (?, ?, ?, ?)',
        sample_events
    )
    print("Sample events inserted.")

conn.commit()
conn.close()

print("Database created successfully: events.db")
print("Tables created: events, registrations")