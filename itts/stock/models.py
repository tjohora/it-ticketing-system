from tokenize import ContStr
from django.db import models

# Create your models here.
class StockItem(models.Model):
    name = models.CharField(max_length=100)
    # barcode
    # stock_alert

class StockIn(models.Model):
    item = models.CharField(max_length=100)
    # supplier
    # quantity
    # daterecieved
    # created_by
    # cost
    # comment


class Stockout(models.Model):
    item = models.CharField(max_length=100)
    # supplier
    # quantity
    # daterecieved
    # created_by
    # cost
    # comment