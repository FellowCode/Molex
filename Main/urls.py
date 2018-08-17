from django.urls import path
from Main.views import Index, About, Support, SupportAccept

urlpatterns = [
    path('about/', About),
    path('support/accept/', SupportAccept),
    path('support/', Support),
    path('', Index),
]