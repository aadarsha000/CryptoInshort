from django.db import models
from apps.shared.abstract_base_model import AbstractBaseModel


class CryptoTricker(AbstractBaseModel):
    ticker = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "crypto_tricker"

    def __str__(self):
        return self.ticker
