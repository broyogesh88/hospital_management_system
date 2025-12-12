from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # redirect "/" → "/hospitals/dashboard/"
    path("", lambda request: redirect("hospitals/dashboard/")),

    # include all hospital routes
    path("hospitals/", include("hospitals.urls")),
]
