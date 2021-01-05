from django.shortcuts import render, get_object_or_404, redirect
from board.models import Post
from django.core.paginator import Paginator
from datetime import timezone
from board.forms import PostCreate_Form

def board_list(request):
    page = request.GET.get("page", 1)
    post_list = Post.objects.filter(is_deleted=False, display_avilable=False)
    page_count = Paginator(post_list , 5)
    page_obj = page_count.get_page(page)

    if request.method == "GET":
        search_input = request.GET.get("search_input")
        if search_input is not None:
            post_list = Post.objects.filter(is_deleted=False, display_avilable=False, title__icontains=search_input)
            page_count = Paginator(post_list, 5)
            page_obj = page_count.get_page(page)
    
    return render(request, "board/board_list.html", {"post_list": page_obj})


def board_create(request):
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


def board_detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    return render(request, "board/board_detail.html", {"post": post})





