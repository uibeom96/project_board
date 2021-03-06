from django.urls import path
from board import views


app_name = "board"

urlpatterns = [
    path("", views.board_list, name="board_list"),
    path("my/post/<int:pk>/", views.board_list, name="board_mypost"),
    path("my/like/post/<int:pk>/", views.board_like_list, name="board_like_list"),
    path("my/dislike/post/<int:pk>/", views.board_dislike_list, name="board_dislike_list"),
    path("create/", views.board_create, name="board_create"),
    path("detail/<int:pk>/<str:slug>/", views.board_detail, name="board_detail"),
    path("update/<int:pk>/<str:slug>/", views.board_update, name="board_update"),
    path("delete/<int:pk>/<str:slug>/", views.board_delete, name="board_delete"),
    path("post/likes/", views.board_likes, name="board_likes"),
    path("post/dislikes/", views.board_dis_likes, name="board_dis_likes"),
]