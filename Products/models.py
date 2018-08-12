from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('name', 'slug', 'parent')
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]

        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return '->'.join(full_path[::-1])

    def getFullSlug(self):
        full_slug = [self.slug]

        k = self.parent
        while k is not None:
            full_slug.append(k.slug)
            k = k.parent

        return '/'.join(full_slug[::-1])

def preview_directory_path(instance, filename):
    name, ext = filename.split('.')
    path = 'images/product/{0}/preview/preview.{1}'.format(instance.category.slug, ext)
    return path

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True, default='')
    price = models.IntegerField()
    sale = models.IntegerField(null=True, blank=True, default=None)
    count = models.IntegerField(null=True, blank=True, default=0)
    deliveryDays = models.IntegerField(default=30)
    bestOffer = models.BooleanField(default=False)

    imagePreview = ProcessedImageField(
                                upload_to=preview_directory_path,
                                processors=[ResizeToFill(128, 128)],
                                format='JPEG',
                                options={'quality': 75})

    def getFullSlug(self):
        self.category.getFullSlug()

def img_directory_path(instance, filename):
    name, ext = filename.split('.')
    path = 'images/product/{0}/carousel/carousel.{1}'.format(instance.product.category.slug, ext)
    return path

class Image(models.Model):
    image = ProcessedImageField(upload_to=img_directory_path,
                                processors=[ResizeToFill(800, 800)],
                                format='JPEG',
                                options={'quality': 85})
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

def color_img_directory_path(instance, filename):
    name, ext = filename.split('.')
    path = 'images/product/{0}/color/color.{1}'.format(instance.product.category.slug, ext)
    return path

class Color(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    image = ProcessedImageField(upload_to=color_img_directory_path,
                                null=True,
                                blank=True,
                                default=None,
                                processors=[ResizeToFill(128, 128)],
                                format='JPEG',
                                options={'quality': 60})
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.name


class Order(models.Model):
    person = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    person_name = models.CharField(max_length=50)
    person_phone = models.CharField(max_length=12)
    person_pay = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    isProcessed = models.BooleanField(default=True)
    goods = models.TextField()

    class Meta:
        ordering = ['isCompleted']

