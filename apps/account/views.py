from django.contrib.auth import views as auth_views
from .forms import LoginForm


class ViewLogin(auth_views.LoginView):
    template_name = "login.html"
    form_class = LoginForm
