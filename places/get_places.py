from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from places.models import Place


def get_point(request: HttpRequest, pk: int) -> JsonResponse:  # noqa: WPS210
    """Get point by id."""
    place = get_object_or_404(Place, pk=pk)
    images = place.images.all()
    images_urls = [image.picture.url for image in images]
    response = {
        'title': place.title,
        'imgs': images_urls,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        },
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 4})
