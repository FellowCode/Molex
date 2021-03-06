from django import template
from Products.helper import rgetattr
from Products.views import category_prop_list

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def has_item(dictionary, key):
    return key in dictionary
#{{ dictionary|get_item:key }}

""""@register.filter
def get_attr(device, key):
    param = getattr(device, key)
    return param"""

@register.filter
def get_children_list(device, key):
    param = getattr(device, key)
    return param.all()

@register.filter
def get_first_image(device):
    image_url = device.images.all()[0].image.url
    return image_url

@register.filter
def get_attr(device, key):
    return rgetattr(device, key)

@register.filter
def filter_units(value):
    value = value.replace(' ', '')
    if value != '':
        value = ' (' + value + ')'
    return value

@register.filter
def get_children(device, category_slug):
    _id = device.id
    model = category_prop_list[category_slug]['model']
    children = model.objects.get(id=_id)
    return children

@register.filter
def get_param_list(device, dictionary):
    key = dictionary.get('param')
    return (get_attr(device, key)).all()

@register.filter
def string(value):
    return str(value)

@register.filter
def integer(value):
    return int(value)

@register.filter
def normalize(value):
    try:
        return value.normalize()
    except:
        return value

@register.filter
def count(list):
    return list.count()

@register.filter
def replace_spaces(value):
    return str(value).replace(' ', '_')


