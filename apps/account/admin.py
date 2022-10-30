from django.contrib import admin
from .models import BasicUser
from django.contrib.auth.admin import UserAdmin


@admin.register(BasicUser)
class BasicUserAdmin(UserAdmin):
    model = BasicUser
    list_per_page = 15
    list_display = ["username", "is_superuser", "is_staff"]
