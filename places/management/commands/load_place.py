"""Load places."""
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def get_content(url):
    """
    Get content.

    :param url:
    :return:
    """
    try:  # noqa: WPS229
        req = requests.get(url=url)
        req.raise_for_status()
    except (requests.RequestException, ValueError):
        print('Network Error')  # noqa: WPS421
        return False
    return req


def create_place(url):
    """
    Create place.

    :param url:
    :return:
    """
    raw_data = get_content(url)
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
            img_data = get_content(img_url)
            file_content = ContentFile(img_data.content)
            new_image = Image.objects.create(place_id=obj.pk)
            new_image.picture.save(file_name[-1], content=file_content, save=True)


class Command(BaseCommand):
    """Command class."""

    help = 'Download place from json'  # noqa: WPS125

    def add_arguments(self, parser):
        """
        Added arguments.

        :param parser:
        :return:
        """
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):  # noqa: WPS110
        """
        Handle function.

        :param args:
        :param options:
        :return:
        :raises KeyError: If key does not exist
        :raises ValueError: Wrong format data(m.b. not JSON)
        """
        for url in options['url']:
            try:
                create_place(url)
            except KeyError:
                raise CommandError('Missing required key')
            except ValueError:
                raise CommandError('Wrong format data')

            self.stdout.write(
                self.style.SUCCESS('Successfully added place'),
            )
