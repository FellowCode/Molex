from .models import Mouse, MouseBrand, Keyboard, KeyboardBrand, Headphone, HeadphoneBrand
from Products.helper import getNamesFromChoices




mousePropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'always',
              'units': '', 'set': MouseBrand.objects.all()},

    'interface': {'type': 'strArray', 'name': 'Интерфейс', 'display': 'always',
                  'units': '', 'set': getNamesFromChoices(Mouse.INTERFACE_TYPE_CHOICES)},

    'wire_length': {'type': 'floatRange', 'name': 'Длина провода', 'display': 'always', 'units': ' м'},

    'max_dpi': {'type': 'intRange', 'name': 'Точек на дюйм', 'display': 'always', 'units': ''},

    'button_count': {'type': 'intRange', 'name': 'Количество кнопок', 'display': 'always', 'units': ''},

    'weight': {'type': 'intRange', 'name': 'Вес', 'display': 'always', 'units': ' г'},
}



keyboardPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'always',
              'units': '', 'set': KeyboardBrand.objects.all()},

    'interface': {'type': 'strArray', 'name': 'Интерфейс', 'display': 'always',
                  'units': '', 'set': getNamesFromChoices(Keyboard.INTERFACE_TYPE_CHOICES)},

    'type': {'type': 'strArray', 'name': 'Тип клавиатуры', 'display': 'always',
             'units': '', 'set': getNamesFromChoices(Keyboard.TYPE_CHOICES)},

    'wire_length': {'type': 'floatRange', 'name': 'Длина провода', 'display': 'always', 'units': ' м'},

    'key_count': {'type': 'intRange', 'name': 'Количество кнопок', 'display': 'always', 'units': ''},

    'weight': {'type': 'intRange', 'name': 'Вес', 'display': 'always', 'units': ' г'},
}



headphonePropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'always',
              'units': '', 'set': HeadphoneBrand.objects.all()},

    'earbubs_type': {'type': 'strArray', 'name': 'Тип амбушюр', 'display': 'always',
                     'units': '', 'set': getNamesFromChoices(Headphone.EARBUBS_TYPE_CHOICES)},

    'connection_type': {'type': 'strArray', 'name': 'Тип подключения', 'display': 'always',
                        'units': '', 'set': getNamesFromChoices(Headphone.CONNECTION_TYPE_CHOICES)},

    'microphone': {'type': 'strArray', 'name': 'Микрофон', 'display': 'always',
                        'units': '', 'set': getNamesFromChoices(Headphone.MICROPHONE_CHOICES)},

    'wire_length': {'type': 'floatRange', 'name': 'Длина провода', 'display': 'always', 'units': ' м'},

    'resistance': {'type': 'intRange', 'name': 'Сопротивление', 'display': 'always', 'units': ' Ом'},

    'weight': {'type': 'intRange', 'name': 'Вес', 'display': 'always', 'units': ' г'},
}



mousepadPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'length': {'type': 'floatRange', 'name': 'Длина', 'display': 'always', 'units': ' см'},

    'width': {'type': 'floatRange', 'name': 'Ширина', 'display': 'always', 'units': ' см'},

    'height': {'type': 'floatRange', 'name': 'Ширина', 'display': 'always', 'units': ' мм'},
}