class Password_Manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        return password == self.get_password()


pm = Password_Manager()

# Setting password
print(pm.set_password("abc123"))  # True (New password set)
print(pm.set_password("xyz7fwfw89"))  # True (New password set)
print(pm.set_password("abc123"))  # False (Already used)

# Getting current password
print("Current password:", pm.get_password())  # xyz789

# Checking password if correct or not
print(pm.is_correct("xyz789"))  # True
print(pm.is_correct("abc123"))  # False
