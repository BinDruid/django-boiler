from django.views.decorators.cache import cache_page
from django.urls import path
from .views import ViewHome


urlpatterns = [
    path("", ViewHome.as_view(), name="home"),
    # path("", cache_page(60 * 15)(ViewHome.as_view()), name="home"),
]
