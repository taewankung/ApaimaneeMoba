from wtforms import fields
from wtforms import validators
from wtforms import form


class AccountForm(form.Form):
    email       = fields.TextField('Email', validators=[validators.required(message="Email is required."), validators.Email()])
    password    = fields.PasswordField('Password', validators=[validators.required(message="Passwords is required.")])

class RegisterForm(form.Form):
    name     = fields.TextField('Name', validators=[validators.required(message="Name is required.")])
    surname  = fields.TextField('Surname', validators=[validators.required(message="Surname is required.")])
    email    = fields.TextField('Email', validators=[validators.required(message="Email is required."), validators.Email()])
    password = fields.PasswordField('New Password', [validators.Required(message="New Password is required."), validators.EqualTo('confirm', message='Passwords must match')])
    confirm  = fields.PasswordField('Repeat Password')

