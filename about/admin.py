from django.contrib import admin

# Register your models here.
from about.models import WhyModel, AboutModel



admin.site.register(AboutModel)
admin.site.register(WhyModel)
