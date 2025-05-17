from django.shortcuts import render, redirect, get_object_or_404

# import httpresponse
#views are request handler functions that return a HttpResponse
from django.http import HttpResponse

#handle login users with tasks
from django.contrib.auth import get_user_model
from .models import Task, Note


#for users
User = get_user_model()

# Create your views here.


def index(request):
    dict = {
        'title' : 'Welcome to the To-Do-List Home Page',
        'comment' : 'Here you can create and manage tasks along with notes.',
        'outro' : 'Enjoy organizing and managing your workflow!',
    }
    return render(request, 'task_app/index.html', context=dict)

def tasklist(request):
    #filter task for task belong to the user
    
    if request.user.is_authenticated:
        user_to_display = request.user
    else:
        user_to_display, created = User.objects.get_or_create(
            username='guest',
            defaults={'password': '!', 'email': 'guest@example.com'}
        )

    untracked_tasks = Task.objects.filter(user=user_to_display, task_status="Untracked")
    in_progress_tasks = Task.objects.filter(user=user_to_display, task_status="In Progress")
    completed_tasks = Task.objects.filter(user=user_to_display, task_status="Completed")

    context = {
        'untracked_tasks': untracked_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'task_app/tasklist.html', context)


def taskform(request):
    return render(request, 'task_app/taskform.html')

#add task for the user


def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_desc = request.POST.get('task_desc')
        task_status = request.POST.get('task_status')

        #Create a new task instance
        task = Task()

        task.task_name = task_name
        task.task_desc = task_desc
        task.task_status = task_status

        #Associate task with the user
        if request.user.is_authenticated:
            task.user = request.user
        else: #or guest user
            guest_user, created = User.objects.get_or_create(
                username = 'guest',
                defaults={'password': '!', 'email': 'guest@example.com'}
            )
            task.user = guest_user

        #Save the task
        task.save()
        return redirect('tasklist')
    return render(request, 'task_app/taskform.html')

def update_task(request, task_id):
    task = get_object_or_404(Task, pk =task_id)
    if request.method == 'POST':
        task.task_name = request.POST.get('task_name')
        task.task_desc = request.POST.get('task_desc')
        task.task_status = request.POST.get('task_status')
        task.save()
        return redirect('tasklist')
    return render(request, 'task_app/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasklist')
    return render(request, 'task_app/delete_task_confirm.html', {'task' : task})

