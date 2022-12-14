import os
from pathlib import Path
from dotenv import load_dotenv

class Settings:
    PROJECT_TITLE = 'LoveBnB API'
    PROJECT_DESCRIPTION = 'Book unique homes and experiences in the world\'s best cities.'
    PROJECT_VERSION = '0.0.1'

settings = Settings()

#Import secret key from .env file
load_dotenv('../.env')
SECRET_KEY = os.getenv('SECRET_KEY')