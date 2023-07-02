# In this exercise, you will create a Python container for a weather forecast application. The application will retrieve weather information from an API and display it to the user. You will encapsulate the necessary code and dependencies into a single executable file using PyInstaller. This will enable the application to run on a client computer without requiring the installation of additional packages.
#
# Instructions:
#
# Create a new Python file called "weather_app.py".
#
# Define a class called "WeatherApp" with the following methods:
#
# __init__(self): Initializes the WeatherApp object.
# get_weather(self, city): Retrieves the weather information for the given city using an API.
# display_weather(self, weather_data): Displays the weather information to the user.
# Implement the get_weather(self, city) method:
#
# Use the requests library to send a GET request to a weather API (e.g., OpenWeatherMap API).
# Retrieve the weather data for the specified city.
# Return the weather data as a dictionary.
# Implement the display_weather(self, weather_data) method:
#
# Extract relevant information from the weather data dictionary (e.g., temperature, humidity, description).
# Display the weather information to the user in a user-friendly format.
# Create an instance of the WeatherApp class in the main section of the script.
#
# Inside the main section, prompt the user to enter a city name.
#
# Call the get_weather() method with the user's input and store the weather data.
#
# Call the display_weather() method with the obtained weather data to display the weather information to the user.
#
# Test your application by running the script and entering different city names.
#
# Install PyInstaller using pip install pyinstaller.
#
# Use PyInstaller to create a single executable file for your weather application:
#
# css
# Copy code
# pyinstaller --onefile weather_app.py
# Once the packaging process is complete, locate the executable file in the "dist" directory.
#
# Share the executable file with others and verify that the application runs without requiring the installation of additional packages.


import requests

class WeatherApp:
    def __init__(self):
        pass

    def get_weather(self, city):
        pass
        # Your code here

    def display_weather(self, weather_data):
        pass
        # Your code here

if __name__ == "__main__":
    pass
        # Your code here