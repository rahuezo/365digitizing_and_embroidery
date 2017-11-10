# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import BaseItem, Order
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup as BS


@login_required(login_url='login')
def builder_view(request):
    styles = {}
    sizes = {}
    placements = {}

    for item in BaseItem.objects.all():
        styles[item.name] = [str(s.name) for s in item.style_set.all()]
        sizes[item.name] = [str(s.size) for s in item.size_set.all()]
        placements[item.name] = [str(p.position) for p in item.placement_set.all()]

    try:
        user_object = User.objects.get(username=request.user.username)
        current_user = "{0} {1}".format(user_object.first_name, user_object.last_name)

        current_user_pk = request.user.pk
        orders = Order.objects.filter(customer__pk=current_user_pk)

        context = {
            'current_user': current_user,
            'base_items': BaseItem.objects.all(),
            'styles': styles,
            'sizes': sizes,
            'placements': placements,
            'nitems_in_cart': len(orders),
        }
    except:
        context = {
            'base_items': BaseItem.objects.all(),
            'styles': styles,
            'sizes': sizes,
            'placements': placements,
        }

    return render(request, 'builder/builder.html', context)


@login_required(login_url='login')
def add_to_cart(request):
    if request.method == 'POST' and request.FILES['item-logo-input']:
        base_item = request.POST.get('item-select')
        style = request.POST.get('item-style-select')
        item_logo = request.FILES['item-logo-input']
        item_logo_placement = request.POST.get('item-placement-select')
        item_logo_width = request.POST.get('logo-width')
        item_logo_height = request.POST.get('logo-height')
        details = request.POST.get('order-details')
        order_total = request.POST.get('order-total')
        extra_details = request.POST.get('extra-info')

        current_customer = User.objects.all().get(pk=request.user.pk)

        new_order = Order(customer=current_customer, order_base_item=base_item,
                          order_style=style, order_logo=item_logo, order_item_placement=item_logo_placement,
                          order_logo_width=item_logo_width, order_logo_height=item_logo_height,
                          order_details=get_table_details(details), extra_details=extra_details, total=order_total)

        fs = FileSystemStorage()

        fs.save(item_logo.name, item_logo)

        new_order.save()

        return redirect('/cart')

    return render(request, 'builder/builder.html')


def get_table_details(table):
    soup = BS(table, 'html.parser')

    html = """
    <div class="row">
        <div class="col-lg-12">
        <table class="table">
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>
        </table>
        </div>
    </div>
    """
    return '<br>'.join([html.format(tr.find_all('td')[0], tr.find_all('td')[1], tr.find_all('td')[2],
                                    tr.find_all('td')[3]) for tr in soup.find_all('tr')[1:]])







