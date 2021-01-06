from django.urls import path 
from accounts import views
from django.contrib.auth import views as auth_view


app_name = "accounts"

urlpatterns =  [
    path("signup/", views.signup, name="signup"),
    path("signin/", auth_view.LoginView.as_view(template_name="accounts/signin.html"), name="signin"),
    path("signout/", auth_view.LogoutView.as_view(), name="signout"),
    path("login_list/", views.user_manager, name="user_manager"),
]
