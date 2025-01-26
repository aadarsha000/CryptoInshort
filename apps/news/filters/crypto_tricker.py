import django_filters

from django.db import models

from apps.news.models import CryptoTricker


class CryptoTrickerFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
    )

    class Meta:
        model = CryptoTricker
        fields = {
            "ticker": ["icontains"],
        }

    def filter_search(self, queryset, name, value):
        return queryset.filter(models.Q(ticker__icontains=value))
