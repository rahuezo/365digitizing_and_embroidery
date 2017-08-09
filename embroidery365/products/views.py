# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User


def products_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/products.html', context)


def shirts_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/shirts.html', context)


def jackets_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/jackets.html', context)


def hats_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/hats.html', context)


def backpacks_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/backpacks.html', context)


def custom_items_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'products/custom.html', context)