# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class BaseItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=255)
    base_item = models.ForeignKey(BaseItem)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=3)
    base_item = models.ForeignKey(BaseItem)

    def __str__(self):
        return "{0}-{1}".format(self.base_item.name, self.size)


class Placement(models.Model):
    position = models.CharField(max_length=255)
    base_item = models.ForeignKey(BaseItem)

    def __str__(self):
        return "{0}-{1}".format(self.base_item.name, self.position)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_base_item = models.CharField(max_length=255)
    order_style = models.CharField(max_length=255)
    order_logo = models.ImageField(blank=True)
    order_item_placement = models.CharField(max_length=255)
    order_logo_width = models.DecimalField(max_digits=10, decimal_places=2)
    order_logo_height = models.DecimalField(max_digits=10, decimal_places=2)
    order_details = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    extra_details = models.TextField(blank=True, null=True)
    logo_colors = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.customer, self.order_base_item, self.order_style)








