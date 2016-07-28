from geopy.geocoders import Nominatim


def get_lat_long(street_address):
    geolocator = Nominatim()
    location = geolocator.geocode(street_address)
    print(location)
    return location.latitude, location.longitude
