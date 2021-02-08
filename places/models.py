"""Models."""
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Class Place."""

    title = models.CharField('Название', max_length=200)  # noqa: WPS432
    short_description = models.TextField('Краткое описание', blank=True)  # noqa: WPS432
    long_description = HTMLField('Полное описание', blank=True)  # noqa: WPS432
    lng = models.DecimalField('Долгота', max_digits=16, decimal_places=14)  # noqa: WPS432
    lat = models.DecimalField('Широта', max_digits=16, decimal_places=14)  # noqa: WPS432

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ['title']
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'

    def __str__(self) -> str:
        """Return humans string."""
        return self.title


class Image(models.Model):
    """Class Image."""

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Расположение',
    )
    picture = models.ImageField('Фотография')
    numeration = models.PositiveIntegerField('ID фотографии', default=0)

    class Meta:  # noqa: WPS306
        """Meta class."""

        ordering = ['numeration']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self) -> str:
        """Return humans string."""
        return f'{self.numeration} {self.place}'
