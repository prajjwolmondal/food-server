from app.data_sources import data_sources_blueprint
from app.data_sources import utils
from flask import session, render_template
from flask_login import login_required

@data_sources_blueprint.route('/googleplaces')
@login_required
def get_restaurant_from_google():
    user_instance = session['userInstance']
    user_lat_long = utils.convert_postal_code_to_latlong(user_instance['postal_code'])
    print(f"user_lat_long: {user_lat_long}")
    render_template('search/results.html')