from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class SearchForm(FlaskForm):
    search_query = StringField('What cuisine are you in the mood for today?', validators=[DataRequired(), 
                               Length(3, 20, "Must be longer than 3 characters and under 20")],
                               render_kw=({'placeholder': "Enter a cuisine (e.g. Nepali, Thai, etc)"}))
    submit = SubmitField('Search')

class SurpriseForm(FlaskForm):
    surpise_me_button = SubmitField("Surprise Me")