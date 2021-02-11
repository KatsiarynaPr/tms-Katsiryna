from django_filters import rest_framework as filters

from applications.KPI.models import KPI


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class KPIFilter(filters.FilterSet):
    month = CharFilterInFilter(field_name="month", lookup_expr="in")
    year = filters.RangeFilter()

    class Meta:
        model = KPI
        fields = ["month", "year"]
