from django import forms
from django.forms import ModelForm, TextInput

from contact.models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ["name", "email", "subject","message"]
        widgets ={
            'name': TextInput(
                attrs={'id': 'input_name', 'class': 'form-control', 'name': 'your-name', 'placeholder': 'İsminiz'}),
            'email': TextInput(
                attrs={'id': 'input_email', 'class': 'form-control', 'name': 'your-email', 'placeholder': 'E-Posta'}),
            'subject': TextInput(
                attrs={'id': 'subject', 'class': 'form-control', 'name': 'your-subject', 'placeholder': 'Konu'}),
            'message': TextInput(
                attrs={'id': 'subject', 'class': 'form-control', 'name': 'your-message', 'placeholder': 'Mesajınız'}),
        }
