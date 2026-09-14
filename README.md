# PhD Student Academic Website

A personal/academic portfolio website for a PhD student, built with **Flask**,
**Jinja2**, and **vanilla CSS/JavaScript** (no frontend frameworks). The
content currently loaded is based on the publicly listed SLU research profile
for **Gitta Shrestha Thapa** (PhD Candidate, Division of Rural Development,
Swedish University of Agricultural Sciences).

## 1. Project Overview

The site has seven pages — Home, About, Research, Publications, Projects,
Education, and Contact — all sharing one navigation bar and footer through
Jinja template inheritance (`base.html`). Publications, projects, and
education entries are stored in a small SQLite database and rendered
dynamically; a few fields (exact years, methodology details, etc.) are left
as `[ADD ...]` placeholders because that information wasn't provided — replace
these once you have the real details.

## 2. Features

- Server-rendered Flask + Jinja2 pages (no React/Vue/Node)
- SQLite database via Flask-SQLAlchemy, auto-created and auto-seeded on first run
- Contact form with Flask-WTF validation and CSRF protection, storing messages in the database
- Publication filtering by type (vanilla JS)
- Mobile-friendly navigation menu (vanilla JS)
- Fully responsive layout (desktop, tablet, mobile)
- Accessible: semantic HTML, alt text, labeled form fields, visible focus states

## 3. Folder Structure

```
phd_student_website/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configuration (secret key, database URL)
│   ├── database.py        # DB init + seed data
│   ├── models.py          # SQLAlchemy models
│   ├── forms.py           # Contact form (Flask-WTF)
│   ├── routes.py          # Page routes + student info dictionary
│   ├── templates/         # Jinja2 templates
│   └── static/
│       ├── css/style.css
│       ├── js/main.js
│       ├── images/        # put profile.jpg here
│       └── files/         # put your CV PDF here
├── instance/               # SQLite database file lives here (auto-created)
├── run.py                  # App entry point
├── requirements.txt
└── README.md
```

## 4. Requirements

- Python 3.9 or newer
- pip

## 5. Installation

### Windows (PowerShell or Command Prompt)

```
cd phd_student_website
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux

```
cd phd_student_website
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 6. Virtual Environment Setup

The commands above already create and activate a virtual environment
(`venv`). Always activate it before running the app:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

## 7. Database Setup

Nothing to do manually. The first time you run the app, Flask-SQLAlchemy
creates `instance/site.db` and seeds it with the publication, project, and
education entries listed in `app/database.py`.

If you ever want to reset the database, stop the app and delete
`instance/site.db`, then restart the app — it will be recreated and reseeded.

## 8. How to Run the Application

```
python run.py
```

Then open **http://127.0.0.1:5000** in your browser.

## 9. How to Add/Change Student Information

Open `app/routes.py` and edit the `STUDENT` dictionary near the top of the
file. This controls the name, title, university, bio text, email, research
description, and social/profile links shown across every page.

## 10. How to Add Publications

Open `app/database.py` and edit the `seed_initial_data()` function — add,
remove, or edit entries in the `publications` list (title, authors, venue,
year, DOI, description, link, type). Delete `instance/site.db` afterward and
restart the app so the new seed data is loaded, or add rows directly through
a Python shell using the `Publication` model in `app/models.py`.

## 11. How to Add the CV

1. Place your CV PDF in `app/static/files/`, e.g. `student_cv.pdf`.
2. In `app/routes.py`, set `"cv_filename": "student_cv.pdf"` in the
   `STUDENT` dictionary.
3. The "Download CV" button will automatically appear in the navigation and
   on the homepage, linked via `url_for()`.

## 12. How to Customize the Design

- Colors, fonts, spacing: edit `app/static/css/style.css` (CSS variables are
  defined at the top of the file under `:root`).
- Layout/content per page: edit the corresponding file in `app/templates/`.
- Interactive behavior (mobile menu, publication filters): edit
  `app/static/js/main.js`.

