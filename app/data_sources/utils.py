from googlemaps import Client
from googlemaps import places
from flask import current_app as app
from flask import session

import datetime
import os
import re
import requests
import time

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
    """ Given the resultList, filters out the values that we don't care about and fetches some additional info"""

    formatted_results = []
    t = time.perf_counter()
    for place in resultList:
        place_id = place['place_id']
        formatted_address = place['formatted_address']
        name = place['name']
        price_level = place['price_level']
        rating = int(place['rating'])
        total_ratings = place['user_ratings_total']

        # Some of the places don't have open_now set
        open_now = None
        try:
            open_now = place['opening_hours']['open_now']
        except KeyError:
            # Printing just for debugging/logging purposes
            print(f"{name}|{additional_details['url']} doesn't have open_now key")
        
        additional_details = get_place_details(place_id)

        formatted_place = {'name': name, 'address': formatted_address, 'open_now': open_now, 'price': price_level,
                           'rating': rating, 'total_ratings': total_ratings, 'url': additional_details['url']}
        
        # TODO: These blogto calls are taking up too much time, need to make it more efficient and re-enable
        # print(f"time before blogto call: {time.perf_counter() - t}")
        # blogto_review_link = get_blogto_review_link(name)
        # print(f"time after blogto call: {time.perf_counter() - t}")
        # if blogto_review_link != "":
        #     formatted_place['blogto_link'] = blogto_review_link

        try:
            formatted_place['website'] = additional_details['website']
        except KeyError:
            print(f"{name}|{additional_details['url']} doesn't have a website on maps")

        try:
            todays_hours = additional_details['opening_hours']['weekday_text'][datetime.datetime.today().weekday()]
            formatted_place['opening_hours'] = todays_hours.split("day: ")[1]
        except KeyError:
            print(f"{name}|{additional_details['url']} doesn't have their hours on maps")

        formatted_results.append(formatted_place)

    print(f"time after formatting all results: {time.perf_counter() - t}")
    return formatted_results

def get_user_latlong() -> tuple:
    """Returns the latlong of the user if set, if it isn't then returns Eaton centers latlong"""

    if ('userInstance' in session):
        user_instance = session['userInstance']
        return user_instance['lat_long']
    return (43.654487, -79.380407)  # Eaton center lat long is used if user isn't logged in

def get_blogto_review_link(restaurant_name: str) -> str:
    formatted_restaurant_name = restaurant_name.lower()
    formatted_restaurant_name = formatted_restaurant_name.replace(' ', '-')
    formatted_restaurant_name = re.sub(r"\'|\(|\)", "", formatted_restaurant_name)
    formatted_restaurant_name = formatted_restaurant_name.replace('&amp; ', '')
    possible_review_url = f'https://www.blogto.com/restaurants/{formatted_restaurant_name}-toronto/'
    response = requests.get(possible_review_url)
    if response.status_code == 200:
        return possible_review_url
    return ""

def get_place_details(place_id):
        """ Returns a dict of - website, opening hours and maps url of the given place_id  """

        google_client = Client(app.config['GOOGLE_API_KEY'])
        
        result = places.place(google_client, place_id, fields=['url', 'website', 'opening_hours'])
        return result['result']
