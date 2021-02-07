import delorean
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Manager
from django.urls import reverse
from django.urls import reverse_lazy

User = get_user_model()


def _now():
    return delorean.utcnow().datetime


class PostManager(Manager):
    pass


month_list = (
    [1, "Январь"],
    [2, "Февраль"],
    [3, "Март"],
    [4, "Апрель"],
    [5, "Май"],
    [6, "Июнь"],
    [7, "Июль"],
    [8, "Август"],
    [9, "Сентябрь"],
    [10, "Октябрь"],
    [11, "Ноябрь"],
    [12, "Декабрь"],
)


class KPI(models.Model):
    objects = PostManager()
    employee = models.TextField(null=True, blank=True)
    position = models.TextField(null=True, blank=True)
    final_coefficient = models.IntegerField(default=0)
    plan_сoefficient = models.IntegerField(default=0)
    quality_сoefficient = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(2045)],
        help_text="Use the following format: <YYYY>",
    )
    month = models.TextField(null=True, blank=True)
    #month = models.IntegerField(choices=month_list, default=1)

    def get_absolute_url(self):
        return reverse("KPI", args=[str(self.id)])


class KPI_quality(models.Model):
    Number = models.TextField(null=True, blank=True)
    employee = models.TextField(null=True, blank=True)
    Assessment = models.IntegerField(default=0)
    quality_сoefficient = models.IntegerField(default=0)
    Total_assessment = models.IntegerField(default=0)
    Total_quality_сoefficient = models.IntegerField(default=0)
    Comments = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(2045)],
        help_text="Use the following format: <YYYY>",
    )
    month = models.TextField(null=True, blank=True)
