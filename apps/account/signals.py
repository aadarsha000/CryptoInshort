import pyotp
from io import BytesIO
import qrcode
from datetime import datetime, timezone

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.core.files.base import ContentFile

from apps.account.models import User


@receiver(post_save, sender=User)
def create_user_authenticator(sender, instance, created, **kwargs):
    if created:
        user = instance
        otp_base32 = pyotp.random_base32()
        email = instance.email
        otp_auth_url = pyotp.totp.TOTP(otp_base32).provisioning_uri(
            name=email.lower(), issuer_name="Crypto Inshort"
        )
        stream = BytesIO()
        image = qrcode.make(f"{otp_auth_url}")
        image.save(stream)
        user.qr_code = ContentFile(
            stream.getvalue(), name=f"qr{get_random_string(10)}.png"
        )
        user.otp_base32 = otp_base32
        totp = pyotp.TOTP(otp_base32).now()
        user.login_otp = totp
        user.otp_created_at = datetime.now(timezone.utc)
        user.save()
