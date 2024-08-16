# User Authentication Service

## Overview
This project is a user authentication service designed to manage user registration, login, and session management. It provides secure methods for handling user credentials and ensures that only authenticated users can access certain resources.

## Features
- **User Registration**: Allows new users to create an account.
- **User Login**: Authenticates users and provides them with a session token.
- **Session Management**: Manages user sessions and ensures secure access to resources.
- **Password Hashing**: Uses secure hashing algorithms to store user passwords.
- **Token-Based Authentication**: Issues and validates tokens for user sessions.

## Technologies Used
- **Python**: The primary programming language used for the service.
- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: An ORM for database interactions.
- **JWT**: JSON Web Tokens for secure token-based authentication.
- **bcrypt**: A library for password hashing.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/user_authentication_service.git
    ```
2. Navigate to the project directory:
    ```sh
    cd user_authentication_service
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    flask run
    ```
2. Access the service at `http://127.0.0.1:5000`.

## API Endpoints
- **POST /register**: Register a new user.
- **POST /login**: Authenticate a user and return a session token.
- **GET /profile**: Retrieve the authenticated user's profile information.

