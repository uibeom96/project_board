from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserForm, UserUpdateForm
from user.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseForbidden
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
    if request.method == "GET":     # 로그아웃 
        logout(request)
        return redirect("board:board_list")

    if request.method == "POST":    # 로그인
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect("board:board_list")
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')


def user_info(request, pk):
    user = get_object_or_404(User, id=pk)
    return render(request, "accounts/user_info.html", {"user": user}) 


def user_update(request, pk):
    if request.user.id == pk:
        user = get_object_or_404(User, id=pk)
        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect("accounts:user_info", request.user.pk)
        else:
            form = UserUpdateForm(instance=user)
        return render(request, "accounts/user_update.html", {"form":form})
    else:
        return HttpResponseForbidden()

def user_delete(request, pk):
    if request.user.id == pk:
        user = get_object_or_404(User, id=pk)
        if request.method == "POST":
            check = request.POST.get("delete_input")
            print(check)
            if check != "탈퇴하기":
                return HttpResponse("잘못된 타이핑입니다")
            user.delete()
            return redirect("board:board_list")
        return render(request, "accounts/user_delete.html", {"user": user})
    else:
        return HttpResponseForbidden()

def user_active(request, pk):
    if request.user.id == pk:
        user = get_object_or_404(User, id=pk)
        user.is_deleted = False
        user.deleted = None
        user.save()
        return redirect("board:board_list")
    else:
        return HttpResponseForbidden()

def target_user(request):
    if request.method == "GET":
        target_user = User.objects.filter(nick_name=request.GET.get("search_user"))
        if target_user:
            return render(request, "accounts/target_user.html", {"target_user": target_user[0]})
        else:
            return redirect("accounts:user_info", request.user.pk)
        