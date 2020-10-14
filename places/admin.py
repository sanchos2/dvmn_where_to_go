from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from . import models


class ImageInline(admin.TabularInline):
    model = models.Image
    readonly_fields = ['preview_image']

    def preview_image(self, image):
        preview = mark_safe(
            f'<img src="{settings.MEDIA_URL + str(image.picture)}" width="200" />'
        )
        return format_html(preview)


class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]



admin.site.register(models.Place, PlacesAdmin)
admin.site.register(models.Image)
