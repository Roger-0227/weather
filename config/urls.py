from django.urls import path, include

urlpatterns = [
    path("", include("weather.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
