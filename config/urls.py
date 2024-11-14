from django.urls import include, path

urlpatterns = [
    path("", include("weather.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
