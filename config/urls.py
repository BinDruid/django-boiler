from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
