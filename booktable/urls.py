from django.urls import  path

from booktable import views

urlpatterns = [
    path('booktable/',views.booktable,name='booktable')
]