from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    if request.method == "POST":
        data: dict = request.POST
        user = CustomUser()
        if data.get("first_name"):
            user.first_name = data["first_name"]
        if data.get("last_name"):
            user.last_name = data["last_name"]
        if data.get("email"):
            user.email = data["email"]
        if data.get("username"):
            user.username = data["username"]
        
        else:
            return HttpResponse("Username dont provided")

        if data.get("password1") == data.get("password2") and data.get("password1") != "":
            user.password = data["password1"]
        else:
            return HttpResponse("Password do not match!")

        CustomUser.objects.create_user(
            username = user.username,
            email = user.email,
            password = user.password,
            first_name = user.first_name,
            last_name = user.last_name,
        )

        return redirect("/blog/")

    if request.method == "GET":
        return render(request, 'register_form.html')

def login_view(request):
    if request.method == "POST":
        data: dict = request.POST
        if not data.get("username"):
            return HttpResponse("Имя пользователя не указано")
        if not data.get("password"):
            return HttpResponse("Нету пароля")
        user = authenticate(
            request,
            username = data["username"],
            password = data["password"],
        )

        if user is not None:
            login(request, user)
            return redirect("/blog/")
        
        else:
            HttpResponse("Incorrect username or password!")
                    

    if request.method == "GET":
        return render(request, 'login.html')

def logout_view(request):
    if request.user:
        logout(request)
    return redirect("/blog/")

def profile_view(request):
    return render(request, 'profile.html')