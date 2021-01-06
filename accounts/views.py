from django.shortcuts import render, redirect
from accounts.forms import UserForm
from user.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.serializer import Accounts_Serializer


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            del(form.cleaned_data["password2"])
            User.objects.create_user(**form.cleaned_data)
            return redirect("board:board_list")
    else:
        form = UserForm()
    return render(request, "accounts/signup.html", {"form": form})

    

@api_view(["GET", "POST"])
def user_manager(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = Accounts_Serializer(users, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect("board:board_list")
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')

        