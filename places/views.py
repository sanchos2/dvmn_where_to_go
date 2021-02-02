from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    """Render template with context."""
    places = Place.objects.all()
    serialized_places = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in places:
        serialized_places['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat],
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('place', kwargs={'pk': place.pk}),
                },
            },
        )
    context = {'serialized_places': serialized_places}
    return render(request, 'index.html', context=context)


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
