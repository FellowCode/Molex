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
    OPERATING_SYSTEM_CHOICE = [("Android", "Android"), ("Windows 10", "Windows 10"),
                               ("iOS", "iOS"), ("Windows 10 и Android", "Windows 10 и Android")]
    ANDROID_CHOICES = [("5.1", "5.1"), ("6.0", "6.0"), ("7.0", "7.0"), ("7.1", "7.1"), ("8.0", "8.0"), ("8.1", "8.1")]
    MATRIX_CHOICES = [("IPS", "IPS"), ("OLED", "OLED"), ("TFT", "TFT")]
    RESOLUTION_CHOICES = [("1920x1080", "1920x1080"), ("2160х1080", "2160х1080"),
                          ("1280x720", "1280x720"), ("1440x720", "1440x720"),
                          ("1024x600", "1024x600"), ("1920x1200", "1920x1200"),
                          ("1920x1280", "1920x1280"), ("1280x800", "1280x800")]
    FINGERPRINT_CHOICES = [('есть', 'есть'), ('нет', 'нет')]
    SIM_CHOICES = [("1 SIM", "1 SIM"), ("2 SIM", "2 SIM")]
    NET_CHOICES = [("3G", "3G"), ("4G", "4G")]

    brand = models.ForeignKey(BrandSmartphone, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    operating_system = models.CharField(max_length=40, choices=OPERATING_SYSTEM_CHOICE, default="Android")
    android = models.CharField(max_length=4, choices=ANDROID_CHOICES, default="8.1", null=True, blank=True)
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

    def getShortenParams(self):
        android = self.operating_system
        if android != 'iOS':
            android += ' ' + self.android
        camera = self.camera
        if camera == int(camera):
            camera = int(camera)
        else:
            camera = camera.normalize()
        shorten_params = '[{0}, {1} Мп, {2}, {3}, {4} мАч, {5}, {6}/{7}, {8}, {9}]'.format(android,
                                                                                           camera,
                                                                                           self.resolution,
                                                                                           self.matrix,
                                                                                           self.battery,
                                                                                           self.CPU,
                                                                                           self.RAM,
                                                                                           self.ROM,
                                                                                           self.SIM_count,
                                                                                           self.net)
        return shorten_params

    def __str__(self):
        diagonal = int(self.diagonal)
        if diagonal != self.diagonal:
            diagonal = self.diagonal.normalize()
        return str(diagonal) + '\" ' + self.brand.name + ' ' + self.name

    class Meta:
        verbose_name = '> Smartphone and Tablet'
        verbose_name_plural = '> Smartphones and Tablets'

