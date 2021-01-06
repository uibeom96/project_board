from django.shortcuts import render, get_object_or_404, redirect
from board.models import Post
from django.core.paginator import Paginator
from datetime import timezone
from board.forms import PostCreate_Form
from django.http import HttpResponseForbidden, HttpResponse


def board_list(request):
    page = request.GET.get("page", 1)
    post_list = Post.objects.filter(is_deleted=False, display_avilable=False).select_related("author")
    page_count = Paginator(post_list , 8)
    page_obj = page_count.get_page(page)

    if request.method == "GET":
        search_input = request.GET.get("search_input")
        if search_input is not None:
            post_list = Post.objects.filter(is_deleted=False, display_avilable=False, title__icontains=search_input).select_related("author")
            page_count = Paginator(post_list, 8)
            page_obj = page_count.get_page(page)
    
    return render(request, "board/board_list.html", {"post_list": page_obj})


def board_create(request):
    if request.user.is_deleted == False:
        if request.method == "POST":
            form = PostCreate_Form(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = form.cleaned_data.get("title")
                post.save()
                return redirect(Post.get_absolute_url(post))
        else:
            form = PostCreate_Form()
        return render(request, "board/board_create.html", {"form": form})
    else:
        return HttpResponseForbidden


def board_update(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    if request.user == post.author:
        if request.method == "POST":
            form = PostCreate_Form(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = form.cleaned_data.get("title")
                post.save()
                return redirect(Post.get_absolute_url(post))
        else:
            form = PostCreate_Form(instance=post)
        return render(request, "board/board_create.html", {"form": form})
    else:
        return HttpResponseForbidden()


def board_detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    return render(request, "board/board_detail.html", {"post": post})


def board_delete(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    if request.user == post.author:
        post.delete()
        return redirect("board:board_list")
    else:
        return HttpResponseForbidden()



def board_likes(request):
    if request.is_ajax():
        post_id = request.GET.get("post_id")
        post = Post.objects.get(id=post_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세욥"
            context = {"like_count": post.like.count(), "message": message}
            return http