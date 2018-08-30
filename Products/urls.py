from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^orders/$', OrderListView, name='OrderList'),
    re_path(r'^order/confirm/$', OrderPaymentView, name='OrderConfirm'),
    re_path(r'^order/$', OrderView, name='Order'),
    re_path(r'^cart/$', CartView, name='Cart'),
    re_path(r'^(?P<hierarchy>.+)/id/(?P<id>.+)/copy/$', CopyProduct),
    re_path(r'^(?P<hierarchy>.+)/id/(?P<id>.+)/$', ProductView, name='Product'),
    re_path(r'^(?P<hierarchy>.+)/$', CategoryView, name='Category'),

]
