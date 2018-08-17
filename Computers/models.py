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

    def getShortenParams(self):
        shorten_params = '[{0}, {1}x{2}Ghz, видеокарта {3} ({4}G), RAM {5} GB]'.format(self.CPU,
                                                                                       self.CPU.coreCount,
                                                                                       self.CPU.frequency,
                                                                                       self.graphic_card.GPU,
                                                                                       self.graphic_card.RAM,
                                                                                       self.ram_amount)
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
        name = str(self.name)
        if self.count > 0:
            name += ' x' + str(self.count)
        return name


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
    frequency = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class LaptopGPU(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ram_amount = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self):
        name = str(self.name)
        if self.ram_amount > 0:
            name += ' (' + str(self.ram_amount) + 'G)'
        return name

class LaptopIntegralGPU(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Laptop(Product):
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("1366х768", "1366х768"), ("2736x1824", "2736x1824")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("TN", "TN"), ("VA", "VA")]
    GRAPHICCAD_CHOICES = [('есть', 'есть'), ('нет', 'нет')]

    brand = models.ForeignKey(LaptopBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    diagonal = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=12, choices=RESOLUTION_CHOICES, default="1920x1080")
    matrix = models.CharField(max_length=12, choices=MATRIX_CHOICES, default="IPS")

    cpu = models.ForeignKey(LaptopCPU, on_delete=models.PROTECT)

    ram_amount = models.IntegerField()

    integralGraphic = models.ForeignKey(LaptopIntegralGPU, on_delete=models.PROTECT, default=None, null=True, blank=True)
    discreteGraphic = models.CharField(max_length=10, choices=GRAPHICCAD_CHOICES, default='нет')
    gpu = models.ForeignKey(LaptopGPU, on_delete=models.PROTECT, null=True, blank=True)
    hdd_amount = models.IntegerField(default=0)
    ssd_amount = models.IntegerField(default=0)
    emmc_amount = models.IntegerField(default=0)

    weight = models.DecimalField(max_digits=4, decimal_places=2)

    def getShortenParams(self):
        if self.discreteGraphic == 'нет':
            graphiccard = str(self.integralGraphic)
        else:
            graphiccard = str(self.gpu)
        shorten_params = '[{0}, {1}, {2}, {3}x{4} Ghz, RAM {5} GB, {6}]'.format(self.resolution,
                                                                                  self.matrix,
                                                                                  self.cpu,
                                                                                  self.cpu.core_count,
                                                                                  self.cpu.frequency.normalize(),
                                                                                  self.ram_amount,
                                                                                  graphiccard)
        return shorten_params

    def __str__(self):
        return str(self.diagonal.normalize()) + '\" ' + str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Laptop'

class LaptopInterface(models.Model):
    name = models.ForeignKey(InterfaceName, on_delete=models.CASCADE, default=1)
    count = models.IntegerField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        name = str(self.name)
        if self.count > 0:
            name += ' x' + str(self.count)
        return name

