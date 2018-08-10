from django.shortcuts import render
from .helper import Filter, getCategory, getDeviceById, getDeviceListByCategory, ToStrArray
from Smart.helper import smartphonePropForm
from Smart.models import Smartphone
from Parts.helper import graphiccardPropForm, CPUPropForm, RAMPropForm
from Parts.models import GraphicCard, CPU, RAM
from Computers.models import Computer
from Computers.helper import computerPropForm
from .models import Order
from django.http import Http404
from decimal import *

category_prop_list = {
    'smartphone': {'prop_form': smartphonePropForm, 'model': Smartphone, 'app': 'Smart'},
    'tablet': {'prop_form': smartphonePropForm, 'model': Smartphone, 'app': 'Smart'},
    'graphic-card': {'prop_form': graphiccardPropForm, 'model': GraphicCard, 'app': 'Parts'},
    'cpu': {'prop_form': CPUPropForm, 'model': CPU, 'app': 'Parts'},
    'ram': {'prop_form': RAMPropForm, 'model': RAM, 'app': 'Parts'},
    'fixed-pc': {'prop_form': computerPropForm, 'model': Computer, 'app': 'Computers'},
    'laptop': {'prop_form': computerPropForm, 'model': Computer, 'app': 'Computers'},
}

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
    return render(request, 'Products/Order.html', {'device_list': device_list})

def OrderConfirm(request):
    if request.method == 'POST':
        print(request.POST)
        order = Order.objects.create(goods=request.POST['goods'], person_name=request.POST['person_name'],
                                     person_phone=request.POST['person_phone'],
                                     payment_amount=float(request.POST['payment_amount']))
        order.save()
        return render(request, 'Products/OrderConfirm.html')


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


def getCartDevices(json):
    device_list = []
    for prop_name, prop in json.items():
        values = ToStrArray(prop)
        for value in values:
            device = {}
            params = value.split('.')
            device_id = params[0]
            device['count'] = params[2]
            model = category_prop_list[prop_name]['model']
            device['device'] = model.objects.get(id=device_id)
            if params[1] != 'null':
                device['color'] = device['device'].colors.get(id=params[1])
            else:
                device['color'] = None
            options = device['device'].options.filter(id__in=params[3:])
            device['options'] = options
            device['fullSlug'] = device['device'].category.getFullSlug()
            if device['color'] is not None:
                device['options_price'] = device['color'].price
            else:
                device['options_price'] = 0
            for option in options:
                device['options_price'] += option.price
            device['fullPrice'] = Decimal(device['device'].price + device['options_price']).normalize()
            device_list.append(device)
    return device_list

def GETStringToJSON(getString):
    json = {}
    values = getString.split('&')
    for value in values:
        key, param = value.split('=')
        json[key] = param
    return json


