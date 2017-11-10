from django.conf.urls import url

from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    url(r'^$', views.dashboard_view, name='dashboard'),
    url(r'^update_status/', views.status_update_view, name='update_status'),
    url(r'^cancel_order/', views.cancel_order_view, name='cancel_order'),
    url(r'^restore_order/', views.restore_order_view, name='restore_order'),
    url(r'^delete_order/', views.delete_order_view, name='delete_order'),
]
