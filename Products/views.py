from django.shortcuts import render, redirect
from .helper import *
from .models import Order
from django.http import Http404
from SMTP.tasks import sendConfirmOrderMail
from Payment.helper import getYandexPaymentUrl
from SMS.tasks import sendConfirmOrderSMS
from Main.models import Budget

def CategoryView(request, hierarchy= None):
    device_list = None
    prop_form = {}
    category = getCategory(hierarchy)
    if request.method == "GET":
        for category_prop in category_prop_list:
            if category_prop == category.slug:
                prop_form = category_prop_list[category_prop]['prop_form']
                device_list = category_prop_list[category_prop]['model'].objects.filter(category__slug=category_prop)
                device_list = Filter(device_list, request, prop_form)

        return render(request, 'Products/Category.html', {'category': category,
                                                      'device_list': device_list,
                                                      'propForm': prop_form})


def ProductView(request, hierarchy=None, id=None):
    device = None
    id = int(id)
    prop_form = {}
    category = getCategory(hierarchy)
    for category_prop in category_prop_list:
        if category_prop == category.slug:
            prop_form = category_prop_list[category_prop]['prop_form']
            device = getDeviceById(category_prop_list[category_prop]['model'], id)
    return render(request, 'Products/Product.html', {'device': device, 'propForm': prop_form,
                                                     'category_prop': category_prop_list[category.slug]})

def CartView(request):
    device_list = getCartDevices(request.GET)
    return render(request, 'Products/Cart.html', {'device_list': device_list})

def OrderView(request):
    device_list = getCartDevices(request.GET)
    payment_amount = 0
    for device in device_list:
        payment_amount += device['fullPrice']
    budget = Budget.objects.all()[0].amount_of_budget
    if payment_amount > budget:
        return render(request, 'Products/Order.html', {'device_list': device_list, 'onlyPayment': True})
    else:
        return render(request, 'Products/Order.html', {'device_list': device_list, 'onlyPayment': False})

def OrderPaymentView(request):
    if request.method == 'POST':
        if checkReCaptcha(request.POST['g-recaptcha-response']):
            order = Order.objects.create(goods=request.POST['goods'], person_name=request.POST['person_name'],
                                         person_phone=request.POST['person_phone'],
                                         person_email=request.POST['person_email'],
                                         payment_amount=int(request.POST['payment_amount']),)
            order.save()
            #if order.person_email  != '':
            #    sendConfirmOrderMail()
            if request.POST['pay'] == 'True':
                return redirect(getYandexPaymentUrl(order))
            else:
                sendConfirmOrderMail.delay(userEmail=order.person_email, order_id=order.id)
                budget = Budget.objects.all()[0]
                budget.amount_of_budget -= order.payment_amount
                budget.save()
                #sendConfirmOrderSMS(order.id)
                return render(request, 'Products/OrderConfirm.html')
        else:
            return redirect('/')


def OrderListView(request):
    if request.user.is_superuser:
        order_list = []
        orders = Order.objects.all()
        for order in orders:
            json_devices = GETStringToJSON(order.goods)
            device_list = getCartDevices(json_devices)
            orderJSON = {}
            orderJSON['order'] = order
            orderJSON['devices'] = device_list
            order_list.append(orderJSON)
        return render(request, 'Products/OrderList.html', {'order_list': order_list})
    else:
        raise Http404



