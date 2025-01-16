# auth/login.py

import bcrypt
import getpass
from storage import users

def login():
    """Log in the user by verifying the password."""
    username = input("\nEnter Username: ")
    if username not in users:
        print("\nUsername Not Found!")
        return None

    password = getpass.getpass("\nEnter Password: ")
    if bcrypt.checkpw(password.encode(), users[username]):
        print(f"\nWelcome, {username}!")
        return username
    else:
        print("\nIncorrect Password!")
        return None
