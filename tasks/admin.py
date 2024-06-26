from django.contrib import admin
from .models import Task, TotalTaskLog

admin.site.register(Task)

class TotalTaskLogAdmin(admin.ModelAdmin):
  readonly_fields = ['total']

admin.site.register(TotalTaskLog, TotalTaskLogAdmin)