from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def create_user_account(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email_id")
        passwd = request.POST.get("passwd")

        if not User.objects.filter(username=username):
            user = User.objects.create_user(username=username, email=email)
            user.save()
            user.set_password(passwd)
            user.save()
            # return HttpResponse("User created")
            return render(request, "user_created_popup.html", context={})
        else:
            return render(request, "user_already_exists_popup.html", context={})

    return render(request, "sign_up.html", context={})

def sign_in_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")

        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            return redirect("todo_home")
            return HttpResponse("User exist in our db")
        else:
            return HttpResponse("user does not exist")

    return render(request, "sign_in.html")

def logout_user(request):
    logout(request)

    return redirect("login")