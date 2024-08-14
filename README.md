# Scalable Tracking Number Generator
This is a Flask application that generates and manages unique tracking numbers. It leverages Redis for ensuring the uniqueness and scalability of the tracking numbers.

## Features

- Generates unique tracking numbers.
- Ensures high concurrency and scalability.
- Provides RESTful endpoints to generate and retrieve tracking numbers.
- Includes fault-tolerant mechanisms.

## Prerequisites
- Python 3
- Redis server

## Installation
Pip install virtualenv
virtualenv venv
Source venv/Scripts/activate
pip install Flask redis

# redise
download and run redise-server.exe

# run Application
python app.py

# Api
http://127.0.0.1:5000/generate
http://127.0.0.1:5000/tracking_number


