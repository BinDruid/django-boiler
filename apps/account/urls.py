from django.urls import path
from .views import ViewLogin

urlpatterns = [
    path("login/", ViewLogin.as_view(), name="login"),
]
