from django.shortcuts import render
from .helper import Filter, getCategory, getDeviceById, getDeviceListByCategory, ToStrArray
from Smart.helper import smartphonePropForm
from Smart.models import Smartphone
from Parts.helper import graphiccardPropForm, CPUPropForm, RAMPropForm
from Parts.models import GraphicCard, CPU, RAM
from Computers.models import Computer
from Computers.helper import computerPropForm

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
    device_list = getCartDevices(request)
    return render(request, 'Products/Cart.html', {'device_list':device_list})

def getCartDevices(request):
    device_list = []
    for prop_name, prop in request.GET.items():
        values = ToStrArray(prop)
        for value in values:
            device = {}
            params = value.split('.')
            device_id = params[0]
            device['count'] = params[2]
            model = category_prop_list[prop_name]['model']
            device['device'] = model.objects.get(id=device_id)
            device['color'] = device['device'].colors.get(id=params[1])
            options = device['device'].options.filter(id__in=params[3:])
            print(options)
            if options.count() > 0:
                device['options'] = options
            else:
                device['options'] = None
            device['fullSlug'] = device['device'].category.getFullSlug()
            device['options_price'] = device['color'].price
            for option in options:
                device['options_price'] += option.price
            device_list.append(device)
    return device_list




