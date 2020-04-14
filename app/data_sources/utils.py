from googlemaps import Client
from googlemaps import places
from flask import current_app as app
from flask import session

import os

def convert_postal_code_to_latlong(postal_code: str) -> dict:
        """ Converts the given postal code to a lat/long and returns it as a dict """
        google_client = Client(app.config['GOOGLE_API_KEY'])
        geo_code_object = google_client.geocode(postal_code)
        return (geo_code_object[0]["geometry"]["location"]["lat"], geo_code_object[0]["geometry"]["location"]["lng"])

def find_using_google(user_query, lat_long_coordinates, minimum_price=0, maximum_price=2, next_page_token=""):
        google_client = Client(app.config['GOOGLE_API_KEY'])
        radius = 500
        result_type_filter = 'restaurant'

        result = places.places(google_client, query=user_query, location=lat_long_coordinates, 
                               radius=radius, min_price=minimum_price, max_price=maximum_price, 
                               type=result_type_filter, page_token=next_page_token)
        formatted_results = format_google_return_list(result['results'])
        if 'next_page_token' in result:
            return {'resultList': formatted_results, 'nextPageToken': result['next_page_token']}
        return {'resultList': formatted_results, 'nextPageToken': None}

def format_google_return_list(resultList: list) -> list:
    """ Given the resultList, filters out the values that we don't care about"""

    formatted_results = []
    for place in resultList:
        formatted_address = place['formatted_address']
        name = place['name']
        open_now = place['opening_hours']['open_now']
        price_level = place['price_level']
        rating = place['rating']
        total_ratings = place['user_ratings_total']
        maps_url = f"https://www.google.com/maps/search/?api=1&query={place['geometry']['location']['lat']},\
                    {place['geometry']['location']['lng']}&query_place_id={place['place_id']}"
        formatted_place = {'name': name, 'address': formatted_address, 'open_now': open_now, 'price': price_level,
                           'rating': rating, 'total_ratings': total_ratings, 'url': maps_url}
        formatted_results.append(formatted_place)

    return formatted_results

def get_user_latlong() -> tuple:
    """Returns the latlong of the user if set, if it isn't then returns Eaton centers latlong"""

    user_lat_long = (43.654487, -79.380407) # Eaton center lat long is used if user isn't logged in
    if ('userInstance' in session):
        user_instance = session['userInstance']
        user_lat_long = user_instance['lat_long']
    return user_lat_long

