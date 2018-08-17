from django.shortcuts import render
from Products.models import Product
from .models import CarouselImage
from SMTP.main import sendSupportMsg

def Index(request):
    devices = Product.objects.filter(bestOffer=True).order_by('?')
    carouselImg = CarouselImage.objects.all()
    return render(request, 'Main/Index.html', {'carouselImg': carouselImg, 'devices': devices})

def About(request):
    return render(request, 'Main/About.html')

def Support(request):
    return render(request, 'Main/Support.html')

def SupportAccept(request):
    if request.method == 'POST':
        email = request.POST['person_email']
        text = request.POST['text']
        sendSupportMsg(email, text)
    return render(request, 'Main/SupportAccept.html')


