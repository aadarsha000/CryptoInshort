from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.news.models import CryptoNews
from apps.news.serializers.crypto_news import CryptoNewsSerializer
from apps.news.filters.crypto_news import CryptoNewsFilter
from apps.shared.custom_response import FailedResponse, SuccessResponse


class CryptoNewsViewSet(ReadOnlyModelViewSet):
    queryset = CryptoNews.objects.all()
    serializer_class = CryptoNewsSerializer
    filterset_class = CryptoNewsFilter

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
