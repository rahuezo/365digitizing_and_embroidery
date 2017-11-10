from django.conf.urls import url

from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_view, name='cart'),
    url(r'^remove-from-cart/', views.remove_from_cart_view, name='remove_from_cart'),
    url(r'^checkout/', views.checkout_cart_view, name='checkout_cart'),
]
