from geopy.geocoders import Nominatim


def get_lat_long(street_address):
    geolocator = Nominatim()
    location = geolocator.geocode(street_address)
    return location.latitude, location.longitude


def get_street_address(latitude, longitude):
    geolocator = Nominatim()
    query = "%10.6f, %10.6f" % (latitude, longitude)
    location = geolocator.reverse(query)
    return location.address
