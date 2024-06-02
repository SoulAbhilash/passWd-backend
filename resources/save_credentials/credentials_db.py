# from .crypto_manager import CryotoManager
from ..user.user_db import UserDB
from resources.initalizations import firebase

class CredentialsDB():
    
    def __init__(self) -> None:
        db = firebase.database()
        self.ref = db.child("Credentials")
        # self.crypto_mangaer = CryotoManager()
        self.user_db = UserDB()
        
    
    def save_credentials(self, username:str, website:str, uid:str, password:str) -> tuple:
        
        try:

            data = {
                'password': password,
                'username': username,
                'website': website
            }
            
            self.ref.child(uid).push(data) 
            
            return True, None
            
        except Exception as e:
            print(e)
            return False, e
    
    def get_credentials(self, uid):
        try:
            response = []
            credentials = dict(self.ref.child(uid).get().val())
            for credential in credentials.keys():
                data = {**credentials[credential], "credential_id": credential}
                response.append(data)
                 
            return True, response
        
        except Exception as e:
            print(e)
            return False, e  
            
            
    