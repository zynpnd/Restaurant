from django.db import models

# Create your models here.

class MenuModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=' Yemek Adı')
    category = models.ForeignKey('CategoryModel',on_delete=models.SET_NULL,null=True)
    content = models.TextField(max_length=600, verbose_name='Açıklama')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Yemek'
        verbose_name_plural = 'Yemekler'

class CategoryModel(models.Model):
   category = models.CharField(max_length=50, verbose_name='Kategori')

   def __str__(self):
       return self.category

   class Meta:
       verbose_name = 'Kategori'
       verbose_name_plural = 'Kategoriler'

