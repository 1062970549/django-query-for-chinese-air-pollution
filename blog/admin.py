from django.contrib import admin
from blog.models import city, cityPM, cityAir, region, regionPM

admin.site.register(city)
admin.site.register(cityPM)
admin.site.register(cityAir)
admin.site.register(region)
admin.site.register(regionPM)

# Register your models here.
