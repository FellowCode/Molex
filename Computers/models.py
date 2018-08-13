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

    def getShortenParams(device):
        shorten_params = '[{0}, {1}x{2}Ghz, видеокарта {3} ({4}G), RAM {5} GB]'.format(device.CPU,
                                                                                       device.CPU.core_count,
                                                                                       device.CPU.frequency,
                                                                                       device.graphic_card.GPU,
                                                                                       device.graphic_card.RAM_amount,
                                                                                       device.ram_amount)
        return shorten_params

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
    core_count = models.CharField(max_length=2, choices=CORE_COUNT_CHOICES, default="4")
    thread_count = models.CharField(max_length=2, choices=THREAD_COUNT_CHOICES, default="4")

    def __str__(self):
        return self.name

class Laptop(Product):
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("1366х768", "1366х768")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("TN", "TN"), ("VA", "VA")]


    brand = models.ForeignKey(LaptopBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    diagonal = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=12, choices=RESOLUTION_CHOICES, default="1920x1080")
    matrix = models.CharField(max_length=12, choices=MATRIX_CHOICES, default="IPS")

    cpu = models.ForeignKey(LaptopCPU, on_delete=models.PROTECT)

    ram_amount = models.IntegerField()

    discreteGraphic = models.BooleanField(default=False)
    gpu = models.CharField(max_length=20, default=None)
    graphic_ram_amount = models.IntegerField(default=None)

    hdd_amount = models.IntegerField(default=0)
    ssd_amount = models.IntegerField(default=0)
    emmc_amount = models.IntegerField(default=0)

    weight = models.DecimalField(max_digits=4, decimal_places=2)

    def getShortenParams(device):
        shorten_params = '[{0}, {1}, {2}, {3} ядра, потоков - {4}]'.format(device.resolution,
                                                                         device.matrix,
                                                                         device.cpu,
                                                                         device.cpu.core_count,
                                                                         device.cpu.thread_count)
        return shorten_params

    def __str__(self):
        return str(self.diagonal.normalize()) + '\" ' + str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Laptop'

class LaptopInterface(models.Model):
    name = models.OneToOneField(InterfaceName, on_delete=models.CASCADE, unique=True)
    count = models.IntegerField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)

