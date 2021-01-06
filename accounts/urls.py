from django.urls import path 
from accounts import views
from django.contrib.auth import views as auth_view


app_name = "accounts"

urlpatterns =  [
    path("signup/", views.signup, name="signup"),
    path("signin/", auth_view.LoginView.as_view(template_name="accounts/signin.html"), name="signin"),
    path("signout/", views.user_manager, name="signout"),
    path("login_list/", views.user_manager, name="user_manager"),
    path("user/info/<int:pk>/", views.user_info, name="user_info"),
    path("user/update/<int:pk>/", views.user_update, name="user_update"),
    path("user/delete/<int:pk>/", views.user_delete, name="user_delete"),
    path("user/active/<int:pk>/", views.user_active, name="user_active"),
    path("target_user/info/", views.target_user, name="target_user"),
]
