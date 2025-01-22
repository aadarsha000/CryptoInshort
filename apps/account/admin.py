from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apps.account.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ["-id"]
    list_display = [
        "id",
        "username",
        "email",
        "name",
        "is_verified",
        "subscription_status",
        "date_joined",
        "last_login",
    ]
    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            "other",
            {
                "fields": (
                    "is_subscribed",
                    "is_first_month",
                    "role",
                    "is_verified",
                    "is_connected_to_authenticator",
                    "qr_code",
                    "otp_base32",
                    "login_otp",
                    "subscription_status",
                    "case_insensitive_username",
                ),
            },
        ),
    )
