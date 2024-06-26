from celery import shared_task
from .models import Task, TotalTaskLog

@shared_task
def check_and_log_completed_tasks():
    completed_tasks = Task.objects.filter(completed=True)
    completed_tasks_count = completed_tasks.count()
    print(f"Found {completed_tasks_count} completed tasks.")

    # Optional: Log details of each completed task
    for task in completed_tasks:
        print(f"Task completed: {task.title}")

    TotalTaskLog.objects.create(total=completed_tasks_count)
    return completed_tasks_count