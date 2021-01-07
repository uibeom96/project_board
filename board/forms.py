from django import forms
from board.models import Post, Comment

class PostCreate_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "display_avilable")


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", )