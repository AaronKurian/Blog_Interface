import bcrypt
import getpass


# Store users and their encrypted passwords (in-memory)
users = {}

# Store blog posts for each user
blogs = {}

#User Registration:

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("User already exists!")
        return

    password = getpass.getpass("Enter a new password: ")
    encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users[username] = encrypted_password
    blogs[username] = []  # Initialize an empty list for the user's blogs
    print(f"User '{username}' registered successfully!")


    #User Login:
def login():
    username = input("Enter username: ")
    if username not in users:
        print("Username not found!")
        return None

    password = getpass.getpass("Enter password: ")
    if bcrypt.checkpw(password.encode(), users[username]):
        print(f"Welcome, {username}!")
        return username
    else:
        print("Incorrect password!")
        return None