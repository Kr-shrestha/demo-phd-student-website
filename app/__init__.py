"""
Flask application factory.

create_app() builds and configures the Flask app: it loads the config,
sets up the database, and registers the page routes.
"""

import os
from flask import Flask
from app.config import Config, BASE_DIR
from app.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Make sure the instance folder (where the SQLite file lives) exists.
    os.makedirs(os.path.join(BASE_DIR, "instance"), exist_ok=True)

    init_db(app)

    from app.routes import main
    app.register_blueprint(main)

    # Make the current year available in every template (used in the footer).
    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {"current_year": datetime.utcnow().year}

    return app
