from django.shortcuts import get_object_or_404
from .models import Category, Product
import functools
from Smart.helper import smartphonePropForm
from Smart.models import Smartphone
from Parts.helper import *
from Parts.models import *
from Computers.models import Computer, Laptop
from Computers.helper import computerPropForm, laptopPropForm
from CompPeripherals.helper import *
from Accessories.models import Mousepad
from Accessories.helper import mousepadPropForm
from decimal import Decimal
import requests
import json
from Molex.settings import RE_CAPTCHA_SECRET

category_prop_list = {
    'smartphone': {'prop_form': smartphonePropForm, 'model': Smartphone, 'changeUrl': 'Smart/smartphone'},
    'tablet': {'prop_form': smartphonePropForm, 'model': Smartphone, 'changeUrl': 'Smart/smartphone'},

    'graphic-card': {'prop_form': graphiccardPropForm, 'model': GraphicCardProduct, 'changeUrl': 'Parts/graphiccardproduct'},
    'cpu': {'prop_form': CPUPropForm, 'model': CPUProduct, 'changeUrl': 'Parts/cpuproduct'},
    'ram': {'prop_form': RAMPropForm, 'model': RAM, 'changeUrl': 'Parts/ram'},
    'motherboard': {'prop_form': motherboardPropForm, 'model': Motherboard, 'changeUrl': 'Parts/motherboard'},
    'ssd': {'prop_form': ssdPropForm, 'model': SSD, 'changeUrl': 'Parts/ssd'},

    'fixed-pc': {'prop_form': computerPropForm, 'model': Computer, 'changeUrl': 'Computers/computer'},
    'laptop': {'prop_form': laptopPropForm, 'model': Laptop, 'changeUrl': 'Computers/laptop'},

    'mouse': {'prop_form': mousePropForm, 'model': Mouse, 'changeUrl': 'CompPeripherals/mouse'},
    'keyboard': {'prop_form': keyboardPropForm, 'model': Keyboard, 'changeUrl': 'CompPeripherals/keyboard'},
    'headphone': {'prop_form': headphonePropForm, 'model': Headphone, 'changeUrl': 'CompPeripherals/headphone'},
    'speaker': {'prop_form': speakerPropForm, 'model': Speaker, 'changeUrl': 'CompPeripherals/speaker'},

    'mousepad': {'prop_form': mousepadPropForm, 'model': Mousepad, 'changeUrl': 'Accessories/mousepad'},
}

def ToIntegerRange(val):
    val = val.split('-')
    min = val[0]
    max = val[1]
    if min == '':
        min = -10000000
    else:
        min = int(val[0])
    if max == '':
        max = 10000000
    else:
        max = int(val[1])
    return min, max


def ToFloatRange(val):
    val = val.split('-')
    min = val[0]
    max = val[1]
    if min == '':
        min = -float('inf')
    else:
        min = float(val[0])
    if max == '':
        max = float('inf')
    else:
        max = float(val[1])
    return min, max


def ToStrArray(val):
    val = val.replace('_', ' ')
    val = list(map(str, val.split('~')))
    return val


def ToIdArray(val):
    val = val.replace('_', ' ')
    val = list(map(int, val.split('~')))
    return val


def FilterInStock(device_list, prop_name, value):
    values = ToIdArray(value)
    value = min(values)
    kwargs = {'{}__gte'.format(prop_name): value}
    device_list = device_list.filter(**kwargs)
    return device_list

def FilterBoolean(device_list, prop_name, value):
    values = ToStrArray(value)
    bool_values = []
    for val in values:
        bool_values.append(bool(val))
    kwargs = {'{}__in'.format(prop_name): bool_values}
    device_list = device_list.filter(**kwargs)
    return device_list

def FilterRange(device_list, prop_name, min, max):
    kwargs = {'{0}__gte'.format(prop_name): min,
              '{0}__lte'.format(prop_name): max}
    device_list = device_list.filter(**kwargs)
    return device_list


def FilterIntRange(device_list, prop_name, value):
    min, max = ToIntegerRange(value)
    return FilterRange(device_list, prop_name, min, max)



def FilterFloatRange(device_list, prop_name, value):
    min, max = ToFloatRange(value)
    return FilterRange(device_list, prop_name, min, max)



def FilterIdArray(device_list, prop_name, value):
    values = ToIdArray(value)
    kwargs = {'{0}__id__in'.format(prop_name): values}
    device_list = device_list.filter(**kwargs)
    return device_list


def FilterStrArray(device_list, prop_name, value):
    values = ToStrArray(value)
    kwargs = {'{0}__in'.format(prop_name): values}
    device_list = device_list.filter(**kwargs)
    return device_list


def Filter(device_list, request, propForm):
    for prop_name, value in request.GET.items():
        if propForm[prop_name]['type'] == 'inStock':
            device_list = FilterInStock(device_list, prop_name, value)
        elif propForm[prop_name]['type'] == 'intRange':
            device_list = FilterIntRange(device_list, prop_name, value)
        elif propForm[prop_name]['type'] == 'floatRange':
            device_list = FilterFloatRange(device_list, prop_name, value)
        elif propForm[prop_name]['type'] == 'idArray':
            device_list = FilterIdArray(device_list, prop_name, value)
        elif propForm[prop_name]['type'] == 'strArray':
            device_list = FilterStrArray(device_list, prop_name, value)
        elif propForm[prop_name]['type'] == 'Boolean':
            device_list = FilterBoolean(device_list, prop_name, value)
    return device_list



def getCategory(hierarchy):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category, slug=slug, parent=parent)

    return parent



def getDeviceById(model, id):
    return model.objects.get(id=id)


def getDeviceListByCategory(model, category):
    return model.objects.filter(category=category)


def getDeviceListByHierarchy(model, hierarchy):
    return model.objects.filter(category=getCategory(hierarchy))





def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('__'))

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
            try:
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
            except:
                pass
    return device_list
