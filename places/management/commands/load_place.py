from typing import Dict

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def create_place(url: str) -> None:
    """Create place."""
    raw_data = requests.get(url)
    raw_data.raise_for_status()
    pretty_data = raw_data.json()
    obj, created = Place.objects.get_or_create(  # noqa: WPS110
        title=pretty_data['title'],
        description_short=pretty_data['description_short'],
        description_long=pretty_data['description_long'],
        lng=pretty_data['coordinates']['lng'],
        lat=pretty_data['coordinates']['lat'],
    )
    if created:
        for img_url in pretty_data['imgs']:
            file_name = img_url.split('/')
            img_data = requests.get(img_url)
            img_data.raise_for_status()
            file_content = ContentFile(img_data.content)
            new_image = Image.objects.create(place_id=obj.pk)
            new_image.picture.save(file_name[-1], content=file_content, save=True)


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
