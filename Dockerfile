FROM python:3.11.4-slim-bullseye

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

# Copy project code
COPY . .

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Expose the Django development port (default: 8000)
EXPOSE 8000

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

