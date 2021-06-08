from django.db import models

# Create your models here.

class BookTableModel(models.Model):
    name = models.CharField(max_length=75, verbose_name='İsim')
    email = models.CharField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=11, verbose_name='Telefon')
    date = models.DateField(verbose_name='Date')
    time = models.TimeField(verbose_name='Saat')
    people = models.DecimalField(max_digits=50,decimal_places=2,verbose_name='Kişi Sayısı')
    message = models.TextField(max_length=600, verbose_name='Mesaj')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rezervasyon'
        verbose_name_plural = 'Rezervasyonlar'