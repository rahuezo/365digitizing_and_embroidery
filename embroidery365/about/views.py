# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from builder.models import Order


def about_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        current_user_pk = request.user.pk
        orders = Order.objects.filter(customer__pk=current_user_pk)

        context = {
            'current_user': current_user,
            'nitems_in_cart': len(orders),
        }
    except:
        context = {}

    return render(request, 'about/about.html', context)
