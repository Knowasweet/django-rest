from django.urls import path, include

urlpatterns = [
    path("users/", include("users.urls")),
    path("persons/", include("film_crews.urls.person")),
    path("categories/", include("film_crews.urls.category")),
]

