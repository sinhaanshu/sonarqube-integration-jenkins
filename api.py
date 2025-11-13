def get_geocode_api(service, location):
    """Geocoding API call."""

    geocode_result = service.geocode(query=location).execute()
    return geocode_result


def main():
    # Replace these values with your own
    api_key = 'YOUR_API_KEY3'  # Your Google Maps Geocoding API Key
    location = 'London, UK'

    # Create the client instance.
    service = build('geolocation', 'v1', developerKey=api_key)

    geocode_result = get_geocode_api(service, location)

    if geocode_result['results']:
        lat = geocode_result['results'][0]['geometry']['location']['lat']
        lng = geocode_result['results'][0]['geometry']['location']['lng']

        print(f"Latitude: {lat}, Longitude: {lng}")
    else:
        print("Geocoding result not found.")


if __name__ == '__main__':
    main()
