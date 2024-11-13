
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class AuthService:
    def __init__(self):
        self.users = {
            "admin": User("admin", "adminpass", "Admin"),
            "user": User("user", "userpass", "User")
        }

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        raise Exception("Invalid username or password")
