import os
from typing import Dict
from urllib.parse import unquote, urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def create_place(url: str) -> None:
    """Create place."""
    raw_data = requests.get(url)
    raw_data.raise_for_status()
    pretty_data = raw_data.json()
    place, created = Place.objects.get_or_create(  # noqa: WPS110
        title=pretty_data['title'],
        defaults={
            'short_description': pretty_data['description_short'],
            'long_description': pretty_data['description_long'],
            'lng': pretty_data['coordinates']['lng'],
            'lat': pretty_data['coordinates']['lat'],
        },
    )
    if created:
        for img_url in pretty_data['imgs']:
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
