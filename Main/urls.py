from django.urls import path
from Main.views import Index, About

urlpatterns = [
    path('about/', About),
    path('', Index),

]