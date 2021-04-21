from django.contrib import admin
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'panel/',
        views.HomePage.as_view(),
        name = "panel"
    ),
]
