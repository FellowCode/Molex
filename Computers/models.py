from django.db import models
from Products.models import Product
from Parts.models import CPU, GraphicCard

class InterfaceName(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

#################################
#################################


class Computer(Product):

    name = models.CharField(max_length=50)
    CPU = models.ForeignKey(CPU, on_delete=models.PROTECT)
    graphic_card = models.ForeignKey(GraphicCard, models.PROTECT)
    ram_amount = models.IntegerField()
    hdd_amount = models.IntegerField()
    ssd_amount = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '> Computer'


class ComputerInterface(models.Model):
    name = models.OneToOneField(InterfaceName, on_delete=models.CASCADE, unique=True)
    count = models.IntegerField()
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)


############################################
############################################

class LaptopBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class LaptopCPU(models.Model):
    CORE_COUNT_CHOICES = [("2", "2"), ("4", "4")]
    THREAD_COUNT_CHOICES = [("4", "4"), ("8", "8")]

    name = models.CharField(max_length=50, unique=True)
    core_count = models.CharField(max_length=2, choices=CORE_COUNT_CHOICES)
    thread_count = models.CharField(max_length=2, choices=THREAD_COUNT_CHOICES, default=None)

    def __str__(self):
        return self.name

class Laptop(Product):
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("1366х768", "1366х768")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("TN", "TN"), ("VA", "VA")]


    brand = models.ForeignKey(LaptopBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    diagonal = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=12, choices=RESOLUTION_CHOICES)
    matrix = models.CharField(max_length=12, choices=MATRIX_CHOICES)

    cpu = models.ForeignKey(LaptopCPU, on_delete=models.PROTECT)

    ram_amount = models.IntegerField()

    discreteGraphic = models.BooleanField(default=False)
    gpu = models.CharField(max_length=20, default=None)
    graphic_ram_amount = models.IntegerField(default=None)

    hdd_amount = models.IntegerField(default=0)
    ssd_amount = models.IntegerField(default=0)
    emmc_amount = models.IntegerField(default=0)

    weight = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Laptop'

class LaptopInterface(models.Model):
    name = models.OneToOneField(InterfaceName, on_delete=models.CASCADE, unique=True)
    count = models.IntegerField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)

