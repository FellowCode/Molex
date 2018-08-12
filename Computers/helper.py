from .models import Computer
from Parts.models import GraphicCard, CPU, GPU, InterfaceName
from .models import Laptop, LaptopCPU, LaptopBrand
from Products.helper import getNamesFromChoices

computerPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'CPU': {'type': 'idArray', 'name': 'Процессор', 'display': 'always',
            'units': '', 'set': CPU.objects.all()},

    'CPU__core_count': {'type': 'intRange', 'name': 'Количество ядер', 'display': 'always', 'units': ''},

    'CPU__threads_count': {'type': 'intRange', 'name': 'Количество потоков', 'display': 'always', 'units': ''},

    'CPU__frequency': {'type': 'floatRange', 'name': 'Частота процессора', 'display': 'always', 'units': ' Ghz'},

    'graphic_card__GPU_ruler': {'type': 'strArray', 'name': 'Линейка граф. процессора', 'display': 'always',
                                'units': '', 'set': getNamesFromChoices(GraphicCard.GPU_RULER_CHOICES)},

    'graphic_card__GPU': {'type': 'idArray', 'name': 'Графический процессор', 'display': 'filterOnly',
                          'units': '', 'set': GPU.objects.all()},

    'graphic_card__RAM_type': {'type': 'strArray', 'name': 'Тип памяти видеокарты', 'display': 'always',
                              'units': '', 'set': getNamesFromChoices(GraphicCard.RAM_TYPE_CHOICES)},

    'graphic_card__RAM_amount': {'type': 'intRange', 'name': 'Объем видеопамяти', 'display': 'always', 'units': ''},

    'CPU__RAM_type': {'type': 'strArray', 'name': 'Тип памяти', 'display': 'always',
                              'units': '', 'set': getNamesFromChoices(CPU.RAM_TYPE_CHOICES)},

    'ram_amount': {'type': 'intRange', 'name': 'Объём оперативной памяти', 'display': 'always', 'units': ''},

    'hdd_amount': {'type': 'intRange', 'name': 'Объём HDD', 'display': 'always', 'units': ' GB'},

    'ssd_amount': {'type': 'intRange', 'name': 'Объём SSD', 'display': 'always', 'units': ' GB'},

    'interfaces__name': {'type': 'strArray', 'name': 'Интерфейсы', 'display': 'always',
                        'units': '', 'set': InterfaceName.objects.all(), 'param': 'interfaces'},

}

laptopPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'always',
              'units': '', 'set': LaptopBrand.objects.all()},

    'diagonal': {'type': 'floatRange', 'name': 'Диагональ', 'display': 'always', 'units': '\"'},

    'resolution': {'type': 'strArray', 'name': 'Разрешение', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Laptop.RESOLUTION_CHOICES)},

    'matrix': {'type': 'strArray', 'name': 'Матрица', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Laptop.MATRIX_CHOICES)},

    'cpu': {'type': 'idArray', 'name': 'Процессор', 'display': 'always',
            'units': '', 'set': LaptopCPU.objects.all()},

    'cpu__core_count': {'type': 'strArray', 'name': 'Количество ядер', 'display': 'always',
                        'units': '', 'set': getNamesFromChoices(LaptopCPU.CORE_COUNT_CHOICES)},

    'cpu__thread_count': {'type': 'strArray', 'name': 'Количество потоков', 'display': 'always',
                          'units': '', 'set': getNamesFromChoices(LaptopCPU.THREAD_COUNT_CHOICES)},

    'discreteGraphic': {'type': 'Boolean', 'name': 'Дискретная видеокарта', 'display': 'always',
                        'units': '', 'set': ['нет', 'есть']},

    'gpu': {'name': 'Модель дискретной видеокарты', 'display': 'paramOnly', 'units': ''},

    'graphic_ram_amount': {'name': 'Модель дискретной видеокарты', 'display': 'paramOnly', 'units': ''},

    'hdd_amount': {'type': 'intRange', 'name': 'Объём HDD', 'display': 'always', 'units': ' GB'},

    'ssd_amount': {'type': 'intRange', 'name': 'Объём SSD', 'display': 'always', 'units': ' GB'},

    'emmc_amount': {'type': 'intRange', 'name': 'Объём EMMC памяти', 'display': 'always', 'units': ' GB'},

    'weight': {'type': 'floatRange', 'name': 'Вес', 'display': 'always', 'units': ' кг.'},

}
