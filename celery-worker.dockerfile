FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "task_manager", "worker", "-l", "info", "-c", "2"]  # Adjust concurrency with -c

