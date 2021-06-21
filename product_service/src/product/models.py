from django.db import models
from django.db.models.base import Model

# Create your models here.


class Inventory(models.Model):
    product_name = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    shop_name = models.CharField(max_length=256)
    qty_available = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product_name + '_' + self.shop_name + '_' + self.user_id
