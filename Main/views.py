from django.shortcuts import render
from Products.models import Product
from .models import CarouselImage, ServiceOrder, Budget
from SMTP.tasks import sendSupportMsg
from Molex.helper import checkReCaptcha

try:
    Budget._meta.verbose_name_plural = str(Budget.objects.all()[0])
except:
    pass

def Index(request):
    devices = Product.objects.filter(bestOffer=True).order_by('?')
    carouselImg = CarouselImage.objects.all()
    return render(request, 'Main/Index.html', {'carouselImg': carouselImg, 'devices': devices})

def About(request):
    return render(request, 'Main/About_v2.html')

def ServiceOrderView(request):
    if request.method == 'GET':
        service_type = 'pc'
        service_type_verbose = 'ПК'
        try:
            service_type = request.GET['type']
        except: pass
        return render(request, 'Main/ServiceOrder.html', {'service_type': service_type,
                                                          'service_type_verbose': service_type_verbose})

def ServiceOrderAccept(request):
    if request.method == 'POST':
        print(request.POST['type'])
        order = ServiceOrder(service_type=request.POST['type'], name=request.POST['name'],
                                            email=request.POST['email'], phone=request.POST['phone'],
                                            note=request.POST['note'])
        order.save()
        return render(request, 'Main/SupportAccept.html')

def Support(request):
    return render(request, 'Main/Support.html')

def SupportAccept(request):
    if request.method == 'POST':
        if checkReCaptcha(request.POST['g-recaptcha-response']):
            email = request.POST['person_email']
            text = request.POST['text']
            sendSupportMsg(email, text)
            return render(request, 'Main/SupportAccept.html')

def error_404(request):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')


