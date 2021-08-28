

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todo/', include("Todo.urls")),
    path("", include("account.urls")),
]
#http://127.0.0.1:8000/Todo/
#http://127.0.0.1:8000/user_account/create_user_account/
#http://127.0.0.1:8000/upload/Image/
