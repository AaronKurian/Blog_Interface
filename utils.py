# utils.py

from blog import create_post, modify_post, delete_post

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
