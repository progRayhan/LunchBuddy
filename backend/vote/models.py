from django.db import models

from menu.models import MenuModel
from utils.models import TimeStamp
from utils.utils import PHONE_REGEX


class VoteModel(TimeStamp):
    menu = models.ForeignKey(MenuModel, on_delete=models.DO_NOTHING)
    vote = models.BooleanField(default=False)
    employee_phone_number = models.CharField(validators=[PHONE_REGEX], max_length=11)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
        db_table = "vote"
