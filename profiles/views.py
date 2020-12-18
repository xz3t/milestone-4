from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.translation import ugettext as _

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    """ If method is post, save profile information """
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, _('Profile updated successfully'))
        else:
            messages.error(request, _('Update failed. Please ensure the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Retrieve order and retur"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        _(f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.')
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
