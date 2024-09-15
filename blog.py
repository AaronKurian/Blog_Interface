import bcrypt
import getpass


#Store users and their encrypted passwords (in-memory)
users = {}

#Store blog posts for each user
blogs = {}


#User Registration
def register():
    username = input("Enter a New Username: ")
    if username in users:
        print("User Already Exists!")
        return

    password = getpass.getpass("Enter a New Password: ")
    encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users[username] = encrypted_password
    blogs[username] = []  # Initialize an empty list for the user's blogs
    print(f"User '{username}' Registered Successfully!")


#User Login
def login():
    username = input("Enter Username: ")
    if username not in users:
        print("Username Not Found!")
        return None

    password = getpass.getpass("Enter Password: ")
    if bcrypt.checkpw(password.encode(), users[username]):
        print(f"Welcome, {username}!")
        return username
    else:
        print("Incorrect Password!")
        return None
    

#Creating a Blog Post
def create_post(username):
    title = input("Enter Post Title: ")
    content = input("Enter Post Content: ")
    blogs[username].append({'title': title, 'content': content})
    print(f"Post '{title}' Created!")


#Modifying a Blog Post
def modify_post(username):
    if not blogs[username]:
        print("No Posts Available To Modify.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("Enter Post Number To Modify: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        new_title = input("Enter New Title: ")
        new_content = input("Enter New Content: ")
        blogs[username][post_num] = {'title': new_title, 'content': new_content}
        print("Post Modified Successfully!")
    else:
        print("Invalid Post Number.")


#Deleting a Blog Post
def delete_post(username):
    if not blogs[username]:
        print("No Posts Available to Delete.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("Enter Post Number to Delete: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        removed_post = blogs[username].pop(post_num)
        print(f"Post '{removed_post['title']}' deleted!")
    else:
        print("Invalid Post Number.")


#Blog Management Menu
def blog_menu(username):
    while True:
        print("\n1. Create Post\n2. Modify Post\n3. Delete Post\n4. Logout")
        choice = input("Select an Option: ")
        if choice == '1':
            create_post(username)
        elif choice == '2':
            modify_post(username)
        elif choice == '3':
            delete_post(username)
        elif choice == '4':
            print("Logging Out...")
            break
        else:
            print("Invalid Option.")


#Main Program Loop
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an Option: ")
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
            print("Invalid Option.")

if __name__ == "__main__":
    main()
