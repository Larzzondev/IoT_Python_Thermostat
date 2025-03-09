IoT Python Thermostat Simulator
Welcome to the IoT Python Thermostat Simulator! This project simulates an IoT device that generates random temperature and humidity data, sending it to ThingSpeak for monitoring and visualization. This repository contains a Python script that demonstrates real-time data generation and integration with the ThingSpeak IoT platform.
Table of Contents
Overview (#overview)

Features (#features)

Architecture (#architecture)

Installation (#installation)

Usage (#usage)

Configuration (#configuration)

Contributing (#contributing)

License (#license)

Contact (#contact)

Overview
This project is a simple yet effective simulation of an IoT thermostat device. It uses Python to generate random temperature (20-30°C) and humidity (30-60%) values every 60 seconds and sends them to a ThingSpeak channel for real-time tracking. The code includes error handling and debugging features, making it a robust example for IoT development.
Features
Generates random temperature and humidity data within realistic ranges.

Sends data to ThingSpeak using the HTTP GET request method.

Includes robust error handling for network issues and API failures.

Provides debug output for troubleshooting.

Configurable with a ThingSpeak Write API Key.

Architecture
The architecture of this IoT Thermostat Simulator can be visualized as follows:

graph TD
    A[Python Script (IoT.py)] --> B[Data Generation]
    B --> C[Random Temperature (20-30°C)]
    B --> D[Random Humidity (30-60%)]
    A --> E[ThingSpeak API Integration]
    E --> F[requests.get() HTTP Request]
    F --> G[ThingSpeak Server]
    G --> H[Channel: Simulated IoT Device]
    H --> I[Field 1: Temperature]
    H --> J[Field 2: Humidity]
    G --> K[Response (Entry ID or Error)]
    K --> A[Feedback Loop]

    subgraph Local Environment
        A
        B
        E
    end

    subgraph ThingSpeak Cloud
        G
        H
        I
        J
        K
    end


    Explanation:
Python Script (IoT.py): The main entry point that orchestrates data generation and transmission.

Data Generation: Produces random temperature and humidity values.

ThingSpeak API Integration: Uses the requests library to send data via HTTP GET requests.

ThingSpeak Server: Processes the request and updates the specified channel.

Channel: Simulated IoT Device: Stores the data in Field 1 (Temperature) and Field 2 (Humidity).

Feedback Loop: Returns a response (e.g., entry ID or error) to the script for logging.

This diagram highlights the local-to-cloud interaction, making it clear how data flows from the simulator to the ThingSpeak platform.
Installation
Prerequisites
Python 3.12.1 or later

Git (for cloning the repository)

Internet connection (to send data to ThingSpeak)

Steps
Clone the Repository:

git clone git@github.com:Larzzondev/IoT_Python_Thermostat.git
cd IoT_Python_Thermostat

Set Up a Virtual Environment:
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install Dependencies:
pip install requests


Obtain ThingSpeak Write API Key:
Sign up or log in to ThingSpeak.

Create a new channel (e.g., "Simulated IoT Device") with Field 1 (Temperature) and Field 2 (Humidity).

Copy the Write API Key from the "API Keys" tab.

Usage
Configure the Script:
Open IoT.py and update the api_key variable with your ThingSpeak Write API Key:
python
api_key = "YOUR_THINGSPEAK_WRITE_API_KEY"


Run the Script:
Ensure the virtual environment is activated.

Execute the script
python IoT.py

Alternatively, use VS Code by selecting the .venv interpreter and clicking the "Play" button.

Monitor Output:
The terminal will display generated temperature and humidity values, the URL sent to ThingSpeak, and the response (e.g., "Data sent successfully!").

Check your ThingSpeak channel to see the data plotted over time.

Configuration
API Key: Stored in the api_key variable in IoT.py. For security, consider using environment variables (e.g., with python-dotenv).

Interval: Data is sent every 60 seconds (time.sleep(60)). Adjust this value if needed.

Data Ranges: Temperature (20-30°C) and humidity (30-60%) are hardcoded but can be modified in the generate_temperature and generate_humidity functions.

Contributing
Contributions are welcome! Please follow these steps:
Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes and commit them (git commit -m "Add new feature").

Push to the branch (git push origin feature-branch).

Open a Pull Request with a description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
Author: Larzzon

