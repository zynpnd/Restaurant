from django.shortcuts import render,redirect

# Create your views here.
from contact.forms import ContactForm
from contact.models import ContactModel
from django.contrib import messages


def contact(request):

   form = ContactForm(request.POST or None)
   if form.is_valid():
       Contact = form.save()
       return redirect('/contact')

   else:
       context = {
           "form": form
       }
       return render(request, 'partials/contact.html', context)


