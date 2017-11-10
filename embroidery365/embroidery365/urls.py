from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view, account_manager_view, update_account_view)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls'), name='home'),
    url(r'^products/', include('products.urls'), name='products'),
    url(r'^contact/', include('contact.urls'), name='contact'),
    url(r'^about/', include('about.urls'), name='about'),
    url(r'^orders/', include('orders.urls'), name='orders'),
    url(r'^builder/', include('builder.urls'), name='builder'),
    url(r'^cart/', include('cart.urls'), name='cart'),
    url(r'^dashboard/', include('admin_dashboard.urls'), name='dashboard'),
    url(r'^login/', login_view, name='login'),
    url(r'^myaccount/', account_manager_view, name='myaccount'),
    url(r'^update-info', update_account_view, name='update_info'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
