from django.shortcuts import render

# Create your views here.
from chefs.models import ChefModel


def chefs(request):
    chef =ChefModel.objects.all()

    context= {
        'sef' :chef
    }
    return render(request,'partials/chefs.html',context)
