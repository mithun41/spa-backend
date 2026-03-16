from django.urls import path
from .views import homepage_view

urlpatterns = [
    path("homepage/", homepage_view, name="homepage"),
]