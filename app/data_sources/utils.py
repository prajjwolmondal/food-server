from googlemaps import Client
from googlemaps import places
from flask import current_app as app

import os

def convert_postal_code_to_latlong(postal_code: str) -> dict:
        """ Converts the given postal code to a lat/long and returns it as a dict """
        google_client = Client(app.config['GOOGLE_API_KEY'])
        geo_code_object = google_client.geocode(postal_code)
        return (geo_code_object[0]["geometry"]["location"]["lat"], geo_code_object[0]["geometry"]["location"]["lng"])
