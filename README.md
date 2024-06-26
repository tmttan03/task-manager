# task-manager

This repository provides a well-structured Django web application for managing tasks, including basic CRUD (Create, Read, Update, Delete) functionalities. It leverages Celery for asynchronous tasks and benefits from a Docker environment for streamlined deployment.

Requirements:
- Python >= 3.9.18
- pip (package installer)
- Docker Desktop (or a compatible container runtime)

## Set up Instructions

1. Clone project

```
git clone git@github.com:Codev-Team-O/job-board-backend.git
```

2. Set up virtual environment (2 ways)

- Using virtualenv

```
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

- Using pyenv

```
pyenv install 3.9.18
pyenv virtualenv 3.9.18 venv
pyenv local venv
pip install --upgrade pip
pip install -r requirements.txt
```

3. Set up Environment Variables

- copy the .env.sample and rename it to .env, fill it in with the correct values

4. Migrate the files with

```
$ python manage.py migrate
```

5. Run initial fixture data

```
$ python manage.py loaddata data/initial.json
```

6. Create super user

```
$ python manage.py createsuperuser
```

7. Runserver

```
$ python manage.py runserver
```

8. Access the django-admin [http://127.0.0.1:8000/admin/] to add data. Login using the superuser creds.

9. Make sure Redis server is up

10. Run in different terminals
```
$ celery -A task_manager beat -l info
$ celery -A task_manager worker -l info -c 4
```

- Run using dockerfile

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

