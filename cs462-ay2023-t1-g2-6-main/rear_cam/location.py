import geocoder
from geopy.geocoders import Nominatim

def get_location():
    try:
        # Use the 'ipinfo' provider to get geolocation based on IP address
        location = geocoder.ipinfo('me')

        # Check if the location was successfully retrieved
        if location.ok:
            return location.latlng
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_address():
    # Get the geolocation
    coordinates = get_location()

    if coordinates:
        latitude, longitude = coordinates
        # print(f'Latitude: {latitude}, Longitude: {longitude}')
        # importing modules
        
        # calling the nominatim tool
        geoLoc = Nominatim(user_agent="GetLoc")
        
        # passing the coordinates
        locname = geoLoc.reverse((latitude, longitude))
        
        # printing the address/location name
        # print(locname.address)
        return locname.address, latitude, longitude
    else:
        print('Geolocation data not available.')
