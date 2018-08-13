from django.shortcuts import get_object_or_404
from .models import Category, Product
import functools

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


def getNamesFromChoices(choices):
    names = []
    for choice, val in choices:
        names.append(choice)
    return names


def rgetattr(obj, attr, *args):
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split('__'))
