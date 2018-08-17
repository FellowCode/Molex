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
