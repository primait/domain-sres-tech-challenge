# Flask User Management API

This project is a simple Flask application designed to manage user information via a REST API. The application provides endpoints to retrieve a list of all users and add new users.

## Features

- **Retrieve All Users**: Fetch a list of all users in the system.
- **Create User**: Add a new user to the system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following tools installed on your system:

- Python 3.10
- Docker
- Git (optional, for cloning the repository)

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. **Clone the repository (optional)**:

    ```bash
    git clone https://github.com/enekui/prima.git
    ```

To build and run the application using Docker, follow these steps:

1. **Build the Docker image**:

    ```bash
    docker build -t prima .
    ```

2. **Run the container**:

    ```bash
    docker run -p 4000:5000 prima
    ```

    This will start the server on `http://localhost:4000`.

## API Endpoints

Below are the API endpoints included in this application:

- `GET /users`: Retrieves a list of all users.
- `POST /user`: Creates a new user.

### Example Requests

- **Get All Users**:

    ```bash
    curl -X GET http://localhost:4000/users
    ```

- **Create a New User**:

    ```bash
    curl -X POST http://localhost:4000/user -d "name=Adianny Ramirez&email=adianny@example.com"
    ```
