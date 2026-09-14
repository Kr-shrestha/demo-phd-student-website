"""
Database helper functions.

This module keeps the SQLAlchemy instance separate from app/__init__.py
so that models.py can import it without causing circular imports.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """Attach the database to the Flask app and create tables if needed."""
    db.init_app(app)

    with app.app_context():
        # Import models here so SQLAlchemy knows about them before
        # create_all() runs.
        from app import models  # noqa: F401

        db.create_all()
        seed_initial_data()


def seed_initial_data():
    """
    Populate the database with the student's real academic content the
    first time the app runs, so the site works immediately without
    requiring manual data entry.
    """
    from app.models import Publication, Project, Education

    if Publication.query.first() is None:
        publications = [
            Publication(
                title="Women who do not migrate: Intersectionality, social "
                      "relations, and participation in Western Nepal",
                authors="Gitta Shrestha Thapa",
                venue="World Development",
                year=None,
                doi="",
                description="[ADD PUBLICATION DETAILS]",
                link="",
                pub_type="Journal Article",
            ),
            Publication(
                title="Technology for whom? Solar Irrigation Pumps, women "
                      "and smallholders in Eastern Tarai, Nepal",
                authors="Gitta Shrestha Thapa",
                venue="Frontiers in Sustainable Food Systems",
                year=None,
                doi="",
                description="[ADD PUBLICATION DETAILS]",
                link="",
                pub_type="Journal Article",
            ),
            Publication(
                title="Unravelling gendered practices in Nepal water "
                      "bureaucracies",
                authors="Gitta Shrestha Thapa",
                venue="Water Policy",
                year=None,
                doi="",
                description="[ADD PUBLICATION DETAILS]",
                link="",
                pub_type="Journal Article",
            ),
            Publication(
                title="Masculinities in Hydropower: A feminist political "
                      "ecology perspective",
                authors="Gitta Shrestha Thapa",
                venue="International Journal of the Commons",
                year=None,
                doi="",
                description="[ADD PUBLICATION DETAILS]",
                link="",
                pub_type="Journal Article",
            ),
        ]
        db.session.add_all(publications)

    if Project.query.first() is None:
        projects = [
            Project(
                title="The Future of Agrarian Mountain Livelihoods (FAML): "
                      "Youth Aspirations and Irrigation Modernisation in Nepal",
                description=(
                    "PhD research project examining rural transformation as "
                    "traditional irrigation systems shift toward modernised "
                    "systems. The project investigates how rural youth and "
                    "young farmers from intersecting socio-economic "
                    "backgrounds respond to these changes, situated within "
                    "broader socio-economic, political, and ecological "
                    "transformations operating at multiple scales."
                ),
                technologies="Qualitative fieldwork, political ecology, "
                             "intersectionality analysis",
                role="Principal PhD Researcher",
                duration="Ongoing",
                research_area="Rural Development / Agrarian Studies",
                link="",
                funder="FORMAS",
                collaborators="Stephanie Leder, Marien González Hidalgo, "
                               "Jonathan Rigg",
            ),
        ]
        db.session.add_all(projects)

    if Education.query.first() is None:
        education = [
            Education(
                degree="MPhil in Human Geography",
                institution="University of Bergen",
                location="Bergen, Norway",
                start_year="[ADD YEAR]",
                end_year="[ADD YEAR]",
                specialization="Human Geography",
                thesis="",
                order=1,
            ),
            Education(
                degree="Master's Degree in Geography",
                institution="Tribhuvan University",
                location="Kathmandu, Nepal",
                start_year="[ADD YEAR]",
                end_year="[ADD YEAR]",
                specialization="Geography",
                thesis="",
                order=2,
            ),
            Education(
                degree="Bachelor's Degree (Honours) in Geography",
                institution="Calcutta University",
                location="Kolkata, India",
                start_year="[ADD YEAR]",
                end_year="[ADD YEAR]",
                specialization="Geography",
                thesis="",
                order=3,
            ),
        ]
        db.session.add_all(education)

    db.session.commit()
