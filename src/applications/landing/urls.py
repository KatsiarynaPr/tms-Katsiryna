from django.urls import path

from applications.landing.apps import LandingConfig
from applications.landing.views import IndexViex

app_name = LandingConfig.label

urlpatterns = [
    path("", IndexViex.as_view(), name="index"),
]
