from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^robokassa/result/$', RobokassaResult),
    re_path(r'^robokassa/success/$', RobokassaSuccess),
    re_path(r'^robokassa/fail/$', RobokassaFail),
    re_path(r'^yandex/result/$', YandexResult),
    re_path(r'^yandex/success/$', YandexSuccess),
]