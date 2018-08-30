from django.shortcuts import render, redirect
from .helper import *
from .models import Order
from django.http import Http404
from SMTP.tasks import sendConfirmOrderMail
from Payment.helper import getYandexPaymentUrl
from SMS.tasks import sendConfirmOrderSMS
from Main.models import Budget

def updateProductLink():
    products = Product.objects.all()
    for product in products:
        product.save()

#updateProductLink()

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
    show_copy = True
    no_copy = ['laptop', 'fixed-pc', 'motherboard', 'speaker']
    if category.slug in no_copy:
        show_copy = False
    return render(request, 'Products/Product.html', {'device': device, 'propForm': prop_form,
                                                     'category_prop': category_prop_list[category.slug],
                                                     'show_copy': show_copy})

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

def CopyProduct(request, hierarchy, id):
    if request.user.is_superuser:
        category_slug = getCategory(hierarchy).slug
        if category_slug != 'laptop' and category_slug != 'motherboard' and category_slug != 'speaker' and category_slug != 'fixed-pc':
            category_prop = category_prop_list[category_slug]
            model = category_prop['model']
            product = Product.objects.get(id=id)
            images = product.images.all()
            colors = product.colors.all()
            options = product.options.all()
            product.pk = None
            product.save()
            product_extend = model.objects.get(id=id)
            product_extend.id = product.id
            product_extend.save()
            for image in images:
                image.pk = None
                image.product = product
                image.save()
            for color in colors:
                color.pk = None
                color.product = product
                color.save()
            for option in options:
                option.pk = None
                option.product = product
                option.save()
            changeUrl = category_prop['changeUrl']
            return redirect('/admin/{0}/{1}/change/'.format(changeUrl, product.id))


