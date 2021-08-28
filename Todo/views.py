from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Note


def home(request):
    if request.user.is_authenticated:
        #print("Email => ", request.user.email)
        #print("Username => ", request.user.username)
        queryset_note = Note.objects.filter(completed=False, user=request.user)
        #print("count => ", Note.objects.filter(completed=True).count())
        # to get all the Todo's who has completed value = False
        # print(queryset_note)
        # for item in queryset_note:
        #   print("title: ", item.title)
        #   print("description: ", item.description)
        #   print("\n")
        return render(request, "103.html", context={'queryset_note': queryset_note})
    return HttpResponse("User Not Logged in!")

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user
        obj_note = Note(title=title, description=description, user=user)
        obj_note.save()

    return redirect("todo_home")

        #return HttpResponse("<h1>Hello World Post Request</h1><br>{0} <br>{1}".format(title, description))

    return render(request, "add_todo.html", context={})

def update_todo(request):
    if request.method == "POST":
        todo_id = request.POST.get("todo_id")
        title = request.POST.get("title")
        description = request.POST.get("description")

        obj_note = Note.objects.get(id=todo_id)
        obj_note.title = title
        obj_note.description = description
        obj_note.save()

        return redirect("todo_home")

    todo_id = request.GET.get("todo_id")
    obj_todo = Note.objects.get(id=todo_id)
    return render(request, "add_todo.html", context={'obj_todo': obj_todo})

def delete_todo(request):
    if request.method == "GET":
        todo_id = request.GET.get("todo_id")
        obj_todo = Note.objects.get(id=todo_id)
        obj_todo.delete()

        return redirect("todo_home")
#http://127.0.0.1:8000/Todo/todo_completed?todo_id=821

def todo_completed(request):
    if request.method == "GET":
        todo_id = request.GET.get("todo_id")
        if Note.objects.filter(id=todo_id).count():
            obj_todo = Note.objects.get(id=todo_id)
            obj_todo.completed = True
            obj_todo.save()

    return redirect("todo_home")

