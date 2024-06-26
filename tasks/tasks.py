from celery import shared_task
from .models import Task

@shared_task
def check_completed_tasks():
  completed_count = Task.objects.filter(completed=True).count()
  print(f"Number of completed tasks: {completed_count}")
  # You can further process the count here (e.g., log to database)
  return completed_count