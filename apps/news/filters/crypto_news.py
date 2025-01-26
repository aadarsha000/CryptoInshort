import django_filters

from django.db import models

from apps.news.models import CryptoNews


class CryptoNewsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
    )

    class Meta:
        model = CryptoNews
        fields = {
            "title": ["icontains"],
            "published_at": ["gte", "lte", "exact"],
            "tickers": ["exact"],
            "sentiment": ["exact"],
        }

    def filter_search(self, queryset, name, value):
        return queryset.filter(models.Q(title__icontains=value))
