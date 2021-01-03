from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _

from .forms import ContactForm

# Create your views here.


def contact(request):
    """ A view to show contact form,
        on_profile_page used to not display shopping bag in success toast"""

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            body = render_to_string(
                'contact/contact_email/contact_email.txt',
                {'from_email': from_email, 'message': message})
            send_mail(
                subject,
                body,
                from_email,
                [settings.DEFAULT_FROM_EMAIL, ],
            )
            messages.success(
                request, _('Success! Thank you for your message.'))

    return render(
        request,
        'contact/contact.html',
        {'form': form, 'on_profile_page': True})
