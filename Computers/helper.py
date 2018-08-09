from .models import Computer, CPU, GPU
from Products.helper import getNamesFromChoices

computerPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'cpu': {'type': 'idArray', 'name': 'Процессор', 'display': 'always',
            'units': '', 'set': CPU.objects.all()},

    'cpu_core_count': {'type': 'intRange', 'name': 'Количество ядер', 'display': 'always', 'units': ''},

    'cpu_threads_count': {'type': 'intRange', 'name': 'Количество потоков', 'display': 'always', 'units': ''},

    'cpu_frequency': {'type': 'floatRange', 'name': 'Частота процессора', 'display': 'always', 'units': ' Ghz'},

    'graphic_card_full_name': {'type': '', 'name': 'Видеокарта', 'display': 'paramOnly', 'units': ''},

    'graphic_card_gpu': {'type': 'idArray', 'name': 'Графический процессор', 'display': 'filterOnly',
                         'units': '', 'set': GPU.objects.all()},

    'graphic_card_ram_type': {'type': 'strArray', 'name': 'Тип памяти видеокарты', 'display': 'always',
                              'units': '', 'set': getNamesFromChoices(Computer.GPU_RAM_TYPE_CHOICES)},

    'graphic_card_ram_amount': {'type': 'intRange', 'name': 'Объем видеопамяти', 'display': 'always', 'units': ''},

    'ram_type': {'type': 'strArray', 'name': 'Тип памяти', 'display': 'always',
                              'units': '', 'set': getNamesFromChoices(Computer.RAM_TYPE_CHOICES)},

    'ram_amount': {'type': 'intRange', 'name': 'Объём оперативной памяти', 'display': 'always', 'units': ''},

    'hdd_amount': {'type': 'intRange', 'name': 'Объём HDD', 'display': 'always', 'units': ' GB'},

    'ssd_amount': {'type': 'intRange', 'name': 'Объём SSD', 'display': 'always', 'units': ' GB'},

}

