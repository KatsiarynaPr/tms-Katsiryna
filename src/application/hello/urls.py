
from django.urls import path

from application.hello.views import hello

urlpatterns = [
    path("", hello),
]