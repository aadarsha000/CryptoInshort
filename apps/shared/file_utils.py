import os
import uuid

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(
                f"File size must be less than {self.size_to_human_readable(self.max_size)}"
            )

    @staticmethod
    def size_to_human_readable(size_in_bytes):
        for x in ["bytes", "KB", "MB", "GB", "TB"]:
            if size_in_bytes < 1024.0:
                return "%3.1f %s" % (size_in_bytes, x)
            size_in_bytes /= 1024.0


def file_upload_path(instance, filename):
    if hasattr(instance, "tenant") and instance.tenant:
        _, file_extension = os.path.splitext(filename)
        return f"{instance._meta.model_name}/{instance.tenant.id}/{uuid.uuid4()}{file_extension}"
    else:
        _, file_extension = os.path.splitext(filename)
        return f"{instance._meta.model_name}/main/{uuid.uuid4()}{file_extension}"


def validate_one_mb_image_size(image):
    file_size = image.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max allowed size of image is %s MB" % limit_mb)


def validate_five_mb_image_size(image):
    file_size = image.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max allowed size of image is %s MB" % limit_mb)


def validate_twenty_mb_file_size(file):
    file_size = file.size
    limit_mb = 20
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max allowed size of file is %s MB" % limit_mb)


def validate_book_file_size(file):
    file_size = file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max allowed size of file is %s MB" % limit_mb)
