from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class TotalTaskLog(models.Model):
  total = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)