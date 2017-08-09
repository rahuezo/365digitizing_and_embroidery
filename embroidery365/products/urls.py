from django.conf.urls import url

from . import views

app_name = 'products'

urlpatterns = [
    url(r'^$', views.products_view, name='products'),
    url(r'^shirts/', views.shirts_view, name='shirts'),
    url(r'^jackets/', views.jackets_view, name='jackets'),
    url(r'^hats/', views.hats_view, name='hats'),
    url(r'^backpacks/', views.backpacks_view, name='backpacks'),
    url(r'^custom_items/', views.custom_items_view, name='custom_items'),
]
