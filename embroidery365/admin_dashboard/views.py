# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cart.models import PlacedOrder, OrderItem
from builder.models import Order

from datetime import datetime
from builder.models import Order


@login_required(login_url='login')
def dashboard_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            order_number = request.POST.get('order-number-filter')
            placed_orders = PlacedOrder.objects.filter(order_number=order_number)
            filtered = True
        else:
            placed_orders = PlacedOrder.objects.all()
            filtered = False

        customers = map(lambda x: x.customer, placed_orders)

        print "TOTAL ORDERS: ", len(placed_orders)
        orders_per_customer = {}

        for customer in customers:
            orders_per_customer[customer] = placed_orders.order_by('-created').filter(customer=customer)

        current_user_pk = request.user.pk
        current_user = User.objects.get(pk=current_user_pk)

        context = {
            'placed_orders': orders_per_customer,
            'current_user': "{0} {1}".format(current_user.first_name, current_user.last_name),
        }

        if filtered:
            context.update({'filtered_query':order_number})
        return render(request, 'admin_dashboard/dashboard.html', context)
    else:
        return redirect('home:index')


@login_required(login_url='login')
def status_update_view(request):
    order_id = request.POST.get('order-id')
    status_choice = request.POST.get('status-choice')

    current_order = PlacedOrder.objects.get(pk=order_id)

    current_order.status = int(status_choice)
    current_order.save()

    return redirect('/dashboard')


@login_required(login_url='login')
def cancel_order_view(request):
    order_id = request.POST.get('order-id')

    current_order = PlacedOrder.objects.get(pk=order_id)

    current_order.active = False
    current_order.save()

    return redirect('/dashboard')


@login_required(login_url='login')
def restore_order_view(request):
    order_id = request.POST.get('order-id')

    current_order = PlacedOrder.objects.get(pk=order_id)

    current_order.active = True
    current_order.save()

    return redirect('/dashboard')


@login_required(login_url='login')
def delete_order_view(request):
    order_id = request.POST.get('order-id')

    current_order = PlacedOrder.objects.get(pk=order_id)

    current_order.delete()

    return redirect('/dashboard')





