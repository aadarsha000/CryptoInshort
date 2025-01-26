from django.contrib import admin
from apps.news.models import CryptoNews, CryptoTricker

# Register your models here.


@admin.register(CryptoNews)
class CryptoNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "sentiment")
    search_fields = ("title", "content", "summary")
    list_filter = ("sentiment",)
    date_hierarchy = "published_at"


@admin.register(CryptoTricker)
class CryptoTrickerAdmin(admin.ModelAdmin):
    list_display = ("ticker",)
    search_fields = ("ticker",)
    list_filter = ("ticker",)
    date_hierarchy = "created_at"
