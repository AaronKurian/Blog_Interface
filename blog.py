import bcrypt
import getpass


#Store users and their encrypted passwords (in-memory)
users = {}

#Store blog posts for each user
blogs = {}


#User Registration
def register():
    username = input("\nEnter a New Username: ")
    if username in users:
        print("\nUser Already Exists!")
        return

    password = getpass.getpass("\nEnter a New Password: ")
    encrypted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users[username] = encrypted_password
    blogs[username] = []  # Initialize an empty list for the user's blogs
    print(f"\nUser '{username}' Registered Successfully!")


#User Login
def login():
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
    

#Creating a Blog Post
def create_post(username):
    title = input("\nEnter Post Title: ")
    content = input("\nEnter Post Content: ")
    blogs[username].append({'title': title, 'content': content})
    print(f"\nPost '{title}' Created Successfully!")


#Modifying a Blog Post
def modify_post(username):
    if not blogs[username]:
        print("\nNo Posts Available To Modify.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("\nEnter Post Number To Modify: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        new_title = input("\nEnter New Title: ")
        new_content = input("\nEnter New Content: ")
        blogs[username][post_num] = {'title': new_title, 'content': new_content}
        print("\nPost Modified Successfully!")
    else:
        print("\nInvalid Post Number.")


#Deleting a Blog Post
def delete_post(username):
    if not blogs[username]:
        print("\nNo Posts Available to Delete.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    post_num = int(input("\nEnter Post Number to Delete: ")) - 1
    if 0 <= post_num < len(blogs[username]):
        removed_post = blogs[username].pop(post_num)
        print(f"\nPost '{removed_post['title']}' Deleted Successfully!")
    else:
        print("\nInvalid Post Number.")


#Blog Management Menu
def blog_menu(username):
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


#Main Program Loop
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("\nSelect an Option: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
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
