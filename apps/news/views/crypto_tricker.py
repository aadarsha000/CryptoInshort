from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.news.models import CryptoTricker
from apps.news.serializers.crypto_ticker import CryptoTickerSerializer
from apps.news.filters.crypto_tricker import CryptoTrickerFilter
from apps.shared.custom_response import FailedResponse, SuccessResponse


class CryptoTrickerViewSet(ReadOnlyModelViewSet):
    queryset = CryptoTricker.objects.all()
    serializer_class = CryptoTickerSerializer
    filterset_class = CryptoTrickerFilter

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return FailedResponse(message=str(e))

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return FailedResponse(message=str(e))
