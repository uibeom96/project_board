from django.urls import path
from board import views


app_name = "board"

urlpatterns = [
    path("", views.board_list, name="board_list"),
    path("detail/<int:pk>/<str:slug>/", views.board_detail, name="board_detail"),
]