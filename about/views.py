from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):
    """ A view to show all events """

    about = About.objects.all()

    context = {
        'about': about,
    }

    return render(request, 'about/about.html', context)