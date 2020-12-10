from django.urls import path

from application.landing.views import IndexViex

urlpatterns = [
    path("", IndexViex.as_view()),
]
