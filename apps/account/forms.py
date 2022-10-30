from django.contrib.auth.forms import AuthenticationForm
from .models import BasicUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-controll"}
        self.fields["username"].label = "نام کاربری"
        self.fields["password"].label = "رمز عبور"

    class Meta:
        model = BasicUser
