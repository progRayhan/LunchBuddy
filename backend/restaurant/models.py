from django.db import models

from utils.models import CommonInfo
from utils.utils import PHONE_REGEX


class RestaurantModel(CommonInfo):
    restaurant_id = models.CharField(max_length=255, unique=True)
    restaurant_name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True
    )
    location_latitude = models.FloatField(null=True, blank=True)
    location_longitude = models.FloatField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        db_table = "restaurant"
