# main.py
from auth import register, login
from utils import blog_menu

def main():
    """Main program loop for user registration, login, and blog management."""
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
