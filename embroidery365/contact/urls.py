from django.conf.urls import url

from . import views

app_name = 'contact'

urlpatterns = [
    url(r'^$', views.contact_view, name='contact'),
    # url(r'^update_people/$', views.update_people_view, name='update_people'),
]
