from django.contrib.gis import admin
from .models import Providers,Polygons

# Register your models here.
admin.site.register(Providers)
admin.site.register(Polygons)
