from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator



# Create your views here.
def board_list(request):
    page = request.GET.get("page", 1)

    post_list = Post.objects.filter(is_deleted=False, display_avilable=False)

    
    page_count = Paginator(post_list , 5)
    page_obj = page_count.get_page(page)


    return render(request, "board/board_list.html", {"post_list": page_obj})


