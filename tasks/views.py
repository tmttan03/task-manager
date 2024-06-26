from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from .models import Task


class TaskList(ListView):
  model = Task


class TaskCreate(CreateView):
  model = Task
  fields = ['title', 'description']
  success_url = '/'


class TaskUpdate(UpdateView):
  model = Task
  fields = ['title', 'description', 'completed']
  success_url = '/'


class TaskDelete(DeleteView):
  model = Task
  success_url = '/'


def update_task_complete(request, pk):
    """
    Update the completed status of a specific task (non-DRF approach).
    Handles both POST requests for updating and GET requests for rendering the template.
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
      completed = request.POST.get('completed', False).lower() == 'true'  # Convert to lowercase for comparison
      completed = completed in ('true', 'on', 1)  # Check for common representations of True
      task.completed = bool(completed)
      task.save()

      # Redirect to the task list page (or desired success URL)
      return JsonResponse({'message': 'Task updated successfully.'})
    context = {'task': task}
    return render(request, 'tasks/task_list.html', context)
