"""Admin module."""
from adminsortable2.admin import SortableInlineAdminMixin
from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places import models


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    """Class ImageInline."""

    model = models.Image
    extra = 0
    readonly_fields = ['preview_image']

    def preview_image(self, image):
        """
        Preview image.

        :param image:
        :return:
        """
        return format_html(mark_safe(  # noqa: S308, S703
            f'<img src="{settings.MEDIA_URL + str(image.picture)}" height="200px" />',
        ))


class PlacesAdmin(admin.ModelAdmin):
    """Class PlacesAdmin."""

    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


admin.site.register(models.Place, PlacesAdmin)
