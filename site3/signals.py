__author__ = 'pand0rica'
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login


@receiver(pre_social_login)
def example_signal_handler(request, sociallogin, **kwargs):
    user = sociallogin.user
    user.is_staff = True
    user.is_superuser = True
    user.save()
