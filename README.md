# Scalable Task Management with Django and Celery.

This repository provides a well-structured Django web application for managing tasks, including basic CRUD (Create, Read, Update, Delete) functionalities. It leverages Celery for asynchronous tasks and benefits from a Docker environment for streamlined deployment.

**Features:**

- **Task Management:** Create, view, edit, and delete tasks.
- **Prioritization:** Assign priorities to tasks for better organization.
- **Asynchronous Tasks (Optional):** Leverage Celery for performing time-consuming or background tasks without blocking the user interface.

**Requirements:**

- Python: Version 3.9.18 or later (check with python3 --version or python --version)
- pip: Package manager for Python (usually comes bundled with Python)
- Docker Desktop: Container runtime environment (or a compatible alternative like Podman)

# Installation and Setup:

1. Clone the Repository:

Open your terminal or command prompt and navigate to your desired project directory. Then, execute the following command to clone the repository from GitHub:
```
git clone https://github.com/tmttan03/task-manager.git
```

2. Set Up Database Environment:

**Create a copy of the local.py.example file:**
```
cp local.py.example local.py
```
Edit the local.py file using a text editor and replace the placeholder values (e.g., database name, username, password) with your actual PostgreSQL database configuration details.

3. Build and Run with Docker:

- **Build the Image (Optional):**
```
docker-compose build
docker-compose build celery-beat celery-worker
```
This step is only necessary if you haven't built the Docker image before. It creates the image that Docker uses to run your application and dependencies.

- **Start the Application:**
```
docker-compose up -d
```
This command starts the application in detached mode (-d), allowing it to run in the background.

- **Rebuild and Restart (Development):**

If you make changes to your code and want to see those changes reflected in the running application, use this command:
```
docker-compose up --build
```
This rebuilds the image with your latest code and restarts the containers.


4. Access the site `http://0.0.0.0:8000/`
Credentials you can use for django-admin - Celery Task data checking:
- `USERNAME`: admin
- `PASSWORD`: admin12345
