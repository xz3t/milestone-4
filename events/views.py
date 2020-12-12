from django.shortcuts import render
from .models import Event

# Create your views here.

def events(request):
    """ A view to show all events """

    event = Event.objects.all()

    context = {
        'event': event,
    }

    return render(request, 'events/events.html', context)