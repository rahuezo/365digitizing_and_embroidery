from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls'), name='home'),
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^contact/', include('contact.urls'), name='contact'),
    url(r'^about/', include('about.urls'), name='about'),
    url(r'^orders/', include('orders.urls'), name='orders'),
    url(r'^builder/', include('builder.urls'), name='builder'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),

]
