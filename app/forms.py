from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    desc = TextAreaField("Description", validators=[InputRequired()])
    bedrooms = IntegerField("No. of Bedrooms", validators=[InputRequired()])
    bathrooms = IntegerField("No. of Bathrooms", validators=[InputRequired()])
    price = DecimalField("Price", validators=[InputRequired()])
    type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField("Photo", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'jfif', 'png', 'gif'], 'Images only')])
    submit = SubmitField("Add Property")