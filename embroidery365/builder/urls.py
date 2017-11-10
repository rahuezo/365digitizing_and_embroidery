from django.conf.urls import url

from . import views

app_name = 'builder'

urlpatterns = [
    url(r'^$', views.builder_view, name='builder'),
    url(r'^add-to-cart/', views.add_to_cart, name='add_to_cart'),
    # url(r'^update_people/$', views.update_people_view, name='update_people'),
]
