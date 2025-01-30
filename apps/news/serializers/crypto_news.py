from rest_framework import serializers

from apps.news.models import CryptoNews
from apps.news.serializers.crypto_ticker import CryptoTickerSerializer


class CryptoNewsSerializer(serializers.ModelSerializer):
    tickers = CryptoTickerSerializer(many=True, read_only=True)

    class Meta:
        model = CryptoNews
        fields = [
            "id",
            "title",
            "content",
            "summary",
            "source_url",
            "source_name",
            "image_url",
            "published_at",
            "sentiment",
            "tickers",
        ]
