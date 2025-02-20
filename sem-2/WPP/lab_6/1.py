class PasswordManager:
    def __init__(self):
        self.password_history = []

    def get_password(self):
        if self.password_history:
            return self.password_history[-1]
        return None

    def set_password(self, new_password):
        if new_password in self.password_history:
            return False
        self.password_history.append(new_password)
        return True

    def is_correct(self, password):
        return password == self.get_password()

pm = PasswordManager()

# Adding passwords
print(pm.set_password("pass123"))  # True (New password added)
print(pm.set_password("secure456"))  # True (New password added)
print(pm.set_password("pass123"))  # False (Already used)

# Checking current password
print("Current password:", pm.get_password())  # secure456

# Verifying password
print(pm.is_correct("secure456"))  # True
print(pm.is_correct("pass123"))  # False
