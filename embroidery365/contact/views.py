# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User


def contact_view(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        print "Current User", current_user
        context = {
            'current_user': current_user,
        }
    except:
        context = {}

    return render(request, 'contact/contact.html', context)
