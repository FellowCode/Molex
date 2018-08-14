from django.db import models
from Products.models import Product

class Mousepad(Product):
    name = models.CharField(max_length=100)

    length = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Длина (см)')
    width = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Ширина (см)')
    height = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Толщина (мм)')

    def getShortenParams(self):
        shorten_params = '[{0}x{1} см, {2} мм]'.format(self.length,
                                                       self.width,
                                                       self.height)
        return shorten_params

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '> Mousepad'
        default_related_name = 'mousepad'