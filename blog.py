import bcrypt
import getpass

# Store users and their encrypted passwords (in-memory)
users = {}

# Store blog posts for each user
blogs = {}