from django.db import models
from Products.models import Product


class MouseBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Mouse(Product):
    INTERFACE_TYPE_CHOICES = [("USB", "USB"), ("PS/2", "PS/2")]
    CONNECTION_TYPE_CHOICES = [("Провод", "Провод"), ("Беспроводная", "Беспроводная")]

    brand = models.ForeignKey(MouseBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    interface = models.CharField(max_length=5, choices=INTERFACE_TYPE_CHOICES, default="USB")
    connection_type = models.CharField(max_length=15, choices=CONNECTION_TYPE_CHOICES, default="Провод")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    max_dpi = models.IntegerField()
    button_count = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Mouse'


class KeyboardBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Keyboard(Product):
    INTERFACE_TYPE_CHOICES = [("USB", "USB"), ("PS/2", "PS/2")]
    TYPE_CHOICES = [("Мембрана", "Мембрана"), ("Механическая", "Механическая")]
    CONNECTION_TYPE_CHOICES = [("Провод", "Провод"), ("Bluetooth", "Bluetooth"), ("2.4 Ghz", "2.4 Ghz")]

    brand = models.ForeignKey(KeyboardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    interface = models.CharField(max_length=5, choices=INTERFACE_TYPE_CHOICES, default="USB")
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default="Мембрана")
    connection_type = models.CharField(max_length=15, choices=CONNECTION_TYPE_CHOICES, default="Провод")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    key_count = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Keyboard'


class HeadphoneBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Headphone(Product):
    EARBUBS_TYPE_CHOICES = [("Вставные(вакуумные)", "Вставные(вакуумные)"), ("Охватывающие", "Охватывающие")]
    CONNECTION_TYPE_CHOICES = [("USB", "USB"), ("Jack 3.5", "Jack 3.5"), ("Bluetooth", "Bluetooth"), ("2.4 Ghz", "2.4 Ghz")]

    brand = models.ForeignKey(KeyboardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    earbubs_type = models.CharField(max_length=20, choices=EARBUBS_TYPE_CHOICES)
    connection_type = models.CharField(max_length=15, choices=CONNECTION_TYPE_CHOICES, default="Провод")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    resistance = models.IntegerField(null=True, blank=True, default=None)
    weight = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Headphone'