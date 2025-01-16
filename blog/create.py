# blog/create.py

from storage import blogs

def create_post(username):
    """Create a new blog post for the user."""
    title = input("\nEnter Post Title: ")
    content = input("\nEnter Post Content: ")
    blogs[username].append({'title': title, 'content': content})
    print(f"\nPost '{title}' Created Successfully!")
