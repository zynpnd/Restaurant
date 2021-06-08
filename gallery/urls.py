from django.urls import path, include
from gallery import views

urlpatterns = [
    path('gallery/',views.gallery)
]