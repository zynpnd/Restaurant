from django.urls import path

from chefs import views

urlpatterns = [

    path('chef/', views.chefs),
]