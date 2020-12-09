from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
class LoginAjaxMixin(object):
    """
    Mixin which authenticates user if request is not ajax request.
    """

    def form_valid(self, form):
        if not self.request.is_ajax():
            auth_login(self.request, form.get_user())
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())