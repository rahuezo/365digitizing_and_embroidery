# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cart.models import PlacedOrder, OrderItem

# Register your models here.

admin.site.register(PlacedOrder)
admin.site.register(OrderItem)
