# EventHub — Event Registration System

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-purple)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A beginner friendly **Event Registration System** built with Python, Flask, SQLite, Bootstrap 5, and Jinja2.

---

## Screenshots

### Dashboard

![Dashboard Part 1](https://github.com/mibrahim-O2/codealpha-event-registration-system/blob/main/Screenshots/dashboard1.png)
![Dashboard Part 2](https://github.com/mibrahim-O2/codealpha-event-registration-system/blob/main/Screenshots/dashboard2.png)

### All Events

![All Events](https://github.com/mibrahim-O2/codealpha-event-registration-system/blob/main/Screenshots/Events.png)

### Event Registration Form

![Registration](https://github.com/mibrahim-O2/codealpha-event-registration-system/blob/main/Screenshots/resgistration.png)

### Registered Participants

![Participants List](https://github.com/mibrahim-O2/codealpha-event-registration-system/blob/main/Screenshots/list.png)

---

## Features

- Browse all upcoming events on a responsive dashboard
- View full event details before registering
- Register for any event using name and email
- Duplicate registration prevention per event
- View the complete participant list for any event
- Cancel any registration with a confirmation prompt
- Flash notifications for all user actions
- Custom 404 page for invalid routes
- Fully responsive — works on desktop and mobile

---

## Tech Stack

| Layer      | Technology           |
|------------|----------------------|
| Language   | Python 3             |
| Framework  | Flask                |
| Database   | SQLite               |
| Frontend   | HTML5, Bootstrap 5   |
| Templating | Jinja2               |
| Icons      | Bootstrap Icons      |
| Font       | Google Fonts (Inter) |

---

## Folder Structure

```
codealpha-event-registration-system/
|
|-- app.py                   # Flask routes and application logic
|-- database.py              # Database initialization script
|-- requirements.txt         # Python dependencies
|-- README.md                # Project documentation
|
|-- templates/
|   |-- base.html            # Master layout
|   |-- index.html           # Homepage
|   |-- events.html          # All events listing
|   |-- event_detail.html    # Event detail and registration form
|   |-- registrations.html   # Registered participants list
|   |-- 404.html             # Custom error page
|
|-- static/
|   |-- style.css            # Custom CSS
|
|-- Screenshots/
    |-- dashboard1.png
    |-- dashboard2.png
    |-- Events.png
    |-- resgistration.png
    |-- list.png
```

---

## Database Design

### Table: `events`

| Column      | Type    | Description                      |
|-------------|---------|----------------------------------|
| id          | INTEGER | Primary key, auto-incremented    |
| title       | TEXT    | Name of the event                |
| description | TEXT    | Full description                 |
| date        | TEXT    | Event date (YYYY-MM-DD)          |
| venue       | TEXT    | Location of the event            |

### Table: `registrations`

| Column       | Type    | Description                         |
|--------------|---------|-------------------------------------|
| id           | INTEGER | Primary key, auto-incremented       |
| event_id     | INTEGER | Foreign key — references events(id) |
| student_name | TEXT    | Full name of the registrant         |
| email        | TEXT    | Email address of the registrant     |

> One event can have many registrations. `event_id` is the foreign key that links both tables — a one-to-many relationship.

---

## Application Routes

| Method | URL                          | Description                        |
|--------|------------------------------|------------------------------------|
| GET    | /                            | Homepage                           |
| GET    | /events                      | All events listing                 |
| GET    | /events/\<id\>               | Event detail page and form         |
| POST   | /events/\<id\>/register      | Submit registration                |
| GET    | /events/\<id\>/registrations | View all participants for an event |
| POST   | /cancel/\<id\>               | Cancel a registration              |

---

## Installation and Setup

**Prerequisites:** Python 3.8 or above, pip

### Step 1  Clone the Repository

```bash
git clone https://github.com/mibrahim-O2/codealpha-event-registration-system.git
cd codealpha-event-registration-system
```

### Step 2  Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3  Initialize the Database

```bash
python database.py
```

Expected output:

```
Sample events inserted.
Database created successfully: events.db
Tables created: events, registrations
```

### Step 4  Run the Application

```bash
python app.py
```

### Step 5  Open in Browser

```
http://127.0.0.1:5000
```

---

## Future Improvements

- User authentication — login and signup
- Admin panel to manage events
- Email confirmation after registration
- Search and filter events by date or venue
- Export participant list as CSV

---

## Developer

**Muhammad Ibrahim**
BS Computer Science | Student

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/muhammad-ibrahim-o2?utm_source=share_via&utm_content=profile&utm_medium=member_ios)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/mibrahim-O2/codealpha-event-registration-system)

---

## License

This project is developed for internship and educational purposes.
&copy; 2026 Muhammad Ibrahim. All rights reserved.
