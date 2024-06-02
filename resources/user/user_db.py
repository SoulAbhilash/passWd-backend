from resources.initalizations import firebase

class UserDB:
    
    def __init__(self) -> None:
        db = firebase.database()
        self.user_ref = db.child("Users")
    
    def _if_user_exsist(self, uid: str) -> bool:
        return self.user_ref.child(uid).get().val() != None
    
    def _get_user_data(self, uid: str) -> dict:
        return dict(self.user_ref.child(uid).get().val())
    
    def _get_user_data_by_key(self, uid: str, key: str) -> str:
        data = dict(self.user_ref.child(uid).get().val())
        return str(data.get(key))