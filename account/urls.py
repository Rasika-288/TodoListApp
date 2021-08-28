from .views import create_user_account, sign_in_user, logout_user
from django.urls import path

urlpatterns = [
    path("create_user_account/", create_user_account, name='create_user_account'),
    path("", sign_in_user, name="login"),
    path("logout_user/", logout_user, name="logout_user"),

]