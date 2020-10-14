from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Place


def point(request, pk):
    place = get_object_or_404(Place, pk=pk)
    image_url = []
    list_image = place.images.all()
    for url in list_image:
        relative_url = settings.MEDIA_URL + str(url.picture)
        image_url.append(relative_url)
    response = {
        'title': place.title,
        'imgs': image_url,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 4})
