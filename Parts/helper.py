from Products.helper import getNamesFromChoices
from .models import GraphicCard, CPU, RAM, GraphicCardBrand, CPUsocket, GPU

graphiccardPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': GraphicCardBrand.objects.all()},

    'GPU_ruler': {'type': 'strArray', 'name': 'Линейка процессоров', 'display': 'always',
                  'units': '', 'set': getNamesFromChoices(GraphicCard.GPU_RULER_CHOICES)},

    'GPU': {'type': 'idArray', 'name': 'Графический процессор', 'display': 'always',
            'units': '', 'set': GPU.objects.all()},

    'RAM': {'type': 'intRange', 'name': 'Объем видеопамяти', 'display': 'always', 'units': ' GB'},

    'RAM_type': {'type': 'strArray', 'name': 'Тип видеопамяти', 'display': 'always',
                  'units': '', 'set': getNamesFromChoices(GraphicCard.RAM_TYPE_CHOICES)},

    'watts': {'type': 'intRange', 'name': 'Макс. энергопотребление', 'display': 'always', 'units': ' Вт'},
}

CPUPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'strArray', 'name': 'Производитель', 'display': 'filterOnly',
              'units': '', 'set': getNamesFromChoices(CPU.BRAND_CHOICES)},

    'socket': {'type': 'idArray', 'name': 'Сокет', 'display': 'always',
               'units': '', 'set': CPUsocket.objects.all()},

    'coreCount': {'type': 'intRange', 'name': 'Количество ядер', 'display': 'filterOnly', 'units': ''},

    'threadsCount': {'type': 'intRange', 'name': 'Количество потоков', 'display': 'filterOnly', 'units': ''},

    'frequency': {'type': 'intRange', 'name': 'Частота оперативной памяти', 'display': 'filterOnly', 'units': ' Mhz'},

    'RAM_type': {'type': 'strArray', 'name': 'Тип оперативной памяти', 'display': 'always',
                 'units': '', 'set': getNamesFromChoices(CPU.RAM_TYPE_CHOICES)},

}

RAMPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'type':  {'type': 'strArray', 'name': 'Вид оперативной памяти', 'display': 'always',
              'units': '', 'set': getNamesFromChoices(RAM.TYPE_CHOICES)},

    'RAM_type': {'type': 'strArray', 'name': 'Тип оперативной памяти', 'display': 'always',
                 'units': '', 'set': getNamesFromChoices(RAM.RAM_TYPE_CHOICES)},

    'RAM_amount': {'type': 'intRange', 'name': 'Объем', 'display': 'filterOnly', 'units': ' GB'},

    'frequency': {'type': 'intRange', 'name': 'Частота', 'display': 'filterOnly', 'units': ' Mhz'},
}