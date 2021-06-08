from django.db import models

# Create your models here.

class EventsMddel(models.Model):
    name= models.CharField(max_length=100, verbose_name='Başlık')
    content = models.TextField(max_length=700, verbose_name= 'Açıklama')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    image =  models.ImageField(upload_to='events/')


    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Etkinlik'
        verbose_name_plural = 'Etkinlikler'
