# Use official Python base image
FROM python:3.11-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Expose Django port
EXPOSE 8000

# Run Gunicorn as the main process
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_manager.wsgi:application"]
