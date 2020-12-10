from django.urls import path

from application.hello import views
from application.hello.views import HelloView

urlpatterns = [
    path("", HelloView.as_view()),
    path("reset/", views.view_hello_reset),
]
