from rest_framework import serializers

from apps.news.models import CryptoNews
from apps.news.serializers.crypto_ticker import CryptoTickerSerializer


class CryptoNewsSerializer(serializers.ModelSerializer):
    trickers = CryptoTickerSerializer(many=True, read_only=True)

    class Meta:
        model = CryptoNews
        fields = "__all__"
