import os
from typing import Dict
from urllib.parse import unquote, urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def create_place(url: str) -> None:
    """Create place."""
    response = requests.get(url)
    response.raise_for_status()
    payload = response.json()
    place, created = Place.objects.get_or_create(  # noqa: WPS110
        title=payload['title'],
        defaults={
            'short_description': payload['description_short'],
            'long_description': payload['description_long'],
            'lng': payload['coordinates']['lng'],
            'lat': payload['coordinates']['lat'],
        },
    )
    if created:
        for img_url in payload['imgs']:
            path = unquote(urlsplit(img_url).path)
            filename = os.path.split(path)[-1]
            img_data = requests.get(img_url)
            img_data.raise_for_status()
            file_content = ContentFile(img_data.content)
            image = Image.objects.create(place_id=place.pk)
            image.picture.save(filename, content=file_content, save=True)


class Command(BaseCommand):
    """Command class."""

    help = 'Download place from json'  # noqa: WPS125

    def add_arguments(self, parser) -> None:
        """Added arguments."""
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args: str, **options: Dict[str, str]) -> None:  # noqa: WPS110, WPS231
        """Handle function."""
        for url in options['url']:
            try:
                create_place(url)
            except KeyError:
                raise CommandError('Missing required key.')
            except ValueError:
                raise CommandError('Wrong format data.')
            except requests.exceptions.HTTPError:
                raise CommandError('Network error.')

            self.stdout.write(
                self.style.SUCCESS('Successfully added place.'),
            )
