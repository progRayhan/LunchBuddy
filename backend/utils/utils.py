from django.core.validators import RegexValidator

from rest_framework.pagination import PageNumberPagination

PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)


class CustomPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
