import delorean
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.urls import reverse_lazy

User = get_user_model()


def _now():
    return delorean.utcnow().datetime


class Post(models.Model):
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    nr_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=_now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
