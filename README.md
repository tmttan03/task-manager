# task-manager

This repository provides a well-structured Django web application for managing tasks, including basic CRUD (Create, Read, Update, Delete) functionalities. It leverages Celery for asynchronous tasks and benefits from a Docker environment for streamlined deployment.

Requirements:
- Python >= 3.9.18
- pip (package installer)
- Docker Desktop (or a compatible container runtime)

Installation:

1. Clone the Repository:
```
    git clone https://github.com/tmttan03/task-manager.git
```

2. Run docker build

```
docker-compose build
```

3. Run docker container

```
docker-compose up
```

4. Access the django-admin [http://127.0.0.1:8000/admin/] to add data.

