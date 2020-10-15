from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from . import models


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Image
    extra = 0
    readonly_fields = ['preview_image']

    def preview_image(self, image):
        preview = mark_safe(
            f'<img src="{settings.MEDIA_URL + str(image.picture)}" height="200px" />'
        )
        return format_html(preview)


class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(models.Place, PlacesAdmin)
