# LoginPage Authentication in Flask

This repository contains a simple login page with authentication implemented using Flask. The project demonstrates how to create user authentication, handle login sessions, and secure user data.

## Features

- User registration and login functionality
- Secure password handling using hashing
- Session management for authenticated users
- Flask-based backend with template rendering

## Technologies Used

- Flask
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- SQLite (or any preferred database)
- HTML

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Nishchal-Guptaa/LoginPage_Auth_in_Flask.git
   ```
2. Navigate to the project directory:
   ```sh
   cd LoginPage_Auth_in_Flask
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Initialize the database:
   ```sh
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```
6. Run the Flask application:
   ```sh
   python app.py
   ```
7. Open the application in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Folder Structure

```
LoginPage_Auth_in_Flask/
│-- app.py
│-- database.db
│-- requirements.txt
│-- templates/
│   │-- index.html
│   │-- login.html
│   │-- sign_up.html
│   │-- dashboard.html
```

## Usage

- Register a new account.
- Login using registered credentials.
- Access protected routes once authenticated.
- Logout to end the session.
