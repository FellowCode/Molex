from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def corousel_path(instance, filename):
    name, ext = filename.split('.')
    path = 'images/carousel/carousel_img.{}'.format(ext)
    return path

class CarouselImage(models.Model):
    name = models.CharField(max_length=50, default='noName')
    image = ProcessedImageField(
        upload_to=corousel_path,
        processors=[ResizeToFill(1200, 400)],
        format='JPEG',
        options={'quality': 85})

    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceOrder(models.Model):
    service_type = models.CharField(max_length=64, default='')
    email = models.EmailField()
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    note = models.TextField()

    def __str__(self):
        return str(self.service_type) + ' ' + str(self.email)


class Budget(models.Model):

    amount_of_budget = models.IntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # count will have all of the objects from the Aboutus model
        count = Budget.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = Budget.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 2:
            super(Budget, self).save()
        elif save_permission:
            super(Budget, self).save()

        try:
            Budget._meta.verbose_name_plural = str(Budget.objects.all()[0])
        except:
            pass

    def has_add_permission(self):
        return Budget.objects.filter(id=self.id).exists()

    def __str__(self):
        return 'Budget: ' + str(self.amount_of_budget) + 'р.'

    class Meta:
        verbose_name = 'Budget'


