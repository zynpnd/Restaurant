from django.shortcuts import render

# Create your views here.
from events.models import EventsMddel


def events(request):
    events = EventsMddel.objects.all()

    context = {
        'rezervasyon' : events,
    }

    return  render(request,'partials/events.html',context)

