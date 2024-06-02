from resources.initalizations import firebase, helper_functions

class KeyMangaerDB():
    
    def __init__(self) -> None:
        db = firebase.database()
        self.key_ref = db.child("KeyManager")
        
    def save_keys(self, uid):
        try:
            private_key, public_key = helper_functions.generate_key_pair()
            self.key_ref.child(uid).set({"private_key": private_key, "public_key": public_key})
                 
            return True, {"public_key": public_key, "private_key": private_key}
        
        except Exception as e:
            print(e)
            return False, e  
    
    def get_keys(self, uid):
        return  dict(self.key_ref.child(uid).get().val())
            
    