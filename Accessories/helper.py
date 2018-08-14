mousepadPropForm = {
    'price': {'type': 'intRange', 'name': 'Цена', 'display': 'filterOnly', 'units': ' Р.'},

    'count': {'type': 'inStock', 'name': 'Наличие', 'display': 'filterOnly', 'units': '', 'set': ['нет', 'есть']},

    'length': {'type': 'floatRange', 'name': 'Длина', 'display': 'always', 'units': ' см'},

    'width': {'type': 'floatRange', 'name': 'Ширина', 'display': 'always', 'units': ' см'},

    'height': {'type': 'floatRange', 'name': 'Ширина', 'display': 'always', 'units': ' мм'},
}