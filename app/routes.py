"""
Page routes for the PhD student website.

To update the student's personal details (name, university, bio, etc.)
edit the STUDENT dictionary below. Publications, projects, and
education records are stored in the database - see app/database.py
to change that content, or the README for instructions.
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import ContactForm
from app.models import Publication, Project, Education, ContactMessage
from app.database import db

main = Blueprint("main", __name__)

# ---------------------------------------------------------------------
# Student information
# Only real information provided by the student is used here.
# Anything not supplied is left as a clearly marked placeholder.
# ---------------------------------------------------------------------
STUDENT = {
    "name": "Gitta Shrestha",
    "title": "PhD Candidate",
    "department": "Department of Rural and Urban Development",
    "university": "Swedish University of Agricultural Sciences (SLU)",
    "location": "Uppsala, Sweden",
    "email": "gitta.shrestha@slu.se",
    "mobile_phone": "+46 730 51 90 02",
    "phone": "+46 18 67 34 23",
    "research_profile_url": "https://research.slu.se/en/persons/gitta-shrestha-thapa/",
    "researchgate_url": "https://www.researchgate.net/profile/Gitta-Shrestha?ev=prf_overview",
    "linkedin": "",
    "google_scholar": "",
    "orcid": "",
    "github": "",
    "cv_filename": "Gitta_Shrestha_CV.pdf",

    "bio_short": (
        "I am a PhD candidate in rural development at SLU."
    ),
    "bio_long": (
        "My previous experience includes consulting on projects implemented "
        "by various international organizations (USAID, UNICEF-ROSA, IWMI) "
        "and universities (Zurich, Wageningen), and working as a researcher "
        "for a CGIAR centre. I earned a Bachelor's degree with Honours in "
        "Geography from Calcutta University, a Master's degree in Geography "
        "from Tribhuvan University, and an MPhil in Human Geography from the "
        "University of Bergen."
    ),

    # "Current Research" - the overarching research theme/heading,
    # kept separate from the specific funded project below.
    "current_research_title": "Modern irrigation practices, youth subjectivities and new ruralities",
    "research_description": (
        "In my PhD research, I am trying to understand rural transformations "
        "and rural futures in the context of the shift from traditional "
        "irrigation systems to modernised irrigation systems. I aim to "
        "understand how rural youth and young farmers from intersecting "
        "socio-economic backgrounds respond to the ongoing changes "
        "associated with transformations of irrigation systems, in "
        "combination with broader socio-economic, political, and ecological "
        "transformations in the region, driven by forces operating at "
        "multiple scales."
    ),

    # "Project" - kept as its own separate heading from Current Research.
    "research_title": (
        "The Future of Agrarian Mountain Livelihoods (FAML): Youth "
        "Aspirations and Irrigation Modernisation in Nepal"
    ),
    "research_funder": "FORMAS",
    "research_interests": [
        "Rural Development",
        "Agrarian Transformation",
        "Irrigation & Water Governance",
        "Gender & Intersectionality",
        "Political Ecology",
        "Rural Youth Livelihoods",
    ],
}


@main.route("/")
def index():
    return render_template("index.html", student=STUDENT)


@main.route("/about")
def about():
    return render_template("about.html", student=STUDENT)


@main.route("/research")
def research():
    return render_template("research.html", student=STUDENT)


@main.route("/publications")
def publications():
    all_publications = Publication.query.order_by(
        Publication.year.desc().nullslast()
    ).all()
    return render_template(
        "publications.html", student=STUDENT, publications=all_publications
    )


@main.route("/projects")
def projects():
    all_projects = Project.query.all()
    return render_template(
        "projects.html", student=STUDENT, projects=all_projects
    )


@main.route("/education")
def education():
    all_education = Education.query.order_by(Education.order).all()
    return render_template(
        "education.html", student=STUDENT, education=all_education
    )


@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data,
        )
        db.session.add(new_message)
        db.session.commit()
        flash("Thank you - your message has been sent successfully!", "success")
        return redirect(url_for("main.contact"))

    return render_template("contact.html", student=STUDENT, form=form)
