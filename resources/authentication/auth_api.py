from flask_restful import Resource, reqparse
from flask.wrappers import Response
from flask.helpers import make_response
from flask.json import jsonify

from .auth_db import AuthManager
from ..keys_management.key_db import KeyMangaerDB
from ..user.user_db import UserDB

class CreateNewUser(Resource):

    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=str, required=True, help='uid is required')
        self.parser.add_argument('username', type=str, required=True, help='username is required')
        self.parser.add_argument('email', type=str, required=True, help='email is required')
        self.parser.add_argument('access_token', type=str, required=True, help='access_token is required')

        self.auth_manager = AuthManager()
        self.user_db = UserDB()
        super().__init__()

    def post(self):
        try:
            # Parse arguments without strict mode for individual field validation
            args = self.parser.parse_args()
            print(args)

            # Access parsed arguments (after validation)
            uid = args['uid']
            username = args['username']
            email = args['email']
            
            if self.user_db._if_user_exsist(uid):
                return make_response(jsonify({"body": "User already exsist! Signin sucessful"}), 201)
            
            # Handle response from AuthManager
            success, message = self.auth_manager.create_user(uid=uid, username=username, email=email)
            
            if success:
                response = {'body': 'User Created Successfully'}
                return make_response(jsonify(response), 201)
            
            else:
                print(message)
                return make_response({'message': str(message)}, 500)


        except Exception as e:
            print(e)
            return make_response({'message': str(e)}, 400)
