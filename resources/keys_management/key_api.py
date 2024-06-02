from flask_restful import Resource, reqparse
from flask import request, jsonify, make_response

from .key_db import KeyMangaerDB

class Keys(Resource):

    def __init__(self) -> None:
        self.key_manager_db = KeyMangaerDB()
        super().__init__()
    
    def get(self):
        uid = request.headers.get("uid")
        keys = self.key_manager_db.get_keys(uid)
        if keys != None:
            return make_response({**keys})
        else:
            raise Exception("Keys not found")
    
