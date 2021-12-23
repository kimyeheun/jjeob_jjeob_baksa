from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Account
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
        
    return render(request, "USER/login.html")

def logout_view(request):
    logout(request)
    return redirect("USER:login")

def signup_view(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        user_email = request.POST["user_email"]
        user_nick = request.POST["user_nick"]

        user = Account.objects.create(user_name, user_email, password)
        user.user_id = user_id
        user.user_nick = user_nick
        user.save()
        return redirect("USER:login")

    return render(request, "USER/signup.html")