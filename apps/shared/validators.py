import re

from django.core.exceptions import ValidationError
from django.utils import timezone as tz


def validate_date_in_future(value):
    if value < tz.now().date():
        raise ValidationError("date is in the past")


def validate_hex_color(value):
    pattern = r'^#(?:[0-9a-fA-F]{3,4}){1,2}$'
    if not re.match(pattern, value):
        raise ValidationError("Invalid hex color code.")
