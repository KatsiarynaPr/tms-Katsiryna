from django.urls import path

from application.landing.views import index

urlpatterns = [
    path("", index),
]
