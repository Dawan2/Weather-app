# ☁️ Weather Information App 🌍

## Overview

This Python script provides real-time weather information for a specific location using the OpenWeatherMap API. Get the latest updates on temperature, humidity, wind speed, and more in a visually appealing format. The script continuously updates the information to keep you in the know.

## 🌟 Features

- **Location Information:** 📍 Displays the name of the location for which weather information is retrieved.
- **Weather Description:** 🌤️ Provides a brief description of the current weather conditions.
- **Temperature:** 🌡️ Shows the current temperature, feels-like temperature, minimum temperature, and maximum temperature in Celsius.
- **Humidity:** 💧 Indicates the humidity percentage.
- **Wind Speed:** 💨 Displays the wind speed in meters per second.
- **Current Time:** 🕰️ Shows the current time based on the configured time zone.

## 🚀 How to Use

1. **Obtain API Key:**
   - Visit [OpenWeatherMap API](https://openweathermap.org/api) to get your API key.
   - Replace the placeholder `api_key` in the script with your actual API key.

2. **Configure Location:**
   - Set your desired latitude and longitude in the `latitude` and `longitude` variables.

3. **Configure Time Zone:**
   - Update the `timezone` variable with your preferred time zone. The example is set to 'America/New_York'.

4. **Run the Script:**
   - Execute the script, and watch as it brings you the weather updates with simplicity and clarity!

## 🛠️ Dependencies

- **Requests:** Handles HTTP requests to the OpenWeatherMap API.
- **Pytz:** Provides time zone support for accurate time information.
- **Colorama:** Enhances console output with colored text.
