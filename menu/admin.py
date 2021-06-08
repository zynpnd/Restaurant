from django.contrib import admin

# Register your models here.

from menu.models import CategoryModel, MenuModel

admin.site.register(MenuModel)
admin.site.register(CategoryModel)
