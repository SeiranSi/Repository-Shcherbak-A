class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        self.is_active = True

    def verify_username(self, username):
        return self.username == username

    def verify_password(self, password):
        if self.password_hash == password:
            return True
        else:
            return False

    def show_details(self):
        print(f"\nUsername: {self.username}")
        print(f"Is Active: {self.is_active}")

class Administrator(User):
    def __init__(self, username, password_hash, permissions):
        super().__init__(username, password_hash)
        self.permissions = permissions


class RegularUser(User):
    def __init__(self, username, password_hash, last_login_date=""):
        super().__init__(username, password_hash)
        self.last_login_date = last_login_date

class Guest(User):
    def __init__(self):
        super().__init__("Guest", "")
        self.access_level = "limited"


class AccessControl:
    def __init__(self):
        super().__init__()
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        if username in self.users:
            found_user = self.users[username]
            if found_user.verify_password(password):
                return found_user
            else:
                return None


if __name__ == "__main__":
    system = AccessControl()

    admin = Administrator("Admin_Boss", "admin_hash_123", ["delete_users", "edit_roles"])
    regular = RegularUser("Ivan_user", "user_hash_456", "2026-11-09")
    guest = Guest()

    system.add_user(admin)
    system.add_user(regular)
    system.add_user(guest)

    success_login = system.authenticate_user("Admin_Boss", "admin_hash_123")
    if success_login:
        print(f"Успішний вхід! Користувач: {success_login.username}, Права: {getattr(success_login, 'permissions', 'немає')}")

    failed_login = system.authenticate_user("Ivan_user", "wrong_password")
    if not failed_login:
        print("Помилка входу: невірний пароль.")

user1 = User("Alexey", "1234567890")
user2 = User("Sonya", "qwertyuiop[]")





