from django.forms.utils import to_current_timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('/')
               
    context = {'tasks':tasks, "form": form}
    return render(request, 'tasks/list.html', context)

def edit_task(request, primaryKey):
    task = Task.objects.get(id=primaryKey)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/edit_task.html', context)

def delete_task(request, primaryKey):
    item = Task.objects.get(id=primaryKey)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tasks/delete_task.html', context)
    
def update_task_completion(request, primaryKey):
    item = Task.objects.get(id=primaryKey)
    item.update_completion()
    item.save()
    return redirect('/')