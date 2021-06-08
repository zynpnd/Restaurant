from django.db import models

# Create your models here.

class GalleryModel(models.Model):
    name = models.CharField(max_length=25, verbose_name='İsim')
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'
