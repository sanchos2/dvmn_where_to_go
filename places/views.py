from django.shortcuts import render
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
