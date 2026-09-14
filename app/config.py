"""
Application configuration.

Edit the values below to change the site's basic settings.
The SECRET_KEY is used by Flask to protect forms (CSRF) - change it
to any random string before deploying this site publicly.
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    # Change this to a long random string before going live.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

    # SQLite database stored in the project's instance folder.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'site.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
