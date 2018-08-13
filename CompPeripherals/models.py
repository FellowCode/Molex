from django.db import models
from Products.models import Product


class MouseBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Mouse(Product):
    INTERFACE_TYPE_CHOICES = [("USB", "USB"), ("PS/2", "PS/2"), ("Bluetooth", "Bluetooth"), ("2.4Ghz", "2.4Ghz")]

    brand = models.ForeignKey(MouseBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    interface = models.CharField(max_length=5, choices=INTERFACE_TYPE_CHOICES, default="USB")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    max_dpi = models.IntegerField()
    button_count = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)

    def getShortenParams(device):
        shorten_params = '[Интерфейс {0}, {1} DPI, кнопок - {2}]'.format(device.interface,
                                                                         device.max_dpi,
                                                                         device.button_count)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Mouse'


class KeyboardBrand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Keyboard(Product):
    INTERFACE_TYPE_CHOICES = [("USB", "USB"), ("PS/2", "PS/2"), ("Провод", "Провод"), ("Bluetooth", "Bluetooth"), ("2.4 Ghz", "2.4 Ghz")]
    TYPE_CHOICES = [("Мембрана", "Мембрана"), ("Механическая", "Механическая")]
    ILLUMINATION_CHOICES = [("Нет", "Нет"), ("RGB", "RGB"), ("Монотонная", "Монотонная")]

    brand = models.ForeignKey(KeyboardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    interface = models.CharField(max_length=20, choices=INTERFACE_TYPE_CHOICES, default="USB")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="Мембрана")
    illumination = models.CharField(max_length=20, choices=ILLUMINATION_CHOICES, default="RGB")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    key_count = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)

    def getShortenParams(device):
        shorten_params = '[Интерфейс {0}, {1}, кнопок - {2}]'.format(device.interface, device.type, device.key_count)
        return shorten_params

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
    MICROPHONE_CHOICES = [('есть', 'есть'), ('нет', 'нет')]

    brand = models.ForeignKey(KeyboardBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    earbubs_type = models.CharField(max_length=50, choices=EARBUBS_TYPE_CHOICES, default="Охватывающие")
    connection_type = models.CharField(max_length=30, choices=CONNECTION_TYPE_CHOICES, default="Jack 3.5")
    microphone = models.CharField(max_length=10, default='есть', choices=MICROPHONE_CHOICES)
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    resistance = models.IntegerField(null=True, blank=True, default=None)
    weight = models.IntegerField(null=True, blank=True, default=None)

    def getShortenParams(device):
        shorten_params = '[{0}, микрофон - {1}]'.format(device.connection_type, device.microphone)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Headphone'

class Mousepad(Product):
    name = models.CharField(max_length=100)

    length = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Длина (см)')
    width = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Ширина (см)')
    height = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Толщина (мм)')

    def getShortenParams(device):
        shorten_params = '[{0}x{1} см, {2} мм]'.format(device.length,
                                                       device.width,
                                                       device.height)
        return shorten_params

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '> Mousepad'

