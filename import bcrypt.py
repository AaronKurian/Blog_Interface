import bcrypt
import getpass

# To store users and their encrypted passwords (in-memory)
users = {}

# To store blog posts for each user
blogs = {}


def register_user():
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


def login_user():
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


def list_posts(username):
    """List all blog posts for a user."""
    if not blogs[username]:
        print("\nNo Posts Available.")
        return False
    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")
    return True


def create_post(username):
    """Create a new blog post for the user."""
    title = input("\nEnter Post Title: ")
    content = input("\nEnter Post Content: ")
    blogs[username].append({'title': title, 'content': content})
    print(f"\nPost '{title}' Created Successfully!")


def modify_post(username):
    """Modify an existing blog post."""
    if not list_posts(username):
        return

    try:
        post_num = int(input("\nEnter Post Number To Modify: ")) - 1
    except ValueError:
        print("\nInvalid Input. Please Enter a Number.")
        return

    if 0 <= post_num < len(blogs[username]):
        new_title = input("\nEnter New Title: ")
        new_content = input("\nEnter New Content: ")
        blogs[username][post_num] = {'title': new_title, 'content': new_content}
        print("\nPost Modified Successfully!")
    else:
        print("\nInvalid Post Number.")


def delete_post(username):
    """Delete an existing blog post."""
    if not list_posts(username):
        return

    try:
        post_num = int(input("\nEnter Post Number to Delete: ")) - 1
    except ValueError:
        print("\nInvalid Input. Please Enter a Number.")
        return

    if 0 <= post_num < len(blogs[username]):
        removed_post = blogs[username].pop(post_num)
        print(f"\nPost '{removed_post['title']}' Deleted Successfully!")
    else:
        print("\nInvalid Post Number.")


def blog_menu(username):
    """Display the blog management menu."""
    while True:
        print("\n1. Create Post\n2. Modify Post\n3. Delete Post\n4. Logout")
        choice = input("\nSelect an Option: ")
        if choice == '1':
            create_post(username)
        elif choice == '2':
            modify_post(username)
        elif choice == '3':
            delete_post(username)
        elif choice == '4':
            print("\nLogging Out...")
            print("Logged Out Successfully :)")
            break
        else:
            print("\nInvalid Option.")


def main():
    """Main program loop for user registration, login, and blog management."""
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("\nSelect an Option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
            if username:
                blog_menu(username)
        elif choice == '3':
            print("\nExiting...")
            print("Thanks for Visiting! :) \n")
            break
        else:
            print("\nInvalid Option.")


if __name__ == "__main__":
    main()
