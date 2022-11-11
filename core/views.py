from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *
from .forms import TodoForm, CreateUserForm
# Create your views here.


def register(request: HttpRequest):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user: User = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for {username}")
            return redirect("accounts:user_login")

    context = {"form": form}
    return render(request, 'core/user/register.html', context)


def user_login(request: HttpRequest):

    context = {}
    return render(request, 'core/user/login.html', context)
    pass


def home(request: HttpRequest):
    return redirect("core:collection", Collection.objects.first().pk)


def add_to_collection(request: HttpRequest, pk: int = None):
    if request.method == "POST":
        todo = Todo.objects.create(
            title=request.POST.get('todo_text'), collection_id=pk)
        todo.save()
        messages.success(request, "Todo has been created!")
    else:
        messages.error(request, "Only POST methods allowed!")

    return redirect("core:collection", pk)


def delete_collection(request: HttpRequest, pk: int = None):
    collection = Collection.objects.get(pk=pk)
    collection.delete()
    messages.success(request, f"Collection {collection.name} was deleted!")
    return redirect("core:collection", Collection.objects.first().pk)


def add_collection(request: HttpRequest):
    if request.method == "POST":
        collection = Collection.objects.create(
            name=request.POST.get('collection_name'))
        collection.save()
        messages.success(request, "Collection has been created!")
    else:
        messages.error(request, "Only POST methods allowed!")

    return redirect("core:collection", collection.pk)


def collection(request: HttpRequest, pk: int = None):
    collections = Collection.objects.all()
    total_incomplete = Todo.objects.filter(status="PENDING").count()
    total_complete = Todo.objects.filter(status="COMPLETED").count()
    active_collection = Collection.objects.get(id=pk)
    active_incomplete_todos = active_collection.todo_set.filter(
        status="PENDING")
    active_total_incomplete = active_incomplete_todos.count()
    active_complete_todos = active_collection.todo_set.filter(
        status="COMPLETED")
    active_total_complete = active_complete_todos.count()
    context = {'page_title': 'Collection',
               'collections': collections,
               'total_complete': total_complete,
               'total_incomplete': total_incomplete,
               'active_collection': active_collection,
               'active_incomplete_todos': active_incomplete_todos,
               'active_total_incomplete': active_total_incomplete,
               'active_complete_todos': active_complete_todos,
               'active_total_complete': active_total_complete}
    return render(request, 'core/collection.html', context)


def todo(request: HttpRequest, pk: int = None):
    active_todo = Todo.objects.get(pk=pk)
    context = {
        'page_title': 'Todo',
        'todo': active_todo
    }
    return render(request, 'core/todo.html', context)


def mark_complete(request: HttpRequest, pk: int = None):
    todo = Todo.objects.get(pk=pk)
    todo.status = "COMPLETED"
    todo.save()
    messages.success(request, "Todo marked complete!")
    return redirect("core:collection", todo.collection.pk)


def mark_pending(request: HttpRequest, pk: int = None):
    todo = Todo.objects.get(pk=pk)
    todo.status = "PENDING"
    todo.save()
    messages.success(request, "Todo marked incomplete!")
    return redirect("core:collection", todo.collection.pk)


def delete_todo(request: HttpRequest, pk: int = None):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    messages.success(request, f"Todo {todo.title} was deleted!")
    return redirect("core:collection", todo.collection.id)


def update_todo(request: HttpRequest, pk: int = None):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo has been updated successfully")
            return redirect('core:todo', todo.pk)

    context = {
        "page_title": "Update Todo",
        "form": form
    }
    return render(request, 'core/todo_form.html', context)
