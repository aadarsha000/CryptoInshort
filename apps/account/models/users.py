import uuid
import pyotp

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from apps.shared.file_utils import file_upload_path, validate_one_mb_image_size


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    class SubscriptionStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        REGISTERED = "registered", "Registered"

    role = models.CharField(max_length=5, choices=Roles.choices, default=Roles.USER)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    user_uuid = models.UUIDField(default=uuid.uuid4)
    avatar = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_one_mb_image_size],
        blank=True,
        null=True,
    )
    country = models.CharField(max_length=255, null=True)
    referred_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_referred_by",
    )
    otpauth_url = models.CharField(max_length=225, blank=True, null=True)
    otp_base32 = models.CharField(max_length=255, null=True)
    qr_code = models.ImageField(upload_to="user/qr_code/", blank=True, null=True)
    login_otp = models.CharField(max_length=255, null=True, blank=True)
    login_otp_used = models.BooleanField(default=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    is_connected_to_authenticator = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_first_month = models.BooleanField(default=True)
    subscription_status = models.CharField(
        max_length=50,
        choices=SubscriptionStatus.choices,
        default=SubscriptionStatus.REGISTERED,
    )
    case_insensitive_username = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "users"
        constraints = [
            UniqueConstraint(
                Lower("case_insensitive_username"), name="unique_lower_name"
            )
        ]

    def is_valid_otp(self, otp):
        totp = pyotp.TOTP(self.otp_base32)
        return totp.verify(otp, valid_window=1) and not self.login_otp_used
