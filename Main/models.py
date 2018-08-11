from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class CarouselImage(models.Model):
    image = ProcessedImageField(
        upload_to='images/carousel/',
        processors=[ResizeToFill(1200, 400)],
        format='JPEG',
        options={'quality': 85})
