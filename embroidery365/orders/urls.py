from django.conf.urls import url

from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^$', views.orders_view, name='orders'),
    # url(r'^update_people/$', views.update_people_view, name='update_people'),
]
