# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from builder.models import Order

import re


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        login(request, user)

        try:
            next_page = request.GET.get('next')
            return redirect(next_page)
        except:
            messages.add_message(request, messages.SUCCESS, 'Welcome, {0} {1}!'.format(user.first_name, user.last_name))
            return redirect('/home')

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        email = form.cleaned_data.get("email1")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")

        user.set_password(password)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        user.save()
        login(request, user)

        messages.add_message(request, messages.SUCCESS, 'Welcome, {0} {1}!'.format(user.first_name, user.last_name))
        return redirect('/home')

    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


@login_required(login_url='login')
def account_manager_view(request):
    current_user_pk = request.user.pk
    current_user = User.objects.get(pk=current_user_pk)
    orders = Order.objects.filter(customer__pk=current_user_pk)

    context = {
        'current_user': "{0} {1}".format(current_user.first_name, current_user.last_name),
        'nitems_in_cart': len(orders),
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }
    return render(request, "accounts/account_manager.html", context)


def validate_password(p):
    if re.findall("^[A-Za-z0-9_-]*$", p) and len(p) >= 6:
        return True
    return False


@login_required(login_url='login')
def update_account_view(request):
    first_name = request.POST.get('first-name')
    last_name = request.POST.get('last-name')
    email = request.POST.get('email')

    current_password = request.POST.get('current-password')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    new_user = User.objects.get(username=request.user.username)

    if current_password:
        if authenticate(username=request.user.username, password=current_password):
            if current_password == password1 == password2:
                messages.error(request,
                               "The new password must be different than the old one!",
                               extra_tags="invalid_password")
            elif password1 == password2 and validate_password(password1):
                new_user.set_password(password1)
            elif password1 == password2 and validate_password(password1) == False:
                messages.error(request,
                               "Passwords must be longer or equal to 6 characters and contain at least one letter!",
                               extra_tags="invalid_password")
            else:
                messages.error(request,
                               "Passwords don't match!",
                               extra_tags="invalid_password")
        else:
            messages.error(request,
                           "Invalid credentials!",
                           extra_tags="invalid_password")

    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.email = email

    new_user.save()

    messages.success(request, "Changes saved successfully!")
    return redirect('/myaccount')


def logout_view(request):
    logout(request)

    context = {
        'logout_message': "You have successfully logged out!",
    }
    return render(request, "home/index.html", context)

