from .models import Smartphone, BrandSmartphone, CPUSmartphone
from Products.helper import getNamesFromChoices

def getSmartphoneShortenParams(device):
    shorten_params = '[Android {0}, {1} Мп, {2}, {3}, {4} мАч, {5}, {6}/{7}, {8}, {9}]'.format( device.android,
                                                                                                device.camera,
                                                                                                device.resolution,
                                                                                                device.matrix,
                                                                                                device.battery,
                                                                                                device.CPU,
                                                                                                device.RAM,
                                                                                                device.ROM,
                                                                                                device.SIM_count,
                                                                                                device.net)
    return shorten_params

smartphonePropForm = {
        'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

        'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

        'brand': {'type': 'idArray', 'name': 'Производитель', 'display': 'filterOnly',
                  'units': '', 'set': BrandSmartphone.objects.all()},

        'android': {'type': 'strArray', 'name': 'Android', 'display': 'always',
                    'units': '', 'set': getNamesFromChoices(Smartphone.ANDROID_CHOICES)},

        'camera': {'type': 'intRange', 'name': 'Камера', 'display': 'always', 'units': ' Мп'},

        'front_camera': {'type': 'intRange', 'name': 'Фронтальная камера', 'display': 'always', 'units': ' Мп'},

        'diagonal': {'type': 'floatRange', 'name': 'Диагональ', 'display': 'always', 'units': '\"'},

        'resolution': {'type': 'strArray', 'name': 'Разрешение', 'display': 'always',
                       'units': '', 'set': getNamesFromChoices(Smartphone.RESOLUTION_CHOICES)},

        'matrix': {'type': 'strArray', 'name': 'Матрица', 'display': 'always',
                   'units': '', 'set': getNamesFromChoices(Smartphone.MATRIX_CHOICES)},

        'battery': {'type': 'intRange', 'name': 'Ёмкость аккумулятора', 'display': 'always', 'units': ' mAh'},

        'CPU': {'type': 'idArray', 'name': 'Процессор', 'display': 'always',
                'units': '', 'set': CPUSmartphone.objects.all()},

        'CPU__core_count': {'type': 'intRange', 'name': 'Количество ядер', 'display': 'always', 'units': ''},

        'RAM': {'type': 'intRange', 'name': 'Оперативная память (RAM)', 'display': 'always', 'units': ' GB'},

        'ROM': {'type': 'intRange', 'name': 'Постоянная память (ROM)', 'display': 'always', 'units': ' GB'},

        'fingerprint': {'type': 'strArray', 'name': 'Сканер отпечатка', 'display': 'always',
                        'units': '', 'set': getNamesFromChoices(Smartphone.FINGERPRINT_CHOICES)},

        'SIM_count': {'type': 'strArray', 'name': 'Кол-во симкарт', 'display': 'always',
                     'units': '', 'set': getNamesFromChoices(Smartphone.SIM_CHOICES)},

        'net': {'type': 'strArray', 'name': 'Поддержка сетей', 'display': 'always',
                'units': '', 'set': getNamesFromChoices(Smartphone.NET_CHOICES)},
}
