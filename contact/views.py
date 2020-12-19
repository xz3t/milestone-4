from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _

from .forms import ContactForm

# Create your views here.

def contact(request):
    """ A view to show contact form """

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                from_email,
                [settings.DEFAULT_FROM_EMAIL,],
            )
            messages.success(request, _('Success! Thank you for your message.'))

    return render(request, 'contact/contact.html', {'form': form})