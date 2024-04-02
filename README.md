# Password Generator API

This is a simple REST API built with FastAPI that allows users to generate passwords based on specified criteria.

## Features

- Generate passwords of variable lengths.
- Secure password generation using best practices.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/password-generator-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-generator-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

5. The API will now be available at `http://localhost:8000`. You can access the `/generate-password` endpoint to generate passwords.

## API Documentation

You can access the API documentation by visiting `http://localhost:8000/docs` in your browser.

