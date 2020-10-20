"""Models."""
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Class Place."""

    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.DecimalField(max_digits=16, decimal_places=14)
    lat = models.DecimalField(max_digits=16, decimal_places=14)

    def __str__(self):
        """Return humans string."""
        return self.title

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ('title', )


class Image(models.Model):
    """Class Image."""

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
    )
    picture = models.ImageField()
    picture_index = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Return humans string."""
        return f'{self.picture_index} {self.place}'

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ('picture_index', )
