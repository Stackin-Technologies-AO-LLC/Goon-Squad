import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.db')
