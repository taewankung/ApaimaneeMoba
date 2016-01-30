from wtforms import form
from wtforms import validators
from wtforms import fields

class CreateRoom(form.Form):
    room_name = fields.TextField('Room name', validators=[validators.required("Please Room Name.")])
