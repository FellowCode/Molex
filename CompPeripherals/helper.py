from .models import Mouse, MouseBrand, Keyboard, KeyboardBrand, Headphone, HeadphoneBrand, SpeakerBrand, Speaker, SpeakerFrequencyDiapason, SpeakerInterfaceName
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



speakerPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'always',
              'units': '', 'set': SpeakerBrand.objects.all()},

    'channels': {'type': 'strArray', 'name': 'Каналы', 'display': 'always',
                 'units': '', 'set': getNamesFromChoices(Speaker.CHANNELS_CHOICES)},

    'power': {'type': 'intRange', 'name': 'Макс. мощность', 'display': 'always', 'units': ' Вт'},

    'power_output': {'type': 'intRange', 'name': 'Выходная мощность', 'display': 'always', 'units': ' Вт'},

    'frequency_diapason': {'type': 'idArray', 'name': 'Диапазон частот', 'display': 'always',
                           'units': '', 'set': SpeakerFrequencyDiapason.objects.all()},

    'battery': {'type': 'intRange', 'name': 'Ёмкость аккумулятора', 'display': 'always', 'units': ' мАч', 'hideZero': True},

    'waterproof': {'type': 'strArray', 'name': 'Влагозащита', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Speaker.YES_NO_CHOICES)},

    'microsd': {'type': 'strArray', 'name': 'microSD', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Speaker.YES_NO_CHOICES)},

    'microphone': {'type': 'strArray', 'name': 'Микрофон', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Speaker.YES_NO_CHOICES)},

    'interfaces__name__name': {'type': 'strArray', 'name': 'Интерфейсы', 'display': 'always',
                               'units': '', 'set': SpeakerInterfaceName.objects.all(), 'param': 'interfaces'},
}
