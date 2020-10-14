from django.contrib import admin

from . import models


class ImageInline(admin.TabularInline):
    model = models.Image


class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(models.Place, PlacesAdmin)
admin.site.register(models.Image)
