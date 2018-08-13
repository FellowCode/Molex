from django.db import models
from Products.models import Product

class CPUSocket(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CPU Socket'

class CPU(models.Model):
    BRAND_CHOICES = [("Intel", "Intel"), ("AMD", "AMD")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]

    brand = models.CharField(max_length=8, choices=BRAND_CHOICES, default="Intel")
    name = models.CharField(max_length=50, unique=True)
    socket = models.ForeignKey(CPUSocket, on_delete=models.PROTECT)
    coreCount = models.IntegerField()
    threadsCount = models.IntegerField()
    frequency = models.DecimalField(max_digits=3, decimal_places=2)
    RAM_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES, default="DDR3")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPU'

class CPUProduct(Product):
    cpu = models.OneToOneField(CPU, on_delete=models.CASCADE)

    def getShortenParams(device):
        shorten_params = '[{0}, {1}x{2}Ghz, {3} потоков, {4}]'.format(device.cpu.socket,
                                                                      device.cpu.coreCount,
                                                                      device.cpu.frequency,
                                                                      device.cpu.threadsCount,
                                                                      device.cpu.RAM_type)
        return shorten_params

    def __str__(self):
        return self.cpu.name

    class Meta:
        verbose_name = '> CPU'
        verbose_name_plural = '> CPU'


################################################
################################################

class GPU(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPU'

class GraphicCardBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class GraphicCard(models.Model):
    GPU_RULER_CHOICES = [("GeForce", "GeForce"), ("Radeon", "Radeon")]
    RAM_TYPE_CHOICES = [("GDDR3", "GDDR3"), ("GDDR4", "GDDR4"), ("GDDR5", "GDDR5")]

    GPU_ruler = models.CharField(max_length=8, choices=GPU_RULER_CHOICES, default="GeForce")
    GPU = models.ForeignKey(GPU, on_delete=models.PROTECT)
    RAM = models.IntegerField()
    RAM_type = models.CharField(max_length=8, choices=RAM_TYPE_CHOICES, default="GDDR5")
    watts = models.IntegerField()

    def __str__(self):
        return str(self.GPU) + ' (' + str(RAM) + 'G)'

class GraphicCardProduct(Product):

    brand = models.ForeignKey(GraphicCardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    graphic_card = models.ForeignKey(GraphicCard, on_delete=models.PROTECT)

    def getShortenParams(device):
        shorten_params = '[{0}, {1} GB, {2} Вт]'.format(device.graphic_card.RAM_type,
                                                        device.graphic_card.RAM,
                                                        device.graphic_card.watts)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.graphic_card.GPU) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Graphiccard'

##############################################
###############################################

class RAM(Product):
    TYPE_CHOICES = [("DIMM", "DIMM"), ("SO-DIMM", "SO-DIMM")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default="DIMM")
    RAM_type = models.CharField(max_length=8, choices=RAM_TYPE_CHOICES, default="DDR3")
    RAM_amount = models.IntegerField()
    frequency = models.IntegerField()

    def getShortenParams(device):
        shorten_params = '[{0}, {1}, {2} GB, {3} Mhz]'.format(device.type,
                                                              device.RAM_type,
                                                              device.RAM_amount,
                                                              device.frequency)
        return shorten_params

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '> RAM'
        verbose_name_plural = '> RAM'

#########################################
##########################################

class MotherboardBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class MotherboardChipset(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class InterfaceName(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Motherboard(Product):
    FORM_FACTOR_CHOICES = [("MATX", "MATX"), ("ATX", "ATX")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]
    RAM_SLOT_COUNT_CHOICES = [("2", "2"), ("4", "4")]

    brand = models.ForeignKey(MotherboardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    formFactor = models.CharField(max_length=5, choices=FORM_FACTOR_CHOICES, default="MATX")
    socket = models.ForeignKey(CPUSocket, on_delete=models.PROTECT)

    RAM_slot_count = models.CharField(max_length=2, choices=RAM_SLOT_COUNT_CHOICES, default="2")
    RAM_type = models.CharField(max_length=8, choices=RAM_TYPE_CHOICES, default="DDR3")

    chipset = models.ForeignKey(MotherboardChipset, models.PROTECT, default=None)

    def getShortenParams(device):
        shorten_params = '[{0}, {1}, слотов RAM: {2}, чипсет {3}]'.format(device.formFactor,
                                                                          device.socket,
                                                                          device.RAM_slot_count,
                                                                          device.chipset)
        return shorten_params

    class Meta:
        verbose_name = '> Motherboard'

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

class MotherboardInterface(models.Model):
    name = models.OneToOneField(InterfaceName, models.PROTECT, unique=True)
    count = models.IntegerField()
    Motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name) + ' x' + str(self.count)

##############################################
##############################################

class SSDBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SSD Brand'

class SSD(Product):
    MEMORY_TYPE_CHOICES = [("SLC", "SLC"), ("MLC", "MLC"), ("TLC", "TLC")]

    brand = models.ForeignKey(SSDBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    memory_type = models.CharField(max_length=5, choices=MEMORY_TYPE_CHOICES, default="TLC")

    memory_amount = models.IntegerField()

    read_speed = models.IntegerField()
    write_speed = models.IntegerField()

    def getShortenParams(device):
        shorten_params = '[{0}, чтение {1} Mb/s, запись {2} Mb/s]'.format(device.memory_type,
                                                                          device.read_speed,
                                                                          device.write_speed)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name) + ' ' + str(self.memory_amount)

    class Meta:
        verbose_name = '> SSD'
        verbose_name_plural = '> SSD'

