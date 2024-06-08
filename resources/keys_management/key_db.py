from resources.initalizations import firebase, helper_functions

class KeyMangaerDB():
    
    def __init__(self) -> None:
        db = firebase.database()
        self.key_ref = db.child("KeyManager")
        
    def save_keys(self, uid):
        try:
            keys_iv = helper_functions.generate_keys_iv()
            self.key_ref.child(uid).set({**keys_iv})
                 
            return True, "key saved"
        
        except Exception as e:
            print(e)
            return False, e  
    
    def get_keys(self, uid) -> dict:
            response = dict(self.key_ref.child(uid).get().val())
            print(type(response))
            return response

        
            
    