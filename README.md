# Email Scheduler Flask

Auto email scheduler built with Flask.

## Features

- Schedule emails to be sent at a specific time
- Celery for asynchronous task management
- Docker for deployment

## Requirements

- Python 3.9
- PostgreSQL
- Redis
- Flask
- Celery

## Getting Started

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/email-scheduler-flask.git
    cd email-scheduler-flask
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file at the root level of the project and add the following environment variables:
    ```env
    DATABASE_URL=postgresql+psycopg2://postgres:postgres@host/db_name
    CELERY_BROKER_URL=redis://host:6379/0
    CELERY_RESULT_BACKEND=redis://host:6379/0
    MAIL_PORT=465
    MAIL_USERNAME=your-email@example.com
    MAIL_PASSWORD=your-email-password
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@host/db_name
    ```

### Database Setup

1. Initialize the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

### Running the Application

1. Start the Flask development server:
    ```sh
    flask run
    ```

2. Start the Celery worker:
    ```sh
    celery -A app.celery worker --loglevel=info
    ```

3. Start the Redis server (if not already running):
    ```sh
    redis-server
    ```

### Docker Setup

1. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

