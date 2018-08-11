from django.db import models
from Products.models import Product
from Parts.models import CPU, GraphicCard

class InterfaceName(models.Model):
    name = models.CharField(max_length=20)

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



class ComputerInterface(models.Model):
    name = models.ForeignKey(InterfaceName, on_delete=models.CASCADE)
    count = models.IntegerField()
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)


############################################
############################################

class LaptopBrand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LaptopCPU(models.Model):
    CORE_COUNT_CHOICES = [("2", "2"), ("4", "4")]
    THREAD_COUNT_CHOICES = [("4", "4"), ("8", "8")]

    name = models.CharField(max_length=50)
    core_count = models.CharField(max_length=2, choices=CORE_COUNT_CHOICES)
    thread_count = models.CharField(max_length=2, choices=THREADS_COUNT_CHOICES, default=None)

    def __str__(self):
        return self.name

class Laptop(Product):
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("1366х768", "1366х768")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("TN", "TN"), ("VA", "VA")]


    brand = models.ForeignKey(LaptopBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    diagonal = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=8, choices=RESOLUTION_CHOICES)
    matrix = models.CharField(max_length=8, choices=MATRIX_CHOICES)

    cpu = models.ForeignKey(LaptopCPU, on_delete=models.PROTECT)

    ram_amount = models.IntegerField()

    discreteGraphic = models.BooleanField(default=False)
    gpu = models.CharField(max_length=20, default=None)
    graphic_ram_amount = models.IntegerField(default=None)

    hdd = models.IntegerField(default=0)
    ssd = models.IntegerField(default=0)
    emmc = models.IntegerField(default=0)

    weight = models.DecimalField(max_digits=4, decimal_places=2)

class LaptopInterface(models.Model):
    name = models.ForeignKey(InterfaceName, on_delete=models.CASCADE)
    count = models.IntegerField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)

