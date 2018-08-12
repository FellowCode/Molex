from Products.helper import getNamesFromChoices
from .models import GraphicCardProduct, CPU, RAM, GraphicCardBrand, CPUSocket, GPU, \
    Motherboard, MotherboardBrand, InterfaceName, SSD, SSDBrand, MotherboardChipset, GraphicCard

graphiccardPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': GraphicCardBrand.objects.all()},

    'graphic_card__GPU_ruler': {'type': 'strArray', 'name': 'Линейка процессоров', 'display': 'always',
                                'units': '', 'set': getNamesFromChoices(GraphicCard.GPU_RULER_CHOICES)},

    'graphic_card__GPU': {'type': 'idArray', 'name': 'Графический процессор', 'display': 'always',
                          'units': '', 'set': GPU.objects.all()},

    'graphic_card__RAM': {'type': 'intRange', 'name': 'Объем видеопамяти', 'display': 'always', 'units': ' GB'},

    'graphic_card__RAM_type': {'type': 'strArray', 'name': 'Тип видеопамяти', 'display': 'always',
                               'units': '', 'set': getNamesFromChoices(GraphicCard.RAM_TYPE_CHOICES)},

    'graphic_card__watts': {'type': 'intRange', 'name': 'Макс. энергопотребление', 'display': 'always', 'units': ' Вт'},
}

CPUPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'cpu__brand': {'type': 'strArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': getNamesFromChoices(CPU.BRAND_CHOICES)},

    'cpu__socket': {'type': 'idArray', 'name': 'Сокет', 'display': 'always',
                    'units': '', 'set': CPUSocket.objects.all()},

    'cpu__coreCount': {'type': 'intRange', 'name': 'Количество ядер', 'display': 'filterOnly', 'units': ''},

    'cpu__threadsCount': {'type': 'intRange', 'name': 'Количество потоков', 'display': 'filterOnly', 'units': ''},

    'cpu__frequency': {'type': 'intRange', 'name': 'Частота оперативной памяти', 'display': 'filterOnly', 'units': ' Mhz'},

    'cpu__RAM_type': {'type': 'strArray', 'name': 'Тип оперативной памяти', 'display': 'always',
                      'units': '', 'set': getNamesFromChoices(CPU.RAM_TYPE_CHOICES)},

}

RAMPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'type':  {'type': 'strArray', 'name': 'Вид оперативной памяти', 'display': 'always',
              'units': '', 'set': getNamesFromChoices(RAM.TYPE_CHOICES)},

    'RAM_type': {'type': 'strArray', 'name': 'Тип оперативной памяти', 'display': 'always',
                 'units': '', 'set': getNamesFromChoices(RAM.RAM_TYPE_CHOICES)},

    'RAM_amount': {'type': 'intRange', 'name': 'Объем', 'display': 'always', 'units': ' GB'},

    'frequency': {'type': 'intRange', 'name': 'Частота', 'display': 'always', 'units': ' Mhz'},
}

motherboardPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': MotherboardBrand.objects.all()},

    'formFactor': {'type': 'strArray', 'name': 'Форм фактор', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Motherboard.FORM_FACTOR_CHOICES)},

    'socket': {'type': 'idArray', 'name': 'Сокет', 'display': 'always',
               'units': '', 'set': CPUSocket.objects.all()},

    'RAM_slot_count': {'type': 'strArray', 'name': 'Кол-во слотов RAM', 'display': 'always',
                       'units': '', 'set': getNamesFromChoices(Motherboard.RAM_SLOT_COUNT_CHOICES)},

    'RAM_type': {'type': 'strArray', 'name': 'Тип оперативной памяти', 'display': 'always',
                 'units': '', 'set': getNamesFromChoices(Motherboard.RAM_TYPE_CHOICES)},

    'chipset': {'type': 'idArray', 'name': 'Чипсет', 'display': 'always',
               'units': '', 'set': MotherboardChipset.objects.all()},

    'interfaces.name': {'type': 'strArray', 'name': 'Интерфейсы', 'display': 'always',
                        'units': '', 'set': InterfaceName.objects.all(), 'param': 'interfaces'},
}

ssdPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': SSDBrand.objects.all()},

    'memory_type' : {'type': 'strArray', 'name': 'Тип памяти', 'display': 'always',
                     'units': '', 'set': getNamesFromChoices(SSD.MEMORY_TYPE_CHOICES)},

    'read_speed': {'type': 'intRange', 'name': 'Скорость чтения', 'display': 'always', 'units': ' Mb/s'},
    'write_speed': {'type': 'intRange', 'name': 'Скорость записи', 'display': 'always', 'units': ' Mb/s'},

}