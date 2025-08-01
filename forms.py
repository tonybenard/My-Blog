from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# RegisterForm to register new users
class RegisterForm(FlaskForm):
    name =StringField("Full name", [DataRequired()])
    email = EmailField("Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired(), length(min=8, message='Password must be at least 8 characters long.')])
    submit = SubmitField("Sign Me Up!")

# User Login form
class LoginForm(FlaskForm):
    email = EmailField("Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("LET ME IN!")

# Blog Comment form
class CommentForm(FlaskForm):
    comments = CKEditorField("Comment", [DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")

#Contact Form
class ContactForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = EmailField("Email address", [DataRequired(), Email()])
    phone = StringField("Phone Number", [DataRequired()])
    message = TextAreaField("Message", [DataRequired()])
    submit = SubmitField("Send")