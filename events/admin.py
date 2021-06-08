from django.contrib import admin

# Register your models here.
from events.models import EventsMddel


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class Meta:
    EventsMddel = PostAdmin



admin.site.register(EventsMddel,PostAdmin)
