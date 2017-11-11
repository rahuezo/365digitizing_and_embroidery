# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from builder.models import Order
from django.utils import timezone


class PlacedOrder(models.Model):
    customer = models.ForeignKey(User, default=1)
    order_number = models.CharField(max_length=255, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2) #models.FloatField(default=0.0)
    created = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{0} {1}: #{2}".format(self.customer.first_name, self.customer.last_name, self.order_number)


class OrderItem(models.Model):
    placed_order = models.ForeignKey(PlacedOrder, on_delete=models.CASCADE)

    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    order_base_item = models.CharField(max_length=255, default='')
    order_style = models.CharField(max_length=255, default='')
    order_logo = models.ImageField(blank=True)
    order_item_placement = models.CharField(max_length=255, default='')
    order_logo_width = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    order_logo_height = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    order_details = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    extra_details = models.TextField(blank=True, null=True)
    logo_colors = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.customer, self.order_base_item, self.order_style)
