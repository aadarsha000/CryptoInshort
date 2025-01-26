from django.urls import path, include

from rest_framework import routers

from apps.news.views.crypto_news import CryptoNewsViewSet
from apps.news.views.crypto_tricker import CryptoTrickerViewSet


router = routers.DefaultRouter()
router.register("crypto-news", CryptoNewsViewSet, basename="crypto-news")
router.register("crypto-tricker", CryptoTrickerViewSet, basename="crypto-tricker")

urlpatterns = [
    path("", include(router.urls)),
]
