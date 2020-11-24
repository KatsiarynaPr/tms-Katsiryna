from django.urls import path

from application.hello import views

urlpatterns = [
    path("", views.hello),
    path("greet/", views.view_hello_greet),
    path("reset/", views.view_hello_reset),
]
