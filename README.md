# Full Stack Django Blog App

This is a full stack Django blog application that consists of both a frontend and backend. The application allows users to create accounts, and write blog posts.

## Features

- User Authentication: Users can create accounts, log in, and log out. Authentication is required for creating, updating, and deleting blog posts, as well as for commenting and liking posts.

- Blog Post Management: Authenticated users can create, read, update, and delete their blog posts. Each blog post includes a title, content, publication date, and author information.

## Technology Stack

The application is built using the following technologies:

- Python 3.7 or higher
- Django 3.1 or higher
- Django Rest Framework 3.12 or higher (Backend API)
- HTML, CSS, JavaScript (Frontend)

## Installation

1. Clone the repository:

```
git clone <repository_url>
```

2. Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Set up the database:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

The app will be accessible at `http://localhost:8000/`.

## Usage

### User Registration

1. Access the frontend application at `http://localhost:8000/`.
2. Click on the "Register" link to create a new user account.
3. Fill in the required fields (e.g., username, email, password) and submit the form.
4. Upon successful registration, you will be redirected to the login page.

### User Login

1. Access the frontend application at `http://localhost:8000/login`.
2. Click on the "Login" link.
3. Enter your credentials (username and password) and submit the form.
4. If the provided credentials are valid, you will be redirected to the homepage.

### Creating a Blog Post

1. After logging in, click on the "New Post" button on the homepage.
2. Fill in the title and content of the blog post.
3. Click on the "Publish" button to create the post.
4. The post will be displayed on the homepage and accessible to other users.

## Contributions

Contributions to the Django blog app are welcome. If you find any bugs, have

 feature suggestions, or would like to contribute in any way, please feel free to submit a pull request or open an issue on the repository.

## License

The Django blog app is open-source and released under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Conclusion

The full stack Django blog app provides a comprehensive platform for users to create and share their blog posts. It allows for user registration, authentication, blog post management, commenting, and liking functionality. Explore the application, share your thoughts, and enjoy blogging with Django!
