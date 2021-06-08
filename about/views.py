from django.shortcuts import render

# Create your views here.
from about.models import AboutModel, WhyModel


def about(request):
    about = AboutModel.objects.all()
    why = WhyModel.objects.all()

    context = {

        'hakkimizda' : about,
        'nedenbiz' : why,
    }

    return  render(request,'partials/about.html',context)
