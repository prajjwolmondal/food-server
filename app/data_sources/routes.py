from app.data_sources import data_sources_blueprint
from app.data_sources import utils
from flask import session, render_template, request
from random import randrange

@data_sources_blueprint.route('/googleplaces')
def get_restaurant_from_google():
    user_lat_long = utils.get_user_latlong()
    cuisine = session['searchQuery']
    session.pop('searchQuery', None)
    search_results = utils.find_using_google(cuisine, user_lat_long)
    next_page_token = search_results['nextPageToken']   # TODO: Add pagination to search results
    restaurant_list = search_results['resultList']
    return render_template('search/results.html', restaurant_list=restaurant_list, cuisine=cuisine)

@data_sources_blueprint.route('/supriseme')
def surprise_me():
    user_lat_long = utils.get_user_latlong()
    cuisine_list = [('albanian','Albanian'),('argentine','Argentine'),('arab','Arab'),('armenian','Armenian'),
    ('bangladeshi','Bangladeshi'),('bengali','Bengali'),('brazilian','Brazilian'),('buddhist','Buddhist'),
    ('bulgarian','Bulgarian'),('cajun','Cajun'),('cantonese','Cantonese'),('caribbean','Caribbean'),('chinese','Chinese'),
    ('danish','Danish'),('english','English'),('estonian','Estonian'),('fast food','Fast food'),('french','French'),
    ('filipino','Filipino'),('german','German'),('greek','Greek'),('gujarati','Gujarati'),('hakka', 'Hakka'),('indian','Indian'),
    ('indonesian','Indonesian'),('inuit','Inuit'),('irish','Irish'),('italian','Italian'),('jamaican','Jamaican'),
    ('japanese','Japanese'),('jewish','Jewish'),('korean','Korean'),('kurdish','Kurdish'),('lebanese','Lebanese'),
    ('latvian','Latvian'),('lithuanian','Lithuanian'),('malay','Malay'),('mediterranean','Mediterranean'),
    ('mexican','Mexican'),('native american','Native American'),('nepalese','Nepalese'),('polish','Polish'),
    ('pakistani','Pakistani'),('persian','Persian'),('peruvian','Peruvian'),('portuguese','Portuguese'),('romanian','Romanian'),
    ('russian','Russian'),('seafood','Seafood'),('serbian','Serbian'),('south indian','South Indian'),('spanish','Spanish'),
    ('sri lankan','Sri Lankan'),('taiwanese','Taiwanese'),('thai','Thai'),('turkish','Turkish'),('udupi','Udupi'),
    ('ukrainian','Ukrainian'),('vietnamese','Vietnamese'),('zambian','Zambian'),('zanzibari','Zanzibari')]
    cuisine_choice = cuisine_list[randrange(0, len(cuisine_list))][1]
    if 'userInstance' in session:
        user_instance = session['userInstance']
        cuisine_list = user_instance['cuisine_preferences']
        print(f'cuisine_list: {cuisine_list}')
        cuisine_choice = cuisine_list[randrange(0, len(cuisine_list))]
        print(f'cuisine_choice: {cuisine_choice}')
    
    search_results = utils.find_using_google(cuisine_choice, user_lat_long)
    restaurant_list = search_results['resultList']
    return render_template('search/results.html', restaurant_list=restaurant_list, cuisine=cuisine_choice)
