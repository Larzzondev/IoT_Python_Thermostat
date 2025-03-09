import random
import time
import requests
from requests.exceptions import RequestException

# Function to generate random temperature data between 20 and 30 degrees Celsius
def generate_temperature():
    return round(random.uniform(20, 30), 1)

# Function to generate random humidity data between 30 and 60 percent
def generate_humidity():
    return round(random.uniform(30, 60), 1)

# Function to send data to ThingSpeak
def send_data_to_thingspeak(api_key, temperature, humidity):
    try:
        # Construct the API endpoint URL
        url = f"https://api.thingspeak.com/update?api_key={api_key}&field1={temperature}&field2={humidity}"
        # Print the URL for debugging
        print(f"Sending to URL: {url}")
        
        # Send data to ThingSpeak using GET request
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200 and response.text != '0':
            print("Data sent successfully!")
            return True
        else:
            print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")
            return False
            
    except RequestException as e:
        print(f"Network error occurred: {e}")
        return False

# Replace with your ThingSpeak Write API Key
api_key = "TD44BM9L5JXYZOXH"  # Update this with the correct Write API Key from your channel

# Continuously generate and send data every 60 seconds
while True:
    try:
        # Generate random temperature and humidity
        temperature = generate_temperature()
        humidity = generate_humidity()
        
        # Print the generated values
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        
        # Send data to ThingSpeak
        send_data_to_thingspeak(api_key, temperature, humidity)
        
        # Wait for 60 seconds before next update
        time.sleep(60)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(10)  # Wait 10 seconds before retrying on error