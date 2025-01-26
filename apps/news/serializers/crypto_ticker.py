from rest_framework import serializers

from apps.news.models import CryptoTricker


class CryptoTickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoTricker
        fields = "__all__"
