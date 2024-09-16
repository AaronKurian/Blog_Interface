# Blog_Interface

This is a terminal-based blog interface written in Python. It allows multiple users to create, modify, and delete blog posts. Each user has their own account, with passwords securely encrypted and stored to allow login for future sessions.

## Features

- **User Authentication**: Users can register and log in to the system. Passwords are encrypted to ensure security.
- **Create Blog Posts**: Users can write and publish their own blog posts.
- **Modify Blog Posts**: Users can update any blog posts they have created.
- **Delete Blog Posts**: Users can remove any of their own blog posts.
- **Multiple Users**: Each user can maintain their own collection of blog posts, isolated from others.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/AaronKurian/Blog_Interface.git
    cd Blog_Interface
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Python script:
    ```bash
    python blog.py
    ```

## Usage

1. **Register**: New users must register by providing a username and password.
2. **Login**: Existing users can log in using their username and password.
3. **Create a Post**: After login, users can create new blog posts.
4. **Modify/Delete**: Users can modify or delete their blog posts.
5. **Logout**: Users can log out of the system after completing their tasks.

## Technologies Used

- **Python**: Core programming language.
- **bcrypt**: For password encryption and decryption.

## Security Features

- Passwords are stored securely using encryption (bcrypt).
- User accounts and blog posts are isolated, allowing for multiple user support.

## Future Improvements

- Add a graphical user interface (GUI).
- Implement a database (such as MongoDB) for more flexible data management and scalability.
- Enable comments on blog posts.

## License

This project is licensed under the MIT License.

---

Happy Blogging!
