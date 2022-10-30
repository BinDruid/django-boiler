from django.contrib import admin
from django.urls import path, include
from apps.common.views import handle_erro_404

handler404 = handle_erro_404

urlpatterns = [
    path("master/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += [
    path("accounts/", include("apps.account.urls")),
    path("", include("apps.common.urls")),
]
