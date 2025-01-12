from django.db import models


class Item(models.Model):
    name = models.CharField(unique=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)


class Status(models.Model):
    name = models.CharField(unique=True) 


class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(Item, related_name='orders')
    total_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    