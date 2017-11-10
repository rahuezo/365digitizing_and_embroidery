# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import BaseItem, Style, Size, Placement, Order  # HatStyle, ShirtStyle, JacketStyle,

# Register your models here.

# admin.site.register(HatStyle)
# admin.site.register(ShirtStyle)
# admin.site.register(JacketStyle)

admin.site.register(BaseItem)
admin.site.register(Style)
admin.site.register(Size)
admin.site.register(Placement)
admin.site.register(Order)

# admin.site.register(Hat)
# admin.site.register(Jacket)

