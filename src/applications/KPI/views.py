from typing import Dict
from django_filters.rest_framework import DjangoFilterBackend
from service

import xlwt
from django import forms
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic import ListView

from applications.KPI.models import KPI


class AllKPIView(ListView):
    template_name = "KPI/KPI.html"
    model = KPI
    filter_backend = (DjangoFilterBackend,)

    def get_extended_context(self) -> Dict:
        context = {"form": KPIForm()}
        return context


class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ["employee"]
        widgets = {"employee": forms.Textarea(attrs={"rows": 2})}


class QualityKPIView(ListView):
    template_name = "KPI/quality_сoefficient.html"
    model = KPI

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)


class NewQualityKPIView(CreateView):
    model = KPI
    fields = ["Number", "Assessment", "quality_сoefficient", "Comments"]
    success_url = "/KPI/"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user

        return super().form_valid(form)


class PlanKPIView(ListView):
    template_name = "KPI/plan.html"
    model = KPI

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)


class FinalKPIView(ListView):
    template_name = "KPI/final.html"
    model = KPI

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)


def export_users_xls(_request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="KPI.xls"'

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("KPI")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        "Сотрудник",
        "Должность",
        "Итоговый коэффициент",
        "План",
        "Оценка",
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = KPI.objects.all().values_list(
        "employee",
        "position",
        "final_coefficient",
        "plan_сoefficient",
        "quality_сoefficient",
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
