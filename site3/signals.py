__author__ = 'pand0rica'
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def example_signal_handler(request, user, **kwargs):
    user.is_staff = True
    user.is_superuser = True
    user.save()
