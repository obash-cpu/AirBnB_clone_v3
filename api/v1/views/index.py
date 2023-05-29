#!/usr/bin/python3xx
"""Index of Airbnb clonee"""


from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def returstatus():
    """returns status in json"""
    return jsonify(status='OK')

@app_views.route('/stats', strict_slashes=False)
def getobjs():
    """retrieves the number of each objects by type"""
    obs = {'amenities':storage.count('Amenity'), 
            'cities': storage.count('City'),
            'places': storage.count('Place'), 
            'reviews': storage.count('Review'),
            'states': storage.count('State'), 
            'users': storage.count('User')
            }
    return jsonify(obs)

if __name__ == "__main__":
    pass
