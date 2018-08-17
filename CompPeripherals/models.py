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
    interface = models.CharField(max_length=20, choices=INTERFACE_TYPE_CHOICES, default="USB")
    wire_length = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, default=None)
    max_dpi = models.IntegerField()
    button_count = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)

    def getShortenParams(self):
        shorten_params = '[Интерфейс {0}, {1} DPI, кнопок - {2}]'.format(self.interface,
                                                                         self.max_dpi,
                                                                         self.button_count)
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
    INTERFACE_TYPE_CHOICES = [("USB", "USB"), ("PS/2", "PS/2"), ("Bluetooth", "Bluetooth"), ("2.4 Ghz", "2.4 Ghz")]
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

    def getShortenParams(self):
        shorten_params = '[Интерфейс {0}, {1}, кнопок - {2}]'.format(self.interface, self.type, self.key_count)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Keyboard'


class HeadphoneBrand(models.Model):
    name = models.CharField(max_length=40, unique=True)

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

    def getShortenParams(self):
        shorten_params = '[{0}, микрофон - {1}]'.format(self.connection_type, self.microphone)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Headphone'


class SpeakerInterfaceName(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class SpeakerBrand(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class SpeakerFrequencyDiapason(models.Model):
    name = models.CharField(max_length=40, unique=True)

class Speaker(Product):
    CHANNELS_CHOICES = [("2.0", "2.0"), ("2.1", "2.1"),  ("5.1", "5.1"),  ("7.1", "7.1")]
    YES_NO_CHOICES = [('есть', 'есть'), ('нет', 'нет')]

    brand = models.ForeignKey(SpeakerBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    channels = models.CharField(max_length=10, choices=CHANNELS_CHOICES, default="2.0")
    power = models.IntegerField()
    power_output = models.IntegerField()
    frequency_diapason = models.ForeignKey(SpeakerFrequencyDiapason, models.PROTECT)
    battery = models.IntegerField()
    waterproof = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='нет')
    microsd = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='нет')
    microphone = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='нет')

    def getShortenParams(self):
        battery = ''
        if self.battery > 0:
            battery = str(self.battery) + ' мАч,'
        shorten_params = '[{0}, выходная мощность {1}, {2},{3} microSD: {4}, влагозащита: {5}]'.format(self.channels,
                                                                                                       self.power_output,
                                                                                                       self.frequency_diapason,
                                                                                                       battery,
                                                                                                       self.microsd,
                                                                                                       self.waterproof)
        return shorten_params

    def __str__(self):
        return str(self.brand) + ' ' + str(self.name)

    class Meta:
        verbose_name = '> Speaker'

class SpeakerInterface(models.Model):
    name = models.ForeignKey(SpeakerInterfaceName, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='interfaces')

    def __str__(self):
        return str(self.name)
