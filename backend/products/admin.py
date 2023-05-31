from django.contrib import admin

from .models import Categories, Info, URL, Pictures, Cost


admin.site.register(Categories)
admin.site.register(Info)
admin.site.register(URL)
admin.site.register(Pictures)
admin.site.register(Cost)
