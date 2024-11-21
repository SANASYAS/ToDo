from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo_entry

def todo(request):
    todos = Todo_entry.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'ListApp/todo.html', context)

def add(request):
    if request.method == 'POST':
        entry = request.POST['entry']
        todo_entry = Todo_entry(entry=entry)
        todo_entry.save()
        return HttpResponseRedirect(reverse('todo'))  # Redirect to the todo list page after adding

def delete(request, id=None):
    if id is not None:
        # Using get_object_or_404 to handle invalid IDs gracefully
        todo_entry = get_object_or_404(Todo_entry, id=id)
        todo_entry.delete()
        return HttpResponseRedirect(reverse('todo'))  # Redirect to the todo list page after deletion
    else:
        # If no ID is passed, delete all entries
        Todo_entry.objects.all().delete()
        return HttpResponseRedirect(reverse('todo'))  # Redirect after deleting all tasks
