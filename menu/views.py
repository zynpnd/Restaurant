from django.shortcuts import render

# Create your views here.
from menu.models import MenuModel, CategoryModel


def menu(request):
    menu = MenuModel.objects.all()
    category = CategoryModel.objects.all()

    context = {
        'yemek' : menu,
        'kategori' :category,
    }

    return  render(request,'partials/menu.html',context)
