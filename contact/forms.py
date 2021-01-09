from django import forms
from django.utils.translation import ugettext as _


class ContactForm(forms.Form):
    email = forms.EmailField(label=_('Email '), required=True)
    subject = forms.CharField(label=_('Subject '), required=True)
    message = forms.CharField(
        label=_('Message '), widget=forms.Textarea, required=True)
