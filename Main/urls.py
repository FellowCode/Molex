from django.urls import path
from Main.views import Index, About, ServiceOrderView, ServiceOrderAccept, Support, SupportAccept

urlpatterns = [
    path('about/', About),
    path('support/accept/', SupportAccept),
    path('support/', Support),
    path('serviceorder/accept/', ServiceOrderAccept),
    path('serviceorder/', ServiceOrderView),
    path('', Index),
]

