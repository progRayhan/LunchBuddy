from django.db import models

from restaurant.models import RestaurantModel
from utils.models import TimeStamp


class WinnerRestaurantModel(TimeStamp):
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Winner Restaurant"
        verbose_name = "Winner Restaurants"
        db_table = "winner_restaurant"
