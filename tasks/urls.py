from django.urls import path, include
from . import views

app_name = 'tasks'

urlpatterns = [
  path('', views.TaskList.as_view(), name='task_list'),
  path('create/', views.TaskCreate.as_view(), name='task_create'),
  path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
  path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
  path('<int:pk>/complete/', views.update_task_complete, name='update_task_complete'),

]
