# SkyCast

SkyCast is a Flask-based weather dashboard that shows current weather for selected Nigerian cities. 
It fetches data from the OpenWeatherMap API, saves it in a local SQLite database, and presents weather history and charts in a simple web interface.

## Features

- Real-time weather for 10 Nigerian cities
- Scheduled updates every 4 hours
- Weather history storage
- Trend charts (temperature, humidity, wind, rain)
- CSV export
- API key is loaded from `.env` file

## Setup

1. Clone the repository:


2. Create and activate a virtual environment:


3. Install dependencies:


4. Create a `.env` file in the project root with this content:


5. Run the application:


6. In another terminal, start the scheduler:

