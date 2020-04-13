from app import bcrypt, login, db
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, username, password, id, email):
        self.id = str(id)
        self.username = username
        self.password = password
        self.email = email

    def set_postal_code_and_lat_long(self, new_postal_code):
        self.postal_code = new_postal_code

    def update_password(self, new_password):
        self.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

    def __repr__(self):
        return f"<User {self.username}>"

@login.user_loader
def load_user(id):
    print(f"in load_user with username {id}")
    user_db_dict = db.get_user_by_id(id)
    return User(user_db_dict["username"], user_db_dict["password"], user_db_dict["_id"], user_db_dict["email"])