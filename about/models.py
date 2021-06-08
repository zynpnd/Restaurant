from django.db import models

# Create your models here.


class AboutModel(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'Başlık')
    content = models.TextField(max_length=600, verbose_name='Açıklama')
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızdakiler'

class WhyModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Başlık')
    content = models.TextField(max_length=600, verbose_name='Açıklama')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Neden Biz'
        verbose_name_plural = 'Neden Biz'

