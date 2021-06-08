from django.db import models

# Create your models here.
from django.forms import ModelForm , TextInput


class ContactModel(models.Model):
    name = models.CharField(max_length=75,verbose_name='Adı Soyadı')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    subject = models.CharField(max_length=75,verbose_name='Konu')
    message = models.TextField(max_length=600,verbose_name='Mesaj')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'



