from django.shortcuts import render
from Products.models import Product
from .models import CarouselImage

def Index(request):
    devices = Product.objects.filter(bestOffer=True)
    carouselImg = CarouselImage.objects.all()
    return render(request, 'Main/Index.html', {'carouselImg': carouselImg, 'devices': devices})

def About(request):
    return render(request, 'Main/About.html')


