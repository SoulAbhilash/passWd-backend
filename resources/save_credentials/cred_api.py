from flask_restful import Resource, reqparse
from flask import request, jsonify, make_response

from .credentials_db import CredentialsDB

class Credentials(Resource):
    
    def __init__(self) -> None:
        
        # Using parser for data validation
        self.save_cred_parser = reqparse.RequestParser()
        self.save_cred_parser.add_argument('website', type=str, required=True, help='website is required')
        self.save_cred_parser.add_argument('username', type=str, required=True, help='username is required')
        self.save_cred_parser.add_argument('password', type=str, required=True, help='email is required')
        self.save_cred_parser.add_argument('uid', type=str, required=True, help='uid is required')
        

        self.cred_manager = CredentialsDB()
        
        super().__init__()
    
    def get(self):
        try:
            uid = request.headers.get("uid")
            print(uid)
            success, message = self.cred_manager.get_credentials(uid)
            if success:
                return make_response(jsonify({'data': message}), 201)
            else:
                return make_response({'message': str(message)}, 500)
        
        except Exception as e:
            return make_response({'message': str(e)}, 400)

    def post(self):
        try:
            args = self.save_cred_parser.parse_args(strict=True)
            
            # Access the parsed arguments
            uid = args['uid']
            username = args['username']
            website = args['website']
            password = args['password']
            
            # Handle response
            success, message = self.cred_manager.save_credentials(
                uid=uid, 
                username=username, 
                password=password, 
                website=website,
                )
            
            
            if success:
                return make_response(jsonify({'body': 'Password Saved'}), 201)
            else:
                return make_response({'message': str(message)}, 500)
            
        except Exception as e:
            return make_response({'message': str(e)}, 400)
    
    

    