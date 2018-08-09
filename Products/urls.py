from django.urls import path, re_path
from .views import CategoryView, ProductView, CartView, OrderView

urlpatterns = [
    re_path(r'^order/$', OrderView, name='Order'),
    re_path(r'^cart/$', CartView, name='Cart'),
    re_path(r'^(?P<hierarchy>.+)/id/(?P<id>[0-9])/$', ProductView, name='Product'),
    re_path(r'^(?P<hierarchy>.+)/$', CategoryView, name='Category'),

]
