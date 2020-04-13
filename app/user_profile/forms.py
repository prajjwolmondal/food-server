from app import db
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Regexp, ValidationError, Email, InputRequired


class AdditionalInfoForm(FlaskForm):

    cuisine_list = [('american','American'), ('chinese', 'Chinese'), ('fast_food', 'Fast Food'), ('french', 'French'), ('indian', 'Indian'), ('italian', 'Italian'), ('japanese', 'Japanese'), ('mexican', 'Mexican'), ('nepali', 'Nepali'), ('seafood', 'Seafood'), ('thai', 'Thai')]

    postal_code = StringField('Postal code', validators=[Regexp("^[A-Z|a-z]\\d[A-Za-z][ -]?\\d[A-Za-z]\\d$")])
    cuisine_preferences = SelectMultipleField('Select your top 5 cuisines:', choices=cuisine_list, validators=[InputRequired()])
    submit = SubmitField('Submit')