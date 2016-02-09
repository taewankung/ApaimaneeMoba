from wtforms import fields
from wtforms import validators
from wtforms import form


class AccountForm(form.Form):
    username    = fields.TextField('Username', validators=[validators.required(message="Username is required.")])
    password    = fields.PasswordField('Password', validators=[validators.required(message="Passwords is required.")])

class RegisterForm(form.Form):
    username  = fields.TextField('Name', validators=[validators.required(message="Name is required.")])
    firstname = fields.TextField('Firstname', validators=[validators.required(message="Firstname is required.")])
    lastname  = fields.TextField('Lastname', validators=[validators.required(message="Lastname is required.")])
    email    = fields.TextField('Email', validators=[validators.required(message="Email is required."),
            validators.Email()])
    password = fields.PasswordField('New Password',
            validators=[validators.Required(message="New Password is required."),
            validators.EqualTo('confirmpassword', message='Passwords must match')])
    confirmpassword  = fields.PasswordField('Repeat Password')

