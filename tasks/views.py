from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
