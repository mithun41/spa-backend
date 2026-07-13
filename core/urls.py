from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# JWT এর জন্য এই দুইটা ইম্পোর্ট লাগবে
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ChangePasswordView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vipspa/", include("vipspa.urls")),
    path("api/redlightspa/", include("redlightspa.urls")),
    path("api/elitespa/", include("elitespa.urls")),
    # লগইন করার জন্য এই রুটগুলো যোগ করুন
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/change-password/", ChangePasswordView.as_view(), name="change_password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
