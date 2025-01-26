from django.db import models

from apps.shared.abstract_base_model import AbstractBaseModel
from apps.news.models.crypto_tricker import CryptoTricker


class CryptoNews(AbstractBaseModel):
    class SENTIMENT_CHOICES(models.TextChoices):
        POSITIVE = "positive", "Positive"
        NEGATIVE = "negative", "Negative"
        NEUTRAL = "neutral", "Neutral"

    unique_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    source_url = models.URLField(max_length=2000)
    source_name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    published_at = models.DateTimeField()
    sentiment = models.CharField(max_length=20, choices=SENTIMENT_CHOICES)
    tickers = models.ManyToManyField(CryptoTricker, related_name="crypto_news_tickers")

    class Meta:
        db_table = "crypto_news"
        ordering = ["-published_at"]
        verbose_name_plural = "Crypto News"
