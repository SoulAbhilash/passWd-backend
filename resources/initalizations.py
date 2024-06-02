from dotenv import dotenv_values
import pyrebase
from .helpers import HelperFunctions

config = { **dotenv_values('.env.firebase') }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

helper_functions = HelperFunctions()