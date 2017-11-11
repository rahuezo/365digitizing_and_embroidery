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
def cart_view(request):
    current_user_pk = request.user.pk
    orders = Order.objects.filter(customer__pk=current_user_pk)

    current_user = User.objects.get(pk=current_user_pk)

    context = {
        'all_orders': orders,
        'current_user': "{0} {1}".format(current_user.first_name, current_user.last_name),
        'nitems_in_cart': len(orders),
        'cart_total': sum([i.total for i in orders])
    }
    return render(request, 'cart/cart.html', context)


@login_required(login_url='login')
def remove_from_cart_view(request):
    item_to_remove = request.POST.get('item-to-remove')

    order_to_remove = Order.objects.get(pk=item_to_remove)
    order_to_remove.delete()

    return redirect('/cart')


@login_required(login_url='login')
def checkout_cart_view(request):
    current_user_pk = request.user.pk
    orders = Order.objects.filter(customer__pk=current_user_pk)

    user = User.objects.get(pk=current_user_pk)

    total = sum([o.total for o in orders])

    placed_order_object = PlacedOrder(customer=user, order_number=make_unique_order_number(request), total=total)
    placed_order_object.save()

    for order in orders:
        noi = OrderItem(placed_order=placed_order_object, customer=order.customer, order_base_item=order.order_base_item,
                        order_style=order.order_style, order_logo=order.order_logo,
                        order_item_placement=order.order_item_placement, order_logo_width=order.order_logo_width,
                        order_logo_height=order.order_logo_height, order_details=order.order_details,
                        total=order.total, extra_details=order.extra_details,
                        logo_colors=order.logo_colors, created=order.created
                        )
        noi.save()

        order.delete()

    return redirect('/orders')


def make_unique_order_number(request):
    ext = request.user.first_name[0] + request.user.last_name[0]
    return ext.upper() + datetime.now().strftime('%m%d%y%H%M%S')



