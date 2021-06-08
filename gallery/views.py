from django.shortcuts import render

# Create your views here.
from gallery.models import GalleryModel


def gallery(request):
    gallery = GalleryModel.objects.all()

    context= {
        'resim' :gallery
    }

    return  render(request,'partials/gallery.html',context)