from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('taskform', views.taskform, name='taskform'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:task_id>', views.update_task, name='update_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]