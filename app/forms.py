"""
Form definitions using Flask-WTF.

Using Flask-WTF gives us automatic CSRF protection and simple
server-side validation for the contact form.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired(), Length(min=2, max=150)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(max=150)]
    )
    subject = StringField(
        "Subject", validators=[DataRequired(), Length(min=2, max=200)]
    )
    message = TextAreaField(
        "Message", validators=[DataRequired(), Length(min=10, max=3000)]
    )
    submit = SubmitField("Send Message")
