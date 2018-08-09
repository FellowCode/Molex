from django.db import models
from Products.models import Product

class CPU(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GPU(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Computer(Product):
    GPU_RAM_TYPE_CHOICES = [("GDDR3", "GDDR3"), ("GDDR4", "GDDR4"), ("GDDR5", "GDDR5")]
    RAM_TYPE_CHOICES = [("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")]

    name = models.CharField(max_length=50)

    _CPU = models.ForeignKey(CPU, on_delete=models.PROTECT)
    cpu_core_count = models.IntegerField()
    cpu_threads_count = models.IntegerField()
    cpu_frequency = models.DecimalField(max_digits=4, decimal_places=2)

    graphic_card_name = models.CharField(max_length=50)
    graphic_card_gpu = models.ForeignKey(GPU, on_delete=models.PROTECT)
    graphic_card_ram_type = models.CharField(max_length=10, choices=GPU_RAM_TYPE_CHOICES)

    ram_type = models.CharField(max_length=10, choices=RAM_TYPE_CHOICES)
    ram_amount = models.IntegerField()

    hdd_amount = models.IntegerField()
    ssd_amount = models.IntegerField()


    def __str__(self):
        return self.name

    def graphic_card_full_name(self):
        return self.graphic_card_name + ' ' + str(self.graphic_card_gpu)
