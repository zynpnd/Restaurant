from django.db import models

# Create your models here.

class ChefModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='İsim')
    unvan = models.CharField(max_length=100, verbose_name='Unvan')
    image = models.ImageField(upload_to='chef/')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Şef'
        verbose_name_plural = 'Şefler'