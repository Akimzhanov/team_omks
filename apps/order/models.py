from django.db import models
from django.contrib.auth import get_user_model
from apps.smartphones.models import Smartphone
from apps.travel.models import Travel

User = get_user_model()

class Order(models.Model):
    
    user = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='orders'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    card = models.BigIntegerField()
    product = models.ManyToManyField(
        to=Smartphone,
        through='OrderItems'
    )
    total_sum = models.DecimalField(max_digits=14, decimal_places=2, default=0)


class OrderItems(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.RESTRICT,
        related_name='items'
    )
    product = models.ForeignKey(
        to=Smartphone,
        on_delete=models.RESTRICT,
        related_name='items'
    )
    quantity = models.PositiveIntegerField(default=1)





class OrderTravel(models.Model):
    
    user = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='ordertravels'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    card = models.BigIntegerField()
    product = models.ManyToManyField(
        to=Travel,
        through='OrderItemsTravel'
    )
    total_sum = models.DecimalField(max_digits=14, decimal_places=2, default=0)


class OrderItemsTravel(models.Model):
    order = models.ForeignKey(
        to=OrderTravel,
        on_delete=models.RESTRICT,
        related_name='travelitems'
    )
    product = models.ForeignKey(
        to=Travel,
        on_delete=models.RESTRICT,
        related_name='travelitems'
    )
    quantity = models.PositiveIntegerField(default=1)




    