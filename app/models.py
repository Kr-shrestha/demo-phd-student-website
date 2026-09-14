"""
Database models for the PhD student website.

Each class here maps to a table in the database. Flask-SQLAlchemy
creates the tables automatically the first time the app runs
(see app/database.py).
"""

from datetime import datetime
from app.database import db


class Publication(db.Model):
    __tablename__ = "publications"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    authors = db.Column(db.String(300), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    doi = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(300), nullable=True)
    pub_type = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Publication {self.title}>"


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=True)
    technologies = db.Column(db.String(300), nullable=True)
    role = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.String(100), nullable=True)
    research_area = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    funder = db.Column(db.String(200), nullable=True)
    collaborators = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Project {self.title}>"


class Education(db.Model):
    __tablename__ = "education"

    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(200), nullable=False)
    institution = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=True)
    start_year = db.Column(db.String(20), nullable=True)
    end_year = db.Column(db.String(20), nullable=True)
    specialization = db.Column(db.String(200), nullable=True)
    thesis = db.Column(db.String(300), nullable=True)
    order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Education {self.degree}>"


class Experience(db.Model):
    __tablename__ = "experience"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(200), nullable=False)
    organization = db.Column(db.String(200), nullable=False)
    dates = db.Column(db.String(100), nullable=True)
    responsibilities = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Experience {self.position}>"


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ContactMessage from {self.name}>"
