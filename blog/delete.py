# blog/delete.py

from storage import blogs

def delete_post(username):
    """Delete an existing blog post."""
    if not blogs[username]:
        print("\nNo Posts Available to Delete.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    try:
        post_num = int(input("\nEnter Post Number to Delete: ")) - 1
        if 0 <= post_num < len(blogs[username]):
            removed_post = blogs[username].pop(post_num)
            print(f"\nPost '{removed_post['title']}' Deleted Successfully!")
        else:
            print("\nInvalid Post Number.")
    except ValueError:
        print("\nInvalid Input. Please enter a number.")
