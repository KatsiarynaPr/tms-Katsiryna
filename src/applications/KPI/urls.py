from django.http import HttpResponse
from django.urls import path
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from applications.blog.models import Post
from applications.KPI import views
from applications.KPI.apps import KPIConfig

app_name = KPIConfig.label


urlpatterns = [
    path("", views.AllKPIView.as_view(), name="allKPI"),
    path("quality/<int:pk>/", views.QualityKPIView.as_view(), name="qualityKPI"),
    path(
        "quality/<int:pk>/new/", views.NewQualityKPIView.as_view(), name="newqualityKPI"
    ),
    path("plan/<int:pk>/", views.PlanKPIView.as_view(), name="planKPI"),
    path("final/<int:pk>/", views.FinalKPIView.as_view(), name="finalKPI"),
    path("export/xls/", views.export_users_xls, name="export_users_xls"),
]
