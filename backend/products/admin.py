from django.contrib import admin

from .models import URL, Info, Cost, Picture

admin.site.register(URL)
admin.site.register(Info)
admin.site.register(Cost)
admin.site.register(Picture)
