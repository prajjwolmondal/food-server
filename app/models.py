from app import bcrypt, login, db
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, username, password, id, email):
        self.id = str(id)
        self.username = username
        self.password = password
        self.email = email
        self.postal_code = None
        self.lat_long = None
        self.cuisine_preferences = None

    def update_password(self, new_password):
        self.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

    def __repr__(self):
        return f"<User {self.username}>"

    def set_user_preferences(self, preferences_dict):
        self.postal_code = preferences_dict['postal_code']
        self.cuisine_preferences = preferences_dict['cuisine_preferences']

    def toDict(self) -> dict:
        user_dict = {'id': self.id, 'username': self.username, 'email': self.email}
        if self.postal_code:
            user_dict['postal_code'] = self.postal_code
        if self.lat_long:
            user_dict['lat_long'] = self.lat_long
        if self.cuisine_preferences:
            user_dict['cuisine_preferences'] = self.cuisine_preferences
        
        return user_dict

@login.user_loader
def load_user(id):
    print(f"in load_user with username {id}")
    user_db_dict = db.get_user_by_id(id)
    return User(user_db_dict["username"], user_db_dict["password"], user_db_dict["_id"], user_db_dict["email"])