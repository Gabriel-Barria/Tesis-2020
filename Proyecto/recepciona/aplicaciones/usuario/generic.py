import django
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .mixins import LoginAjaxMixin

DJANGO_VERSION = django.get_version().split('.')
DJANGO_MAJOR_VERSION = DJANGO_VERSION[0]
DJANGO_MINOR_VERSION = DJANGO_VERSION[1]

# Import custom LoginView for Django versions < 1.11
if DJANGO_MAJOR_VERSION == '1' and '11' not in DJANGO_MINOR_VERSION:
    from .compatibility import LoginView
else:
    from django.contrib.auth.views import LoginView


class BSModalLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    pass
