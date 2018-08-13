from django.db import models
from Products.models import Category, Product

class CPUSmartphone(models.Model):
    BRAND_CHOICES = [("MediaTek", "MediaTek"), ("Snapdragon", "Snapdragon"), ("Other", "Other")]

    brand = models.CharField(max_length=15, choices=BRAND_CHOICES)
    name = models.CharField(max_length=60, unique=True)
    core_count = models.IntegerField(default=8)

    def __str__(self):
        if self.brand == 'Other':
            return self.name
        else:
            return self.brand + ' ' + self.name


class BrandSmartphone(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Smartphone(Product):
    ANDROID_CHOICES = [("6.0", "6.0"), ("7.0", "7.0"), ("7.1", "7.1"), ("8.0", "8.0"), ("8.1", "8.1")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("OLED", "OLED"), ("TFT", "TFT")]
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("2160х1080", "2160х1080"),
                          ("1280x720", "1280x720"), ("1440x720", "1440x720")]
    FINGERPRINT_CHOICES = [('есть', 'есть'), ('нет', 'нет')]
    SIM_CHOICES = [("1 SIM", "1 SIM"), ("2 SIM", "2 SIM")]
    NET_CHOICES = [("3G", "3G"), ("4G", "4G")]

    brand = models.ForeignKey(BrandSmartphone, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    android = models.CharField(max_length=4, choices=ANDROID_CHOICES, default="8.1")
    camera = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    front_camera = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    matrix = models.CharField(max_length=6, choices=MATRIX_CHOICES, default="IPS")
    diagonal = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=12, choices=RESOLUTION_CHOICES, default="2160х1080")
    battery = models.IntegerField()
    CPU = models.ForeignKey(CPUSmartphone, on_delete=models.PROTECT)
    RAM = models.IntegerField()
    ROM = models.IntegerField()
    fingerprint = models.CharField(max_length=10, default='нет', choices=FINGERPRINT_CHOICES)
    SIM_count = models.CharField(max_length=8, choices=SIM_CHOICES, default="2")
    net = models.CharField(max_length=3, choices=NET_CHOICES, default="4G")

    def getShortenParams(device):
        shorten_params = '[Android {0}, {1} Мп, {2}, {3}, {4} мАч, {5}, {6}/{7}, {8}, {9}]'.format(device.android,
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

    def __str__(self):
        return str(self.diagonal.normalize()) + '\" ' + self.brand.name + ' ' + self.name

    class Meta:
        verbose_name = '> Smartphone and Tablet'
        verbose_name_plural = '> Smartphones and Tablets'

