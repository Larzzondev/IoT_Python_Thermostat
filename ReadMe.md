# IoT Python Thermostat Simulator

Welcome to the **IoT Python Thermostat Simulator**! This project simulates an IoT device that generates random temperature and humidity data, sending it to ThingSpeak for monitoring and visualization. This repository contains a Python script that demonstrates real-time data generation and integration with the ThingSpeak IoT platform.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)


## Overview
This project is a simple yet effective simulation of an IoT thermostat device. It uses Python to generate random temperature (20-30°C) and humidity (30-60%) values every 60 seconds and sends them to a ThingSpeak channel for real-time tracking. The code includes error handling and debugging features, making it a robust example for IoT development.

## Features
- Generates random temperature and humidity data within realistic ranges.
- Sends data to ThingSpeak using the HTTP GET request method.
- Includes robust error handling for network issues and API failures.
- Provides debug output for troubleshooting.
- Configurable with a ThingSpeak Write API Key.

## Architecture
The architecture of this IoT Thermostat Simulator can be visualized as follows:

```mermaid
graph TD
    A[Script] --> B[Data Gen]
    B --> C[Temp]
    B --> D[Humidity]
    A --> E[API]
    E --> F[HTTP]
    F --> G[Server]
    G --> H[Channel]
    H --> I[Field 1]
    H --> J[Field 2]
    G --> K[Response]
    K --> A

    subgraph Local
        A
        B
        E
    end

    subgraph Cloud
        G
        H
        I
        J
        K
    end