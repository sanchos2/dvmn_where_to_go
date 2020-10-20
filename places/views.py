"""Views."""
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    """Render template with context.

    :param request: request
    :return: returns
    """
    places = Place.objects.all()
    place_data = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in places:
        place_data['features'].append(
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
    context = {'data': place_data}
    return render(request, 'index.html', context=context)
