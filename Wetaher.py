# Initialize the dictionary to store weather information
weather_info = {}

def add_city(city, temperature, humidity, wind_speed):
    """
    Adds a new city's weather information to the dictionary.
    """
    if city in weather_info:
        print(f"City '{city}' already exists. Use update_city to update the information.")
    else:
        weather_info[city] = {'temperature': temperature, 'humidity': humidity, 'wind_speed': wind_speed}
        print(f"Weather information for '{city}' has been added.")

def update_city(city, temperature=None, humidity=None, wind_speed=None):
    """
    Updates an existing city's weather information.
    """
    city_info = weather_info.get(city)
    if city_info:
        if temperature is not None:
            city_info['temperature'] = temperature
        if humidity is not None:
            city_info['humidity'] = humidity
        if wind_speed is not None:
            city_info['wind_speed'] = wind_speed
        print(f"Weather information for '{city}' has been updated.")
    else:
        print(f"City '{city}' does not exist. Use add_city to add the city.")

def delete_city(city):
    """
    Deletes a city's weather information from the dictionary.
    """
    if city in weather_info:
        weather_info.pop(city)
        print(f"Weather information for '{city}' has been deleted.")
    else:
        print(f"City '{city}' does not exist.")

def display_cities():
    """
    Displays all cities and their weather information.
    """
    if weather_info:
        print("Weather Information for Cities:")
        for city, info in weather_info.items():
            print(f"City: {city}, Temperature: {info['temperature']}°C, Humidity: {info['humidity']}%, Wind Speed: {info['wind_speed']} km/h")
    else:
        print("No weather information available.")

# Test the functions
add_city("New York", 20, 60, 15)
add_city("Los Angeles", 25, 50, 10)
display_cities()

update_city("New York", humidity=70)
update_city("San Francisco", temperature=18)  # Attempt to update a non-existent city
display_cities()

delete_city("Los Angeles")
delete_city("Chicago")  # Attempt to delete a non-existent city
display_cities()
