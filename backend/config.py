import os

class Config:
    DEBUG = False
    TESTING = False
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    DEFAULT_CITY = "Abuja"

