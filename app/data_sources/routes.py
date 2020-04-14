from app.data_sources import data_sources_blueprint
from app.data_sources import utils
from flask import session, render_template

@data_sources_blueprint.route('/googleplaces')
def get_restaurant_from_google():
    user_lat_long = (43.654487, -79.380407) # Eaton center lat long is used if user isn't logged in
    if ('userInstance' in session):
        user_instance = session['userInstance']
        user_lat_long = utils.convert_postal_code_to_latlong(user_instance['postal_code'])
    search_results = utils.find_using_google("mexican", user_lat_long)
    next_page_token = search_results['nextPageToken']   # TODO: Add pagination to search results
    restaurant_list = search_results['resultList']
    return render_template('search/results.html', restaurant_list=restaurant_list)