from django.shortcuts import render, redirect

# Create your views here.
from booktable.models import BookTableModel


def booktable(request):

    if request.POST:

        name    = request.POST['name']
        email   = request.POST['email']
        phone   = request.POST['phone']
        date    = request.POST['date']
        time    = request.POST['time']
        people  = request.POST['people']
        message = request.POST['message']

        booktable = BookTableModel.objects.create(
            name = name,
            email = email,
            phone = phone,
            date = date,
            time = time,
            people = people,
            message = message,
        )
        booktable.save()
        return redirect('/booktable')
    else:
        return render(request, 'partials/bookatable.html')




