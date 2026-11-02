from django.urls import path

from .views import SearchView, health

urlpatterns = [
    path("health", health),
    path("search", SearchView.as_view()),
]
