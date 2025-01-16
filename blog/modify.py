# blog/modify.py

from storage import blogs

def modify_post(username):
    """Modify an existing blog post."""
    if not blogs[username]:
        print("\nNo Posts Available To Modify.")
        return

    for idx, post in enumerate(blogs[username], 1):
        print(f"{idx}. {post['title']}")

    try:
        post_num = int(input("\nEnter Post Number To Modify: ")) - 1
        if 0 <= post_num < len(blogs[username]):
            new_title = input("\nEnter New Title: ")
            new_content = input("\nEnter New Content: ")
            blogs[username][post_num] = {'title': new_title, 'content': new_content}
            print("\nPost Modified Successfully!")
        else:
            print("\nInvalid Post Number.")
    except ValueError:
        print("\nInvalid Input. Please enter a number.")
