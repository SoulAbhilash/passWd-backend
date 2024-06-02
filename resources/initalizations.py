from dotenv import dotenv_values, load_dotenv
import pyrebase
import os
from .helpers import HelperFunctions

# config = { **dotenv_values('.env.firebase') }
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

helper_functions = HelperFunctions()

# Load environment variables from .env files
load_dotenv('.env.firebase')
load_dotenv('.env.secret')


# Pyrebase configuration
firebase_config = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()
auth = firebase.auth()

