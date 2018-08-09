from django.db import models
from Products.models import Product

class CPUsocket(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CPU(Product):
    BRAND_CHOICES = [("Intel", "Intel"), ("AMD", "AMD")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]

    brand = models.CharField(max_length=8, choices=BRAND_CHOICES)
    name = models.CharField(max_length=50)
    socket = models.ForeignKey(CPUsocket, on_delete=models.PROTECT)
    coreCount = models.IntegerField()
    threadsCount = models.IntegerField()
    frequency = models.IntegerField()
    RAM_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES)


class GPU(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GraphicCardBrand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GraphicCard(Product):
    GPU_RULER_CHOICES = [("GeForce", "GeForce"), ("Radeon", "Radeon")]
    RAM_TYPE_CHOICES = [("GDDR3", "GDDR3"), ("GDDR4", "GDDR4"), ("GDDR5", "GDDR5")]

    graphic_card_names = ['Линейка графических процессоров', 'Графический процессор', 'Объем видеопамяти',
                          'Тип памяти', 'Максимальное энергопотребление']
    graphic_card_units = ['', '', ' GB', '', ' Вт']


    brand = models.ForeignKey(GraphicCardBrand, on_delete=models.PROTECT)
    GPU_ruler = models.CharField(max_length=8, choices= GPU_RULER_CHOICES)
    GPU = models.ForeignKey(GPU, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    RAM = models.IntegerField()
    RAM_type = models.CharField(max_length=8, choices=RAM_TYPE_CHOICES)
    watts = models.IntegerField()

    def __str__(self):
        return str(self.brand) + ' ' + str(self.GPU) + ' ' + str(self.name)


class RAM(Product):
    TYPE_CHOICES = [("DIMM", "DIMM"), ("SO-DIMM", "SO-DIMM")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    RAM_type = models.CharField(max_length=8, choices=RAM_TYPE_CHOICES)
    RAM_amount = models.IntegerField()
    frequency = models.IntegerField()

