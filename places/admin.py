from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places import models


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    """Class ImageInline."""

    model = models.Image
    extra = 0
    readonly_fields = ['preview_image']

    def preview_image(self, image) -> str:
        """Get image preview."""
        if image.picture:
            return format_html('<img src="{}" height="200px" />', image.picture.url)  # noqa: P103
        return 'Здесь будет превью, когда вы выберете файл.'


class PlacesAdmin(admin.ModelAdmin):
    """Class PlacesAdmin."""

    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


admin.site.register(models.Place, PlacesAdmin)
