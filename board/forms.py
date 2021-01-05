from django import forms
from board.models import Post

class PostCreate_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "display_avilable")