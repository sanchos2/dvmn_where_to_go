"""Models."""
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Class Place."""

    title: models.CharField = models.CharField('Название', max_length=200)  # noqa: WPS432
    short_description: models.TextField = models.TextField('Краткое описание', blank=True)  # noqa: WPS432
    long_description: HTMLField = HTMLField('Полное описание', blank=True)  # noqa: WPS432
    lng: models.DecimalField = models.DecimalField('Долгота', max_digits=16, decimal_places=14)  # noqa: WPS432
    lat: models.DecimalField = models.DecimalField('Широта', max_digits=16, decimal_places=14)  # noqa: WPS432

    def __str__(self) -> str:
        """Return humans string."""
        return self.title

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ['title']
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'


class Image(models.Model):
    """Class Image."""

    place: models.ForeignKey = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Расположение',
    )
    picture: models.ImageField = models.ImageField('Фотография')
    picture_index: models.PositiveIntegerField = models.PositiveIntegerField(
        'ID фотографии',
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        """Return humans string."""
        return f'{self.picture_index} {self.place}'

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ['picture_index']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
