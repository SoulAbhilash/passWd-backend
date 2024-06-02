from flask_restful import Api
from flask import Flask

from resources.authentication.auth_api import CreateNewUser
from resources.save_credentials.cred_api import Credentials
from resources.keys_management.key_api import Keys

app = Flask(__name__)
api = Api(app)


api.add_resource(CreateNewUser, '/create_new_user')
api.add_resource(Credentials, '/credentials_handlers')
api.add_resource(Keys, '/keys')

if __name__ == '__main__':
    app.run(debug=True)