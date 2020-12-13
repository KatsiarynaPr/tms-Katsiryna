from django.urls import path

from applications.hello import views
from applications.hello.views import HelloView

urlpatterns = [
    path("", HelloView.as_view()),
    path("reset/", views.view_hello_reset),
]
