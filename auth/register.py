# auth/register.py

import bcrypt
import getpass
from storage import users, blogs

def register():
    """Register a new user with a username and password."""
    username = input("\nEnter a New Username: ")
    if username in users:
        print("\nUser Already Exists!")
        return

    password = getpass.getpass("\nEnter a New Password: ")
    encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users[username] = encrypted_password
    blogs[username] = []  # Initialize an empty list for the user's blogs
    print(f"\nUser '{username}' Registered Successfully!")
