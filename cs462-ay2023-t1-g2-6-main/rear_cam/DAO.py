import requests
from urllib.parse import urlencode

def send_data(bus, videoLink, datetime, location, date, lat, long, postalCode, country, timestamp):
    # Parameters as a dictionary
    params = {
        "bus": bus,
        "videoLink": videoLink,
        "datetime": datetime,
        "location": location,
        "country": country,
        "date": date,
        "lat": lat,
        "long": long,
        "postalCode": postalCode,
        "timestamp": timestamp
    }

    # Define the URL
    url = "https://grz8jgqey0.execute-api.ap-southeast-1.amazonaws.com/prod?" + urlencode(params)
    
    response = requests.request("POST", url)

    print(response.text)

    # Check the response status code
    if response.status_code == 200:
        # print('Request was successful.')
        # print('Response content:', response.text)
        return "Successfully sent to database!"
    else:
        print('Request failed with status code:', response.status_code)
        return "Requests to the database failed"
    
# send_data('bus', 'videoLink', 'datetime', 'location') # testing