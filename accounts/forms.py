from django import forms
from user.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput)
    password2 = forms.CharField(label="패스워드 확인", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("nick_name", "username", "password", "password2")
        labels= {
            "nick_name": "닉네임"
            }
        
