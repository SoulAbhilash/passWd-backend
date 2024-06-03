from resources.initalizations import db
from ..helpers import HelperFunctions
from ..keys_management.key_db import KeyMangaerDB

from Crypto.Random import get_random_bytes

class AuthManager:
    """
    This class manages user authentication functionalities.
    """

    def create_user(self, uid:str, username:str, email:str) -> tuple:
        """
        Creates a new user in the Firebase Realtime Database.

        Args:
            self: Reference to the current AuthManager object.
            uid: (String) Unique identifier for the user.
            name: (String) User's name.
            email: (String) User's email address.
            access_token: (String) User's access token (potentially obtained from an external authentication provider).

        Returns:
            A tuple containing two elements:
                * The first element is a boolean (`True` on success, `False` on failure).
                * The second element is either `None` (on success) or an `Exception` object containing details about any errors encountered during user creation.
        """

        try:
            data = {
                'username': username,
                'email': email,
            }

            status, key = KeyMangaerDB().save_keys(uid)

            if status:
                db.child("Users").child(uid).set(data)
            else:
                raise Exception("Unable to generate/save keys")

            return True, key

        except Exception as e:
            return False, e
