#! /usr/bin/python3
# vim: set expandtab tabstop=4 shiftwidth=4 :
import collections
import requests
import time
import urllib.parse
import os

# CITY MAPPER API:
# https://citymapper.3scale.net/docs
# https://developer.citymapper.com/api/1/traveltime/?startcoord=51.525246%2C0.084672&endcoord=51.559098%2C0.074503&time=2014-11-06T19%3A00%3A02-0500&time_type=arrival&key=XXXXXXXXXXXXXXXXXXXX"
CITYMAPPER_TRAVEL_TIME_URL = "https://developer.citymapper.com/api/1/traveltime/?"
CITYMAPPER_TRAVEL_TIME_DELAY_SEC = 20
CITYMAPPER_USER_KEY = os.getenv('CITYMAPPER_API_KEY', None)
if CITYMAPPER_USER_KEY is None:
    raise Exception("CITYMAPPER_API_KEY is not provided in the environment")

# GOOGLE API:
GOOGLE_GEOCODE_URL = 'http://maps.google.com/maps/api/geocode/json?'


coord = collections.namedtuple('coord', ['address', 'latitude', 'longitude'])


def convert_val_to_coord(val):
    """Try to convert value to WGS84 '<latitude>,<longitude>' format like '51.525246,0.084672'.

    Supported types are:
     - str
     - coord."""
    if isinstance(val, str):
        return val
    elif isinstance(val, coord):  # Could use ",".join on tuple ...
        return "%s,%s" % (val.latitude, val.longitude)
    else:
        raise TypeError("Invalid value for convert_val_to_coord : %s" % str(type(val)))


def convert_val_to_time(val):
    """Try to convert value to date & time in ISO-8601 format, including time zone information
    like '2014-11-06T19:00:02-0500' or None

    Supported types are:
     - NoneType
     - str."""
    if val is None:
        return None
    elif isinstance(val, str):
        return val
    else:
        raise TypeError("Invalid value for convert_val_to_time : %s" % str(type(val)))


def get_travel_time(start, end, arrival_time=None):
    """Return travel time from the start/end coordinates (for a optional arrival time).

    This is a wrapper around `get_travel_time_internal` taking parameters with more
    conventional types and handling the conversion."""
    startcoord = convert_val_to_coord(start)
    endcoord = convert_val_to_coord(end)
    arrival_time = convert_val_to_time(arrival_time)
    return get_travel_time_internal(startcoord, endcoord, arrival_time)


def get_travel_time_internal(startcoord, endcoord, arrival_time=None):
    """Return travel time from the start/end coordinates (for a optional arrival time).

    This is a wrapper around the CityMapper API.
    All parameters are strings expected to be formatted as per the CityMapper API:
     - coordinates in WGS84 '<latitude>,<longitude>' format like '51.525246,0.084672'
     - time in ISO-8601 format, including time zone information like '2014-11-06T19:00:02-0500'

    Examples:
     get_travel_time_internal('51.525246%2C0.084672', '51.559098,0.074503', '2014-11-06T19:00:02-0500')
     get_travel_time_internal('51.525246%2C0.084672', '51.559098,0.074503')
    """
    params = {
        'key': CITYMAPPER_USER_KEY,
        'startcoord': startcoord,
        'endcoord': endcoord,
    }
    if arrival_time is not None:
        params['time'] = arrival_time
        params['time_type'] = 'arrival'
    url = CITYMAPPER_TRAVEL_TIME_URL + urllib.parse.urlencode(params)
    response = requests.get(url)
    json = response.json()
    if 'travel_time_minutes' not in json:
        raise ValueError('Invalid response: %s' % str(json))
    time.sleep(CITYMAPPER_TRAVEL_TIME_DELAY_SEC)
    return json['travel_time_minutes']


def get_coord_from_addr(address_arg):
    """Get coordinates (as a coord object) from an address.

    This calls the Google Geocode API. As such it is probably a good idea to
    cache results likely to be used more than once."""
    param = urllib.parse.urlencode({'address': address_arg})
    url = GOOGLE_GEOCODE_URL + param
    response = requests.get(url)
    json = response.json()
    res = json['results']
    if len(res) > 1:
        raise ValueError("More than 1 result found for %s: %s" % (address_arg, str(res)))
    elif len(res) < 1:
        raise ValueError("No result found for %s: %s" % (address_arg, str(res)))
    assert len(res) == 1
    result = res[0]
    address = result['formatted_address']
    location = result['geometry']['location']
    lat, lng = location['lat'], location['lng']
    return coord(address, lat, lng)
