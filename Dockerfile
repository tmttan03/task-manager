# Use official Python base image
FROM python:3.11-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Use environment variables in configuration file
ENV DJANGO_SETTINGS_MODULE=task_manager.settings

# Inject environment variables from .env (using sed)
RUN sed -i "s/DATABASE_HOST=.*/DATABASE_HOST=${DATABASE_HOST}/" task_manager/settings.py
RUN sed -i "s/DATABASE_USER=.*/DATABASE_USER=${DATABASE_USER}/" task_manager/settings.py
RUN sed -i "s/DATABASE_PASSWORD=.*/DATABASE_PASSWORD=${DATABASE_PASSWORD}/" task_manager/settings.py
RUN sed -i "s/DATABASE_NAME=.*/DATABASE_NAME=${DATABASE_NAME}/" task_manager/settings.py

# Apply database migrations (assuming PostgreSQL)
RUN python manage.py makemigrations && python manage.py migrate

# Create initial superuser
RUN python manage.py loaddata data/initial.json

# Expose Django port
EXPOSE 8000

# Run Gunicorn as the main process
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_manager.wsgi:application"]


