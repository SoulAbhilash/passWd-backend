from flask_restful import Resource, reqparse
from flask import Response, jsonify, make_response

from .auth_db import AuthManager
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

            # Access parsed arguments (after validation)
            uid = args['uid']
            username = args['username']
            email = args['email']
            access_token = args['access_token']
            
            if self.user_db._if_user_exsist(uid):
                return make_response(jsonify({"body": "User already exsist! Signin sucessful"}), 201)
            
            # Handle response from AuthManager
            success, keys_or_error = self.auth_manager.create_user(uid=uid, username=username, email=email, access_token=access_token)
            
            if success:
                response = {'body': 'User Created Successfully', **keys_or_error }
                return make_response(jsonify(response), 201)
            
            else:
                return make_response({'message': str(keys_or_error)}, 500)


        except Exception as e:
            return make_response({'message': str(e)}, 400)
