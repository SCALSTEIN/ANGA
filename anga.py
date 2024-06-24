import requests
import json

# Function to fetch weather data from API
def fetch_weather_data(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to display weather information
def display_weather(data):
    if data:
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Weather Condition: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No data available.")

# Main function to run weather station
def main():
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
    city = "New York"  # Replace with your city
    
    weather_data = fetch_weather_data(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
