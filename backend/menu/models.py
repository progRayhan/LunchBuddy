from django.db import models

from restaurant.models import RestaurantModel
from utils.models import TimeStamp


class MenuModel(TimeStamp):
    item_id = models.CharField(max_length=255, unique=True)
    food_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    vote_count = models.PositiveIntegerField(default=0)
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        db_table = "menu"
