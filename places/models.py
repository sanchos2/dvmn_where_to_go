from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=16, decimal_places=14)
    lat = models.DecimalField(max_digits=16, decimal_places=14)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    picture = models.ImageField()
    picture_index = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.picture_index} {self.place}'
