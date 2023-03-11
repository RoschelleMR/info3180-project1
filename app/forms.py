from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    desc = TextAreaField("Description", validators=[InputRequired()])
    rooms = IntegerField("No. of Rooms", validators=[InputRequired()])
    bathrooms = IntegerField("No. of Bathrooms", validators=[InputRequired()])
    price = IntegerField("Price", validators=[InputRequired()])
    type = SelectField('Property Type', choices=[('house', 'House'), ('apart', 'Apartment')])
    location = StringField('Property Title', validators=[InputRequired()])
    photo = FileField("Photo", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'jfif', 'png', 'gif'], 'Images only')])
    submit = SubmitField("Add Property")