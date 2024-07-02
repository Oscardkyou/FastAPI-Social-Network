![Social Network](121233.png)
# FastAPI Social Network

## Overview

FastAPI Social Network is a simple social media platform built with FastAPI, SQLAlchemy, and PostgreSQL. It supports user authentication, posting, commenting, liking, and notifications.

## Features

- User Registration and Authentication (JWT)
- Create, Read, Update, Delete (CRUD) Posts
- Comment on Posts
- Like/Unlike Posts
- User Profiles
- Notifications for User Actions

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-social-network.git
    cd fastapi-social-network
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database and environment variables:
    - Create a `.env` file in the root directory and add your database URL and secret key:
        ```
        DATABASE_URL=postgresql://user:password@localhost/dbname
        SECRET_KEY=your_secret_key
        ```

5. Run the database migrations:
    ```bash
    alembic upgrade head
    ```

6. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

7. Access the API documentation at `http://127.0.0.1:8000/docs`.




