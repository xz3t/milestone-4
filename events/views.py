from django.shortcuts import render
from .models import Event


def events(request):
    """ A view to show all events """

    event = Event.objects.all().order_by('-date')

    context = {
        'event': event,
    }

    return render(request, 'events/events.html', context)
