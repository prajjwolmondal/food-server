from app import db
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Regexp, ValidationError, Email, InputRequired


class AdditionalInfoForm(FlaskForm):

    cuisine_list = [('albanian','Albanian'),('argentine','Argentine'),('arab','Arab'),('armenian','Armenian'),
    ('bangladeshi','Bangladeshi'),('bengali','Bengali'),('brazilian','Brazilian'),('buddhist','Buddhist'),
    ('bulgarian','Bulgarian'),('cajun','Cajun'),('cantonese','Cantonese'),('caribbean','Caribbean'),('chinese','Chinese'),
    ('danish','Danish'),('english','English'),('estonian','Estonian'),('fast food','Fast food'),('french','French'),
    ('filipino','Filipino'),('german','German'),('greek','Greek'),('gujarati','Gujarati'),('hakka','Hakka'),('indian','Indian'),
    ('indonesian','Indonesian'),('inuit','Inuit'),('irish','Irish'),('italian','Italian'),('jamaican','Jamaican'),
    ('japanese','Japanese'),('jewish','Jewish'),('korean','Korean'),('kurdish','Kurdish'),('lebanese','Lebanese'),
    ('latvian','Latvian'),('lithuanian','Lithuanian'),('malay','Malay'),('mediterranean','Mediterranean'),
    ('mexican','Mexican'),('native american','Native American'),('nepalese','Nepalese'),('polish','Polish'),
    ('pakistani','Pakistani'),('persian','Persian'),('peruvian','Peruvian'),('portuguese','Portuguese'),('romanian','Romanian'),
    ('russian','Russian'),('seafood','Seafood'),('serbian','Serbian'),('south indian','South Indian'),('spanish','Spanish'),
    ('sri lankan','Sri Lankan'),('taiwanese','Taiwanese'),('thai','Thai'),('turkish','Turkish'),('udupi','Udupi'),
    ('ukrainian','Ukrainian'),('vietnamese','Vietnamese'),('zambian','Zambian'),('zanzibari','Zanzibari')]

    postal_code = StringField('Postal code', validators=[Regexp("^[A-Z|a-z]\\d[A-Za-z][ -]?\\d[A-Za-z]\\d$")])
    cuisine_preferences = SelectMultipleField('Select your top 5 cuisines:', choices=cuisine_list, validators=[InputRequired()], render_kw=({'multiple': 'multiple', 'data-max-options': '5', 'title': "Select your fav 5 cuisines", 'data-selected-text-format':'count > 3', 'data-live-search': 'true'}))
    submit = SubmitField('Submit')