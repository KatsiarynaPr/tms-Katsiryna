from django.urls import path

from application.blog import views

urlpatterns = [
    path("", views.all_posts_view),
    path("new/", views.new_post_view),
    path("reset/", views.reset_post_view),
]
