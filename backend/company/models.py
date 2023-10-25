from django.db import models

from utils.models import CommonInfo


class CompanyModel(CommonInfo):
    company_id = models.CharField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.company_id

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "company"
