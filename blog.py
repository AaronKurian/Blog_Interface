import bcrypt
import getpass


#Store users and their encrypted passwords (in-memory)
users = {}

# Store blog posts for each user
blogs = {}


#User Registration
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


#User Login
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
    

#Creating a Blog Post
def create_post(username):
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    blogs[username].append({'title': title, 'content': content})
    print(f"Post '{title}' created!")


#Modifying a Blog Post
def modify_post(username):
    if not blogs[username]:
        print("No posts available to modify.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("Enter post number to modify: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        new_title = input("Enter new title: ")
        new_content = input("Enter new content: ")
        blogs[username][post_num] = {'title': new_title, 'content': new_content}
        print("Post modified successfully!")
    else:
        print("Invalid post number.")


#Deleting a Blog Post
def delete_post(username):
    if not blogs[username]:
        print("No posts available to delete.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("Enter post number to delete: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        removed_post = blogs[username].pop(post_num)
        print(f"Post '{removed_post['title']}' deleted!")
    else:
        print("Invalid post number.")


#Blog Management Menu
def blog_menu(username):
    while True:
        print("\n1. Create Post\n2. Modify Post\n3. Delete Post\n4. Logout")
        choice = input("Select an option: ")
        if choice == '1':
            create_post(username)
        elif choice == '2':
            modify_post(username)
        elif choice == '3':
            delete_post(username)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option.")


#Main Program Loop
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                blog_menu(username)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
